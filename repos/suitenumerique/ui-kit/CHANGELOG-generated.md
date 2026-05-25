## Changelog : ui-kit (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'ajout de nouvelles fonctionnalités de prévisualisation de fichiers, l'amélioration de la gestion des icônes et la correction de bugs liés à l'accessibilité et à l'affichage. Des tests automatisés ont également été ajoutés pour garantir la qualité et la stabilité des composants.

### Évolutions fonctionnelles
- Ajout du composant `FilePreview` permettant de visualiser des fichiers, avec prise en charge de différents viewers. [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b)
- Ajout d'une nouvelle locale : néerlandais (nl-NL). [#121966c](https://github.com/suitenumerique/ui-kit/commit/121966c)
- Amélioration du menu d'actions avec l'introduction de `customHeaderActions` et `menu options`, offrant plus de flexibilité. [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e)
- Mise à jour de l'icône utilisée pour le menu d'actions, passant à `more_horiz`. [#5e5a964](https://github.com/suitenumerique/ui-kit/commit/5e5a964)
- Amélioration de la gestion des icônes avec un nouveau point d'entrée dédié et un processus de génération amélioré. [#75664ce](https://github.com/suitenumerique/ui-kit/commit/75664ce) et [#289ce30](https://github.com/suitenumerique/ui-kit/commit/289ce30)

### Évolutions techniques
- Ajout de tests Playwright pour le composant `FilePreview` afin d'assurer sa qualité. [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9)
- Intégration de l'exécution des tests Playwright e2e dans le pipeline CI. [#caaa464](https://github.com/suitenumerique/ui-kit/commit/caaa464)
- Correction de la manière dont les fichiers de style PDF sont chargés. [#8bf11e9](https://github.com/suitenumerique/ui-kit/commit/8bf11e9)
- Correction de la gestion des types MIME pour servir correctement les fichiers `.mjs` et `.wasm`. [#2af81e4](https://github.com/suitenumerique/ui-kit/commit/2af81e4)
- Refactoring de la gestion des actions dans l'en-tête, remplaçant `headerRightContent` par `customHeaderActions`. [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e)
- Ajout de tests pour la synchronisation de React avant l'entrée dans le champ de saisie PDF pour éviter des sauts de page. [#902ac73](https://github.com/suitenumerique/ui-kit/commit/902ac73)

### Autres changements
- Documentation des options `customHeaderActions` et `menu options` dans Storybook. [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7)
- Correction de l'affichage de l'icône dans le menu déroulant. [#94e0e8c](https://github.com/suitenumerique/ui-kit/commit/94e0e8c)
- Mise à jour du type `OnboardingStep`. [#f454a4f](https://github.com/suitenumerique/ui-kit/commit/f454a4f)
- Suppression de fichiers de style inutilisés de `cunningham-react` pour améliorer la priorité CSS.
