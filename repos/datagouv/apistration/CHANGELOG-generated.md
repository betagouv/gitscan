## Changelog : apistration (30 derniers jours, au 2026-05-22)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la gestion des données, notamment avec l'ajout de tableaux de bord améliorés pour les fournisseurs de données, l'ajout de nouvelles données (région PACA pour la scolarité, données CNAV) et l'amélioration de la documentation et des outils pour les développeurs. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la page d'édition des délégations API : affichage de l'UUID, de la date de création, des scopes et possibilité de copier l'UUID. [#142](https://github.com/datagouv/apistration/pull/142)
- Ajout de données pour la v5 de scolarité, pour la région PACA. [#141](https://github.com/datagouv/apistration/pull/141), [#5ec85f54](https://github.com/datagouv/apistration/commit/5ec85f54)
- Clarification du périmètre du quotient familial. [#136](https://github.com/datagouv/apistration/pull/136)
- Correction d'une erreur dans l'URL du changelog pour l'API Particulier. [#135](https://github.com/datagouv/apistration/pull/135)
- Ajout d'un SDK Node.js (TypeScript) pour les API Entreprise et Particulier. [#126](https://github.com/datagouv/apistration/pull/126)
- Refonte des tableaux de bord pour les fournisseurs de données : ajout de graphiques, de filtres, de la possibilité d'exporter les données en CSV, et amélioration de l'interface utilisateur. [#118](https://github.com/datagouv/apistration/pull/118), [#124](https://github.com/datagouv/apistration/pull/124), [#80](https://github.com/datagouv/apistration/pull/80)
- Ajout d'une section "Maintenance & incidents" à la newsletter de l'API Particulier. [#122](https://github.com/datagouv/apistration/pull/122)
- Ajout d'une page "Nouveautés" avec un lien vers le changelog. [#123](https://github.com/datagouv/apistration/pull/123)
- Ajout d'une fonctionnalité de souscription à une newsletter hebdomadaire avec le changelog. [#95](https://github.com/datagouv/apistration/pull/95)
- Ajout d'un endpoint pour les habilitations avec filtrage par scope. [#109](https://github.com/datagouv/apistration/pull/109)
- Ajout d'une option pour rendre le lieu de naissance optionnel pour les endpoints CNAV. [#91](https://github.com/datagouv/apistration/pull/91)

### Évolutions techniques
- Refactorisation de la gestion des erreurs et ajout d'un système d'émission d'erreurs plus robuste. [#74](https://github.com/datagouv/apistration/pull/74)
- Amélioration de la gestion des dépendances et mise à jour des versions.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests d'acceptation pour les fichiers `.expand`. [#88](https://github.com/datagouv/apistration/pull/88)
- Utilisation de `mrml` (Rust) au lieu de `MJML` (Node.js) pour le rendu des emails. [#102](https://github.com/datagouv/apistration/pull/102)
- Amélioration de la configuration et du déploiement.
- Ajout de workflows CI/CD pour les SDK Ruby. [#96](https://github.com/datagouv/apistration/pull/96)
- Mise en place d'un système de rotation automatique des mots de passe pour l'INSEE. [#3](https://github.com/datagouv/apistration/pull/3)

### Autres changements
- Documentation améliorée pour les nouveaux SDK et les fonctionnalités.
- Ajout de fichiers de configuration pour les environnements de développement et de production.
- Corrections de bugs mineurs et améliorations de la performance.
- Ajout de la possibilité de télécharger les données des tableaux de bord en CSV.
- Ajout de la gestion des erreurs 502.
- Amélioration de la gestion des pings de monitoring.
- Ajout d'un skill pour la gestion des budgets.
- Ajout d'un skill pour la gestion des endpoints.
- Ajout d'un skill pour la gestion des nouveautés.
- Suppression de déclencheurs inutiles dans le CI.
- Amélioration de la sécurité et de la conformité.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de la documentation pour refléter les changements.
- Ajout de la possibilité de configurer le cache GIP-MDS pour la fin du mois. [#63](https://github.com/datagouv/apistration/pull/63)
- Ajout de la possibilité de configurer un agent VM. [#70](https://github.com/datagouv/apistration/pull/70)
- Correction d'un bug lié à l'authentification DataSubvention. [#72](https://github.com/datagouv/apistration/pull/72)
- Correction d'un bug lié aux liens incorrects dans la documentation de l'API Siren. [#58](https://github.com/datagouv/apistration/pull/58)
