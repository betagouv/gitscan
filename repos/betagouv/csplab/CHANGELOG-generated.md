## Changelog : csplab (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois-ci, la plateforme a considérablement enrichi ses capacités de recherche et de filtrage, permettant aux utilisateurs de trouver des offres d'emploi avec une précision accrue (par zone géographique, mots-clés, domaine ou type de contrat). La gestion des recrutements a été fluidifiée par l'introduction du traitement par lots des candidatures et des améliorations de l'interface Kanban. Enfin, la sécurité a été renforcée par la mise en place d'un système de gestion des droits d'accès (RBAC) plus granulaire pour les agents et les recruteurs.

### Évolutions fonctionnelles
- **Recherche et filtrage des offres** : Ajout de nombreux filtres pour affiner la recherche d'offres : mots-clés (recherche plein texte) [#1125](https://github.com/betagouv/csplab/issues/1125), zone géographique (pays, région, département, coordonnées GPS) [#1092](https://github.com/betagouv/csplab/issues/1092), domaine, organisme, type de contrat, niveau d'expérience et lieu de travail [#1100](https://github.com/betagouv/csplab/issues/1100), [#1077](https://github.com/betagouv/csplab/issues/1077).
- **Gestion des candidatures et recrutements** : 
    - Possibilité de modifier les étapes des candidatures par lots [#948](https://github.com/betagouv/csplab/issues/948).
    - Distinction des dates de mise à jour entre le recruteur et le candidat [#1156](https://github.com/betagouv/csplab/issues/1156).
    - Nouvelle interface pour la consultation, la mise à jour et la réinitialisation des étapes du pipeline d'une offre [#1050](https://github.com/betagouv/csplab/issues/1050), [#1048](https://github.com/betagouv/csplab/issues/1048).
- **Expérience utilisateur (UX)** : 
    - Amélioration du tableau Kanban avec un défilement automatique (autoscroll) [#1107](https://github.com/betagouv/csplab/issues/1107).
    - Optimisation de la navigation et correction de divers éléments d'interface (barre de recherche, modales, largeur des pages) [#1104](https://github.com/betagouv/csplab/issues/1104), [#1094](https://github.com/betagouv/csplab/issues/1094).

### Évolutions techniques
- **Sécurité et gestion des droits (RBAC)** : Déploiement massif du contrôle d'accès basé sur les rôles pour sécuriser la création d'organismes, la gestion des recrutements et l'accès aux détails des offres selon le profil de l'agent [#1054](https://github.com/betagouv/csplab/issues/1054), [#1030](https://github.com/betagouv/csplab/issues/1030), [#1025](https://github.com/betagouv/csplab/issues/1025), [#1002](https://github.com/betagouv/csplab/issues/1002).
- **API et Performance** : 
    - Optimisation du système de limitation de débit (throttling) en utilisant Redis comme backend [#1086](https://github.com/betagouv/csplab/issues/1086).
    - Ajout d'en-têtes de réponse pour informer sur les limites de l'API (RateLimit) [#1068](https://github.com/betagouv/csplab/issues/1068).
    - Création de nouveaux endpoints dédiés pour le détail des recrutements et les formats spécifiques (Talentsoft) [#1101](https://github.com/betagouv/csplab/issues/1101), [#1071](https://github.com/betagouv/csplab/issues/1071).
- **Frontend** : Migration de la gestion d'état et de la récupération de données vers Pinia Colada pour plus de robustesse et de stabilité [#1022](https://github.com/betagouv/csplab/issues/1022), [#1011](https://github.com/betagouv/csplab/issues/1011), [#1003](https://github.com/betagouv/csplab/issues/1003).
- **Données et Ingestion** : Intégration du nouveau référentiel métier RMFPv2 dans les données des offres [#1081](https://github.com/betagouv/csplab/issues/1081), [#1095](https://github.com/betagouv/csplab/issues/1095) et amélioration du mapping des données d'ingestion.

### Autres changements
- **Documentation** : Mise à jour régulière de la documentation de l'API à partir du schéma OpenAPI [#1108](https://github.com/betagouv/csplab/issues/1108), [#1137](https://github.com/betagouv/csplab/issues/1137).
- **Outils de développement** : Introduction de `mise` pour simplifier l'exécution des tâches de développement [#1043](https://github.com/betagouv/csplab/issues/1043).
