## Changelog : ocr-api (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, l'API OCR a bénéficié d'améliorations significatives en termes de fonctionnalités et de stabilité. Les utilisateurs peuvent désormais profiter d'une interface améliorée pour la visualisation et la sélection de zones dans les documents, ainsi que d'une prise en charge de nouveaux formats de fichiers. Des corrections et optimisations ont également été apportées pour améliorer la robustesse et la performance du système.

### Évolutions fonctionnelles
- Ajout d'une interface OpenWebUI avec un point d'accès pour le traitement des documents.
- Amélioration de l'OcrViewer avec des fonctionnalités de recherche et de sélection de zones.
- Prise en charge de formats de fichiers supplémentaires pour l'upload OCR.
- Ajout d'une vue détaillée des tâches et navigation améliorée dans l'onglet "Tasks".
- Possibilité de supprimer une tâche et le fichier associé après traitement.

### Évolutions techniques
- Amélioration de la configuration Redis avec support Sentinel.
- Initialisation du pipeline OCR dans le processus worker pour une meilleure stabilité.
- Utilisation de la méthode de démarrage multiprocessing 'spawn' pour PaddleOCR.
- Mise à jour de la gestion des dépendances Langfuse.
- Correction de problèmes liés à l'initialisation du modèle PaddleOCR et aux tests d'inférence.
- Ajout de la variable d'environnement `TORCHINDUCTOR_CACHE_DIR` aux Dockerfiles.
- Intégration de la librairie liteparse et ajout d'un worker associé.
- Correction d'une vulnérabilité de sécurité.
- Mise en place de la remontée d'erreurs vers Sentry pour l'API, le worker et le frontend ([#398](https://github.com/IA-Generative/ocr-api/issues/398)).
- Correction d'une assertion dans les tests de tracing et stabilisation des tests SDK ([#399](https://github.com/IA-Generative/ocr-api/issues/399)).

### Autres changements
- Renommage de la variable d'environnement `S3_BUCKET_NAME` en `AWS_BUCKET_NAME` pour plus de cohérence.
- Amélioration de la lisibilité du code dans la méthode `batch_predict` de PaddleOCR.
- Ajout de documentation Markdown.
- Plusieurs corrections et améliorations liées au processus de release.
