## Changelog : meet-matting (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, le projet meet-matting a connu des avancées significatives en termes d'optimisation des performances, d'amélioration de la qualité du matting (segmentation de l'arrière-plan) et de l'ajout de nouvelles fonctionnalités pour faciliter l'évaluation et la configuration des pipelines de traitement vidéo. L'accent a été mis sur la réduction du temps d'inférence, la stabilisation de l'image et l'amélioration de l'expérience utilisateur via une interface plus flexible et informative.

### Évolutions fonctionnelles
- Ajout d'une interface pour télécharger la configuration d'un pipeline en JSON [#7be7d2a](https://github.com/suitenumerique/meet-matting/issues/7be7d2a).
- Amélioration de la qualité du matting avec l'ajout de méthodes anti-flickering et de post-processing en temps réel [#4baa2b5](https://github.com/suitenumerique/meet-matting/issues/4baa2b5), [#acdec57](https://github.com/suitenumerique/meet-matting/issues/acdec57).
- Possibilité de choisir la couleur de l'arrière-plan [#164a81d](https://github.com/suitenumerique/meet-matting/issues/164a81d).
- Implémentation d'une fonctionnalité de zoom sur la personne détectée, avec des améliorations de la pré-traitement et de la post-traitement [#82bc80f](https://github.com/suitenumerique/meet-matting/issues/82bc80f), [#a0e84ba](https://github.com/suitenumerique/meet-matting/issues/a0e84ba).
- Amélioration de la détection des bords avec différentes méthodes d'upsampling [#2232d3b](https://github.com/suitenumerique/meet-matting/issues/2232d3b).
- Possibilité de visualiser et sauvegarder l'intégralité du pipeline de traitement vidéo [#35e6642](https://github.com/suitenumerique/meet-matting/issues/35e6642), [#96b7693](https://github.com/suitenumerique/meet-matting/issues/96b7693).
- Mise en place d'une détection instantanée de la vidéo [#bc8bfc1](https://github.com/suitenumerique/meet-matting/issues/bc8bfc1).

### Évolutions techniques
- Optimisation significative de la composition, de la CCA (Chromaticity Correction Algorithm) et de la fonction sigmoïde pour réduire le temps d'inférence en temps réel (divisé par deux) [#ba53273](https://github.com/suitenumerique/meet-matting/issues/ba53273), [#125006a](https://github.com/suitenumerique/meet-matting/issues/125006a).
- Amélioration du calcul des FPS (images par seconde) pour une mesure plus précise des performances, en excluant le temps d'inférence du serveur Streamlit [#81c441b](https://github.com/suitenumerique/meet-matting/issues/81c441b), [#2c62ad5](https://github.com/suitenumerique/meet-matting/issues/2c62ad5).
- Implémentation de stratégies de "frame skipping" (saut d'images) basées sur le "flow warping" pour améliorer les performances [#5c0b5fc](https://github.com/suitenumerique/meet-matting/issues/5c0b5fc), [#eac4525](https://github.com/suitenumerique/meet-matting/issues/eac4525), [#67dc4c8](https://github.com/suitenumerique/meet-matting/issues/67dc4c8).
- Refactoring du code et mise à jour des dépendances avec des outils comme `ruff`, `mypy` et `uv` [#ceb9989](https://github.com/suitenumerique/meet-matting/issues/ceb9989).
- Unification des paramètres d'arrière-plan et de "skip_frame" pour les vidéos en direct et enregistrées [#0ef1741](https://github.com/suitenumerique/meet-matting/issues/0ef1741).
- Ajout d'un benchmark pour mesurer les performances et l'impact des différentes optimisations [#fc56379](https://github.com/suitenumerique/meet-matting/issues/fc56379), [#52aecbd](https://github.com/suitenumerique/meet-matting/issues/52aecbd).
- Implémentation d'un pipeline pour tester différentes méthodes de pré-traitement et de post-traitement [#687525c](https://github.com/suitenumerique/meet-matting/issues/687525c).

### Autres changements
- Ajout de documentation et de métriques pour l'évaluation des performances [#2991c71](https://github.com/suitenumerique/meet-matting/issues/2991c71).
- Ajout d'un fichier `config.json` pour partager les résultats et les configurations [#2a4c73e](https://github.com/suitenumerique/meet-matting/issues/2a4c73e).
- Suppression des fichiers de vidéos de sortie du suivi Git [#84eec18](https://github.com/suitenumerique/meet-matting/issues/84eec18).
- Initialisation du projet par Samuel Paccoud [#cfaea70](https://github.com/suitenumerique/meet-matting/issues/cfaea70).
- Initial commit par Léa BOUSSEKEYT [#2c8e2dc](https://github.com/suitenumerique/meet-matting/issues/2c8e2dc).
