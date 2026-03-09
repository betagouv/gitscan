## Changelog : territoires-en-transitions (30 derniers jours)

### Résumé
Les dernières mises à jour de la plateforme se concentrent sur l'amélioration de la performance, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment autour de la gestion des référentiels, des notifications et de l'interface utilisateur. Des optimisations ont été apportées à l'affichage des données, à la gestion des permissions et à l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Possibilité de définir des préférences utilisateur pour les notifications (activation/désactivation). [#88cef83](https://github.com/incubateur-ademe/territoires-en-transitions/commit/88cef83)
- Amélioration de l'affichage des badges dans l'export PDF des fiches action. [#aeb4570](https://github.com/incubateur-ademe/territoires-en-transitions/commit/aeb4570)
- Ajout de la colonne COT (Code de l'Organisme Territorial) dans la liste des collectivités et les informations utilisateur. [#ff525e8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ff525e8)
- Correction de l'affichage des plans et des sous-actions dans l'interface utilisateur. [#309db8e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/309db8e)
- Ajout d'une date maximale à la saisie de la date de fin d'une sous-action. [#9914848](https://github.com/incubateur-ademe/territoires-en-transitions/commit/9914848)
- Amélioration de la gestion des notifications d'affectation comme pilote, avec consolidation des notifications pour plusieurs fiches. [#2e4806f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2e4806f)
- Correction de l'affichage de l'historique en mode visite. [#06a5bdb](https://github.com/incubateur-ademe/territoires-en-transitions/commit/06a5bdb)
- Ajout de la possibilité de mettre à jour les réponses aux questions de personnalisation via tRPC. [#f6faef9](https://github.com/incubateur-ademe/territoires-en-transitions/commit/f6faef9)
- Correction de l'affichage des actions liées pour le rôle contributeur. [#03e79f7](https://github.com/incubateur-ademe/territoires-en-transitions/commit/03e79f7)

### Évolutions techniques
- Migration des endpoints de la liste des membres vers tRPC. [#b9f53cd](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9f53cd)
- Refactoring de l'import des référentiels. [#8eaedd4](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8eaedd4)
- Migration des filtres de la page des collectivités vers nuqs. [#804c35b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/804c35b)
- Utilisation de tRPC pour la sauvegarde des actions statuts et des preuves. [#91e11d5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/91e11d5)
- Suppression de code obsolète (vues SQL, fonctions, tests). [#906b00f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/906b00f), [#7246743](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7246743), [#04fcb13](https://github.com/incubateur-ademe/territoires-en-transitions/commit/04fcb13), [#287bab6](https://github.com/incubateur-ademe/territoires-en-transitions/commit/287bab6)
- Mise à jour des dépendances Supabase et ESLint. [#5dfe3db](https://github.com/incubateur-ademe/territoires-en-transitions/commit/5dfe3db), [#6ae6e50](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6ae6e50)
- Activation de Turbopack pour les builds en développement et production (app et auth). [#466128a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/466128a)
- Migration des graphiques Nivo vers Echarts. [#6e5eebe](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6e5eebe)
- Ajout de logs Sentry pour le backend. [#95018da](https://github.com/incubateur-ademe/territoires-en-transitions/commit/95018da)

### Autres changements
- Ajout d'un ResizeObserver pour ajuster le layout des graphiques. [#b80c4ba](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b80c4ba)
- Correction de bugs mineurs liés à l'affichage des tooltips et des badges. [#8de4b9d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8de4b9d), [#de81dff](https://github.com/incubateur-ademe/territoires-en-transitions/commit/de81dff)
- Amélioration de la documentation et des tests unitaires.
- Correction de coquilles et amélioration de la lisibilité du code.
- Ajout d'événements pour le suivi des actions dans l'interface utilisateur. [#87cbb55](https://github.com/incubateur-ademe/territoires-en-transitions/commit/87cbb55)
