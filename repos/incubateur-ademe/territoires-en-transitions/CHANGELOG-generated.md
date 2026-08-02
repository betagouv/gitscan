## Changelog : territoires-en-transitions (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des indicateurs et des référentiels, avec l'ajout de nouvelles fonctionnalités comme l'import IA de plans, l'amélioration de la gestion des données open data et la préparation de la bascule vers le nouveau référentiel Climat Ressources. Des corrections de sécurité et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'importer un plan via l'IA, incluant la création, le suivi de progression et la reprise. [#7043259](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7043259)
- Amélioration de la gestion des statuts et des liens des fiches actions dans le référentiel TE. [#9397c7d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/9397c7d)
- Ajout d'une vue SGPE avec persistance locale pour le référentiel TE. [#9397c7d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/9397c7d)
- Possibilité de modifier les dates de début et de fin d'un plan. [#81bf6e6](https://github.com/incubateur-ademe/territoires-en-transitions/commit/81bf6e6)
- Amélioration de l'affichage et de la gestion des données open data dans les indicateurs, avec ajout d'infobulles et de pastilles. [#fbaa1bb](https://github.com/incubateur-ademe/territoires-en-transitions/commit/fbaa1bb), [#ce52b98](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ce52b98)
- Ajout d'un bandeau d'information pour les référentiels archivés ou en lecture seule. [#d71bd9b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d71bd9b)
- Amélioration de la gestion des permissions pour les utilisateurs et les collectivité. [#b6c20b4](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b6c20b4)
- Ajout de la possibilité de changer l'année de référence des indicateurs. [#220087e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/220087e)

### Évolutions techniques
- Refactor de l'authentification pour simplifier l'architecture et améliorer la sécurité. [#7d22412](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7d22412), [#65c15f7](https://github.com/incubateur-ademe/territoires-en-transitions/commit/65c15f7)
- Mise à jour de Next.js et de TypeScript vers les dernières versions. [#607de86](https://github.com/incubateur-ademe/territoires-en-transitions/commit/607de86), [#de92a34](https://github.com/incubateur-ademe/territoires-en-transitions/commit/de92a34)
- Amélioration de la gestion des variables d'environnement avec dotenvx. [#98259de](https://github.com/incubateur-ademe/territoires-en-transitions/commit/98259de)
- Refactor de plusieurs composants pour améliorer la performance et la maintenabilité.
- Préparation de la bascule vers le nouveau référentiel Climat Ressources avec l'ajout d'un garde de mode et des scripts d'import. [#d91b75e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d91b75e), [#66413fe](https://github.com/incubateur-ademe/territoires-en-transitions/commit/66413fe)
- Amélioration de la robustesse des tests e2e. [#dff76c4](https://github.com/incubateur-ademe/territoires-en-transitions/commit/dff76c4)

### Autres changements
- Suppression des feature flags PostHog complètement déployés. [#5ce9432](https://github.com/incubateur-ademe/territoires-en-transitions/commit/5ce9432)
- Nettoyage du code et des fichiers de configuration.
- Mise à jour de la documentation.
- Correction de bugs mineurs et amélioration de l'accessibilité.
