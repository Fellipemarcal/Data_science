<section>
  <h1 style="text-align:center;">🧠 Explicação da Rede Neural Convolucional (CNN)</h1>

  <p>
    Esta rede neural convolucional (CNN) é usada para <strong>classificação de imagens</strong>.  
    Ela aprende padrões visuais através de camadas de convolução e pooling, até conseguir identificar objetos complexos.
  </p>

  <!-- GIF 1 – visão geral CNN -->
  <div style="text-align:center;">
    <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="350" alt="CNN animation">
    <p><em>Como uma CNN aprende padrões visuais.</em></p>
  </div>

  <h2>📌 Arquitetura Geral</h2>

  <ul>
    <li>4 blocos de Convolução + Pooling</li>
    <li>Flatten</li>
    <li>Camada Densa de 512 neurônios</li>
    <li>ReLU para ativação</li>
    <li>Softmax para classificação final (5 classes)</li>
  </ul>

  <h2>🔍 Explicação Camada por Camada</h2>

  <h3>1️⃣ Entrada (224 × 224 × 3)</h3>
  <p>
    A rede recebe imagens coloridas com 224 pixels de altura e largura.
  </p>

  <div style="text-align:center;">
    <img src="https://media.giphy.com/media/Q8xuJjjxQYfwj2s7jv/giphy.gif" width="260" alt="Image pixels">
    <p><em>Uma imagem sendo processada em forma de matriz.</em></p>
  </div>

  <h3>2️⃣ Conv2D + ReLU</h3>
  <p>
    A convolução aplica filtros para encontrar padrões básicos como bordas, linhas e texturas.
  </p>

  <div style="text-align:center;">
    <img src="https://i.imgur.com/0Z6FQYB.gif" width="430" alt="Convolution filter animation">
    <p><em>Exemplo de um filtro convolucional percorrendo a imagem.</em></p>
  </div>

  <h3>3️⃣ MaxPooling2D</h3>
  <p>
    Reduz a dimensão da imagem, mantendo apenas os valores mais importantes.
  </p>

  <div style="text-align:center;">
    <img src="https://i.imgur.com/o7k1jW9.gif" width="300" alt="Max pooling animation">
    <p><em>Pooling reduzindo a resolução.</em></p>
  </div>

  <h3>🌀 Repetição dos blocos Conv + Pool</h3>
  <p>
    A CNN repete esse processo várias vezes.  
    A cada bloco, a rede aprende padrões cada vez mais complexos:
  </p>

  <ul>
    <li><strong>1º bloco</strong>: bordas e formas simples</li>
    <li><strong>2º bloco</strong>: curvas, texturas</li>
    <li><strong>3º bloco</strong>: partes de objetos</li>
    <li><strong>4º bloco</strong>: objetos inteiros</li>
  </ul>

  <div style="text-align:center;">
    <img src="https://media.giphy.com/media/kEKcOWl8RMLde/giphy.gif" width="260" alt="Feature extraction gif">
    <p><em>Extração progressiva de características.</em></p>
  </div>

  <h3>6️⃣ Flatten</h3>
  <p>
    Transforma o mapa de características final em um vetor 1D para alimentar a camada totalmente conectada.
  </p>

  <div style="text-align:center;">
    <img src="https://i.imgur.com/SWfYxL9.gif" width="320" alt="Flatten layer gif">
    <p><em>Transformando o mapa 2D em vetor 1D.</em></p>
  </div>

  <h3>7️⃣ Dense (512 neurônios)</h3>
  <p>
    Combina todas as características aprendidas e prepara a decisão final.
  </p>

  <h3>8️⃣ Dense Final (5 classes, Softmax)</h3>
  <p>
    Produz uma probabilidade para cada classe.  
    A classe com maior probabilidade é a predição.
  </p>

  <div style="text-align:center;">
    <img src="https://i.imgur.com/rVnY6Yc.gif" width="330" alt="Classification softmax gif">
    <p><em>Softmax transformando scores em probabilidades.</em></p>
  </div>

  <h2>🎯 Resumo</h2>
  <p>
    <strong>
      Imagem → Convoluções → Pooling → Extração de características → Flatten → Classificação Softmax.
    </strong>
  </p>

  <div style="text-align:center;">
    <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="330" alt="Deep learning summary">
    <p><em>Fluxo completo do deep learning.</em></p>
  </div>

</section>

