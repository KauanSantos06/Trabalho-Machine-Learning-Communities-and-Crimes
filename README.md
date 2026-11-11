# 📊 Trabalho-Machine-Learning-Communities-and-Crimes

**Tema:** Análise e Predição da Taxa de Criminalidade por Comunidade
**Disciplina:** Aprendizagem de Máquina
**Docente:** Prof. Rodrigo Gonçalves Pinto
**Integrantes:** Artur Martins, Guilherme Gomes, Kauan Santos

## 🎯 Objetivo do Projeto
Este projeto aplica o fluxo completo de Machine Learning sobre o dataset público **"Communities and Crime"** (UCI Machine Learning Repository). O foco central é analisar as variáveis socioeconômicas e prever a taxa de crimes violentos por 100 mil habitantes (`ViolentCrimesPerPop`).

Conforme as diretrizes atualizadas da disciplina, o escopo do projeto foi focado na aplicação e interpretação da **Regressão Linear Múltipla**, comparando seu desempenho contra um modelo de referência (Baseline) e validando os pressupostos estatísticos através da análise de resíduos.

## 📁 Estrutura do Repositório
Para facilitar a execução e a avaliação, todo o fluxo de trabalho foi consolidado em um único arquivo:

- `Projeto_AM_Completo.ipynb`: Notebook principal contendo todas as etapas (Obtenção de Dados, EDA, Pré-processamento, Split, Baseline, Regressão Linear e Validação).
- `requirements.txt`: Dependências do projeto (bibliotecas e versões).
- `AUTORES.md`: Declaração da divisão de responsabilidades da equipe.
- `scripts/download_data.py`: Script auxiliar para baixar o dataset original da UCI.
- `.gitignore`: Arquivo para evitar o envio de pastas desnecessárias e arquivos temporários.

## ⚙️ Como Reproduzir o Projeto (Passo a Passo)

O projeto foi desenhado para rodar perfeitamente no **Google Colab**, com fallback automático para execução local.

**Passo 1:** Abra o arquivo `Projeto_AM_Completo.ipynb` no Google Colab.
**Passo 2:** No menu superior, clique em **`Ambiente de execução` > `Executar tudo`** (Run all).
**Passo 3:** O próprio notebook gerenciará a obtenção dos dados:
   - Ele tentará buscar os arquivos na pasta `/content/drive/MyDrive/MachineLearning2026/dados`.
   - Caso os arquivos não existam (ex: rodando na máquina de outro professor/aluno), o código fará o **download automático** direto do repositório da UCI e salvará na memória.
**Passo 4:** O notebook executará todas as etapas em sequência: Limpeza -> EDA -> Split (70/15/15) -> Padronização (sem vazamento) -> Baseline -> Regressão Linear -> Análise de Resíduos.

## 🔬 Metodologia e Resultados Esperados
- **Baseline (DummyRegressor):** Prevê sempre a média da criminalidade. Serve como nosso "piso" de performance (RMSE ≈ 0.21).
- **Regressão Linear Múltipla:** Modelo escolhido para produção devido à sua **alta interpretabilidade**. Ele permitirá afirmar, com base nos coeficientes, o peso exato de variáveis como pobreza e desemprego na criminalidade.
- **Protocolo Rigoroso:** Semente global fixada (`SEED=42`) e padronização (`StandardScaler`) ajustada estritamente nos dados de treino para evitar vazamento de dados (Data Leakage).


