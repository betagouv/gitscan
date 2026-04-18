## Changelog : territoires-en-transitions (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'ergonomie de l'interface et de la gestion des données. Des corrections de bugs et des optimisations ont été apportées pour fluidifier le workflow des utilisateurs et améliorer la stabilité de la plateforme. Des travaux importants ont également été réalisés sur la gestion des référentiels et des indicateurs, ainsi que sur l'intégration avec des services externes.

### Évolutions fonctionnelles
- Amélioration de l'ergonomie de l'EDL (Environnement de travail) avec l'utilisation d'un side panel pour une meilleure gestion de l'espace et de l'affichage. [#7d4d322](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7d4d322)
- Mise à jour de la gestion des tags dans l'export PDF des Fiches d'Action. [#c3aea8a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c3aea8a)
- Correction d'un bug empêchant la mise à jour des budgets. [#78afa2a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/78afa2a)
- Amélioration de l'affichage du prénom plutôt que du nom dans les emails de notification pour les pilotes. [#bf25b94](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bf25b94)
- Ajout d'un bloc "centralisez, pilotez, etc." et remaniement de la page d'accueil avec une nouvelle bannière et vidéo de présentation. [#ffcca76](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ffcca76) et suivants.
- Transformation des étapes d'une fiche en sous-actions. [#1760794](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1760794)
- Ajout du type de collectivité 'service_public'. [#8ed6da9](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8ed6da9)
- Amélioration de la pagination de la page Actualités. [#bc04d44](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bc04d44)

### Évolutions techniques
- Refactoring et centralisation de certains hooks d'accès aux données pour une meilleure maintenabilité. [#01810e2](https://github.com/incubateur-ademe/territoires-en-transitions/commit/01810e2)
- Mise à jour de Next.js pour améliorer les performances en développement. [#6e4e681](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6e4e681)
- Utilisation de transactions pour la sauvegarde de l'historique des statuts et commentaires des actions. [#e1fd5c2](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e1fd5c2)
- Amélioration de la gestion des erreurs et du batch processing dans le script de migration des étapes en sous-actions. [#dd7950d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/dd7950d)
- Ajout de tests et amélioration de la couverture de test.
- Mise en place de scripts de backup et restore pour la base de données. [#89c01cf](https://github.com/incubateur-ademe/territoires-en-transitions/commit/89c01cf)
- Intégration de l'application Streamlit dans le healthcheck et ajout d'un dashboard privé. [#1b92c46](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1b92c46) et [#81f2122](https://github.com/incubateur-ademe/territoires-en-transitions/commit/81f2122)

### Autres changements
- Suppression de code legacy et de feature flags inutilisés. [#308b70e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/308b70e) et [#0ef8125](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0ef8125)
- Suppression de vues SQL obsolètes. [#ca24423](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ca24423)
- Mise à jour de la documentation et des templates d'import de plan. [#87f0eed](https://github.com/incubateur-ademe/territoires-en-transitions/commit/87f0eed)
- Amélioration de la gestion des configurations et des variables d'environnement.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des dépendances.
