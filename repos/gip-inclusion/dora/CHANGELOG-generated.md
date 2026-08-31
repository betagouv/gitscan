## Changelog : dora (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a connu des évolutions structurelles importantes, notamment une refonte de la gestion des services et des publics pour gagner en cohérence et en fiabilité. Les utilisateurs bénéficieront d'une expérience de recherche améliorée, de nouvelles notifications Slack et d'exports de données plus complets.

### Évolutions fonctionnelles
- **Notifications & Accès** : Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296) et accès facilité aux pages d'administration pour les GT [#1286](https://github.com/gip-inclusion/dora/issues/1286).
- **Recherche & Filtres** : Amélioration de la recherche textuelle [#1254](https://github.com/gip-inclusion/dora/issues/1254), limitation du nombre de résultats pour une meilleure lisibilité [#1245](https://github.com/gip-inclusion/dora/issues/1245) et correction des filtres de publics [#1261](https://github.com/gip-inclusion/dora/issues/1261).
- **Gestion des Services** : Ajout de champs de mobilisation, suppression de la limite de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289) et affichage détaillé des précisions des publics dans les fiches services [#1264](https://github.com/gip-inclusion/dora/issues/1264).
- **Exports & Corrections** : Ajout de l'identifiant FT dans les exports d'orientations reçues [#1290](https://github.com/gip-inclusion/dora/issues/1290), correction des URL d'administration [#1295](https://github.com/gip-inclusion/dora/issues/1295) et garantie de l'unicité des critères d'admission [#1243](https://github.com/gip-inclusion/dora/issues/1243).

### Évolutions techniques
- **Refonte du modèle Services** : Simplification majeure de la gestion des types de services via l'introduction d'un champ unique `kind` et suppression des anciennes relations complexes (M2M) [#1266](https://github.com/gip-inclusion/dora/issues/1266), [#1249](https://github.com/gip-inclusion/dora/issues/1249), [#1282](https://github.com/gip-inclusion/dora/issues/1282) et [#1257](https://github.com/gip-inclusion/dora/issues/1257).
- **Migration des données (Publics)** : Transition vers le référentiel DI et restructuration de la lecture des publics pour assurer la cohérence des données [#1237](https://github.com/gip-inclusion/dora/issues/1237), [#1283](https://github.com/gip-inclusion/dora/issues/1283) et [#1252](https://github.com/gip-inclusion/dora/issues/1252).
- **Optimisations & Intégrité** : Parallélisation des appels pour accélérer l'édition des services et modèles [#1281](https://github.com/gip-inclusion/dora/issues/1281), fusion algorithmique des descriptions pour éviter les doublons [#1293](https://github.com/gip-inclusion/dora/issues/1293) et migration des champs de recherche vers des formats plus performants (`ArrayField`) [#1247](https://github.com/gip-inclusion/dora/issues/1247).

### Autres changements
- **Nettoyage** : Suppression de commandes d'import/export obsolètes [#1260](https://github.com/gip-inclusion/dora/issues/1260), [#1285](https://github.com/gip-inclusion/dora/issues/1285) et de code devenu inutile [#1278](https://github.com/gip-inclusion/dora/issues/1278).
- **Maintenance** : Ajout d'une commande de normalisation des mots de passe [#1271](https://github.com/gip-inclusion/dora/issues/1271).
