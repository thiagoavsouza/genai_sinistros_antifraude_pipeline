# 🧠 GenAI para Triagem e Análise de Sinistros em Seguradoras

## Descrição do Projeto

Este projeto utiliza Inteligência Artificial Generativa (LLMs) para automatizar a análise de sinistros em seguradoras, transformando descrições textuais (não estruturadas) em dados estruturados e indicadores de risco antifraude.

A solução permite extrair automaticamente informações relevantes de sinistros, como tipo de ocorrência, data, valor do prejuízo e gerar um score de risco, auxiliando na triagem, priorização e tomada de decisão operacional.

## Objetivo

Desenvolver um pipeline de IA Generativa capaz de:

- Processar textos de sinistros a partir de um arquivo Excel  
- Extrair informações estruturadas usando LLMs  
- Gerar um score de risco antifraude  
- Classificar os sinistros em níveis de risco (Baixo, Médio, Alto)  
- Produzir uma base final pronta para uso em BI, análise antifraude e tomada de decisão  

## Dataset

O conjunto de dados de entrada é um arquivo Excel (`sinistros.xlsx`) contendo:

- numero_sinistro  
- apolice  
- texto_original  

## Etapas do Projeto

1. Leitura da base em Excel  
2. Extração dos campos via IA Generativa  
3. Aplicação de regras de negócio para classificação de risco  
4. Enriquecimento com data, mês/ano e metadados  
5. Geração do Excel final (`sinistros_enriquecidos.xlsx`)  

## Conclusão

O projeto demonstra como IA Generativa pode ser usada para automatizar a análise de sinistros, padronizar dados e criar motores de priorização antifraude em ambientes corporativos.

## Principais Bibliotecas Utilizadas

- pandas  
- openai  
- streamlit  
- json  
- datetime  

## Contato

E-mail: thiago.a.v.souza@gmail.com  
LinkedIn: https://www.linkedin.com/in/thiagoavsouza/
