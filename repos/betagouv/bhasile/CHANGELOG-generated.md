## Changelog : bhasile (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur la gestion des transformations de structures, avec l'ajout de formulaires de création et de validation, ainsi que l'amélioration de l'expérience utilisateur autour de ces fonctionnalités. Des améliorations significatives ont également été apportées aux statistiques et aux rapports, notamment avec l'ajout de nouveaux indicateurs et blocs d'informations. Enfin, des corrections de bugs et des optimisations de performance ont été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier le cas de figure d'une structure [#1406](https://github.com/betagouv/bhasile/issues/1406).
- Ajout d'un onglet "Historique" pour visualiser l'évolution des structures [#1382](https://github.com/betagouv/bhasile/issues/1382).
- Possibilité de supprimer les transformations [#1404](https://github.com/betagouv/bhasile/issues/1404).
- Ajout de la possibilité de créer des structures à partir de transformations, avec validation et gestion des actes associés [#1402](https://github.com/betagouv/bhasile/issues/1402).
- Ajout de filtres pour afficher les structures fermées ou actives [#1401](https://github.com/betagouv/bhasile/issues/1401).
- Ajout de statistiques sur les finances [#1366](https://github.com/betagouv/bhasile/issues/1366).
- Ajout de statistiques sur les types de places [#1361](https://github.com/betagouv/bhasile/issues/1361).
- Ajout de statistiques sur les structures [#1337](https://github.com/betagouv/bhasile/issues/1337).
- Ajout de la possibilité de créer des structures *ex nihilo* avec des formulaires dédiés pour les places, les hébergements et les documents administratifs [#1290](https://github.com/betagouv/bhasile/issues/1290), [#1291](https://github.com/betagouv/bhasile/issues/1291), [#1294](https://github.com/betagouv/bhasile/issues/1294).
- Ajout de la gestion de la fermeture complète d'une structure [#1293](https://github.com/betagouv/bhasile/issues/1293).
- Ajout de la gestion des avenants liés aux transformations.
- Ajout de la possibilité d'ajouter un logo aux opérateurs [#1286](https://github.com/betagouv/bhasile/issues/1286).
- Amélioration de l'affichage des dates d'expiration des documents [#1295](https://github.com/betagouv/bhasile/issues/1295).

### Évolutions techniques
- Refonte des requêtes SQL liées aux structures [#1400](https://github.com/betagouv/bhasile/issues/1400).
- Mise en place d'une gestion des versions des structures pour faciliter le suivi des modifications [#1354](https://github.com/betagouv/bhasile/issues/1354).
- Amélioration des tests d'intégration et de bout en bout (E2E) pour couvrir les nouvelles fonctionnalités et corriger les tests existants [#1395](https://github.com/betagouv/bhasile/issues/1395), [#1394](https://github.com/betagouv/bhasile/issues/1394), [#1390](https://github.com/betagouv/bhasile/issues/1390), [#1389](https://github.com/betagouv/bhasile/issues/1389).
- Optimisation du cache et de la construction des slugs pour améliorer les performances sur Scalingo [#1303](https://github.com/betagouv/bhasile/issues/1303).
- Ajout de documentation pour les types utilisés dans le code [#1305](https://github.com/betagouv/bhasile/issues/1305).
- Migration des transformations et de leurs contraintes.

### Autres changements
- Correction de bugs divers liés aux formulaires de transformation, à l'affichage des adresses et au comportement des champs de saisie [#1410](https://github.com/betagouv/bhasile/issues/1410), [#1375](https://github.com/betagouv/bhasile/issues/1375), [#1374](https://github.com/betagouv/bhasile/issues/1374).
- Amélioration de l'accessibilité (a11y) [#1308](https://github.com/betagouv/bhasile/issues/1308).
- Correction de problèmes de scroll dans les tableaux [#1307](https://github.com/betagouv/bhasile/issues/1307), [#1306](https://github.com/betagouv/bhasile/issues/1306).
- Ajout d'un patch DSFR [#1388](https://github.com/betagouv/bhasile/issues/1388).
- Suppression de fichiers de migration obsolètes.
- Mise à jour de certaines dépendances (hors mises à jour automatiques).
