## Changelog : verseau2 (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, verseau2 a connu des avancées significatives, notamment l'implémentation d'un nouveau tableau de bord de conformité, des améliorations de l'expérience utilisateur pour les filtres de mesures et l'ajout de fonctionnalités liées à la gestion des ouvrages et des indicateurs de conformité. Des optimisations techniques ont également été apportées, incluant la migration vers pnpm et des refactorings pour une meilleure maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord de conformité prévisionnelle des systèmes d'assainissement [#47](https://github.com/MTES-MCT/verseau2/issues/47).
- Ajout d'indicateurs de conformité pour les SCL [#41](https://github.com/MTES-MCT/verseau2/issues/41).
- Amélioration de l'expérience utilisateur des filtres des mesures déposées [#39](https://github.com/MTES-MCT/verseau2/issues/39).
- Ajout d'une page référentiel descriptif des ouvrages [#38](https://github.com/MTES-MCT/verseau2/issues/38).
- Ajout d'un libellé "Remonté X fois" dans le badge des mesures [#46](https://github.com/MTES-MCT/verseau2/issues/46).
- Implémentation d'un endpoint MASA [#68](https://github.com/MTES-MCT/verseau2/issues/68).
- Gestion côté front des appels multiples au endpoint de refresh token [#61](https://github.com/MTES-MCT/verseau2/issues/61).
- Ajout de notifications d'événements [#51](https://github.com/MTES-MCT/verseau2/issues/51) et correction des notifications [#54](https://github.com/MTES-MCT/verseau2/issues/54).
- Modification des filtres pour le contrôle 59 [#45](https://github.com/MTES-MCT/verseau2/issues/45).
- Les exploitants ne peuvent plus déposer de flux qualifiés [#36](https://github.com/MTES-MCT/verseau2/issues/36).

### Évolutions techniques
- Migration du projet vers pnpm [#52](https://github.com/MTES-MCT/verseau2/issues/52).
- Refactoring et renommage de propriétés pour adopter une convention de domaine cohérente [#65](https://github.com/MTES-MCT/verseau2/issues/65).
- Simplification de la gestion des dates [#57](https://github.com/MTES-MCT/verseau2/issues/57).
- Augmentation de la durée de vie du cookie `access_token` et suppression de `idToken` dans les réponses [#64](https://github.com/MTES-MCT/verseau2/issues/64).
- Correction du type de réponse pour le refresh token [#70](https://github.com/MTES-MCT/verseau2/issues/70).
- Suppression de propriétés inutilisées dans les filtres [#67](https://github.com/MTES-MCT/verseau2/issues/67).
- Simplification des mappers de conformité [#59](https://github.com/MTES-MCT/verseau2/issues/59).
- Correction des valeurs de tranche d'obligation [#55](https://github.com/MTES-MCT/verseau2/issues/55).

### Autres changements
- Ajout d'un fichier `.dockerignore` pour exclure `node_modules` [#52](https://github.com/MTES-MCT/verseau2/issues/52).
- Ajout d'un fichier `SKILL.md` pour une implémentation complète fs de table-page [#52](https://github.com/MTES-MCT/verseau2/issues/52).
- Ajout d'un fichier `.opencode` à la liste d'ignorés [#52](https://github.com/MTES-MCT/verseau2/issues/52).
- Correction de la gestion des erreurs lors de la récupération des informations utilisateur [#63](https://github.com/MTES-MCT/verseau2/issues/63).
- Amélioration temporaire du restore dump [#42](https://github.com/MTES-MCT/verseau2/issues/42).
- Ajout d'une notice d'information sur la fraîcheur des données du tableau de bord conformité.
- Correction du flux d'authentification mock.
- Analyse des tables après restauration.
- Ajout de `startedAt` pour l'analyse des processus postgres.
- Dictionnaire DTO/DB orienté domaine pour l'interface MASA.
