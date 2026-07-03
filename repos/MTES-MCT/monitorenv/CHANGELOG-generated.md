## Changelog : monitorenv (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des missions, notamment avec l'ajout de tags pour une meilleure organisation et un filtrage plus précis. L'interface utilisateur a également été améliorée avec des corrections de bugs et des refactorisations pour une expérience plus fluide. Des corrections ont été apportées aux tests et aux données réglementaires.

### Évolutions fonctionnelles
- Ajout de tags aux missions pour une meilleure catégorisation et organisation [#b26e8b7](https://github.com/MTES-MCT/monitorenv/commit/b26e8b7).
- Possibilité de filtrer les missions par tags, avec prise en compte de la date de début de la mission ou de l'action [#0c611a1](https://github.com/MTES-MCT/monitorenv/commit/0c611a1).
- Amélioration du filtrage des missions avec un "debounce" pour optimiser la performance [#7eb7928](https://github.com/MTES-MCT/monitorenv/commit/7eb7928).
- Augmentation de la taille estimée des missions [#a497eec](https://github.com/MTES-MCT/monitorenv/commit/a497eec).
- Ajout d'un focus sur la ligne de position lors d'un clic [#4df3916](https://github.com/MTES-MCT/monitorenv/commit/4df3916).
- Correction du filtrage des ressources `controlUnit` par `missionsControlResources` [#f23bc46](https://github.com/MTES-MCT/monitorenv/commit/f23bc46).

### Évolutions techniques
- Refactorisation de composants UI (renommage) [#cdc3ca5](https://github.com/MTES-MCT/monitorenv/commit/cdc3ca5) et [#0ae95aa](https://github.com/MTES-MCT/monitorenv/commit/0ae95aa).
- Création et refactorisation de boîtes de dialogue (dialogs) : `CantDoDialog`, `DeleteDialog`, `ArchiveModal` [#c8dc840](https://github.com/MTES-MCT/monitorenv/commit/c8dc840), [#bb05e5b](https://github.com/MTES-MCT/monitorenv/commit/bb05e5b), [#b9586e2](https://github.com/MTES-MCT/monitorenv/commit/b9586e2), [#6a5fab6](https://github.com/MTES-MCT/monitorenv/commit/6a5fab6), [#5480919](https://github.com/MTES-MCT/monitorenv/commit/5480919).
- Correction de bugs et amélioration des tests E2E [#514d0b3](https://github.com/MTES-MCT/monitorenv/commit/514d0b3).
- Ajout de `latest` lors d'une release [#334c957](https://github.com/MTES-MCT/monitorenv/commit/334c957).
- Correction d'un problème de rechargement de la table lors du changement d'onglet [#dde0e1b](https://github.com/MTES-MCT/monitorenv/commit/dde0e1b).

### Autres changements
- Correction d'un bug empêchant le filtrage des nouveaux tags [#5ca7cd9](https://github.com/MTES-MCT/monitorenv/commit/5ca7cd9).
- Correction d'un bug lié à la création de tags fantômes [#852b591](https://github.com/MTES-MCT/monitorenv/commit/852b591).
- Correction du flux `regulatory_areas_open_data` [#54092ee](https://github.com/MTES-MCT/monitorenv/commit/54092ee).
- Corrections de typos et revue de code [#fad7461](https://github.com/MTES-MCT/monitorenv/commit/fad7461).
- Améliorations de l'UX et corrections de bugs d'interface [#4be2665](https://github.com/MTES-MCT/monitorenv/commit/4be2665).
