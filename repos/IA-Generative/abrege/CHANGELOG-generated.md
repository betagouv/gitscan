## Changelog : abrege (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour d'abrege se concentrent sur l'ajout de nouvelles fonctionnalités clés, notamment la génération de questions/réponses (QA), l'extraction de contenu web (scraping), et l'amélioration de la gestion des tâches. Des corrections et des améliorations de la configuration ont également été apportées pour une meilleure stabilité et intégration avec divers services.

### Évolutions fonctionnelles
- Ajout de la génération de questions/réponses (QA) avec une interface utilisateur dédiée et une intégration backend. [#313](https://github.com/IA-Generative/abrege/issues/313)
- Implémentation de la fonctionnalité de scraping web pour extraire du contenu à partir de pages web.
- Ajout de la possibilité d'annuler les tâches en cours et mise à jour de l'interface utilisateur pour refléter cet état.
- Ajout d'une vue détaillée des tâches avec un routage approprié.
- Amélioration du modèle de résultats OCR avec des structures pour pages, boîtes englobantes et cases à cocher.
- Modification du libellé de l'en-tête des tâches pour afficher "Mes tâches".
- Ajout d'une fonctionnalité pour signaler les erreurs à Sentry pour l'API, les workers et l'interface utilisateur.

### Évolutions techniques
- Mise à jour des variables d'environnement pour utiliser `AWS_BUCKET_NAME` au lieu de `S3_BUCKET_NAME` dans les configurations et la documentation.
- Mise à jour de la configuration de Langfuse pour une intégration optionnelle.
- Mise à jour des variables d'environnement et des configurations pour l'intégration avec Redis, MinIO et OpenAI.
- Amélioration de la gestion des erreurs et ajout d'erreurs de surcharge pour LLM et OCR.
- Correction d'un problème d'importation dans les tests.
- Correction d'un problème de sécurité.
- Refactorisation de l'architecture pour utiliser des services.
- Ajout de modèles Pydantic pour les réponses de l'API.

### Autres changements
- Publication des versions 3.3.0, 3.2.0, 3.1.2, 3.1.1, 3.1.0, 3.0.0, 2.3.1, 2.3.0, 2.2.0, 2.1.1, 2.1.0, 2.0.2, 2.0.1 et 2.0.0.
- Mise à jour des paquets.
- Amélioration des logs.
- Ajout de migrations pour les images.
- Ajout de détails de santé.
- Correction de problèmes liés à la CI/CD.
