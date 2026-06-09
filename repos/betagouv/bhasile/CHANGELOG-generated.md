## Changelog : bhasile (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'implémentation des transformations de structures (lieux d'hébergement, actes administratifs, etc.). De nouvelles fonctionnalités permettent la création, la modification et la validation de ces transformations, avec une attention particulière portée à l'expérience utilisateur et à la gestion des erreurs. Des améliorations ont également été apportées à la gestion des opérateurs et à l'interface utilisateur générale.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer la première adresse associée à une structure [#1313](https://github.com/betagouv/bhasile/issues/1313).
- Amélioration de la gestion des documents des opérateurs : ajout de champs et d'un logo [#1326](https://github.com/betagouv/bhasile/issues/1326), [#1319](https://github.com/betagouv/bhasile/issues/1319).
- Implémentation d'une liste des transformations en cours [#1309](https://github.com/betagouv/bhasile/issues/1309).
- Finalisation du processus de création à partir des formulaires "Structures", "Places" et "Actes" [#1310](https://github.com/betagouv/bhasile/issues/1310).
- Ajout de la possibilité d'étendre ou de contracter les formulaires "Actes administratifs" et "Hébergement" [#1323](https://github.com/betagouv/bhasile/issues/1323), [#1321](https://github.com/betagouv/bhasile/issues/1321).
- Ajout d'une page de validation des transformations [#1312](https://github.com/betagouv/bhasile/issues/1312).
- Masquage des adresses pour les agents non autorisés [#1316](https://github.com/betagouv/bhasile/issues/1316).
- Affichage correct de la filiale d'un organisme [#1317](https://github.com/betagouv/bhasile/issues/1317).
- Initialisation des versions de structure lors de la création d'une transformation [#1299](https://github.com/betagouv/bhasile/issues/1299).
- Ajout de contacts pour les opérateurs [#1286](https://github.com/betagouv/bhasile/issues/1286).
- Amélioration de la modal d'accès refusé [#1314](https://github.com/betagouv/bhasile/issues/1314).
- Ajout du flux complet de fermeture (fermeture d'une structure) [#1293](https://github.com/betagouv/bhasile/issues/1293).
- Correction de l'enregistrement du contenu du formulaire lors de la sauvegarde via les boutons d'en-tête [#1297](https://github.com/betagouv/bhasile/issues/1297).
- Ajout de la création *ex nihilo* de documents administratifs [#1291](https://github.com/betagouv/bhasile/issues/1291).
- Ajout de la création *ex nihilo* de lieux d'hébergement [#1290](https://github.com/betagouv/bhasile/issues/1290).
- Affichage des dates d'expiration des documents dans le bloc calendrier [#1295](https://github.com/betagouv/bhasile/issues/1295).
- Ajout d'un CTA (call to action) pour les statistiques [#1273](https://github.com/betagouv/bhasile/issues/1273).
- Ajout de nouveaux champs pour les activités [#1262](https://github.com/betagouv/bhasile/issues/1262).
- Ajout d'autres actes administratifs au CPOM [#1266](https://github.com/betagouv/bhasile/issues/1266).
- Ajout des formulaires de transformation aux structures [#1259](https://github.com/betagouv/bhasile/issues/1259).
- Ajout des boutons d'accès aux transformations [#1256](https://github.com/betagouv/bhasile/issues/1256).

### Évolutions techniques
- Refactorisation du dépôt de transformation [#1280](https://github.com/betagouv/bhasile/issues/1280).
- Migration vers StructureVersion [#1258](https://github.com/betagouv/bhasile/issues/1258).
- Amélioration des performances en mettant en cache `.next/cache` et en optimisant le déploiement sur Scalingo [#1303](https://github.com/betagouv/bhasile/issues/1303).
- Déplacement de la logique de `getStructureDefaultValues` côté serveur pour améliorer les performances [#1272](https://github.com/betagouv/bhasile/issues/1272).
- Ajout de tests E2E pour la nouvelle version [#1284](https://github.com/betagouv/bhasile/issues/1284).
- Ajout de documentation pour dependabot [#1322](https://github.com/betagouv/bhasile/issues/1322).
- Ajout de types et documentation pour améliorer la maintenabilité [#1305](https://github.com/betagouv/bhasile/issues/1305).
- Suppression de fichiers de migration obsolètes [#1276](https://github.com/betagouv/bhasile/issues/1276).

### Autres changements
- Nettoyage du code et correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur [#1311](https://github.com/betagouv/bhasile/issues/1311), [#1307](https://github.com/betagouv/bhasile/issues/1307), [#1308](https://github.com/betagouv/bhasile/issues/1308), [#1248](https://github.com/betagouv/bhasile/issues/1248).
- Correction d'un problème d'affichage de l'alerte pour l'évaluation [#1304](https://github.com/betagouv/bhasile/issues/1304).
- Correction d'un problème de redirection pour les opérateurs [#1252](https://github.com/betagouv/bhasile/issues/1252), [#1251](https://github.com/betagouv/bhasile/issues/1251).
- Correction d'un problème d'affichage du favicon [#1248](https://github.com/betagouv/bhasile/issues/1248).
- Ajout d'un flag `isMissing` pour l'historique [#1278](https://github.com/betagouv/bhasile/issues/1278).
- Suppression de l'obsolescence de seeders [#1276](https://github.com/betagouv/bhasile/issues/1276).
- Ajout de styles CSS mineurs [#1249](https://github.com/betagouv/bhasile/issues/1249).
