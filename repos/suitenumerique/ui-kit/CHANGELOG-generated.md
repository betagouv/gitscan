## Changelog : ui-kit (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration de la gestion des fichiers, notamment avec l'ajout d'un nouveau composant de prévisualisation de fichiers et l'amélioration des tests. Des améliorations ont également été apportées aux icônes et à la gestion des menus, ainsi que des corrections de bugs et des optimisations techniques.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FilePreview` permettant de visualiser différents types de fichiers [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b).
- Amélioration du composant `PdfPreview` avec des corrections de styles [#8bf11e9](https://github.com/suitenumerique/ui-kit/commit/8bf11e9).
- Ajout de nouvelles icônes et mise à jour des icônes existantes [#75664ce](https://github.com/suitenumerique/ui-kit/commit/75664ce).
- Amélioration du menu d'actions avec l'ajout de la possibilité de définir des actions personnalisées via la prop `customHeaderActions` [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e).
- Ajout de la locale néerlandaise (nl-NL) [#121966c](https://github.com/suitenumerique/ui-kit/commit/121966c).
- Utilisation de l'icône `more_horiz` pour le menu d'actions [#5e5a964](https://github.com/suitenumerique/ui-kit/commit/5e5a964).

### Évolutions techniques
- Mise en place de tests E2E avec Playwright pour le composant `FilePreview` [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9).
- Ajout de tests Playwright pour les tests de composants [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9).
- Intégration de l'exécution des tests Playwright E2E dans la CI [#caaa464](https://github.com/suitenumerique/ui-kit/commit/caaa464).
- Amélioration du processus de génération des icônes [#289ce30](https://github.com/suitenumerique/ui-kit/commit/289ce30).
- Correction du service des fichiers `.mjs` et `.wasm` avec les bons types MIME [#2af81e4](https://github.com/suitenumerique/ui-kit/commit/2af81e4).
- Import du worker PDF dans les scripts de pré-construction [#4d8098a](https://github.com/suitenumerique/ui-kit/commit/4d8098a).
- Remplacement de `headerRightContent` par `customHeaderActions` pour une meilleure flexibilité [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e).

### Autres changements
- Documentation des props `customHeaderActions` et `menu options` dans Storybook [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7).
- Corrections de tests pour améliorer la stabilité et la couverture [#902ac73](https://github.com/suitenumerique/ui-kit/commit/902ac73), [#1ddedc0](https://github.com/suitenumerique/ui-kit/commit/1ddedc0).
- Publication de nouvelles versions du package [#5ee2e8f](https://github.com/suitenumerique/ui-kit/commit/5ee2e8f), [#77b2bbc](https://github.com/suitenumerique/ui-kit/commit/77b2bbc), [#7e42aa3](https://github.com/suitenumerique/ui-kit/commit/7e42aa3), [#4713aa6](https://github.com/suitenumerique/ui-kit/commit/4713aa6).
