## Changelog : ui-kit (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration de la gestion des fichiers avec l'ajout d'un nouveau composant de prévisualisation, ainsi que sur l'enrichissement de la bibliothèque d'icônes et l'amélioration des tests automatisés. Des corrections de bugs et des améliorations de l'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- **Prévisualisation de fichiers :** Ajout d'un nouveau composant `FilePreview` permettant de visualiser différents types de fichiers, accompagné de ses viewers associés. [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b)
- **Icônes :** Ajout de nouvelles icônes et mise à jour des icônes existantes, avec une amélioration du processus de génération. [#75664ce](https://github.com/suitenumerique/ui-kit/commit/75664ce)
- **Menu d'actions :** Utilisation de l'icône `more_horiz` pour le menu d'actions. [#5e5a964](https://github.com/suitenumerique/ui-kit/commit/5e5a964)
- **Support linguistique :** Ajout de la locale néerlandaise (nl-NL). [#121966c](https://github.com/suitenumerique/ui-kit/commit/121966c)
- **Options de menu personnalisées :** Possibilité de définir des actions personnalisées et des options de menu pour les en-têtes. [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7) et [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e)

### Évolutions techniques
- **Tests E2E :** Intégration de tests end-to-end (E2E) Playwright dans la CI/CD. [#caaa464](https://github.com/suitenumerique/ui-kit/commit/caaa464)
- **Tests unitaires :** Ajout de tests Playwright pour le composant `FilePreview`. [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9)
- **MIME types :** Amélioration de la gestion des types MIME pour le service de fichiers. [#2af81e4](https://github.com/suitenumerique/ui-kit/commit/2af81e4) et [#0149cbd](https://github.com/suitenumerique/ui-kit/commit/0149cbd)
- **Worker PDF :** Import du worker PDF dans les scripts de pré-construction. [#4d8098a](https://github.com/suitenumerique/ui-kit/commit/4d8098a)
- **Refactoring :** Remplacement de `headerRightContent` par `customHeaderActions` pour une meilleure flexibilité. [#3ee8d3e](https://github.com/suitenumerique/ui-kit/commit/3ee8d3e)

### Autres changements
- **Documentation :** Documentation des options `customHeaderActions` et `menu options` dans Storybook. [#412fec7](https://github.com/suitenumerique/ui-kit/commit/412fec7)
- **Corrections de bugs :** Correction de l'affichage des icônes dans les menus déroulants. [#94e0e8c](https://github.com/suitenumerique/ui-kit/commit/94e0e8c)
- **Typographie :** Correction de fautes de frappe dans la documentation. [#0777ddc](https://github.com/suitenumerique/ui-kit/commit/0777ddc)
- **Configuration :** Configuration de Renovate pour la gestion des dépendances. [#6f6e3d8](https://github.com/suitenumerique/ui-kit/commit/6f6e3d8)
- **Mise à jour des dépendances :** Mise à jour des actions GitHub pour utiliser les dernières versions. [#262aa90](https://github.com/suitenumerique/ui-kit/commit/262aa90)
