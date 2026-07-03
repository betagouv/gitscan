## Changelog : bhasile (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur la gestion des transformations de structures d'accueil, avec l'ajout de nouveaux formulaires, la gestion des validations et l'intégration de l'historique. Des améliorations ont également été apportées aux statistiques, à l'interface utilisateur et à la gestion des opérateurs.

### Évolutions fonctionnelles
- Ajout de la possibilité de visualiser le nombre de places fermées sur la page de vérification [#1429](https://github.com/betagouv/bhasile/issues/1429).
- Ajout de boutons de suppression pour les codes DNA et FINESS [#1428](https://github.com/betagouv/bhasile/issues/1428).
- Affichage d'un badge indiquant les transformations à venir [#1425](https://github.com/betagouv/bhasile/issues/1425).
- Gestion du transfert des codes DNA pour les transformations [#1424](https://github.com/betagouv/bhasile/issues/1424).
- Sauvegarde des valeurs des formulaires lors de la navigation [#1419](https://github.com/betagouv/bhasile/issues/1419).
- Ajout de la date de fermeture à une structure [#1432](https://github.com/betagouv/bhasile/issues/1432).
- Suppression de la question concernant l'adresse administrative [#1427](https://github.com/betagouv/bhasile/issues/1427).
- Préremplissage de l'opérateur lors de la création d'une structure [#1420](https://github.com/betagouv/bhasile/issues/1420).
- Autorisation de sauvegarder un formulaire de transformation sans FINESS [#1421](https://github.com/betagouv/bhasile/issues/1421).
- Amélioration de la mise en page de l'onglet historique [#1423](https://github.com/betagouv/bhasile/issues/1423).
- Affichage des structures fermées côté serveur [#1408](https://github.com/betagouv/bhasile/issues/1408).
- Ajout de marqueurs de transformation sur le tableau des lieux [#1407](https://github.com/betagouv/bhasile/issues/1407).
- Conservation de la date de création d'une structure [#1413](https://github.com/betagouv/bhasile/issues/1413).
- Autorisation de date d'effet nulle [#1412](https://github.com/betagouv/bhasile/issues/1412).
- Possibilité de changer le cas de figure [#1406](https://github.com/betagouv/bhasile/issues/1406).
- Ajout de marqueurs de transformation sur le tableau des finances [#1403](https://github.com/betagouv/bhasile/issues/1403).
- Ajout d'un onglet historique [#1382](https://github.com/betagouv/bhasile/issues/1382).
- Affichage de la structure nouvellement créée [#1399](https://github.com/betagouv/bhasile/issues/1399).
- Ajout de la possibilité de modifier les actes administratifs lors d'une transformation [#1402](https://github.com/betagouv/bhasile/issues/1402).
- Ajout de statistiques sur les types de places [#1366](https://github.com/betagouv/bhasile/issues/1366).
- Ajout de statistiques sur les opérateurs [#1361](https://github.com/betagouv/bhasile/issues/1361).
- Ajout de la possibilité de lier une campagne à une version de structure [#1379](https://github.com/betagouv/bhasile/issues/1379).
- Ajout de formulaires pour l'extension et la contraction d'hébergement et d'actes administratifs [#1321, #1323](https://github.com/betagouv/bhasile/issues/1321, https://github.com/betagouv/bhasile/issues/1323).
- Ajout de la possibilité de créer une structure à partir d'une transformation [#1298, #1310](https://github.com/betagouv/bhasile/issues/1298, https://github.com/betagouv/bhasile/issues/1310).
- Ajout d'une page de validation de transformation [#1312](https://github.com/betagouv/bhasile/issues/1312).
- Ajout de la gestion de la fermeture d'une structure [#1293](https://github.com/betagouv/bhasile/issues/1293).
- Ajout de contacts pour les opérateurs [#1286](https://github.com/betagouv/bhasile/issues/1286).
- Ajout du logo de l'opérateur [#1319](https://github.com/betagouv/bhasile/issues/1319).

### Évolutions techniques
- Refonte de la logique serveur pour les structures fermées [#1408](https://github.com/betagouv/bhasile/issues/1408).
- Amélioration des tests de transformation [#1353](https://github.com/betagouv/bhasile/issues/1353).
- Suppression des requêtes SQL liées aux structures [#1400](https://github.com/betagouv/bhasile/issues/1400).
- Mise en place d'une gestion des versions de structure.
- Correction de bugs liés à la sauvegarde des formulaires de transformation [#1411](https://github.com/betagouv/bhasile/issues/1411).
- Amélioration de la gestion des tests E2E.
- Correction de plusieurs bugs liés aux tests E2E [#1374, #1395](https://github.com/betagouv/bhasile/issues/1374, https://github.com/betagouv/bhasile/issues/1395).
- Amélioration de la gestion des erreurs et des validations de formulaires.

### Autres changements
- Mise à jour de la documentation.
- Corrections de style et améliorations de la lisibilité du code.
- Correction de problèmes liés à la suppression de structures.
- Amélioration de la gestion des dépendances.
- Ajout de logs pour faciliter le débogage.
