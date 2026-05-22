## Changelog : drive (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'intégration de nouveaux composants de l'UI Kit, l'amélioration de la prévisualisation des fichiers PDF et l'ajout d'un système de disclaimer pour les droits d'accès. Des corrections de bugs et des optimisations techniques ont également été apportées, notamment concernant la gestion des fichiers et l'intégration avec des services externes comme PostHog et SSO.

### Évolutions fonctionnelles
- Amélioration de la prévisualisation des fichiers PDF : affichage des miniatures, zoom et navigation entre les pages. [#7c17132](https://github.com/suitenumerique/drive/commit/7c17132)
- Ajout d'une modal de disclaimer pour les droits d'accès, configurable via une variable d'environnement. [#ef675df](https://github.com/suitenumerique/drive/commit/ef675df)
- Intégration de composants de l'UI Kit pour les icônes de fichiers et les prévisualisations, améliorant la cohérence visuelle. [#b7d635b](https://github.com/suitenumerique/drive/commit/b7d635b), [#3ddd7e5](https://github.com/suitenumerique/drive/commit/3ddd7e5)
- Ajout d'événements PostHog pour le suivi de l'utilisation des colonnes personnalisées et de la duplication d'éléments. [#6569287](https://github.com/suitenumerique/drive/commit/6569287)
- Possibilité de configurer la durée de validité des invitations via une variable d'environnement. [#352e195](https://github.com/suitenumerique/drive/commit/352e195)
- Amélioration de la gestion des erreurs et du feedback visuel lors du téléchargement de fichiers.

### Évolutions techniques
- Remplacement de `VersionId` par `Etag` pour la compatibilité WOPI. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)
- Refactorisation du code lié aux droits d'accès pour une meilleure organisation. [#62b8341](https://github.com/suitenumerique/drive/commit/62b8341)
- Amélioration de la gestion des transactions lors de la duplication d'éléments. [#68abb54](https://github.com/suitenumerique/drive/commit/68abb54)
- Mise à jour de la gestion des types MIME pour une meilleure compatibilité avec les fichiers. [#6049113](https://github.com/suitenumerique/drive/commit/6049113)
- Acceptation d'un queryset dans le backend de calcul de stockage. [#8360aec](https://github.com/suitenumerique/drive/commit/8360aec)
- Déplacement des imports liés aux types MIME vers l'UI Kit. [#74b0f84](https://github.com/suitenumerique/drive/commit/74b0f84)

### Autres changements
- Documentation mise à jour. [#18d8b22](https://github.com/suitenumerique/drive/commit/18d8b22), [#7a95dcf](https://github.com/suitenumerique/drive/commit/7a95dcf), [#59292f6](https://github.com/suitenumerique/drive/commit/59292f6)
- Suppression de la fonctionnalité de mirroring. [#805ef77](https://github.com/suitenumerique/drive/commit/805ef77)
- Mise à jour de la version de l'UI Kit. [#d99116e](https://github.com/suitenumerique/drive/commit/d99116e)
- Correction de bugs mineurs et améliorations de la stabilité.
