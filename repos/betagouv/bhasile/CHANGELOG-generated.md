## Changelog : bhasile (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'implémentation et l'amélioration du module de gestion des transformations de structures d'hébergement. Les utilisateurs peuvent désormais initier des transformations à partir de formulaires dédiés, gérer les documents associés, et visualiser l'état d'avancement des différentes étapes. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des données, notamment pour les opérateurs et les documents.

### Évolutions fonctionnelles
- Ajout de la gestion des transformations de structures : création, mise à jour, validation. ([#1234](https://github.com/betagouv/bhasile/issues/1234))
- Possibilité de créer des transformations à partir des formulaires de description des structures. ([#1298](https://github.com/betagouv/bhasile/issues/1298), [#1310](https://github.com/betagouv/bhasile/issues/1310))
- Ajout de formulaires dédiés pour les actes administratifs et les hébergements lors des extensions/contractions. ([#1321](https://github.com/betagouv/bhasile/issues/1321), [#1323](https://github.com/betagouv/bhasile/issues/1323))
- Affichage de la liste des transformations en cours. ([#1309](https://github.com/betagouv/bhasile/issues/1309))
- Amélioration de l'affichage des dates des documents dans le calendrier. ([#1295](https://github.com/betagouv/bhasile/issues/1295))
- Ajout de la possibilité de créer des documents administratifs et des places d'hébergement *ex nihilo*. ([#1290](https://github.com/betagouv/bhasile/issues/1290), [#1291](https://github.com/betagouv/bhasile/issues/1291))
- Ajout de la gestion des documents de l'opérateur (logo, etc.). ([#1326](https://github.com/betagouv/bhasile/issues/1326), [#1319](https://github.com/betagouv/bhasile/issues/1319))
- Ajout de contacts pour les opérateurs. ([#1286](https://github.com/betagouv/bhasile/issues/1286))
- Amélioration du bloc d'activité avec un CTA vers les statistiques. ([#1273](https://github.com/betagouv/bhasile/issues/1273), [#1287](https://github.com/betagouv/bhasile/issues/1287))
- Affichage des filiales correctement. ([#1317](https://github.com/betagouv/bhasile/issues/1317))

### Évolutions techniques
- Refactorisation du code lié aux transformations pour une meilleure conformité REST.
- Migration vers une nouvelle structure de version pour les structures d'hébergement.
- Optimisation des performances en mettant en cache les données sur Scalingo.
- Amélioration de la gestion des erreurs et des validations de formulaires.
- Suppression de code obsolète lié aux migrations.
- Ajout de tests E2E pour les nouvelles fonctionnalités. ([#1284](https://github.com/betagouv/bhasile/issues/1284))
- Amélioration de la gestion des types et ajout de documentation. ([#1305](https://github.com/betagouv/bhasile/issues/1305))
- Amélioration de l'accessibilité (a11y). ([#1308](https://github.com/betagouv/bhasile/issues/1308))

### Autres changements
- Mise à jour de la documentation pour dependabot. ([#1322](https://github.com/betagouv/bhasile/issues/1322))
- Corrections de bugs mineurs liés à l'interface utilisateur et au comportement des formulaires. ([#1311](https://github.com/betagouv/bhasile/issues/1311), [#1307](https://github.com/betagouv/bhasile/issues/1307), [#1335](https://github.com/betagouv/bhasile/issues/1335))
- Amélioration des indicateurs d'impact. ([#1331](https://github.com/betagouv/bhasile/issues/1331))
- Correction du comportement des inputs radio. ([#1341](https://github.com/betagouv/bhasile/issues/1341))
- Suppression des tests dupliqués. ([#1340](https://github.com/betagouv/bhasile/issues/1340))
- Correction de bugs dans les tests de développement. ([#1346](https://github.com/betagouv/bhasile/issues/1346))
- Empêchement de la contraction/extension sur des lieux incorrects. ([#1332](https://github.com/betagouv/bhasile/issues/1332))
- Affichage de l'adresse complète dans les formulaires de transformation. ([#1343](https://github.com/betagouv/bhasile/issues/1343))
- Ajout de règles de préremplissage pour les transformations. ([#1339](https://github.com/betagouv/bhasile/issues/1339))
- Ajout de limites de largeur pour les structures, CPOMs, opérateurs et transformations. ([#1338](https://github.com/betagouv/bhasile/issues/1338))
- Correction d'un bug empêchant la suppression silencieuse des avenants. ([#1334](https://github.com/betagouv/bhasile/issues/1334))
- Affichage uniquement des structures finalisées lors de la sélection pour les transformations. ([#1336](https://github.com/betagouv/bhasile/issues/1336))
- Correction d'une redirection après la création d'une transformation. ([#1335](https://github.com/betagouv/bhasile/issues/1335))
- Ajout de l'initialisation des structureVersions lors de la création d'une transformation. ([#1299](https://github.com/betagouv/bhasile/issues/1299))
- Correction de l'affichage des dates expirées des documents. ([#1295](https://github.com/betagouv/bhasile/issues/1295))
- Ajout d'un avertissement pour l'évaluation. ([#1304](https://github.com/betagouv/bhasile/issues/1304))
- Cache des fichiers `.next/cache` et inclusion de `node_modules` dans le slug pour améliorer les builds Scalingo. ([#1303](https://github.com/betagouv/bhasile/issues/1303))
- Suppression des fichiers de migration obsolètes.
