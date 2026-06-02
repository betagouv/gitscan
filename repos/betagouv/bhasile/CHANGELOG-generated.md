## Changelog : bhasile (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment avec l'ajout d'un nouveau bloc d'activité et l'amélioration de la gestion des documents. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant les formulaires et les redirections. Des optimisations techniques ont également été réalisées pour améliorer les performances et la conformité de l'API.

### Évolutions fonctionnelles
- Ajout d'un nouveau bloc d'activité pour une meilleure visibilité des actions récentes [#1262](https://github.com/betagouv/bhasile/issues/1262).
- Amélioration de l'affichage des dates associées aux actes administratifs [#1260](https://github.com/betagouv/bhasile/issues/1260).
- Possibilité de sélectionner plusieurs structures [#1230](https://github.com/betagouv/bhasile/issues/1230).
- Affichage des dates d'expiration des documents dans le calendrier [#1295](https://github.com/betagouv/bhasile/issues/1295).
- Ajout d'un indicateur "manquant" pour l'historique [#1278](https://github.com/betagouv/bhasile/issues/1278).
- Ajout d'autres actes administratifs au CPOM [#1266](https://github.com/betagouv/bhasile/issues/1266).
- Amélioration de l'affichage des corrections pour le bloc d'activité [#1287](https://github.com/betagouv/bhasile/issues/1287).
- Ajout d'un CTA (Call To Action) pour les statistiques [#1273](https://github.com/betagouv/bhasile/issues/1273).
- Correction de l'alerte pour l'évaluation [#1304](https://github.com/betagouv/bhasile/issues/1304).
- Opérateurs peuvent désormais gérer les documents [#1275](https://github.com/betagouv/bhasile/issues/1275).
- Nouvelle structure d'en-tête [#1264](https://github.com/betagouv/bhasile/issues/1264).

### Évolutions techniques
- Mise en cache de `.next/cache` pour les builds Scalingo et inclusion de `node_modules` dans le slug pour optimiser les déploiements [#1303](https://github.com/betagouv/bhasile/issues/1303).
- Déplacement de la logique de `getStructureDefaultValues` côté serveur pour améliorer les performances [#1272](https://github.com/betagouv/bhasile/issues/1272).
- Refactorisation des gestionnaires PUT vers des routes `[id]` pour une meilleure conformité REST [#1270](https://github.com/betagouv/bhasile/issues/1270).
- Extraction de l'état d'interaction de l'adresse dans un hook `useAddressInteraction` pour une meilleure réutilisabilité [#1271](https://github.com/betagouv/bhasile/issues/1271).
- Suppression d'une option TypeScript obsolète [#1235](https://github.com/betagouv/bhasile/issues/1235).
- Migration vers `StructureVersion` [#1258](https://github.com/betagouv/bhasile/issues/1258).
- Ajout de tests de routes [#1210](https://github.com/betagouv/bhasile/issues/1210).
- Mise à jour de TypeScript vers la version 6.0.3 [#1222](https://github.com/betagouv/bhasile/issues/1222).

### Autres changements
- Correction d'un problème d'accessibilité (a11y) [#1308](https://github.com/betagouv/bhasile/issues/1308).
- Ajout de documentation pour les types [#1305](https://github.com/betagouv/bhasile/issues/1305).
- Correction d'un bug de défilement horizontal dans les tableaux [#1306](https://github.com/betagouv/bhasile/issues/1306).
- Correction de redirections incorrectes pour les opérateurs [#1252](https://github.com/betagouv/bhasile/issues/1252), [#1251](https://github.com/betagouv/bhasile/issues/1251), [#1241](https://github.com/betagouv/bhasile/issues/1241).
- Correction de CSS dans la page d'utilisation [#1233](https://github.com/betagouv/bhasile/issues/1233).
- Correction de l'affichage de la favicon "new" [#1248](https://github.com/betagouv/bhasile/issues/1248).
- Limitation des logs pour l'activité utilisateur [#1263](https://github.com/betagouv/bhasile/issues/1263).
- Mise à jour de l'image de la base de données [#1253](https://github.com/betagouv/bhasile/issues/1253).
- Suppression de l'avertissement concernant les multiples DNA sur l'ajout [#1228](https://github.com/betagouv/bhasile/issues/1228).
- Corrections mineures de CSS [#1249](https://github.com/betagouv/bhasile/issues/1249).
- Correction d'une erreur dans les hooks React [#1288](https://github.com/betagouv/bhasile/issues/1288).
