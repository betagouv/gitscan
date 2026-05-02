## Changelog : meet-matting (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, le projet meet-matting a connu des avancées significatives en termes d'optimisation des performances, d'amélioration de la qualité du matting (segmentation de l'arrière-plan) et d'ajout de nouvelles fonctionnalités, notamment un pipeline de traitement configurable et des outils de benchmark pour évaluer les modèles. L'accent a été mis sur la réduction du temps d'inférence et l'amélioration de la stabilité du traitement en temps réel pour la vidéo.

### Évolutions fonctionnelles
- **Pipeline de traitement configurable :** Ajout d'un pipeline permettant de tester différentes combinaisons de pré- et post-traitements pour optimiser le résultat du matting. Il est possible de configurer des étapes comme le filtrage bilatéral, le CLAHE, les corrections de couleur et l'application de masques.  Un bouton permet de télécharger la configuration du pipeline [#7be7d2a](https://github.com/suitenumerique/meet-matting/issues/7be7d2a).
- **Amélioration de la qualité du matting :**
    - Ajout de méthodes anti-flickering pour stabiliser l'affichage en temps réel [#4baa2b5](https://github.com/suitenumerique/meet-matting/issues/4baa2b5).
    - Optimisation de la composition, de la CCA (Chromaticity Correction Algorithm) et de la fonction sigmoïde pour réduire le temps d'inférence [#ba53273](https://github.com/suitenumerique/meet-matting/issues/ba53273).
    - Amélioration du zoom sur la personne dans la vidéo [#fcf56a2](https://github.com/suitenumerique/meet-matting/issues/fcf56a2).
    - Possibilité de choisir la couleur de l'arrière-plan [#164a81d](https://github.com/suitenumerique/meet-matting/issues/164a81d).
- **Gestion de la vidéo :**
    - Prise en charge du démarrage instantané de la vidéo [#bc8bfc1](https://github.com/suitenumerique/meet-matting/issues/bc8bfc1).
    - Possibilité d'enregistrer et de visualiser le traitement vidéo complet dans le pipeline [#35e6642](https://github.com/suitenumerique/meet-matting/issues/35e6642).
    - Unification du fond et du skip_frame entre la vidéo en direct et la vidéo enregistrée [#0ef1741](https://github.com/suitenumerique/meet-matting/issues/0ef1741).
- **Benchmark et métriques :**
    - Implémentation d'un benchmark pour évaluer les performances des modèles et des différentes configurations [#fc56379](https://github.com/suitenumerique/meet-matting/issues/fc56379).
    - Ajout de métriques d'évaluation telles que l'IoU (Intersection over Union) et la Boundary F-measure [#b58e79e](https://github.com/suitenumerique/meet-matting/issues/b58e79e).

### Évolutions techniques
- **Optimisation des performances :** Réduction significative du temps d'inférence, notamment grâce à l'optimisation de la composition, de la CCA et de la fonction sigmoïde, divisant le temps d'inférence par deux [#ba53273](https://github.com/suitenumerique/meet-matting/issues/ba53273).
- **Refactoring et amélioration du code :**
    - Refactorisation du code et application des outils `ruff`, `mypy` et `uv` pour améliorer la qualité et la maintenabilité du code [#ceb9989](https://github.com/suitenumerique/meet-matting/issues/ceb9989).
    - Séparation de la méthode d'upsampling du modèle pour une plus grande flexibilité [#82bc80f](https://github.com/suitenumerique/meet-matting/issues/82bc80f).
- **Gestion des dépendances :** Mise à jour et gestion des dépendances du projet.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés au projet [#2991c71](https://github.com/suitenumerique/meet-matting/issues/2991c71).
- **Configuration :** Ajout d'un fichier `config.json` pour partager les résultats et les configurations [#2a4c73e](https://github.com/suitenumerique/meet-matting/issues/2a4c73e).
- **Gitignore :** Mise à jour du fichier `.gitignore` pour exclure les fichiers inutiles du dépôt [#eac4525](https://github.com/suitenumerique/meet-matting/issues/eac4525) et [#96b7693](https://github.com/suitenumerique/meet-matting/issues/96b7693).
