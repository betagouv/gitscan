## Changelog : bhasile (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau des tableaux de données et de la gestion des documents. Des corrections de bugs et des améliorations de performance ont également été apportées, ainsi que des ajouts concernant la gestion des opérateurs et des structures d'hébergement.

### Évolutions fonctionnelles
- Ajout de la possibilité de masquer les adresses pour les agents non autorisés. [#1316](https://github.com/betagouv/bhasile/issues/1316)
- Affichage correct de la filiale pour les structures. [#1317](https://github.com/betagouv/bhasile/issues/1317)
- Ajout des contacts des opérateurs. [#1286](https://github.com/betagouv/bhasile/issues/1286)
- Amélioration de la modal d'accès refusé. [#1314](https://github.com/betagouv/bhasile/issues/1314)
- Affichage des dates d'expiration des documents dans le calendrier. [#1295](https://github.com/betagouv/bhasile/issues/1295)
- Ajout d'un indicateur "manquant" pour l'historique. [#1278](https://github.com/betagouv/bhasile/issues/1278)
- Ajout d'un nouveau bloc d'activité. [#1262](https://github.com/betagouv/bhasile/issues/1262)
- Ajout de la possibilité d'ajouter des "autres actes administratifs" au CPOM. [#1266](https://github.com/betagouv/bhasile/issues/1266)
- Nouvelle structure d'en-tête. [#1264](https://github.com/betagouv/bhasile/issues/1264)
- Migration vers StructureVersion. [#1258](https://github.com/betagouv/bhasile/issues/1258)
- Affichage des dates inférées à partir des actes administratifs. [#1260](https://github.com/betagouv/bhasile/issues/1260)
- Ajout d'un commentaire pour les documents financiers. [#1261](https://github.com/betagouv/bhasile/issues/1261)
- Ajout d'un CTA pour les statistiques. [#1273](https://github.com/betagouv/bhasile/issues/1273)
- Ajout du logo de l'opérateur. [#1319](https://github.com/betagouv/bhasile/issues/1319)
- Mise à jour des champs des documents opérateur. [#1326](https://github.com/betagouv/bhasile/issues/1326)

### Évolutions techniques
- Amélioration des performances en déplaçant une partie de la logique côté serveur pour `getStructureDefaultValues`. [#1272](https://github.com/betagouv/bhasile/issues/1272)
- Refactorisation des gestionnaires PUT pour respecter la conformité REST en utilisant les routes `[id]`. [#1270](https://github.com/betagouv/bhasile/issues/1270)
- Extraction de l'état d'interaction de l'adresse dans un hook `useAddressInteraction`. [#1271](https://github.com/betagouv/bhasile/issues/1271)
- Mise en cache de `.next/cache` et envoi de `node_modules` dans le slug pour améliorer les builds Scalingo. [#1303](https://github.com/betagouv/bhasile/issues/1303)
- Correction d'un problème de scroll horizontal dans les tableaux. [#1306](https://github.com/betagouv/bhasile/issues/1306)
- Correction d'un problème de la barre de défilement qui se superposait au contenu dans les tableaux. [#1307](https://github.com/betagouv/bhasile/issues/1307)
- Amélioration de l'accessibilité (a11y). [#1308](https://github.com/betagouv/bhasile/issues/1308)
- Ajout de documentation pour les types. [#1305](https://github.com/betagouv/bhasile/issues/1305)

### Autres changements
- Ajout de documentation pour Dependabot. [#1322](https://github.com/betagouv/bhasile/issues/1322)
- Correction de la redirection de l'opérateur. [#1251](https://github.com/betagouv/bhasile/issues/1251) et [#1252](https://github.com/betagouv/bhasile/issues/1252)
- Ajout d'une alerte pour l'évaluation. [#1304](https://github.com/betagouv/bhasile/issues/1304)
- Correction d'un bug lié à l'affichage de la favicon "new". [#1248](https://github.com/betagouv/bhasile/issues/1248)
- Mise à jour de l'image de la base de données. [#1253](https://github.com/betagouv/bhasile/issues/1253)
- Mineures mises à jour CSS. [#1249](https://github.com/betagouv/bhasile/issues/1249)
- Limitation des logs pour l'activité utilisateur. [#1263](https://github.com/betagouv/bhasile/issues/1263)
- Ajout d'une erreur pour `react-hooks/exhaustive-deps`. [#1288](https://github.com/betagouv/bhasile/issues/1288)
