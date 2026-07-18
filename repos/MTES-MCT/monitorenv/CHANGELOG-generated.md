## Changelog : monitorenv (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des missions et des navires, notamment l'ajout de pièces jointes et d'informations supplémentaires aux navires, ainsi que la possibilité pour le CACEM de mettre à jour les missions à partir de rapports de navigation. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des informations et des fichiers supplémentaires aux navires.
- Le CACEM peut désormais mettre à jour les missions à partir de rapports de navigation. [#40bbc44](https://github.com/MTES-MCT/monitorenv/commit/40bbc44)
- Ajout de tags aux missions, avec une interface de gestion en back-office pour créer, modifier et supprimer des tags. [#b5d88fe](https://github.com/MTES-MCT/monitorenv/commit/b5d88fe)
- Possibilité de spécifier si une mission est "noteworthy" (remarquable). [#03cea13](https://github.com/MTES-MCT/monitorenv/commit/03cea13)
- Utilisation du composant FileUploader de monitor-ui pour la gestion des fichiers. [#6ad6960](https://github.com/MTES-MCT/monitorenv/commit/6ad6960)

### Évolutions techniques
- Correction d'un bug empêchant le filtrage correct des nouveaux tags. [#5ca7cd9](https://github.com/MTES-MCT/monitorenv/commit/5ca7cd9)
- Amélioration du calcul de la taille estimée des missions. [#a497eec](https://github.com/MTES-MCT/monitorenv/commit/a497eec)
- Ajout d'un debounce au filtre de recherche des missions pour améliorer la performance. [#7eb7928](https://github.com/MTES-MCT/monitorenv/commit/7eb7928)
- Correction pour recharger la table des missions lors du changement d'onglet. [#dde0e1b](https://github.com/MTES-MCT/monitorenv/commit/dde0e1b)
- Utilisation de `savedMission` pour conserver les données externes modifiées (par exemple, les calculs de la façade `env_action`). [#d658689](https://github.com/MTES-MCT/monitorenv/commit/d658689)

### Autres changements
- Corrections de bugs et améliorations de l'UX. [#4be2665](https://github.com/MTES-MCT/monitorenv/commit/4be2665)
- Corrections de tests E2E. [#514d0b3](https://github.com/MTES-MCT/monitorenv/commit/514d0b3) et [#ef6baef](https://github.com/MTES-MCT/monitorenv/commit/ef6baef)
- Corrections de typos et revue de code. [#fad7461](https://github.com/MTES-MCT/monitorenv/commit/fad7461)
- Correction d'un bug lié à la création de tags fantômes. [#852b591](https://github.com/MTES-MCT/monitorenv/commit/852b591)
