## Changelog : csplab (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante en renforçant sa sécurité grâce au déploiement d'un système de gestion des droits d'accès (RBAC) et en enrichissant considérablement la précision des données ingérées (référentiels métiers, localisation). L'expérience utilisateur a également été fluidifiée par l'ajout de capacités de filtrage étendues et une modernisation de l'interface de gestion des recrutements.

### Évolutions fonctionnelles
- **Amélioration massive des capacités de filtrage** : Ajout de filtres avancés pour les offres (localisation par rayon/coordonnées, domaine, organisme, date de publication, type de contrat, niveau d'expérience, lieu de travail et management) [#1100, #1099, #1098, #1097, #1092, #1091, #1079, #1078, #1077, #1075].
- **Optimisation de la gestion des recrutements** : Amélioration de l'interface Kanban (défilement automatique, gestion des étapes du pipeline) et ajout d'un système de gestion des notes [#1107, #1105, #1088, #1050, #1048, #879, #878].
- **Gestion des candidatures** : Intégration de nouvelles vues dédiées et ajout de fonctions de recherche et de filtrage pour les candidatures [#977, #946, #947].
- **Améliorations UX** : Corrections de l'affichage (largeur des barres de recherche, débordements du Kanban) et amélioration de la navigation générale [#1104, #1102, #1094].

### Évolutions techniques
- **Sécurité et accès (RBAC)** : Mise en place complète du contrôle d'accès basé sur les rôles pour sécuriser la création d'organismes, la consultation des listes et la modification des pipelines de recrutement [#1069, #1054, #1030, #1026, #1025, #1020, #1002, #1027].
- **Enrichissement de l'ingestion de données** : Intégration du référentiel RMFPv2, amélioration du mapping des niveaux d'études et des types de contrats (notamment pour Talentsoft et l'ARS), et prise en compte des coordonnées GPS [#1095, #1081, #1049, #1047, #1046, #970, #969, #968].
- **Optimisation de l'API** : Amélioration de la gestion du débit (throttling) via Redis, ajout d'en-têtes de limitation de débit (RateLimit) et création d'endpoints dédiés pour le détail des recrutements [#1086, #1068, #1061, #1101].
- **Modernisation du Frontend** : Migration de la gestion d'état vers Pinia Colada et harmonisation des composants d'interface (scaffolding, sidebar, conteneurs de page) [#1022, #1011, #1003, #983, #979, #1033, #1036, #1038].

### Autres changements
- **Documentation** : Mise à jour du guide de l'API à partir du schéma OpenAPI [#1108].
- **Architecture et recherche** : Ajout de documents d'architecture (ADR) et de notebooks d'exploration de données pour les modèles de localisation et les types de contrats [#958, #902].
