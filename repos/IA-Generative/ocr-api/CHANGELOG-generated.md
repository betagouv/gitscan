## Changelog : ocr-api (30 derniers jours, au 30 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'API OCR, notamment l'ajout de la gestion des emails, l'amélioration de la gestion des fichiers, l'intégration de Sentry pour le suivi des erreurs et des correctifs de sécurité. Plusieurs améliorations techniques ont également été apportées pour optimiser la stabilité et la fiabilité du service.

### Évolutions fonctionnelles
- Ajout de la gestion des fichiers EML et amélioration de la validation des types MIME pour une meilleure cohérence lors du téléchargement de documents.
- Implémentation d'un modèle d'extraction d'emails et d'un worker pour le traitement du contenu des emails.
- Intégration de Sentry pour le reporting des erreurs dans l'API, les workers et l'interface utilisateur, facilitant ainsi le diagnostic et la résolution des problèmes.
- Ajout du support du format Markdown pour les retours d'information.
- Amélioration de la compatibilité avec FastAPI-MCP pour gérer les modèles auto-référentiels.
- Ajout d'un serveur MCP (Model Configuration Provider).

### Évolutions techniques
- Mise à jour de la version de PaddleOCR.
- Correction de vulnérabilités de sécurité identifiées par Dependabot.
- Refactorisation de la gestion des fichiers pour utiliser un `FileHandlerExtractionModel` unifié.
- Amélioration de la gestion des tests, notamment avec l'ajout de tests unitaires pour le stockage vectoriel Qdrant.
- Ajout d'un middleware `NoCacheMiddleware` pour empêcher la mise en cache des réponses.
- Amélioration de la gestion des erreurs et de la journalisation dans les workers.
- Correction de problèmes liés aux assertions dans les tests SDK et stabilisation des tests.
- Amélioration de la gestion des fichiers S3 avec ajout de la fonctionnalité de téléchargement et de gestion des noms de fichiers.

### Autres changements
- Mise à jour de la documentation README avec une introduction et une section sur les formats de fichiers supportés.
- Formatage des commandes de healthcheck dans le fichier `docker-compose.yml` pour une meilleure cohérence.
- Ajout de tests unitaires pour la fonctionnalité `LazyEmailList`.
- Amélioration du typage avec des overloads pour la méthode `__getitem__` de `LazyPDF`.
- Corrections diverses liées au processus de release (CI).
