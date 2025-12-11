<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2c2NzBqbzd2c3B2dzE3ZzFyNTZkbDg1OHZoMmlyb2t0eDFlanRnaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="180" />
</p>

<h1 align="center">📈 Sales Forecasting Project</h1>
<h3 align="center">Previsão de Vendas • Machine Learning • Séries Temporais</h3>

---

## 📌 Sobre este projeto

Este repositório contém um projeto completo de **previsão de vendas (Sales Forecasting)** utilizando Python e técnicas de Machine Learning aplicadas a **séries temporais**.

O objetivo é desenvolver um modelo capaz de:
- Entender padrões históricos de vendas  
- Identificar comportamentos sazonais  
- Criar variáveis temporais para melhorar a previsão  
- Prever valores futuros com boa acurácia  

Este projeto foi desenvolvido como parte do meu aprendizado contínuo em **Ciência de Dados** e **engenharia de machine learning**.

---

## 🎯 Objetivos do projeto

- ✔️ Preparar e limpar dados reais de vendas  
- ✔️ Criar *features* avançadas (lags, médias móveis, tendências)  
- ✔️ Comparar modelos e estratégias preditivas  
- ✔️ Avaliar métricas como RMSE e MAPE  
- ✔️ Gerar gráficos claros e interpretáveis  
- ✔️ Salvar previsões e resultados visualmente  

---

## 🧠 Como funciona o modelo?

O fluxo principal segue estas etapas:

1. **Carregamento dos dados**  
   O dataset é carregado de arquivos CSV na pasta `data/`.

2. **Pré-processamento da série temporal**  
   - Conversão de datas  
   - Ordenação temporal  
   - Criação de variáveis defasadas (*lag features*)  
   - Criação de médias móveis (opcional)

3. **Divisão entre treino e teste**

4. **Treinamento do modelo**  
   O projeto utiliza:
   - **XGBoost Regressor**  
   (Ótimo para séries temporais estruturadas)

5. **Avaliação de desempenho**  
   Métricas incluídas:
   - RMSE (Root Mean Squared Error)  
   - MAE (Mean Absolute Error)

6. **Previsão e visualização**  
   Gera gráficos como:
   - Vendas Reais vs. Previsões  
   - Linha do tempo com tendências  

---

## 📂 Estrutura do repositório

```bash
📁 Sales_Forecasting
 ├── 📁 data
 │    └── train.csv               # Dataset de vendas
 ├── 📁 src
 │    ├── analyse.ipynb           # Limpeza e preparação dos dados                   
 ├── 📁 results
 │    ├── predictions.png         # Gráficos gerados
 │    └── model.pkl               # Modelo treinado
 └── 📄 README.md

