## Changelog : bhasile (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des transformations de structures d'accueil, avec un accent particulier sur la création et la validation de ces transformations. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour la navigation, l'affichage des informations et la gestion des documents. Enfin, des optimisations de performance et des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Possibilité de créer une structure directement depuis les formulaires de création de places et d'actes administratifs ([#1290](https://github.com/betagouv/bhasile/issues/1290), [#1291](https://github.com/betagouv/bhasile/issues/1291)).
- Ajout d'un flux complet pour la fermeture des structures ([#1293](https://github.com/betagouv/bhasile/issues/1293)).
- Ajout de la possibilité de modifier le cas de figure d'une structure ([#1406](https://github.com/betagouv/bhasile/issues/1406)).
- Ajout de la possibilité de modifier les actes administratifs ([#1345](https://github.com/betagouv/bhasile/issues/1345)).
- Ajout d'une liste des transformations en cours ([#1309](https://github.com/betagouv/bhasile/issues/1309)).
- Amélioration de la gestion des documents pour les opérateurs ([#1319](https://github.com/betagouv/bhasile/issues/1319), [#1326](https://github.com/betagouv/bhasile/issues/1326)).
- Possibilité de modifier la date d'effet d'une structure ([#1412](https://github.com/betagouv/bhasile/issues/1412)).
- Pré-remplissage automatique de l'opérateur lors de la création d'une structure ([#1420](https://github.com/betagouv/bhasile/issues/1420)).
- Affichage des structures fermées côté serveur ([#1408](https://github.com/betagouv/bhasile/issues/1408)).
- Ajout de marqueurs de transformation sur le tableau des lieux ([#1407](https://github.com/betagouv/bhasile/issues/1407)).
- Ajout de marqueurs de transformation sur le tableau des finances ([#1403](https://github.com/betagouv/bhasile/issues/1403)).
- Ajout d'un onglet historique pour les structures ([#1382](https://github.com/betagouv/bhasile/issues/1382)).
- Amélioration de l'affichage des cartes de structure, même en phase de création ([#1399](https://github.com/betagouv/bhasile/issues/1399)).
- Ajout d'indicateurs d'impact pour les statistiques ([#1331](https://github.com/betagouv/bhasile/issues/1331), [#1360](https://github.com/betagouv/bhasile/issues/1360), [#1381](https://github.com/betagouv/bhasile/issues/1381)).
- Ajout de statistiques sur les finances ([#1366](https://github.com/betagouv/bhasile/issues/1366)).
- Ajout de statistiques sur les structures ([#1337](https://github.com/betagouv/bhasile/issues/1337)).

### Évolutions techniques
- Refonte de la gestion des versions des structures pour une meilleure cohérence et un suivi des modifications ([#1354](https://github.com/betagouv/bhasile/issues/1354), [#1356](https://github.com/betagouv/bhasile/issues/1356)).
- Optimisation des requêtes SQL pour les structures ([#1400](https://github.com/betagouv/bhasile/issues/1400)).
- Amélioration de la configuration du déploiement sur Scalingo ([#1303](https://github.com/betagouv/bhasile/issues/1303)).
- Mise à jour de plusieurs dépendances (Hono, esbuild, csv-parse, undici, @casl/react, @types/node, tmp).
- Amélioration de la gestion des tests E2E et correction de plusieurs erreurs ([#1329](https://github.com/betagouv/bhasile/issues/1329), [#1353](https://github.com/betagouv/bhasile/issues/1353), [#1374](https://github.com/betagouv/bhasile/issues/1374), [#1390](https://github.com/betagouv/bhasile/issues/1390), [#1394](https://github.com/betagouv/bhasile/issues/1394), [#1395](https://github.com/betagouv/bhasile/issues/1395)).

### Autres changements
- Correction de plusieurs bugs d'interface utilisateur et d'affichage ([#1404](https://github.com/betagouv/bhasile/issues/1404), [#1409](https://github.com/betagouv/bhasile/issues/1409), [#1410](https://github.com/betagouv/bhasile/issues/1410), [#1411](https://github.com/betagouv/bhasile/issues/1411), [#1413](https://github.com/betagouv/bhasile/issues/1413), [#1415](https://github.com/betagouv/bhasile/issues/1415), [#1417](https://github.com/betagouv/bhasile/issues/1417), [#1421](https://github.com/betagouv/bhasile/issues/1421), [#1423](https://github.com/betagouv/bhasile/issues/1423), [#1426](https://github.com/betagouv/bhasile/issues/1426), [#1427](https://github.com/betagouv/bhasile/issues/1427)).
- Amélioration de la documentation et des types ([#1305](https://github.com/betagouv/bhasile/issues/1305)).
- Correction de problèmes d'accessibilité ([#1308](https://github.com/betagouv/bhasile/issues/1308)).
- Suppression de code mort ([#1327](https://github.com/betagouv/bhasile/issues/1327)).
- Ajout d'un patch DSFR ([#1388](https://github.com/betagouv/bhasile/issues/1388)).
- Correction de la gestion des dates expirées des documents ([#1295](https://github.com/betagouv/bhasile/issues/1295)).
- Correction de l'affichage des barres de défilement horizontales ([#1306](https://github.com/betagouv/bhasile/issues/1306), [#1307](https://github.com/betagouv/bhasile/issues/1307)).
