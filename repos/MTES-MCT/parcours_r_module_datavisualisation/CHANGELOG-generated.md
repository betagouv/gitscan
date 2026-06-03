## Changelog : parcours_r_module_datavisualisation (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, les modifications apportées au module de datavisualisation se concentrent sur la mise à jour de l'environnement de construction et de déploiement, notamment l'adaptation à la nouvelle version de R (4.6.0) et l'amélioration de la compatibilité avec les dépendances du module. Ces changements assurent la stabilité et la pérennité du parcours de formation.

### Évolutions techniques
- Mise à jour de l'image Docker pour utiliser R 4.6.0.
- Ajustement des dépendances pour assurer la compatibilité avec R 4.6.0 : `viridis` est maintenant une dépendance explicite et la gestion des palettes de couleurs dans `tmap` a été revue. [#8074237](https://github.com/MTES-MCT/parcours_r_module_datavisualisation/commit/8074237)
- Modifications des fichiers YAML de construction et de déploiement (`bookdown-build.yml`, `bookdown-build-and-deploy.yml`) pour supporter la nouvelle image Docker.
- Amélioration de la configuration du Dockerfile (ajout de `ARG` après `FROM`, mises à jour diverses).

### Autres changements
- Corrections mineures dans le Dockerfile pour améliorer le support de la construction en CI.
