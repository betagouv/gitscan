## Changelog : simplifions (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci est marqué par une refonte majeure de l'interface d'administration, offrant désormais une gestion complète du catalogue (CRUD) et un nouveau système de brouillons permettant de préparer et prévisualiser les contenus avant leur publication. L'importation de données depuis Grist a été sécurisée et l'expérience utilisateur a été enrichie par une meilleure traçabilité et une interface plus intuitive.

### Évolutions fonctionnelles

- **Administration du catalogue**
  - Mise en place d'une gestion complète (création, modification, suppression) de tous les éléments du catalogue via une nouvelle interface d'administration [#57](https://github.com/datagouv/simplifions/pull/57).
  - Introduction d'un système de **brouillons** pour les démarches et les solutions, permettant de travailler sur des modifications sans affecter le contenu publié.
  - Amélioration de l'importation de données depuis Grist avec un meilleur signalement des erreurs et une validation plus stricte des formats d'images.
  - Ajout d'un historique détaillé pour chaque fiche (auteur, date, source de modification comme Grist ou data.gouv).
  - Refonte des formulaires utilisant le Design System (DSFR) pour une saisie plus guidée et une meilleure gestion des erreurs en français.
  - Amélioration de la navigation administrative (connexion/déconnexion, fil d'Ariane, accès direct aux rubriques).

- **Expérience utilisateur (Public)**
  - Amélioration des "Cartes de vérification" avec la possibilité de prévisualiser des brouillons et de gérer les éléments liés de manière plus fluide.
  - Enrichissement des informations sur les API avec l'affichage de données réelles issues de data.gouv [#36](https://github.com/datagouv/simplifions/pull/36).
  - Optimisation de l'interface : ajout d'infobulles [#51](https://github.com/datagouv/simplifions/pull/51), amélioration des filtres de recherche et de la pagination.
  - Amélioration de la présentation des articles et des cas d'usage [#47](https://github.com/datagouv/simplifions/pull/47).

### Évolutions techniques

- **Gestion des tâches et automatisation**
  - Installation de `Solid Queue` pour la gestion des tâches de fond.
  - Automatisation du rafraîchissement nocturne du catalogue (Grist et data.gouv) à 3h du matin pour garantir la fraîcheur des données.

- **Qualité logicielle et CI/CD**
  - Renforcement de l'intégrité de la base de données avec l'intégration de `strong_migrations` et `active_record_doctor` pour détecter les écarts entre le schéma et les modèles.
  - Amélioration de la CI pour garantir la cohérence des migrations avant l'exécution des tests.

- **Observabilité**
  - Optimisation du suivi des erreurs avec Sentry, incluant désormais les environnements de staging, de production et les échecs d'importation [#54](https://github.com/datagouv/simplifions/pull/54).

### Autres changements

- Nettoyage du code et retrait de fonctionnalités obsolètes (ancienne recette de parité, espaces de discussion).
- Mise à jour du pied de page avec l'ajout des logos officiels (data.gouv et numerique.gouv).
