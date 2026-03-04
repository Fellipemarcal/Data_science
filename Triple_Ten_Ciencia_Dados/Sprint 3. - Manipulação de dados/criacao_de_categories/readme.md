# 📊 Création de Catégories Dynamiques avec Pandas

Nous allons :

- Créer un DataFrame
- Définir une fonction de classification
- Appliquer cette fonction à chaque ligne
- Générer une nouvelle colonne catégorielle

---

## 📦 Technologies Utilisées

- Python 3  
- Pandas  

---

## 📁 Structure du Notebook

Le notebook suit les étapes suivantes :

1. Importation de la bibliothèque
2. Création d’un DataFrame
3. Création d’une fonction de catégorisation
4. Application de la fonction
5. Analyse du résultat final

---

# 🔹 1. Importation de Pandas

```python
import pandas as pd
```

# 🔹 2. Création du DataFrame

```python
nom = ['Fellipe', 'Joao','Maria', 'Fernanda']
age = [21,40,33,60]
rev = [19000,13000,6000, 9000]

df = pd.DataFrame({
    'nom': nom,
    'age': age,
    'rev': rev
})
```

## 📌 Explication

Nous créons trois listes :

- `nom` → nom des clients  
- `age` → âge des clients  
- `rev` → revenu des clients  

Puis nous construisons un **DataFrame** à partir de ces listes.

## 📊 Résultat Initial

| nom      | age | rev   |
|----------|-----|-------|
| Fellipe  | 21  | 19000 |
| Joao     | 40  | 13000 |
| Maria    | 33  | 6000  |
| Fernanda | 60  | 9000  |

---

# 🔹 3. Création d'une Fonction de Profil Client

```python
def profil_client(row):  # row représente une ligne du DataFrame
    if row["rev"] > 5000 and row["age"] < 30:
        return "jeune_rich"
    else:
        return "standard"
```

## 📌 Explication

- La fonction reçoit **une ligne complète** du DataFrame.
- Elle vérifie deux conditions :
  - Revenu > 5000
  - Âge < 30
- Si les deux conditions sont vraies → retourne `"jeune_rich"`
- Sinon → retourne `"standard"`

## 🎯 Logique Métier

Cette règle permet une segmentation simple :

- **jeune_rich** → jeunes clients avec revenu élevé  
- **standard** → tous les autres clients  

---

# 🔹 4. Application de la Fonction

```python
df["profil"] = df.apply(profil_client, axis=1)
```

## 📌 Explication Importante

- `df.apply()` applique une fonction personnalisée.
- `axis=1` signifie que l'on travaille **ligne par ligne**.
- Le résultat est enregistré dans une nouvelle colonne appelée `"profil"`.

---

# 🔹 5. Résultat Final

```python
df
```

## 📊 DataFrame Final

| nom      | age | rev   | profil      |
|----------|-----|-------|-------------|
| Fellipe  | 21  | 19000 | jeune_rich  |
| Joao     | 40  | 13000 | standard    |
| Maria    | 33  | 6000  | standard    |
| Fernanda | 60  | 9000  | standard    |

---

# 🧩 Concepts Clés Démontrés

- Création d’un DataFrame  
- Utilisation de fonctions personnalisées  
- Manipulation ligne par ligne  
- Création de colonnes catégorielles  
- Logique conditionnelle avec `if`  

---

# 🚀 Importance en Data Science

Cette technique est très utilisée en :

- Data Science  
- Machine Learning  
- Analyse Marketing  
- Segmentation Client  
- Feature Engineering  

Elle permet de transformer des données brutes en **variables analytiques exploitables**.

---

# ⚡ Optimisation (Méthode Vectorisée)

Pour de grands volumes de données, `apply()` peut être lent.  
Une alternative plus performante utilise une approche vectorisée :

```python
df["profil"] = "standard"
df.loc[(df["rev"] > 5000) & (df["age"] < 30), "profil"] = "jeune_rich"
```

Cette méthode est plus rapide car elle exploite l’optimisation interne de `pandas`.

