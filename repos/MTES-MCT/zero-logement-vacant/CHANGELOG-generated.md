## Changelog : zero-logement-vacant (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation, la refactorisation du code serveur pour une meilleure maintenabilité et performance, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur, notamment concernant l'export de données et la gestion des droits d'accès. L'ajout de tests et l'amélioration de l'infrastructure CI/CD ont également été des points importants.

### Évolutions fonctionnelles
- Amélioration de l'export des données des propriétaires avec la séparation des colonnes d'adresse BAN. [#1719](https://github.com/MTES-MCT/zero-logement-vacant/pull/1719)
- Correction de l'affichage du menu de navigation pour mettre en évidence la section "Parc de logements" lors de la navigation vers les pages associées (groupes, logements, propriétaires). [#1734](https://github.com/MTES-MCT/zero-logement-vacant/pull/1734)
- Amélioration de l'affichage des pourcentages dans les tableaux de bord, avec une seule décimale par défaut. [#1748](https://github.com/MTES-MCT/zero-logement-vacant/pull/1748)
- Ajout de notifications lors de la création d'une campagne et de la suppression d'un groupe. [#1751](https://github.com/MTES-MCT/zero-logement-vacant/pull/1751)
- Correction de l'affichage des aperçus des documents lors du téléchargement. [#1748](https://github.com/MTES-MCT/zero-logement-vacant/pull/1748)
- Amélioration de la gestion des droits d'accès et de la filtration des données en fonction du périmètre Portail DF. [#1644](https://github.com/MTES-MCT/zero-logement-vacant/pull/1644)

### Évolutions techniques
- Refactorisation importante de la configuration du serveur, remplaçant `convict` par `Zod` pour une meilleure validation et gestion des configurations.
- Migration de la spécification OpenAPI de l'API de TypeScript vers YAML, avec remplacement de Swagger UI par Scalar.
- Suppression de dépendances inutilisées et mise à jour de celles existantes.
- Amélioration de l'infrastructure CI/CD avec des mises à jour des actions GitHub et l'ajout de tests Cypress pour les tests end-to-end.
- Ajout de l'outil d'analyse de code Knip pour identifier les dépendances inutilisées.
- Mise à jour de Vite en version 8 et des plugins associés.
- Implémentation de triggers au niveau des instructions SQL pour optimiser le calcul des statistiques sur les groupes de logements.
- Refactorisation du code pour utiliser `axios` au lieu de `fetch` dans le service Cerema.
- Ajout d'une abstraction pour la gestion des fournisseurs d'authentification.
- Amélioration de la gestion des erreurs et des types dans le code.

### Autres changements
- Ajout de documentation technique complète (DAT, DE, DI) avec génération de PDF.
- Ajout de documentation sur les plans et spécifications des "superpowers".
- Ajout de documentation sur l'exploration EETL et la mise en œuvre du pipeline des propriétaires.
- Amélioration de la documentation existante et correction de fautes de frappe.
- Ajout de badges Codecov.
- Correction de problèmes de configuration pour l'exécution des tests en CI.
- Suppression de scripts de test obsolètes.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Mise à jour des fichiers de configuration et des dépendances.
- Correction de problèmes liés à l'environnement macOS en CI.
- Ajout de la possibilité de configurer l'application via CleverCloud.
- Ajout de la gestion des variables d'environnement avec `@dotenvx/dotenvx`.
- Ajout de la gestion des types manquants.
- Amélioration de la gestion des erreurs dans les scripts Python.
- Ajout de la gestion des propriétaires FF25 dans les pipelines Dbt.
- Correction de bugs mineurs et améliorations de la lisibilité du code.
