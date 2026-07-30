## Changelog : api-engagement (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'accessibilité de l'application, notamment pour les utilisateurs ayant des handicaps, en se conformant aux recommandations RGAA. Des corrections de bugs et des optimisations de performance ont également été implémentées, ainsi que de nouvelles fonctionnalités pour l'analyse des données et la gestion des missions, notamment l'ajout de taxonomies évolutives et la prise en charge de missions locales et distantes.

### Évolutions fonctionnelles
- Ajout de la prise en charge de nouvelles taxonomies avec une configuration évolutive pour les missions. [#1350](https://github.com/betagouv/api-engagement/issues/1350)
- Amélioration de la diffusion des missions avec l'ajout d'onglets Typesense pour les documents. [#1340](https://github.com/betagouv/api-engagement/issues/1340)
- Ajout d'un indicateur de performance clé (KPI) pour les recommandations par éditeur et le score des missions cliquées dans les analyses. [#1352](https://github.com/betagouv/api-engagement/issues/1352)
- Possibilité pour les diffuseurs de modérer leurs propres missions. [#1330](https://github.com/betagouv/api-engagement/issues/1330)
- Ajout d'une bannière de cookies pour le respect de la vie privée. [#1329](https://github.com/betagouv/api-engagement/issues/1329)
- Amélioration de l'affichage des statistiques publiques. [#1348](https://github.com/betagouv/api-engagement/issues/1348)
- Ajout de la prise en charge de missions à la fois locales et distantes, avec un score de correspondance optimisé. [#1260](https://github.com/betagouv/api-engagement/issues/1260)
- Ajout de l'export d'événements Posthog pour une analyse plus approfondie. [#1218](https://github.com/betagouv/api-engagement/issues/1218)
- Ajout de la possibilité d'enregistrer l'adresse e-mail pour la newsletter. [#1209](https://github.com/betagouv/api-engagement/issues/1209)

### Évolutions techniques
- Ajout d'en-têtes de sécurité pour le back-office et le widget. [#1354](https://github.com/betagouv/api-engagement/issues/1354)
- Correction d'une vulnérabilité potentielle de prise de contrôle de compte sur l'endpoint d'inscription. [#1253](https://github.com/betagouv/api-engagement/issues/1253)
- Amélioration des performances de la requête de correspondance des missions. [#1268](https://github.com/betagouv/api-engagement/issues/1268)
- Optimisation de la requête pour l'analyse des clics sur les missions. [#1229](https://github.com/betagouv/api-engagement/issues/1229)
- Refactorisation de la diffusion des missions pour utiliser un snapshot. [#1336](https://github.com/betagouv/api-engagement/issues/1336)
- Mise à jour des dépendances Docker et Node.js.
- Amélioration de la gestion des secrets pour l'API. [#1307](https://github.com/betagouv/api-engagement/issues/1307)
- Suppression du workflow Claude.
- Ajout de la prise en charge de la diffusion de règles pour les éditeurs. [#1264](https://github.com/betagouv/api-engagement/issues/1264)

### Autres changements
- Nombreuses corrections pour améliorer la conformité aux recommandations RGAA (accessibilité web), notamment concernant les contrastes, la navigation au clavier, les titres, les liens, les champs de formulaire et les messages d'erreur. [#1273](https://github.com/betagouv/api-engagement/issues/1273), [#1277](https://github.com/betagouv/api-engagement/issues/1277), [#1274](https://github.com/betagouv/api-engagement/issues/1274), [#1278](https://github.com/betagouv/api-engagement/issues/1278), [#1279](https://github.com/betagouv/api-engagement/issues/1279), [#1280](https://github.com/betagouv/api-engagement/issues/1280), [#1282](https://github.com/betagouv/api-engagement/issues/1282), [#1283](https://github.com/betagouv/api-engagement/issues/1283), [#1284](https://github.com/betagouv/api-engagement/issues/1284), [#1285](https://github.com/betagouv/api-engagement/issues/1285), [#1286](https://github.com/betagouv/api-engagement/issues/1286), [#1287](https://github.com/betagouv/api-engagement/issues/1287), [#1288](https://github.com/betagouv/api-engagement/issues/1288), [#1290](https://github.com/betagouv/api-engagement/issues/1290), [#1291](https://github.com/betagouv/api-engagement/issues/1291), [#1292](https://github.com/betagouv/api-engagement/issues/1292), [#1293](https://github.com/betagouv/api-engagement/issues/1293), [#1294](https://github.com/betagouv/api-engagement/issues/1294), [#1295](https://github.com/betagouv/api-engagement/issues/1295), [#1296](https://github.com/betagouv/api-engagement/issues/1296), [#1298](https://github.com/betagouv/api-engagement/issues/1298), [#1308](https://github.com/betagouv/api-engagement/issues/1308), [#1309](https://github.com/betagouv/api-engagement/issues/1309), [#1310](https://github.com/betagouv/api-engagement/issues/1310), [#1311](https://github.com/betagouv/api-engagement/issues/1311), [#1312](https://github.com/betagouv/api-engagement/issues/1312), [#1313](https://github.com/betagouv/api-engagement/issues/1313), [#1314](https://github.com/betagouv/api-engagement/issues/1314), [#1315](https://github.com/betagouv/api-engagement/issues/1315), [#1316](https://github.com/betagouv/api-engagement/issues/1316), [#1317](https://github.com/betagouv/api-engagement/issues/1317), [#1318](https://github.com/betagouv/api-engagement/issues/1318), [#1319](https://github.com/betagouv/api-engagement/issues/1319), [#1320](https://github.com/betagouv/api-engagement/issues/1320), [#1321](https://github.com/betagouv/api-engagement/issues/1321), [#1322](https://github.com/betagouv/api-engagement/issues/1322), [#1323](https://github.com/betagouv/api-engagement/issues/1323), [#1324](https://github.com/betagouv/api-engagement/issues/1324), [#1325](https://github.com/betagouv/api-engagement/issues/1325), [#1326](https://github.com/betagouv/api-engagement/issues/1326), [#1327](https://github.com/betagouv/api-engagement/issues/1327), [#1328](https://github.com/betagouv/api-engagement/issues/1328)
- Correction de données pour les missions de gendarmerie et de police. [#1351](https://github.com/betagouv/api-engagement/issues/1351)
- Correction du sur-comptage des événements mensuels dans les analyses. [#1332](https://github.com/betagouv/api-engagement/issues/1332)
- Correction du chargement préalable des résultats du quiz. [#1344](https://github.com/betagouv/api-engagement/issues/1344)
- Correction de l'affichage des en-têtes des partenaires dans la description des missions. [#1331](https://github.com/betagouv/api-engagement/issues/1331)
- Suppression de l'exclusion des utilisateurs internes au niveau de la personne dans les analyses. [#1333](https://github.com/betagouv/api-engagement/issues/1333)
- Correction de l'injection du token dans l'appel jstag. [#1351](https://github.com/betagouv/api-engagement/issues/1351)
- Amélioration du temps d'exécution du modèle d'analyse. [#1347](https://github.com/betagouv/api-engagement/issues/1347)
- Revert d'une optimisation de la requête de correspondance. [#1306](https://github.com/betagouv/api-engagement/issues/1306)
