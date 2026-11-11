## Changelog : benefriches (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois a été marqué par une refonte de la présentation des résultats, avec l'introduction du "Score de développement" qui remplace les anciens indicateurs. L'expérience utilisateur a été enrichie par de nouveaux guides lors de la saisie de données et par des rapports PDF plus complets et détaillés. Côté administration, de nouveaux outils de suivi permettent de mieux piloter l'utilisation de la plateforme et les exports réalisés.

### Évolutions fonctionnelles
- **Score de développement :**
    - Remplacement des indicateurs ZAN par le score de développement dans les vues d'impacts et les emails d'onboarding.
    - Ajout de modales descriptives pour chaque indicateur du score afin d'en faciliter la compréhension.
    - Intégration de nouveaux indicateurs considérés comme des "bonus" dans le calcul du score.
- **Amélioration des exports PDF :**
    - Enrichissement des rapports avec l'ajout de sous-titres, de descriptions, de valeurs détaillées et de la date d'export.
    - Inclusion des caractéristiques du site et du projet directement dans les exports.
- **Parcours de saisie et UX :**
    - Introduction de pages d'information sur les données manquantes lors des étapes de création de sites (zones urbaines, espaces) et de projets pour mieux guider l'utilisateur.
    - Amélioration de la navigation avec l'ajout de fils d'Ariane (breadcrumbs) dans les modales de score.
    - Correction de la gestion des formats numériques pour accepter la virgule décimale française.
    - Renommage de la route des caractéristiques en `/caracteristiques`.
- **Administration :**
    - Mise en place d'un suivi des exports d'impacts (liste des utilisateurs ayant exporté et visibilité dans la timeline).
    - Amélioration de la timeline utilisateur pour afficher les événements liés au cycle de vie des comptes (emails, etc.).

### Évolutions techniques
- **Tests et Qualité :**
    - Mise en place d'un "agent monkey" pour les tests de bout en bout (E2E) sur l'environnement de staging, permettant de simuler des comportements utilisateurs complexes de manière automatisée.
    - Automatisation des tests E2E en mode nocturne avec lecture automatique des emails de test.
- **Architecture et API :**
    - Migration et optimisation vers NestJS 12, incluant une meilleure gestion de la validation des requêtes (Standard Schema).
    - Optimisation de la base de données PostgreSQL via l'ajout d'index concurrents pour améliorer les performances.
    - Refactorisation du code pour centraliser les types et les énumérations partagées entre le front-end et le back-end.
- **CI/CD et DevOps :**
    - Automatisation de l'envoi des notes de version vers Microsoft Teams après un déploiement réussi en production.
    - Amélioration des outils de génération de notes de version assistés par IA.

### Autres changements
- **Documentation :** Mise à jour du glossaire métier et de la documentation des agents internes.
- **Nettoyage :** Suppression de dépendances et de scripts obsolètes (notamment `cookie-parser` et certains scripts d'administration).
