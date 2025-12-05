import streamlit as st
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# =========================
# CHARGEMENT DES DONNÉES
# =========================
df = pd.read_csv("ratings.csv")

# =========================
# TON MODÈLE (INCHANGÉ)
# =========================
def create_matrix(df):
    user_mapper = {u: i for i, u in enumerate(df["userId"].unique())}
    movie_mapper = {m: i for i, m in enumerate(df["movieId"].unique())}
    movie_inv_mapper = {i: m for m, i in movie_mapper.items()}

    user_index = df["userId"].map(user_mapper)
    movie_index = df["movieId"].map(movie_mapper)

    X = csr_matrix(
        (df["rating"], (movie_index, user_index)),
        shape=(len(movie_mapper), len(user_mapper))
    )

    return X, movie_mapper, movie_inv_mapper


def recommend_similar(movie_title, df, X, movie_mapper, movie_inv_mapper, k=5):
    if movie_title not in df["title"].values:
        return []

    movie_id = df[df["title"] == movie_title]["movieId"].iloc[0]
    movie_idx = movie_mapper[movie_id]

    model = NearestNeighbors(metric="cosine", algorithm="brute")
    model.fit(X)

    distances, indices = model.kneighbors(
        X[movie_idx], n_neighbors=k + 1
    )

    recommendations = []
    for idx in indices.flatten()[1:]:
        rec_movie_id = movie_inv_mapper[idx]
        rec_title = df[df["movieId"] == rec_movie_id]["title"].iloc[0]
        recommendations.append(rec_title)

    return recommendations


# =========================
# INTERFACE STREAMLIT
# =========================
st.set_page_config(page_title="Recommandation de films", layout="centered")

st.title("🎬 Système de recommandation de films")
st.write("Basé uniquement sur ratings.csv")

# Création de la matrice UNE FOIS
X, movie_mapper, movie_inv_mapper = create_matrix(df)

movie_choice = st.selectbox(
    "🎥 Choisis un film :",
    sorted(df["title"].unique())
)

k = st.slider("Nombre de recommandations", 1, 5, 3)

if st.button("🔍 Recommander"):
    results = recommend_similar(
        movie_choice, df, X, movie_mapper, movie_inv_mapper, k
    )

    st.subheader("✅ Films recommandés")
    for movie in results:
        st.write("•", movie)
