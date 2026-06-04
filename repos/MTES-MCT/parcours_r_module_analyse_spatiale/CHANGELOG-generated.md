## Changelog : parcours_r_module_analyse_spatiale (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'environnement de construction du module, notamment via la mise à jour de l'image Docker et l'optimisation des workflows de CI/CD. Des ajustements ont également été apportés à la présentation du module, en particulier concernant l'utilisation de données COG.

### Évolutions fonctionnelles
- Mise à jour de la présentation concernant les données COG, améliorant ainsi la clarté des exemples et des explications. [#55](https://github.com/MTES-MCT/parcours_r_module_analyse_spatiale/issues/55)

### Évolutions techniques
- Mise à jour de l'image Docker pour utiliser R version 4.6.0, assurant ainsi la compatibilité avec les dernières versions du langage.
- Refonte de la configuration Dockerfile pour utiliser `pak` pour la gestion des dépendances, améliorant la reproductibilité et la fiabilité de l'environnement.
- Optimisation de l'ordre des commandes dans le Dockerfile pour une construction plus efficace.
- Ajout d'une variable d'environnement `GITHUB_PAT` dans le Dockerfile pour l'authentification avec GitHub lors de la construction.
- Mise à jour des workflows `bookdown-build.yml` et `bookdown-build-and-deploy.yml` pour améliorer le processus de construction et de déploiement de la documentation.
- Optimisation des requêtes de distance OSM pour améliorer les performances.

### Autres changements
- Fusion de la branche `maj_nov_2025` dans la branche `master`. [#54](https://github.com/MTES-MCT/parcours_r_module_analyse_spatiale/pull/54)
