# 📊 Analyse Bug et Problèmes Informatiques 

---

## 📌 Présentation du Projet

Ce projet a pour objectif d’analyser un dataset d’incidents logiciels classifiés selon :

* Le niveau de sévérité
* Le domaine fonctionnel
* La technologie concernée (tech stack)
* Le type de bug
* Le code d’erreur associé

L’objectif principal est d’identifier les zones critiques du système et de dégager des axes d’amélioration basés sur les données.

---

## 🎯 Objectifs de l’Analyse

* Identifier les technologies les plus exposées aux incidents
* Déterminer les domaines fonctionnels les plus critiques
* Analyser les combinaisons à risque entre sévérité et stack technique
* Mettre en évidence les codes d’erreur récurrents
* Fournir une base pour une future modélisation prédictive

---

## 🗂 Description du Dataset

Le dataset contient les variables suivantes :

* **severity** → Niveau de gravité (Low, Medium, High, Critical)
* **tech_stack** → Technologie concernée
* **bug_category** → Type de problème
* **bug_domain** → Domaine fonctionnel impacté
* **error_code** → Code spécifique d’erreur

Les données couvrent plusieurs périodes, permettant une analyse comparative.

---

## 🧹 Préparation des Données

### 🔎 Traitement des Valeurs Manquantes

Certaines valeurs NULL étaient présentes dans la colonne `error_code`.

Une imputation par **mode conditionnel** a été appliquée :

Pour chaque combinaison `(severity, bug_category, tech_stack)`, les valeurs manquantes ont été remplacées par le code d’erreur le plus fréquent observé dans ce groupe.

✔ Préservation de la cohérence contextuelle
✔ Réduction du biais statistique
✔ Maintien de la logique métier

---

## 📊 Analyses Réalisées

### 🔹 Distribution des Incidents par Sévérité

L’analyse montre qu’une proportion significative des incidents appartient aux catégories **High** et **Critical**, indiquant un impact opérationnel important.

---

### 🔹 Analyse par Domaine Fonctionnel

Le domaine **Backend** concentre une part importante des incidents critiques.

Cela suggère :

* Une complexité technique plus élevée
* Une forte interconnexion des composants
* Un rôle central dans l’architecture

---

### 🔹 Analyse par Technologie (Tech Stack)

Certaines technologies apparaissent plus fréquemment associées à des incidents de haute sévérité.

---

### 🔥 Focus Spécifique : AWS

Un point notable de l’analyse concerne **AWS**, qui apparaît de manière récurrente parmi les technologies les plus associées aux incidents **High** et **Critical**.

Plusieurs hypothèses peuvent expliquer cette concentration :

* Forte dépendance à l’infrastructure cloud
* Architecture distribuée complexe (microservices, IAM, services managés)
* Volume d’utilisation potentiellement supérieur aux autres stacks
* Intégration fréquente avec les systèmes Backend critiques

⚠ Important :
Une fréquence élevée d’incidents liés à AWS ne signifie pas nécessairement une instabilité intrinsèque de la technologie. Sans indicateur de volume d’utilisation, cette concentration peut simplement refléter une plus grande exposition.

---

### 🔹 Analyse des Codes d’Erreur

Certains `error_code` apparaissent de manière récurrente sur plusieurs périodes.

Cela suggère l’existence de problèmes structurels plutôt que ponctuels.

---

## 📌 Insights Clés

* Les incidents critiques sont concentrés sur certaines combinaisons spécifiques.
* Le domaine Backend représente une zone prioritaire d’amélioration.
* AWS est fortement exposée aux incidents critiques.
* Certains codes d’erreur sont structurellement récurrents.

---

## 🚀 Apports Stratégiques

Cette analyse permet de :

* Prioriser les efforts de correction
* Identifier les technologies à surveiller
* Orienter les audits techniques
* Préparer une future modélisation prédictive de la sévérité

---

## 🏁 Conclusion

Ce projet dépasse une simple description statistique des incidents. Il met en lumière des zones critiques au sein de l’architecture logicielle et fournit des éléments concrets pour orienter des décisions d’amélioration technique et stratégique.

Il constitue une base solide pour :

* Une optimisation continue des systèmes
* Une meilleure gestion proactive des incidents
* Le développement futur d’outils prédictifs

---

## 📈 Perspectives Futures

* Modèle de classification pour prédire la sévérité
* Analyse temporelle avancée
* Étude de corrélation plus approfondie
* Mise en place d’indicateurs de performance (KPIs)

---

📎 Projet réalisé dans le cadre d’une analyse exploratoire Data Science (EDA).

