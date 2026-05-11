## Changelog : meet-matting (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, le projet meet-matting a connu des améliorations significatives en termes de performance, de qualité de segmentation et d'expérience utilisateur. L'accent a été mis sur l'optimisation du traitement en temps réel, l'ajout de nouvelles méthodes de post-traitement pour réduire les artefacts visuels, et la mise en place d'une architecture de pipeline flexible pour tester différentes configurations. Des outils de benchmark ont également été introduits pour évaluer objectivement les performances des modèles.

### Évolutions fonctionnelles
- **Amélioration de la qualité de la segmentation :** Ajout de méthodes de post-traitement (CCA, EMA, filtres bilatéraux, CLAHE) pour améliorer la qualité de la segmentation et réduire les effets de flickering [#4baa2b5](https://github.com/suitenumerique/meet-matting/commit/4baa2b5).
- **Optimisation de la performance :** Optimisation de la composition, du CCA et du sigmoid pour réduire le temps d'inférence en temps réel, divisant celui-ci par deux [#ba53273](https://github.com/suitenumerique/meet-matting/commit/ba53273).
- **Pipeline de traitement :** Implémentation d'une architecture de pipeline pour tester différentes combinaisons de pré- et post-traitements [#687525c](https://github.com/suitenumerique/meet-matting/commit/687525c). Possibilité de visualiser et sauvegarder le résultat de chaque étape du pipeline [#82bc80f](https://github.com/suitenumerique/meet-matting/commit/82bc80f).
- **Amélioration de la gestion des vidéos :** Possibilité de traiter des vidéos complètes et de sauvegarder les résultats [#96b7693](https://github.com/suitenumerique/meet-matting/commit/96b7693).
- **Zoom sur la personne :** Ajout d'un pré-traitement pour zoomer sur la personne dans la scène [#8f2fe4b](https://github.com/suitenumerique/meet-matting/commit/8f2fe4b).
- **Configuration via JSON :** Possibilité de télécharger une configuration JSON pour partager les paramètres du pipeline [#7be7d2a](https://github.com/suitenumerique/meet-matting/commit/7be7d2a).

### Évolutions techniques
- **Refactoring du code :** Refactoring du code et application de linters (ruff, mypy, uv) pour améliorer la qualité et la maintenabilité du code [#ceb9989](https://github.com/suitenumerique/meet-matting/commit/ceb9989).
- **Stratégies de skip frames :** Implémentation de différentes stratégies de skip frames basées sur le flow warping pour améliorer la performance [#eac4525](https://github.com/suitenumerique/meet-matting/commit/eac4525).
- **Calcul du FPS :** Amélioration du calcul du FPS pour une mesure plus précise et un affichage unifié [#81c441b](https://github.com/suitenumerique/meet-matting/commit/81c441b).
- **Benchmark :** Mise en place d'un système de benchmark pour évaluer les performances des modèles et des configurations [#52aecbd](https://github.com/suitenumerique/meet-matting/commit/52aecbd).
- **Gestion des dépendances :** Mise à jour des dépendances.

### Autres changements
- **Documentation :** Mise à jour de la documentation et ajout de métriques d'évaluation [#2991c71](https://github.com/suitenumerique/meet-matting/commit/2991c71).
- **Gitignore :** Mise à jour du fichier .gitignore pour exclure les fichiers inutiles du dépôt [#20a648e](https://github.com/suitenumerique/meet-matting/commit/20a648e).
- **Traduction :** Ajout de traductions.
- **Correction de bugs :** Correction de divers bugs liés à l'affichage, au traitement vidéo et à la configuration.
