<h1 align="center">🎬 Sistema de Recomendação em Python</h1>

<p align="center">
  <img src="https://media.giphy.com/media/26gssIytJvy1b1THO/giphy.gif" width="300" />
</p>

<p align="center">
  Um projeto Python que implementa um <b>sistema de recomendação de filmes</b> utilizando
  filtragem colaborativa e similaridade do cosseno.
</p>

<hr/>

<h2>🚀 Funcionalidades</h2>

<ul>
  <li>Importação e tratamento de dados de avaliações de usuários</li>
  <li>Criação da matriz usuário–item</li>
  <li>Cálculo da similaridade entre filmes</li>
  <li>Recomendações baseadas em filmes semelhantes</li>
  <li>Exemplo de uso com retorno de sugestões</li>
</ul>

<p>
  <img src="https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif" width="300"/>
</p>

<hr/>

<h2>🧠 Conceitos Importantes</h2>

<ul>
  <li><b>Sistema de Recomendação:</b> algoritmos que sugerem itens com base no perfil do usuário.</li>
  <li><b>Filtragem Colaborativa:</b> recomendações baseadas em comportamentos de usuários semelhantes.</li>
  <li><b>Matriz Usuário–Item:</b> representação das notas dadas pelos usuários a cada filme.</li>
  <li><b>Similaridade do Cosseno:</b> técnica usada para identificar filmes parecidos.</li>
</ul>

<hr/>

<h2>🛠️ Instalação</h2>

<h3>1. Clonar o repositório</h3>

<pre>
git clone https://github.com/Fellipemarcal/recommendation-system-python.git
cd recommendation-system-python
</pre>

<h3>2. Criar ambiente virtual</h3>

<pre>
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
</pre>

<h3>3. Instalar dependências</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr/>

<h2>▶️ Como Usar</h2>

<ol>
  <li>Coloque os arquivos <code>ratings.csv</code> e <code>movies.csv</code> dentro da pasta <b>data/</b>.</li>
  <li>Execute o script principal:</li>
</ol>

<pre>
python recommendation.py
</pre>

<p>Edite o nome do filme no código para testar recomendações diferentes.</p>

<hr/>

<h2>📌 Exemplo de Código (Função de Recomendação)</h2>

<pre>
def recommend_similar(movie_title, df, X, movie_mapper, movie_inv_mapper, k=5):
    movie_id = df[df['title'] == movie_title]['movieId'].iloc[0]
    movie_idx = movie_mapper[movie_id]
    movie_vec = X[movie_idx]

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(X)
    distances, indices = model.kneighbors(movie_vec, n_neighbors=k + 1)

    neighbor_ids = [movie_inv_mapper[i] for i in indices.flatten()[1:]]
    recommendations = df[df['movieId'].isin(neighbor_ids)]['title'].unique()

    print(f"\nPorque você gostou de {movie_title}, talvez você também curta:")
    for rec in recommendations:
        print(f"- {rec}")
</pre>

<hr/>

<h2>📈 Aplicações</h2>

<ul>
  <li>Plataformas de streaming (Netflix, Prime Video, Spotify)</li>
  <li>E-commerce (produtos recomendados)</li>
  <li>Redes sociais (conteúdo personalizado)</li>
  <li>Educação online (cursos recomendados)</li>
</ul>

<hr/>

<h2>📦 Tecnologias Utilizadas</h2>

<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Matplotlib (opcional para gráficos)</li>
</ul>

<hr/>

<h2>📄 Licença</h2>

<p>MIT — fique à vontade para usar, modificar e distribuir.</p>

<hr/>

<h3 align="center">✨ Desenvolvido com Python e Machine Learning</h3>

<p align="center">
  <img src="https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif" width="200"/>
</p>

