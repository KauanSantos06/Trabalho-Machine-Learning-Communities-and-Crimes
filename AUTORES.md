# 👥 Divisão de Responsabilidades (Frentes de Trabalho)

O projeto foi dividido em três frentes técnicas complementares, conforme as diretrizes da disciplina.

### 👤 Integrante A (Dados e Análise Exploratória)
**Responsável por:** Kauan Nascimento dos Santos
- Obtenção, documentação e descrição do conjunto de dados (Ficha Técnica).
- Análise Exploratória (EDA): distribuições, correlações, outliers e balanceamento.
- Pré-processamento: tratamento de NaNs, imputação, remoção de IDs.
- Definição do protocolo experimental: Split 70/15/15 e padronização sem vazamento.
- Construção do modelo de referência (Baseline).

### 👤 Integrante B (Modelos Interpretáveis e Regressão Linear)
**Responsável por:** Artur Martins
- Aplicação da Regressão Linear Múltipla.
- Análise dos coeficientes de regressão (interpretabilidade para o domínio).
- Diagnóstico de resíduos (Homocedasticidade e Normalidade via QQ-Plot).
- Verificação dos pressupostos estatísticos do modelo linear.

### 👤 Integrante C (Avaliação Comparativa e Validação)
**Responsável por:** Guilherme Gomes
- Avaliação do modelo via Validação Cruzada K-Fold.
- Cálculo de métricas com média e desvio padrão (estabilidade do modelo).
- Quadro comparativo final (Baseline vs. Regressão Linear).
- Análise de limitações, riscos e uso do Atlas Brasileiro como referência cruzada.

---
*Todos os integrantes participaram da revisão do código e estão aptos a explicar qualquer etapa do fluxo de trabalho na arguição.*
