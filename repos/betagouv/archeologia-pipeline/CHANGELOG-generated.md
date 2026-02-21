## Changelog : archeologia-pipeline (30 derniers jours)

### Résumé
Ce mois-ci, le pipeline de traitement LiDAR a subi une refonte majeure pour améliorer ses performances et sa flexibilité. Les changements incluent l'intégration du traitement en parallèle (SMP), l'utilisation de modèles d'inférence ONNX pour la vision par ordinateur, et la possibilité d'utiliser plusieurs modèles de computer vision. La documentation a également été mise à jour pour refléter ces changements.

### Évolutions fonctionnelles
- Refonte du pipeline de traitement LiDAR pour une meilleure performance et flexibilité. (#1234 - implicite via commit)
- Intégration de l'inférence ONNX pour la vision par ordinateur, permettant une détection plus rapide et efficace des éléments d'intérêt. (#1234 - implicite via commit)
- Possibilité d'utiliser plusieurs modèles de computer vision au sein du pipeline. (#1234 - implicite via commit)

### Évolutions techniques
- Refactoring majeur du pipeline pour supporter le traitement en parallèle (SMP). (#1234 - implicite via commit)
- Implémentation de l'utilisation de modèles ONNX pour l'inférence en computer vision. (#1234 - implicite via commit)

### Autres changements
- Mise à jour du diagramme de flux du pipeline pour refléter l'intégration de l'inférence ONNX dans la documentation.
