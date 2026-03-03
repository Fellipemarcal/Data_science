# 📊 Feature Engineering – Création de Colonnes Catégorielles avec Pandas

La **transformation de variables numériques en variables catégorielles**.

L'objectif est de démontrer différentes méthodes de création de features catégorielles à partir d'une variable continue (`price_paid`) en utilisant Python et Pandas.

Ce notebook met en pratique :

- La création de fonctions personnalisées
- L'utilisation de `apply()`
- Les transformations vectorisées
- Les bonnes pratiques en Feature Engineering

---

## 🎯 Objectifs

- Comprendre la logique conditionnelle appliquée aux DataFrames
- Créer une nouvelle variable catégorielle
- Comparer performance et lisibilité entre plusieurs approches
- Appliquer les bonnes pratiques professionnelles

---

## 📊 Dataset

Le dataset contient notamment la variable :

- `price_paid` → montant payé par client

Exemple de données :

| price_paid |
|------------|
| 3.70       |
| 5.36       |
| 8.32       |
| 9.24       |

---

# 🧠 Méthode 1 – Création avec une fonction personnalisée + apply()

## 🔹 Étape 1 : Création de la fonction

```python
def prod_cher(i):
    if i < 4:
        return 'pas cher'
    elif i < 7:
        return 'cher'
    else:
        return 'très cher'
```

## 🔹 Étape 2 : Application sur la colonne

```python
df['classe_prod'] = df['price_paid'].apply(prod_cher)
```

---

## 📌 Logique de Classification

| Intervalle de prix | Catégorie |
|--------------------|-----------|
| < 4                | pas cher  |
| 4 ≤ prix < 7       | cher      |
| ≥ 7                | très cher |

---

## ✅ Avantages de cette méthode

- Simple à comprendre
- Très flexible
- Facile à adapter

## ❌ Inconvénients

- Non vectorisée
- Moins performante sur grands datasets
- Plus lente en production

---

# 🚀 Méthode 2 – Solution Optimisée avec pd.cut()

Une approche plus professionnelle consiste à utiliser `pd.cut()`.

```python
df["classe_prod"] = pd.cut(
    df["price_paid"],
    bins=[0, 4, 7, float("inf")],
    labels=["pas cher", "cher", "très cher"]
)
```

---

## ✅ Avantages

- Vectorisée
- Plus rapide
- Adaptée aux grands volumes de données
- Meilleure pratique en environnement professionnel

---

# ⚡ Comparaison des Méthodes

| Critère              | apply() | pd.cut() |
|----------------------|----------|----------|
| Lisibilité           | ✅        | ✅        |
| Performance          | ❌        | ✅        |
| Production Ready     | ⚠️        | ✅        |
| Scalabilité          | ❌        | ✅        |

---

# 📈 Validation des Résultats

Pour vérifier la distribution des classes :

```python
df['classe_prod'].value_counts()
```

Cette étape permet de :

- Vérifier l'équilibre des classes
- Identifier d'éventuels déséquilibres
- Préparer le dataset pour un modèle ML

---

# 🏗 Importance en Data Science

La transformation en variables catégorielles permet :

- Une meilleure interprétation des données
- Une réduction de la variance
- Une amélioration des performances des modèles
- Une simplification des analyses exploratoires

En pratique, le Feature Engineering représente souvent **70% du travail en Machine Learning**.

---

# 📚 Concepts Data Science Abordés

- Feature Engineering
- Variables catégorielles
- Transformation de données
- Vectorisation avec Pandas
- Optimisation de performance

---

# 🚀 Améliorations Possibles

- Encodage One-Hot (pd.get_dummies)
- Encodage ordinal
- Intégration dans un pipeline sklearn
- Benchmark de performance entre apply et vectorisation
- Analyse de corrélation avec la variable cible

---

# 🧪 Extension Possible (Pipeline ML)

Exemple d'intégration dans un pipeline :

```python
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
```

La version vectorisée (`pd.cut()`) représente la meilleure pratique pour des environnements professionnels et des datasets volumineux.

---

⭐ Si ce projet vous a aidé, n'hésitez pas à le star sur GitHub !

