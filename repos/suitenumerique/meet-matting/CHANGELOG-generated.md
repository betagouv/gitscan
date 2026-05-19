## Changelog : meet-matting (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, le projet meet-matting a connu des améliorations significatives en termes de performance, de qualité de segmentation et d'expérience utilisateur. L'accent a été mis sur l'optimisation du traitement en temps réel, l'ajout de nouvelles méthodes de post-traitement pour réduire les artefacts visuels, et la mise en place d'une architecture de pipeline flexible pour faciliter les tests et l'évaluation de différents modèles et paramètres. Un travail important a également été réalisé sur la mise en place d'un benchmark pour mesurer objectivement les performances du système.

### Évolutions fonctionnelles
- Ajout d'un pipeline pour tester différents pré et post-traitements, incluant des méthodes de zoom sur la personne détectée et des filtres morphologiques.
- Implémentation de méthodes de post-traitement supplémentaires pour réduire le flickering et améliorer la qualité de la segmentation.
- Possibilité de choisir la couleur de fond.
- Amélioration de la qualité des bords grâce à différentes méthodes d'upsampling.
- Ajout de la possibilité de visualiser et sauvegarder le traitement vidéo complet dans le pipeline.
- Ajout d'un bouton pour télécharger la configuration du pipeline.
- Amélioration de la détection et du traitement des personnes avec ppHuman, notamment la résolution de problèmes liés à l'upscaling.
- Mise en place d'une architecture de pipeline pour tester des méthodes de pré et post-traitement.
- Ajout de stratégies de skip frames pour améliorer la performance.
- Amélioration de la gestion des seuils pour une segmentation plus précise.
- Mise en place d'une détection de personnes avec YOLO.

### Évolutions techniques
- Optimisation de la composition, de la CCA (Connected Component Analysis) et de la fonction sigmoïde pour réduire le temps d'inférence de moitié en temps réel.
- Optimisation du calcul du FPS pour une mesure plus précise et une meilleure performance.
- Refactorisation du code et application de linters (ruff, mypy) pour améliorer la qualité et la maintenabilité du code.
- Mise en place d'un squelette de benchmark pour évaluer les performances du système, incluant le calcul de la latence P95.
- Séparation de la méthode d'upsampling du modèle pour une plus grande flexibilité.
- Ajout de métriques d'évaluation (IoU, Boundary f-measure).
- Utilisation de gitignore pour exclure les fichiers inutiles du dépôt.
- Amélioration de la gestion des erreurs et des conflits de merge.
- Correction de bugs liés à l'affichage vidéo et aux post-process en temps réel.

### Autres changements
- Traduction de la documentation.
- Mise à jour de la documentation des métriques.
- Ajout d'un fichier `config.json` pour partager les résultats et la configuration.
- Initialisation du projet par Samuel Paccoud.
- Ajout de la possibilité de télécharger les résultats sous forme de CSV.
