## Changelog : verseau2 (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives en termes de gestion des données, de sécurité et d'expérience utilisateur. L'implémentation d'un tableau de bord des bilans et des correctifs liés aux notifications d'événements sont les évolutions les plus notables. Des optimisations techniques ont également été apportées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord des bilans, permettant une vue d'ensemble des données clés. [#56](https://github.com/MTES-MCT/verseau2/issues/56) et [#58](https://github.com/MTES-MCT/verseau2/issues/58)
- Correction d'un bug concernant la liste des ouvrages RMC. [#69](https://github.com/MTES-MCT/verseau2/issues/69)
- Correction des valeurs de tranche d'obligation. [#55](https://github.com/MTES-MCT/verseau2/issues/55)
- Correction d'un bug lié aux notifications d'événements. [#54](https://github.com/MTES-MCT/verseau2/issues/54) et [#51](https://github.com/MTES-MCT/verseau2/issues/51)
- Correction d'un problème de gestion des erreurs lors de la récupération des informations utilisateur côté front. [#61](https://github.com/MTES-MCT/verseau2/issues/61)
- Ajout d'un endpoint MASA. [#68](https://github.com/MTES-MCT/verseau2/issues/68)
- Correction d'un bug lié à la recette. [#71](https://github.com/MTES-MCT/verseau2/issues/71)

### Évolutions techniques
- Refactor de la gestion des requêtes pour les API REST MASA. [#3ba41ea](https://github.com/MTES-MCT/verseau2/commit/3ba41ea)
- Amélioration du formatage des requêtes SQL dans les logs. [#8078be9](https://github.com/MTES-MCT/verseau2/commit/8078be9)
- Limitation de la longueur des paramètres dans les logs de requête. [#ce04acc](https://github.com/MTES-MCT/verseau2/commit/ce04acc)
- Suppression des propriétés inutilisées dans les filtres. [#67](https://github.com/MTES-MCT/verseau2/issues/67)
- Renommage des propriétés pour respecter la convention de domaine. [#65](https://github.com/MTES-MCT/verseau2/issues/65)
- Augmentation de la durée de vie du cookie `access_token` et suppression de `idToken` dans les réponses. [#64](https://github.com/MTES-MCT/verseau2/issues/64)
- Suppression de `skipSubjectCheck` et ajustement des appels. [#62](https://github.com/MTES-MCT/verseau2/issues/62)
- Correction du type de réponse pour le refresh token. [#7f7e6f4](https://github.com/MTES-MCT/verseau2/commit/7f7e6f4)
- Gestion des erreurs et logs du rafraîchissement des tokens. [#9628ffd](https://github.com/MTES-MCT/verseau2/commit/9628ffd)
- Simplification de la gestion des dates. [#57](https://github.com/MTES-MCT/verseau2/issues/57)
- Correction des erreurs lint et simplification des mappers de conformité. [#59](https://github.com/MTES-MCT/verseau2/issues/59)
- Migration vers pnpm. [#52](https://github.com/MTES-MCT/verseau2/issues/52)
- Trimer les adresses email dans les requêtes. [#70](https://github.com/MTES-MCT/verseau2/issues/70)

### Autres changements
- Amélioration de la documentation et des commandes dans AGENTS.md. [#ee28178](https://github.com/MTES-MCT/verseau2/commit/ee28178)
- Ajout d'un fichier `.dockerignore` pour exclure `node_modules`. [#1cde387](https://github.com/MTES-MCT/verseau2/commit/1cde387)
- Ajout de la documentation SKILL.md pour une implémentation complète fs de table-page. [#ee3815f](https://github.com/MTES-MCT/verseau2/commit/ee3815f)
- Ignore la table 'resj' lors de la restauration. [#5d1e898](https://github.com/MTES-MCT/verseau2/commit/5d1e898)
