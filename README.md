# 📊 Trabalho-Machine-Learning-Communities-and-Crimes

**Tema:** Análise e Predição da Taxa de Criminalidade por Comunidade
**Disciplina:** Aprendizagem de Máquina
**Docente:** Prof. Rodrigo Gonçalves Pinto
**Integrantes:** Artur Martins, Guilherme Gomes, Kauan Santos

## 🎯 Objetivo do Projeto
Este projeto aplica o fluxo completo de Machine Learning sobre o dataset público **"Communities and Crime"** (UCI Machine Learning Repository). O objetivo é analisar as variáveis socioeconômicas e prever a taxa de crimes violentos por 100 mil habitantes (`ViolentCrimesPerPop`) utilizando **Regressão Linear Múltipla**, comparando seu desempenho com um modelo de referência (Baseline).

## 📁 Estrutura do Repositório
- `01_IntegranteA_Dados_EDA_Baseline.ipynb`: Notebook da Parte 1 (Obtenção, EDA, Pré-processamento, Split, Baseline).
- `02_IntegranteB_RegressaoLinear.ipynb`: Notebook da Parte 2 (Regressão Linear Múltipla, Análise de Coeficientes e Resíduos).
- `03_IntegranteC_Avaliacao.ipynb`: Notebook da Parte 3 (Validação Cruzada e Quadro Comparativo Final).
- `scripts/download_data.py`: Script automatizado para baixar o dataset original.
- `requirements.txt`: Dependências do projeto.
- `AUTORES.md`: Divisão de responsabilidades.
- `ficha_dataset.txt`: Metadados do dataset gerados após o tratamento.

## ⚙️ Como Reproduzir o Projeto (Passo a Passo)

**Pré-requisitos:**
- Conta no Google (para uso do Google Colab e Google Drive).
- Google Drive montado com a pasta `MachineLearning2026/dados` (ou utilize a execução local).

**Passo 1:** Faça o upload dos notebooks no Google Colab.
**Passo 2:** Execute o notebook **Parte 1**. Ele fará o download (ou buscará do Drive) o arquivo `communities.data`, realizará a limpeza, treinará o Baseline e salvará os artefatos (`.npy` e `.pkl`) na pasta `modelos` do seu Drive.
**Passo 3:** Execute o notebook **Parte 2**. Ele carregará os artefatos da Parte 1, treinará a Regressão Linear Múltipla e plotará o diagnóstico de resíduos.
**Passo 4:** Execute o notebook **Parte 3**. Ele aplicará a Validação Cruzada K-Fold e gerará o quadro comparativo final contra o baseline.

## 🔬 Metodologia e Resultados
- **Baseline (DummyRegressor):** RMSE de ~0.21 (Piso de performance).
- **Regressão Linear Múltipla:** Modelo escolhido para produção devido à sua **interpretabilidade**, permitindo que gestores públicos entendam o impacto de cada variável (ex: pobreza, desemprego) na criminalidade.
- **Atlas da Violência (Referência):** Utilizado como base conceitual comparativa para discutir os vieses socioeconômicos no Brasil, sem integração direta de dados por falta de chave geográfica comum (EUA vs. Brasil).
