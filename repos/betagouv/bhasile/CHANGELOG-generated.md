## Changelog : bhasile (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration du parcours de création et de modification des structures et de leurs transformations, ainsi que sur l'ajout de nouvelles statistiques et indicateurs de performance. Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser et optimiser l'application.

### Évolutions fonctionnelles
- Ajout d'un bloc de statistiques sur les finances [#1366].
- Possibilité de lier une campagne à une version de structure [#1379].
- Ajout de statistiques sur les types de places [#1361].
- Amélioration de l'affichage des contacts des opérateurs [#1286].
- Ajout d'un logo pour les opérateurs [#1319].
- Ajout de la possibilité de créer des structures *ex nihilo* (à partir de zéro) avec des formulaires dédiés pour les documents administratifs, les places et les hébergements [#1277, #1290, #1291].
- Ajout d'un flux complet pour la fermeture des structures [#1293].
- Amélioration de l'affichage des dates d'expiration des documents dans le calendrier [#1295].
- Ajout d'indicateurs d'impact et amélioration de leur affichage [#1331, #1360].
- Amélioration de la gestion des avenants (extensions/contractions) avec la possibilité de les associer aux transformations [#1330].
- Ajout de la possibilité de supprimer la première adresse [#1313].
- Affichage des adresses complètes dans les formulaires de transformation [#1343].
- Ajout de la possibilité de modifier les transformations [#1283].
- Amélioration de l'accessibilité (a11y) avec correction d'un problème d'alerte [#1308].

### Évolutions techniques
- Mise à jour de plusieurs dépendances (React, Next.js, Prisma, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Refactorisation du code lié aux transformations pour une meilleure maintenabilité [#1370, #1380].
- Amélioration des tests E2E (end-to-end) pour assurer la qualité de l'application [#1329, #1374, #1390, #1394].
- Optimisation de la gestion du cache et des builds sur Scalingo [#1303].
- Correction de problèmes liés aux tests de développement [#1374].
- Ajout de documentation pour les types utilisés dans le code [#1305].
- Suppression de fichiers de migration obsolètes.
- Amélioration de la performance en déplaçant certaines opérations côté serveur [#1272].

### Autres changements
- Ajout d'un patch DSFR (Design System Française) [#1388].
- Correction de bugs mineurs liés à l'affichage et au comportement de certains composants [#1325, #1340, #1346, #1347, #1351, #1352, #1355, #1356, #1357, #1358, #1362, #1363, #1364, #1365, #1371, #1373, #1375, #1381, #1382, #1385, #1387, #1391, #1392, #1393].
- Ajout de logs plus précis pour le backfill des versions de structure [#1393].
- Correction de problèmes liés à l'utilisation des tests E2E avec les versions de structure [#1390, #1394].
- Amélioration de la gestion des erreurs et des validations dans les formulaires [#1296, #1306, #1311, #1314, #1316, #1317].
- Ajout de règles de préremplissage pour la création de structures à partir de transformations [#1339].
- Ajout de liens vers les transformations dans les cartes de structure [#1367, #1368].
- Ajout d'un indicateur visuel pour les structures en cours de finalisation [#1369].
- Correction de problèmes d'affichage des champs DNA et FINESS lors de la création de structures [#1371].
- Ajout de la possibilité de supprimer des transformations [#1365].
- Prévention de la duplication des numéros DNA ou FINESS [#1375].
- Ajout d'une indication visuelle pour les filiales [#1317].
