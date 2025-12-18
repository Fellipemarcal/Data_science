<!DOCTYPE html>
<html lang="pt-BR">
<body style="font-family: Arial, sans-serif; line-height:1.6;">

<h1 align="center">📈 Previsão de Preço do Bitcoin com Machine Learning</h1>

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="280" alt="Bitcoin Machine Learning">
</p>

<p>
  Este projeto implementa um modelo de <strong>Machine Learning em Python</strong> para prever o preço futuro do <strong>Bitcoin (BTC)</strong> com base em dados históricos.
  A ideia é treinar um modelo preditivo que aprenda tendências e padrões dos preços passados para estimar valores futuros.
</p>

<hr/>

<h2>🔍 Visão Geral</h2>

<ul>
  <li>Extração de dados históricos de preços</li>
  <li>Pré-processamento dos dados</li>
  <li>Construção de um modelo de regressão</li>
  <li>Avaliação da performance do modelo</li>
  <li>Predição de preços futuros</li>
</ul>

<p align="center">
  <img src="https://media.giphy.com/media/3oKIPwoeGErMmaI43S/giphy.gif" width="280" alt="Machine Learning Process">
</p>

<hr/>



<h2>🚀 Tecnologias Utilizadas</h2>

<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Matplotlib & Seaborn</li>
  <li>scikit-learn</li>
  <li>Jupyter Notebook (opcional)</li>
</ul>

<hr/>

<h2>🛠️ Instalação</h2>

<h3>1. Clonar o repositório</h3>
<pre>
git clone https://github.com/seuusuario/bitcoin-price-prediction.git
cd bitcoin-price-prediction
</pre>

<h3>2. Criar ambiente virtual</h3>
<pre>
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
</pre>

<h3>3. Instalar dependências</h3>
<pre>
pip install -r requirements.txt
</pre>

<hr/>

<h2>📊 Pré-processamento dos Dados</h2>

<p>
Os dados históricos do Bitcoin são carregados, limpos e transformados em um formato que o modelo consegue interpretar:
</p>

<ul>
  <li>Remover valores faltantes</li>
  <li>Selecionar features relevantes</li>
  <li>Escalar os dados</li>
</ul>

<p align="center">
  <img src="https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif" width="260" alt="Data preprocessing gif">
</p>

<hr/>

<h2>📈 Treinamento do Modelo</h2>

<p>
O modelo de regressão é treinado usando dados históricos.  
Após o ajuste, ele tenta aprender tendências que permitirão prever futuros valores do preço.
</p>

<pre>
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
</pre>

---

<h2>📉 Avaliação</h2>

<ul>
  <li>Métricas como MSE (Mean Squared Error)</li>
  <li>Comparação entre valores reais e previstos</li>
</ul>

<p align="center">
  <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" width="260" alt="Model Evaluation">
</p>

<hr/>

<h2>📅 Previsão de Preços</h2>

<p>
Uma vez treinado, o modelo pode gerar previsões para valores futuros de Bitcoin com base em dados recentes:
</p>

<pre>
predictions = model.predict(X_new)
</pre>

<hr/>

<h2>📌 Considerações Finais</h2>

<p>
Este projeto serve como um exemplo introdutório de como aplicar Machine Learning para prever séries temporais como preço de criptomoeda.
Não deve ser usado para decisões financeiras reais sem uma análise aprofundada.
</p>

<p align="center">
  <img src="https://media.giphy.com/media/oYtVHSxngR3lC/giphy.gif" width="300" alt="Trading is risky">
</p>

<hr/>

<h2>📄 Licença</h2>
<p>
MIT — fique à vontade para usar, modificar ou redistribuir.
</p>

<hr/>

<p align="center">
  ⭐ Desenvolvido com Python e Machine Learning!
</p>

</body>
</html>

