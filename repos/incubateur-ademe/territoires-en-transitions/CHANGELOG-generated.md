## Changelog : territoires-en-transitions (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur autour des audits et de la labellisation, avec une nouvelle interface pour le suivi des audits et la gestion des cycles. Des améliorations significatives ont également été apportées à la gestion des plans d'action, notamment avec la possibilité de les dupliquer et d'éditer les actions directement dans un tableau. Des corrections de sécurité et des optimisations de performance ont également été implémentées.

### Évolutions fonctionnelles
- **Audit et Labellisation :** Nouvelle interface pour le suivi des audits, incluant des onglets pour le suivi et les cycles [#a8b3cb7](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a8b3cb7).
- **Audit et Labellisation :**  Possibilité de demander un audit en fonction de la disponibilité réelle [#d9e5d33](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d9e5d33).
- **Audit et Labellisation :** Affichage d'un badge de statut d'audit sur l'onglet correspondant [#bc4c1e8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bc4c1e8).
- **Plans d'action :** Ajout de la fonctionnalité de duplication d'un plan d'action [#a428150](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a428150).
- **Plans d'action :** Copie des budgets détaillés lors de la duplication d'un plan [#3214abc](https://github.com/incubateur-ademe/territoires-en-transitions/commit/3214abc).
- **Actions :** Possibilité d'éditer les actions directement dans un tableau, avec des options de suppression et d'ouverture simplifiées [#d1da417](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d1da417).
- **Actions :** Ajout d'un filtre pour afficher les actions sans priorité ou sans statut [#396fdd1](https://github.com/incubateur-ademe/territoires-en-transitions/commit/396fdd1).
- **Interface Utilisateur :** Nouvelle primitive `FloatingPanel` non-modale pour les composants de l'interface utilisateur [#5510e5e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/5510e5e).
- **Import de plans :** Amélioration du processus d'import de plans via l'ajout d'une étape de scoring de confiance des actions [#d92eb79](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d92eb79).

### Évolutions techniques
- **Refactoring :** Refactorisation de l'infrastructure `role/referentiel` vers le domaine, avec renommage des champs du view-model [#6bf4002](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6bf4002).
- **Base de données :** Suppression de l'implémentation de la sécurité au niveau des lignes (RLS) du `DatabaseService` [#7217fd4](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7217fd4).
- **Authentification :** Amélioration de la sécurité en bloquant l'IDOR sur les tickets bugs/supports via le SDK Notion [#06999e5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/06999e5).
- **Sécurité :** Correction de vulnérabilités de sécurité (phishing, SSRF) identifiées lors de tests de pénétration [#2930c8b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2930c8b), [#8a731f8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8a731f8).
- **Déploiement :**  Mises à jour de la configuration CI/CD et des dépendances.
- **Tests :** Ajout et mise à jour de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- **Typescript:** Amélioration du typage et de la cohérence du code.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Nettoyage de code :** Suppression de fichiers et de code inutilisés dans divers packages et modules.
- **Conventions de code :** Uniformisation des conventions de nommage (renommage de suffixes `.rule` en `.rules` et `.error` en `.errors`).
- **Améliorations UI :** Diverses améliorations de l'interface utilisateur et corrections de bugs visuels.
- **Gestion des dépendances :** Mise à jour de certaines dépendances (Next.js, eslint-config-next).
- **Refonte des tests:** Migration des tests Storybook vers Vitest.
