## Changelog : recommandations-collaboratives (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur une refonte de l'interface utilisateur pour la gestion des organisations et des projets, l'ajout de fonctionnalités de plugins pour une extensibilité accrue, ainsi que des améliorations de sécurité et de la gestion des utilisateurs. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des organisations :** Refonte complète de la page de gestion des organisations avec une nouvelle interface, des filtres améliorés (géographique, département), et des informations plus détaillées sur les organisations (nombre de membres, dossiers). [#2182](https://github.com/betagouv/recommandations-collaboratives/pull/2182)
- **Fusion d'organisations :** Amélioration de l'expérience utilisateur lors de la fusion d'organisations, avec des récapitulatifs clairs des données de chaque organisation. [#2180](https://github.com/betagouv/recommandations-collaboratives/pull/2180)
- **CRM :** Tri de la liste des utilisateurs du CRM par date d'inscription. [#2226](https://github.com/betagouv/recommandations-collaboratives/pull/2226)
- **Nouveaux projets :** Possibilité de masquer le bouton de création de nouveaux projets via un indicateur de fonctionnalité. [#2205](https://github.com/betagouv/recommandations-collaboratives/pull/2205)
- **Authentification :** Amélioration de la sécurité de l'authentification par code, notamment en limitant la durée de validité du code et en renforçant la gestion des cookies. [#2150](https://github.com/betagouv/recommandations-collaboratives/pull/2150)
- **Conversation :** Ajout de hooks JavaScript pour personnaliser l'affichage des composants de conversation. [#2188](https://github.com/betagouv/recommandations-collaboratives/pull/2188)
- **Gestion des tâches :** Possibilité de déclencher des actions lors du passage d'une tâche à l'état "Terminé" via les plugins.
- **Interface utilisateur :** Ajout d'une nouvelle timeline d'activité. [#2181](https://github.com/betagouv/recommandations-collaboratives/pull/2181)
- **Filtres projets :** Correction d'un bug dans les filtres de la page "Mes projets". [#2152](https://github.com/betagouv/recommandations-collaboratives/pull/2152)

### Évolutions techniques
- **Plugins :** Implémentation d'un système de plugins pour étendre les fonctionnalités de l'application, incluant la découverte automatique des plugins et la gestion des migrations. [#1986](https://github.com/betagouv/recommandations-collaboratives/pull/1986)
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment `uv`, `django`, `pyjwt`, `bleach`, `tornado`, `dompurify`, `vite`, `form-data`, `tar` et `@babel/core`.
- **CI/CD :** Ajout de `uv-audit` pour l'analyse des vulnérabilités des dépendances et remplacement de `uv-secure`.
- **Pré-commit :** Ajout de `gitleaks` au processus de pré-commit pour détecter les secrets potentiellement divulgués.
- **Refactoring :** Suppression de code obsolète et simplification de certaines parties du code.
- **Docker :** Passage à `uv` pour la gestion des dépendances Docker.
- **Tests :** Amélioration de la robustesse des tests, notamment pour les documents et l'authentification.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements de configuration.
- **Configuration :** Amélioration de la configuration de l'authentification et des redirections.
- **Nettoyage de code :** Suppression de fichiers inutiles et amélioration de la lisibilité du code.
- **Correction de bugs mineurs :** Correction de plusieurs bugs mineurs dans l'interface utilisateur et la logique applicative.
- **Amélioration des messages d'erreur :** Augmentation de la longueur maximale des messages d'erreur pour une meilleure clarté. [#2218](https://github.com/betagouv/recommandations-collaboratives/pull/2218)
- **Suppression de `requirements.txt` :** Suppression du fichier `requirements.txt` au profit de `uv`.
- **Amélioration des styles CSS :** Ajustements et corrections de styles CSS pour améliorer l'apparence de l'application.
