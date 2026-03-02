## Changelog : archeologia-pipeline (30 derniers jours)

### Résumé
Ce pipeline de traitement LiDAR a bénéficié d'une refonte majeure, améliorant significativement ses performances grâce à l'utilisation du traitement parallèle (SMP) et de l'inférence ONNX. De plus, la gestion des couleurs pour la détection par computer vision a été améliorée, permettant une meilleure visualisation et consolidation des résultats dans QGIS. La documentation a également été mise à jour pour refléter ces changements.

### Évolutions fonctionnelles
- Amélioration de la gestion des couleurs pour les modèles de détection par computer vision, avec propagation de la carte de couleurs globale et consolidation du projet QGIS. [#1234](https://github.com/betagouv/archeologia-pipeline/pull/1234) (impliqué)
- Mise à jour du diagramme de flux du pipeline pour refléter l'inférence ONNX.

### Évolutions techniques
- Refactoring majeur du pipeline pour améliorer la performance et l'efficacité.
- Intégration du traitement parallèle (SMP) pour accélérer les opérations.
- Utilisation de l'inférence ONNX pour optimiser la vitesse d'exécution des modèles de computer vision.
- Prise en charge de plusieurs modèles de computer vision.
