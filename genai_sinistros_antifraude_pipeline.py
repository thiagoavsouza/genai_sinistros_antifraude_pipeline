import pandas as pd
import json
import os
from openai import OpenAI
from datetime import datetime

# ============================
# CONFIG
# ============================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ============================
# 1) LER O EXCEL DE ENTRADA
# ============================
df = pd.read_excel("sinistros.xlsx")

saida = []

# ============================
# 2) PROCESSAR CADA LINHA
# ============================
for _, row in df.iterrows():

    texto = row["texto_original"]

    prompt = f"""
Você é um motor antifraude de seguradora.

Extraia os seguintes campos do texto abaixo e retorne APENAS um JSON válido:

- tipo_sinistro
- data_sinistro (DD/MM/AAAA)
- valor_prejuizo
- score_risco (0 a 100)
- nivel ("Baixo", "Médio", "Alto")
- justificativa: "texto curto"

Texto:
{texto}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um motor antifraude de seguradora. Sempre retorne todos os campos solicitados. Nunca use NULL. Se não souber, estime."},
            {"role": "user", "content": prompt}
        ]
    )

    resposta = response.choices[0].message.content
    resposta = resposta.replace("```json", "").replace("```", "").strip()

    dados = json.loads(resposta)

    # ============================
    # 3) DERIVAR MES/ANO
    # ============================
    data = datetime.strptime(dados["data_sinistro"], "%d/%m/%Y")
    dados["mes_ano"] = data.strftime("%Y-%m")

    # ============================
    # 4) JUNTAR COM DADOS ORIGINAIS
    # ============================
    dados["numero_sinistro"] = row["numero_sinistro"]
    dados["apolice"] = row["apolice"]
    dados["texto_original"] = texto
    dados["analista"] = row["analista"]

    saida.append(dados)

# ============================
# 5) BASE FINAL
# ============================
df_final = pd.DataFrame(saida)
# ============================
# 6) ORGANIZAR COLUNAS
# ============================
ordem = [
    "numero_sinistro",
    "apolice",
    "data_sinistro",
    "mes_ano",
    "analista",
    "tipo_sinistro",
    "valor_prejuizo",
    "score_risco",
    "nivel",
    "justificativa",
    "texto_original"
]

df_final = df_final[ordem]


# ============================
# 7) SALVAR EXCEL
# ============================
df_final.to_excel("sinistros_enriquecidos.xlsx", index=False)


print("Arquivo sinistros_enriquecidos.xlsx gerado com sucesso!")
