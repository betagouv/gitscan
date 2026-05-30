## Changelog : bhasile (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Bhasile se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau de la présentation des informations sur les structures et les actes administratifs. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'ajout de tests unitaires et d'intégration renforce la qualité du code.

### Évolutions fonctionnelles
- Amélioration de la présentation des activités et des informations sur les structures [#1287, #1262, #1264, #1265].
- Ajout d'un indicateur visuel pour signaler les données manquantes dans l'historique [#1278].
- Possibilité de sélectionner plusieurs structures [#1230].
- Affichage des dates déduites des actes administratifs [#1260].
- Ajout de commentaires sur les documents financiers [#1261].
- Ajout d'autres actes administratifs au CPOM [#1266].
- Ajout d'un CTA (Call To Action) pour accéder aux statistiques [#1273].
- Amélioration de la gestion des documents opérateurs [#1275].
- Migration vers StructureVersion pour une meilleure gestion des versions [#1258].
- Correction du problème de redirection pour les opérateurs [#1252, #1251, #1241].
- Correction de l'affichage de la favicon "new" [#1248].

### Évolutions techniques
- Refactorisation du code pour améliorer la conformité REST des routes PUT [#1270].
- Déplacement de la logique de récupération des valeurs par défaut de la structure côté serveur pour optimiser les performances [#1272].
- Extraction de la logique d'interaction avec l'adresse dans un hook réutilisable `useAddressInteraction` [#1271].
- Suppression d'une option TypeScript obsolète [#1235].
- Passage à TypeScript 6.0.3 [#1222].
- Mise en place d'une architecture à 3 niveaux pour une meilleure organisation du code [#1219].
- Ajout de tests unitaires et d'intégration pour les routes et la page des formulaires [#1210, #1203, #1216].
- Limitation des logs d'activité utilisateur pour améliorer les performances [#1263].
- Ajout d'indicateurs de qualité pour les actes administratifs [#1218].

### Autres changements
- Corrections de style CSS mineures [#1249, #1233, #1213, #1214].
- Mise à jour de l'image de la base de données [#1253].
- Correction d'une erreur dans les dépendances React [#1288].
- Mises à jour de dépendances (tmp, divers paquets mineurs) [#1285, #1274, #1254, #1250, #1247, #1246, #1242].
