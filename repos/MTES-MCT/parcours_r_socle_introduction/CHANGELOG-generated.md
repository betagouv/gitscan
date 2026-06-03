## Changelog : parcours_r_socle_introduction (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, les modifications apportées au projet se concentrent principalement sur l'amélioration du processus de construction et de déploiement continu (CI/CD) du livre interactif. Des investigations ont été menées pour résoudre des erreurs de compilation intermittentes rencontrées lors du déploiement, et la configuration Docker a été mise à jour à plusieurs reprises.

### Évolutions techniques
- Mise à jour du Dockerfile pour améliorer la configuration de l'environnement de construction et de déploiement. Plusieurs modifications ont été apportées, incluant la gestion des variables d'environnement et l'authentification avec GitHub. [#20372f4](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/20372f4)
- Modifications des workflows CI/CD (`bookdown-build.yml` et `bookdown-build-and-deploy.yml`) pour tenter de résoudre des erreurs de compilation lors de la génération du livre. [#803a542](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/803a542), [#7c72b19](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/7c72b19)
- Investigation et tentatives de débogage d'une erreur de compilation spécifique concernant la création d'un histogramme avec `ggplot2`, impliquant un argument non numérique. [#7356865](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/7356865), [#3c0bbf3](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/3c0bbf3), [#20372f4](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/20372f4)

### Autres changements
- Mise à jour de l'argument dans le Dockerfile. [#23a7736](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/23a7736)
- Correction potentielle du CI. [#dd07c56](https://github.com/MTES-MCT/parcours_r_socle_introduction/commit/dd07c56)
