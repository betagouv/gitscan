## Changelog : ui-kit (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, la bibliothèque de composants a été enrichie avec de nouvelles fonctionnalités axées sur la gestion des fichiers (prévisualisation, icônes) et l'amélioration de l'expérience utilisateur, notamment au niveau des menus et des tests automatisés. Des corrections de bugs et des optimisations ont également été apportées pour garantir la stabilité et la performance de la bibliothèque.

### Évolutions fonctionnelles
- Ajout d'un composant `FilePreview` permettant de prévisualiser des fichiers avec différents viewers. [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b)
- Ajout d'un composant `FileIcon` pour afficher des icônes de fichiers. [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b)
- Mise à jour de la bibliothèque d'icônes avec de nouvelles icônes et des améliorations sur les icônes existantes. [#912ab95](https://github.com/suitenumerique/ui-kit/commit/912ab95), [#75664ce](https://github.com/suitenumerique/ui-kit/commit/75664ce)
- Amélioration du menu d'actions avec l'ajout d'options personnalisables via `customHeaderActions` et `menu options`. [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7)
- Ajout de la locale néerlandaise (nl-NL). [#121966c](https://github.com/suitenumerique/ui-kit/commit/121966c)
- Remplacement de `headerRightContent` par `customHeaderActions` dans le composant `FilePreview`.

### Évolutions techniques
- Ajout de tests Playwright pour le composant `FilePreview`. [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9)
- Exécution des tests Playwright E2E dans la CI. [#caaa464](https://github.com/suitenumerique/ui-kit/commit/caaa464)
- Amélioration du processus de génération des icônes. [#289ce30](https://github.com/suitenumerique/ui-kit/commit/289ce30)
- Ajout d'un point d'entrée dédié pour les icônes. [#77b2bbc](https://github.com/suitenumerique/ui-kit/commit/77b2bbc)
- Import du worker PDF dans les scripts de pré-build. [#4d8098a](https://github.com/suitenumerique/ui-kit/commit/4d8098a)
- Correction de la gestion des types MIME pour les fichiers `.mjs` et `.wasm`. [#2af81e4](https://github.com/suitenumerique/ui-kit/commit/2af81e4)
- Déplacement des fichiers de style de `PdfPreview`. [#8bf11e9](https://github.com/suitenumerique/ui-kit/commit/8bf11e9)

### Autres changements
- Utilisation de l'icône `more_horiz` pour le menu d'actions. [#5e5a964](https://github.com/suitenumerique/ui-kit/commit/5e5a964)
- Documentation des options `customHeaderActions` et `menu options` dans les stories. [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7)
- Amélioration des tests pour la page PDF (synchronisation React, suppression d'un cas de test XSS). [#902ac73](https://github.com/suitenumerique/ui-kit/commit/902ac73), [#1ddedc0](https://github.com/suitenumerique/ui-kit/commit/1ddedc0)
