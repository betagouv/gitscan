## Changelog : csplab (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, la mise en place d'une nouvelle architecture pour le frontend et l'ajout de fonctionnalités pour la gestion des utilisateurs. Des améliorations significatives ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- Ajout de la possibilité de lister les offres d'emploi via une API. [#440](https://github.com/betagouv/csplab/issues/440)
- Mise en place de l'authentification par email et mot de passe pour les utilisateurs. [#639](https://github.com/betagouv/csplab/issues/639)
- Ajout de pages statiques : mentions légales, politique de confidentialité, accessibilité. [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#227](https://github.com/betagouv/csplab/issues/227)
- Possibilité de mettre à jour certains champs des utilisateurs dans l'interface d'administration. [#653](https://github.com/betagouv/csplab/issues/653)
- Ajout d'une colonne "référence" aux offres d'emploi. [#657](https://github.com/betagouv/csplab/issues/657)
- Intégration des métiers dans la fonctionnalité de mise en correspondance entre CV et offres. [#637](https://github.com/betagouv/csplab/issues/637)
- Publication du notebook sur GitHub Pages. [#641](https://github.com/betagouv/csplab/issues/641)
- Ajout de la possibilité d'afficher le poste dans le tiroir d'offre. [#550](https://github.com/betagouv/csplab/issues/550)

### Évolutions techniques
- Refonte de l'architecture frontend avec l'utilisation de React.
- Mise en place d'un workflow de publication pour Storybook. [#647](https://github.com/betagouv/csplab/issues/647)
- Isolation des vues d'ingestion pour une meilleure organisation du code. [#662](https://github.com/betagouv/csplab/issues/662)
- Refactoring du code de test pour améliorer la maintenabilité. [#656](https://github.com/betagouv/csplab/issues/656), [#652](https://github.com/betagouv/csplab/issues/652)
- Migration vers un modèle d'utilisateur personnalisé. [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616), [#620](https://github.com/betagouv/csplab/issues/620), [#632](https://github.com/betagouv/csplab/issues/632)
- Amélioration de la gestion des erreurs frontend avec l'interception et la gestion des erreurs. [#629](https://github.com/betagouv/csplab/issues/629)
- Ajout d'une nouvelle application "ingestion" pour gérer l'importation des offres. [#493](https://github.com/betagouv/csplab/issues/493)
- Mise en place d'un système de logging plus robuste. [#501](https://github.com/betagouv/csplab/issues/501)
- Amélioration de la gestion des variables d'environnement pour l'ingestion. [#500](https://github.com/betagouv/csplab/issues/500)
- Ajout de tests de couverture de code. [#498](https://github.com/betagouv/csplab/issues/498)
- Mise à jour des dépendances (vitest, node24). [#674](https://github.com/betagouv/csplab/issues/674)

### Autres changements
- Documentation de l'architecture frontend et des conventions de codage. [#595](https://github.com/betagouv/csplab/issues/595)
- Traduction du template de pull request en français. [#619](https://github.com/betagouv/csplab/issues/619)
- Ajout de règles de linting pour le schéma. [#608](https://github.com/betagouv/csplab/issues/608)
- Ajout d'un workflow pour l'assignation automatique des pull requests. [#606](https://github.com/betagouv/csplab/issues/606)
- Amélioration de la configuration ESLint et VSCode. [#612](https://github.com/betagouv/csplab/issues/612)
- Ajout d'un fichier `.gitattributes` pour ignorer le cache mypy. [#626](https://github.com/betagouv/csplab/issues/626)
- Mise à jour du CHANGELOG.md pour les versions précédentes. [#567](https://github.com/betagouv/csplab/issues/567), [#485](https://github.com/betagouv/csplab/issues/485)
