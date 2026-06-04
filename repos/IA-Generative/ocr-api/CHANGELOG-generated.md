## Changelog : ocr-api (30 derniers jours, au 2 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'API OCR, notamment l'ajout de la prise en charge de l'extraction de texte à partir d'emails, une refonte de la gestion des fichiers pour une meilleure cohérence, et des optimisations de la gestion des tâches d'OCR. La documentation a également été enrichie avec de nouvelles sections.

### Évolutions fonctionnelles
* **Extraction d'emails:** Implémentation d'un modèle et d'un worker pour l'extraction du contenu des emails (format EML supporté).
* **Formats de fichiers:** Ajout du format EML aux formats de fichiers supportés et centralisation de la validation des types MIME pour une meilleure cohérence.
* **Documentation:** Ajout de nouvelles sections à la documentation concernant la classification, l'extraction d'entités et les templates.
* **Amélioration de l'interface:** Mise à jour de l'introduction et ajout d'une section listant les formats de fichiers supportés dans le fichier README.

### Évolutions techniques
* **Refactoring du parser de fichiers:** Refonte des modèles d'extraction de fichiers pour utiliser un `FileHandlerExtractionModel` unifié.
* **Amélioration du typage:** Amélioration de la méthode `__getitem__` de `LazyPDF` avec des surcharges pour un meilleur typage.
* **MCP Server:** Ajout d'un serveur MCP (Model Compatibility Patch) avec un patch de compatibilité pour gérer les modèles auto-référentiels.
* **Optimisation des tâches:** Simplification de la gestion des tâches pour le traitement OCR, en supprimant le découpage en "chunks".
* **Healthcheck Docker:** Formatage des commandes de test de healthcheck dans le fichier `docker-compose` pour une meilleure cohérence.

### Autres changements
* **Versioning:** Ajout d'une stratégie de versioning pour la branche de développement dans le workflow de release.
* **Tests:** Ajout de tests unitaires pour la fonctionnalité `LazyEmailList`.
* **Documentation:** Mise à jour du formatage de la table des matières de la documentation pour une meilleure lisibilité.
