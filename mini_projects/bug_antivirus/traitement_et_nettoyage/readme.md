# 📊 Analyse d’un Dataset de Bugs & Nettoyage Intelligent des Données

## 🎯 Objectif du Projet

Ce notebook a pour objectif d’explorer, d’analyser et d’améliorer la qualité d’un dataset de suivi de bugs.

Les objectifs principaux sont :

- Comprendre la structure du dataset  
- Identifier les catégories de bugs les plus critiques  
- Mettre en place un nettoyage intelligent des données basé sur une logique métier  

---

## 1️⃣ Exploration de la Structure du Dataset

```python
df.columns
df['severity'].unique()
df['bug_category'].unique()
```

### ➡️ Objectif

Cette étape permet de :

- Identifier les variables disponibles  
- Comprendre les dimensions principales des bugs  
- Explorer les différents niveaux de sévérité  
- Explorer les différentes catégories de bugs  

Elle fournit une vision globale de la structure des données avant d’effectuer des analyses plus approfondies.

---

## 2️⃣ Analyse de la Relation entre Sévérité et Catégorie

```python
grouped = df.groupby(['severity','bug_category'])
```

### ➡️ Objectif

Cette analyse permet de :

- Identifier quelles catégories génèrent les problèmes les plus critiques  
- Détecter les zones à risque élevé  
- Prioriser les efforts techniques en fonction de l’impact réel  

Le regroupement multi-dimensionnel permet une prise de décision basée sur les données.

---

## 3️⃣ Traitement Intelligent des Valeurs Manquantes

```python
df['error_code'] = (
    df.groupby(['severity', 'bug_category', 'tech_stack'])['error_code']
    .transform(lambda x: x.fillna(x.mode().iloc[0] if not x.mode().empty else x))
)
```

### 🎯 Objectif

- Remplacer les valeurs manquantes (`NaN`) dans la colonne `error_code`  
- Utiliser la valeur la plus fréquente (le mode)  
- Appliquer cette logique à un niveau granulaire pertinent métier :
  - `severity`
  - `bug_category`
  - `tech_stack`

### 💡 Pourquoi cette approche ?

Contrairement à un remplacement global, cette méthode :

- Préserve la cohérence contextuelle  
- Évite les biais statistiques  
- Respecte la logique métier  
- Améliore significativement la qualité des données  

---

## 🚀 Résultat Attendu

En combinant exploration structurée, analyse multi-dimensionnelle et nettoyage intelligent :

- La fiabilité du dataset est améliorée  
- Les patterns critiques sont identifiés  
- La priorisation technique est facilitée  
- Les données sont prêtes pour des analyses avancées ou des modèles prédictifs  
