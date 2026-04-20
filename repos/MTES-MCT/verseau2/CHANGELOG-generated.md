## Changelog : verseau2 (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration du tableau de bord de conformité, l'ajout de nouvelles fonctionnalités liées aux ouvrages et aux notifications, ainsi que sur des optimisations techniques et des corrections de bugs. L'application a également bénéficié d'une migration vers pnpm pour la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord des bilans et de la conformité prévisionnelle des systèmes d'assainissement [#47](https://github.com/MTES-MCT/verseau2/issues/47).
- Implémentation d'indicateurs de conformité pour les SCL [#41](https://github.com/MTES-MCT/verseau2/issues/41).
- Création d'une page référentiel descriptif des ouvrages [#38](https://github.com/MTES-MCT/verseau2/issues/38).
- Amélioration de l'UX des filtres des mesures déposées [#39](https://github.com/MTES-MCT/verseau2/issues/39).
- Ajout de notifications d'événements [#51](https://github.com/MTES-MCT/verseau2/issues/51) et correction d'un bug lié aux notifications [#54](https://github.com/MTES-MCT/verseau2/issues/54).
- Correction de l'affichage du nombre de remontées pour un ouvrage [#46](https://github.com/MTES-MCT/verseau2/issues/46).
- Ajout d'un endpoint MASA [#68](https://github.com/MTES-MCT/verseau2/issues/68).
- Correction de la liste des ouvrages RMC [#69](https://github.com/MTES-MCT/verseau2/issues/69).
- Ajout d'une notice d'information sur la fraîcheur des données du tableau de bord conformité.

### Évolutions techniques
- Migration du projet vers pnpm pour la gestion des dépendances [#52](https://github.com/MTES-MCT/verseau2/issues/52).
- Refactoring général du code pour améliorer la lisibilité et la maintenabilité, notamment le renommage des propriétés en utilisant la convention domaine [#65](https://github.com/MTES-MCT/verseau2/issues/65).
- Simplification de la gestion des dates [#57](https://github.com/MTES-MCT/verseau2/issues/57).
- Amélioration de la gestion des tokens d'authentification : augmentation de la durée de vie du cookie `access_token` et suppression de l'`idToken` dans les réponses [#64](https://github.com/MTES-MCT/verseau2/issues/64).
- Correction de problèmes liés au rafraîchissement des tokens [#61](https://github.com/MTES-MCT/verseau2/issues/61), [#7f7e6f4](https://github.com/MTES-MCT/verseau2/commit/7f7e6f4).
- Suppression de propriétés inutilisées dans les filtres [#67](https://github.com/MTES-MCT/verseau2/issues/67).
- Amélioration du formatage des logs de requêtes et limitation de la longueur des paramètres [#8078be9](https://github.com/MTES-MCT/verseau2/commit/8078be9), [#ce04acc](https://github.com/MTES-MCT/verseau2/commit/ce04acc).
- Correction de tests en erreur [#1ba772e](https://github.com/MTES-MCT/verseau2/commit/1ba772e).

### Autres changements
- Ajout d'un fichier `.dockerignore` pour exclure `node_modules` [#1cde387](https://github.com/MTES-MCT/verseau2/commit/1cde387).
- Ajout d'un fichier `SKILL.md` pour une implémentation complète fs de table-page [#ee3815f](https://github.com/MTES-MCT/verseau2/commit/ee3815f).
- Ajout de `.opencode` à la liste d'ignorés [#b47d844](https://github.com/MTES-MCT/verseau2/commit/b47d844).
- Correction de l'analyse des tables après restauration [#40](https://github.com/MTES-MCT/verseau2/issues/40).
- Correction de la gestion des erreurs lors de la récupération des informations utilisateur [#c0859df](https://github.com/MTES-MCT/verseau2/commit/c0859df).
- Correction des valeurs de tranche d'obligation [#55](https://github.com/MTES-MCT/verseau2/issues/55).
- Correction de l'analyse des processus postgres sur la table et non le schéma [#4f2a018](https://github.com/MTES-MCT/verseau2/commit/4f2a018).
- Mise à jour des dépendances du monorepo [#4927ced](https://github.com/MTES-MCT/verseau2/commit/4927ced).
- Correction du flux d'authentification mock [#108b4a8](https://github.com/MTES-MCT/verseau2/commit/108b4a8).
- Ajout de `startedAt` pour l'analyse postgres [#18d5f1e](https://github.com/MTES-MCT/verseau2/commit/18d5f1e).
- Correction de 86 - renommage de la conformité nationale en réglementaire [#50](https://github.com/MTES-MCT/verseau2/issues/50).
- Ajout d'un dictionnaire DTO/DB orienté domaine pour l'interface MASA [#b50a500](https://github.com/MTES-MCT/verseau2/commit/b50a500).
