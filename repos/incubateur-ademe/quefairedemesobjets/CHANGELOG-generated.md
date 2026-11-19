## Changelog : quefairedemesobjets (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois a été marqué par une étape majeure : le déploiement général de l'Assistant V2, offrant une expérience utilisateur plus fluide et performante. Parallèlement, l'interface d'administration a été profondément modernisée pour faciliter la gestion des suggestions de données, et les capacités d'Open Data ont été étendues via de nouvelles API.

### Évolutions fonctionnelles
- **Déploiement de l'Assistant V2** : Basculement complet de tous les composants intégrés (iframes) vers la nouvelle version de l'assistant [#3655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3655).
- **Nouvelles fonctionnalités de l'Assistant** : Ajout de fiches de lieux avec géolocalisation [#3577](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3577), d'un nouveau parcours utilisateur (accueil, fiche, solutions, carte) [#3576](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3576) et de nouveaux champs de recherche [#3575](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3575).
- **Refonte de l'administration** : Mise en place d'une nouvelle interface de gestion des suggestions basée sur Django et React [#3488](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3488), incluant des actions de masse [#3493](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3493), la gestion par cohortes [#3489](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3489) et un accès direct à la revue des suggestions [#3694](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3694).
- **Améliorations de l'expérience utilisateur** : Optimisation de la rapidité de la carte et des visuels de l'assistant [#3645](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3645), correction des débordements d'iframes sur mobile [#3635](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3635) et amélioration de l'accessibilité des modales [#3590](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3590).
- **Corrections** : Résolution d'un bug de crash de la liste des labels sous Django 6.1 [#3664](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3664) et rétablissement de la géolocalisation lors des redirections d'iframes [#3498](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3498).

### Évolutions techniques
- **Intelligence Artificielle & Données** : Mise en œuvre d'une approche Machine Learning pour la déduplication des acteurs [#3176](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3176) et extension de l'Open Data (lieux, produits, consignes) via l'API v1 et le stockage S3 [#3517](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3517), [#3444](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3444).
- **Infrastructure & DevOps** : 
    - Optimisation massive de la CI/CD (GitHub Actions) pour réduire les temps de build et améliorer la fiabilité (parallélisation des tests, gestion intelligente du cache) [#3593](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3593), [#3586](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3586).
    - Renforcement de la sécurité via le scan des images Docker avec Trivy [#3665](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3665).
    - Déploiement d'un serveur Nginx serverless pour sécuriser l'accès à Metabase et aux API Airflow [#3446](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3446).
- **Architecture Backend** : Migration vers une nouvelle structure de données pour la gestion des suggestions de clusters [#3536](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3536) et intégration de PostHog pour le suivi analytique de l'assistant [#3666](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3666).

### Autres changements
- **Documentation** : Mise à jour de la documentation pour la nouvelle interface d'administration [#3494](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3494).
- **Nettoyage** : Suppression de dépendances inutilisées [#3584](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3584) et retrait des notifications Mattermost [#3558](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3558).
- **Refactoring** : Renommage de fichiers pour une meilleure cohérence du projet (qfdmd.ts vers quefaire.ts) [#3574](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3574).
