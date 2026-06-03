## Changelog : parcours_r_socle_preparation_des_donnees (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur l'amélioration de l'infrastructure de construction et de déploiement du livre interactif, ainsi que sur l'adaptation du code R aux dernières versions de la librairie `dplyr`. Une mise à jour de l'URL de la source de données Locvac a également été effectuée.

### Évolutions techniques
- Mise à jour de la version de R dans le Dockerfile vers la version 4.6.0 [#fc654a3](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/fc654a3).
- Amélioration des workflows GitHub Actions `bookdown-build.yml` et `bookdown-build-and-deploy.yml` [#4b9d490](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/4b9d490) et [#8bb838e](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/8bb838e).
- Modifications du Dockerfile pour corriger l'ordre des instructions et l'utilisation de `ARG` [#bed1ae4](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/bed1ae4), [#10f1444](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/10f1444) et [#08b4ccf](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/08b4ccf).

### Évolutions fonctionnelles
- Adaptation des fonctions de sélection de données (`select helpers`) pour assurer la compatibilité avec les évolutions récentes de la librairie `dplyr` [#65785fe](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/65785fe).
- Mise à jour de l'URL de la source de données Locvac sur data.gouv.fr [#83fc336](https://github.com/MTES-MCT/parcours_r_socle_preparation_des_donnees/commit/83fc336).
