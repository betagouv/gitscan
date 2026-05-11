## Changelog : ui-kit (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'ajout d'un nouveau composant pour la prévisualisation de fichiers, ainsi que sur l'amélioration de la qualité et de la couverture des tests. Des corrections de bugs et des améliorations de l'accessibilité ont également été apportées. Une nouvelle locale, le néerlandais, a été ajoutée pour une meilleure internationalisation.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FilePreview` permettant de visualiser des fichiers avec différents viewers. [#8578a2b](https://github.com/suitenumerique/ui-kit/commit/8578a2b)
- Ajout de la locale néerlandaise (nl-NL) pour supporter de nouveaux utilisateurs. [#121966c](https://github.com/suitenumerique/ui-kit/commit/121966c)
- Correction de l'affichage de l'icône dans le menu déroulant, qui n'apparaissait pas toujours correctement. [#94e0e8c](https://github.com/suitenumerique/ui-kit/commit/94e0e8c)
- Correction du problème d'enveloppement du label dans les conteneurs de filtre restreints. [#0777ddc](https://github.com/suitenumerique/ui-kit/commit/0777ddc)

### Évolutions techniques
- Ajout de tests Playwright pour le composant `FilePreview` afin d'assurer sa qualité et sa stabilité. [#cbf21f9](https://github.com/suitenumerique/ui-kit/commit/cbf21f9)
- Intégration de l'exécution des tests Playwright E2E dans le pipeline CI. [#caaa464](https://github.com/suitenumerique/ui-kit/commit/caaa464)
- Mise à jour des dépendances GitHub Actions pour utiliser les dernières versions. [#262aa90](https://github.com/suitenumerique/ui-kit/commit/262aa90)
- Configuration de Renovate pour la gestion automatisée des dépendances. [#6f6e3d8](https://github.com/suitenumerique/ui-kit/commit/6f6e3d8)

### Autres changements
- Correction de fautes de frappe dans la documentation. [#0777ddc](https://github.com/suitenumerique/ui-kit/commit/0777ddc)
- Mise à jour du type de l'étape d'onboarding. [#f454a4f](https://github.com/suitenumerique/ui-kit/commit/f454a4f)
