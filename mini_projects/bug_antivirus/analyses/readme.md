# 📊 Analyse Exploratoire des Incidents Logiciels

---

## 📁 1. Structure et Disposition des Données

Le dataset est organisé sous forme tabulaire, où chaque ligne représente un incident unique.

### 🔎 Variables principales utilisées dans l’analyse

- **severity** : niveau de gravité de l’incident *(variable catégorielle ordinale)*  
- **tech_stack** : technologie concernée *(variable catégorielle nominale)*  
- **bug_domain** : domaine fonctionnel impacté *(Backend, Frontend, etc.)*  
- **bug_category** : catégorie spécifique du bug  
- **error_code** : code spécifique associé à l’erreur  
- **mois** : variable temporelle indiquant le mois de l’incident  

Ces variables sont principalement **qualitatives**, ce qui oriente naturellement l’analyse vers :

- des méthodes de **comptage**
- des techniques d’**agrégation**
- des **visualisations adaptées aux données catégorielles**

---

## 🗂 2. Création de Variables Temporelles  
### Segmentation en Périodes

Afin d’introduire une dimension temporelle plus structurée, les données ont été divisées en **quatre sous-ensembles correspondant à des périodes de trois mois consécutifs** :

- **Février – Avril 2025**
- **Mai – Juillet 2025**
- **Août – Octobre 2025**
- **Novembre 2025 – Janvier 2026**

### ⚙️ Méthodologie

Cette division a été réalisée en filtrant la variable `mois` à l’aide de la méthode `isin()`, ce qui a permis de créer quatre DataFrames distincts :

- `fv_ap_25`
- `ma_jl_25`
- `ag_ou_25`
- `nv_jn_26`

### 🎯 Objectifs de la segmentation

- Comparer les périodes entre elles  
- Observer l’évolution des incidents  
- Identifier d’éventuels pics ou tendances saisonnières  
- Éviter qu’une analyse globale masque des variations importantes  

Cette approche introduit une **analyse temporelle comparative**, rendant l’étude plus dynamique.

---

## 🧹 3. Nettoyage des Données

La colonne `error_code` contenait des valeurs manquantes.

Plutôt que de supprimer ces lignes, une **imputation contextuelle** a été appliquée.

### 🔧 Méthode utilisée

Pour chaque combinaison de :

- `severity`
- `bug_category`
- `tech_stack`

Les valeurs manquantes ont été remplacées par **le code d’erreur le plus fréquent du groupe** (mode statistique).

### ✅ Pourquoi cette méthode ?

- Préserver la cohérence contextuelle  
- Limiter la perte d’information  
- Maintenir la structure statistique des groupes  

---

## 📈 4. Analyse des Distributions  
### Analyse Univariée

Une première analyse descriptive a été réalisée afin de comprendre la structure globale du dataset.

### 📊 Analyses effectuées

- Distribution des incidents par niveau de gravité  
- Distribution par domaine fonctionnel  
- Distribution par technologie  

Des **graphiques en barres (bar charts)** ont été utilisés car :

- Ils sont adaptés aux variables catégorielles  
- Ils permettent une lecture claire des fréquences  
- Ils facilitent la comparaison visuelle  

Cette étape permet d’obtenir une **vision globale** avant de croiser les variables.

---

## 🔄 5. Analyse Croisée  
### Analyse Bivariée

L’étape suivante a consisté à croiser les variables afin d’identifier des interactions significatives.

### ⚙️ Méthodologie

Un regroupement (`groupby`) a été effectué sur :

- `severity`
- `tech_stack`

Cela permet de :

- Compter le nombre d’incidents pour chaque combinaison  
- Trier les résultats par fréquence décroissante  
- Extraire les trois technologies les plus fréquentes pour chaque niveau de sévérité  

### 🎯 Objectif

Identifier les technologies les plus associées aux incidents critiques.

---

## 🔥 6. Visualisation avec Heatmap

Les résultats agrégés ont été transformés en matrice afin de créer une **heatmap**.

### 📌 Pourquoi une heatmap ?

Elle permet de :

- Représenter visuellement une matrice croisée  
- Mettre en évidence les zones de forte concentration  
- Faciliter la comparaison entre niveaux de gravité et technologies  

Cette visualisation aide à identifier rapidement les combinaisons critiques.

---

## 🧠 7. Interprétation des Résultats

L’analyse a mis en évidence :

- Une concentration importante d’incidents dans le **Backend**  
- Une forte présence d’**AWS** dans les incidents de sévérité élevée  
- La récurrence de certains codes d’erreur  

### ⚖️ Interprétation critique

Une fréquence élevée ne signifie pas nécessairement une instabilité technique.

Elle peut refléter :

- Un volume d’utilisation plus important  
- Une exposition plus forte dans l’architecture  
- Une centralisation des services  

---

# 🎯 Logique Globale de la Démarche

La méthodologie suivie repose sur une progression structurée :

1. Compréhension de la structure des données  
2. Création de segments temporels  
3. Nettoyage et fiabilisation  
4. Analyse descriptive  
5. Analyse croisée  
6. Visualisation  
7. Interprétation critique  

---

## ✅ Conclusion

Cette démarche montre une approche exploratoire complète, intégrant :

- La dimension temporelle  
- La gravité des incidents  
- Leur contexte technologique  

Elle démontre une analyse rigoureuse, structurée et cohérente, adaptée à un projet Data Science.
