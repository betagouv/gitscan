## Changelog : ocr-api (30 derniers jours, au 17 juillet 2026)

### Résumé
Les dernières mises à jour de l'API OCR se concentrent sur l'ajout de nouvelles fonctionnalités, notamment la transcription de vidéos YouTube, la prise en charge de nouveaux formats de fichiers (EML et ZIP), et l'intégration d'une interface utilisateur web (OpenWebUI) pour le traitement de documents. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
*   Ajout de la transcription de vidéos YouTube.
*   Prise en charge des fichiers EML et ZIP pour l'OCR.
*   Intégration d'une interface OpenWebUI pour le traitement des documents, incluant des fonctionnalités de recherche et de sélection de zones.
*   Amélioration de la gestion des tâches dans l'interface OpenWebUI avec l'ajout d'une vue de détail.

### Évolutions techniques
*   Implémentation du support Redis Sentinel pour une meilleure résilience de la connexion à Redis.
*   Utilisation de `spawn` comme méthode de démarrage pour les processus multiprocessing afin d'améliorer la stabilité de PaddleOCR.
*   Intégration de la librairie `liteparse` pour le traitement de certains formats de fichiers.
*   Amélioration de la configuration de Docker avec l'ajout de la variable d'environnement `TORCHINDUCTOR_CACHE_DIR`.
*   Mise à jour de la gestion des dépendances Langfuse.
*   Refactoring du code pour améliorer la lisibilité et la maintenance, notamment dans la méthode `batch_predict` de PaddleOCR.

### Autres changements
*   Correction de plusieurs vulnérabilités de sécurité.
*   Amélioration des logs et ajout de logs supplémentaires.
*   Mise à jour de la documentation et des noms de variables pour plus de cohérence (ex: `S3_BUCKET_NAME` renommé en `AWS_BUCKET_NAME`).
*   Corrections mineures et ajustements de configuration pour améliorer la stabilité et la fiabilité de l'API.
*   Plusieurs releases de versions (0.19.5, 0.19.4, 0.19.3, 0.19.2, 0.19.1, 0.19.0, 0.18.0, 0.17.0, 0.16.0, 0.15.1, 0.15.0, 0.14.0, 0.13.0, 0.12.6, 0.12.5, 0.12.4, 0.12.3, 0.12.2, 0.12.1, 0.12.0, 0.11.2, 0.11.1, 0.11.0) avec des corrections de bugs et des améliorations mineures.
