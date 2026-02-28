## Changelog : OpenGateLLM (30 derniers jours)

### Résumé
Ce mois-ci, OpenGateLLM a connu une évolution significative vers une architecture plus propre et plus maintenable, avec une refactorisation importante des routes et des points de terminaison de l'API. De nouvelles fonctionnalités ont été ajoutées pour la gestion des chunks de données, la recherche sémantique et le rerank, améliorant ainsi les capacités de recherche et de manipulation de données. Des corrections de bugs et des améliorations de la stabilité ont également été apportées, notamment concernant les métriques et le streaming de réponses.

### Évolutions fonctionnelles
- Ajout du support des modèles vLLM pour le rerank (#719).
- Implémentation d'une recherche dans un outil intégré pour le chat (#708).
- Ajout de la possibilité de trier les documents par ordre croissant ou décroissant (#709).
- Ajout d'un filtre de métadonnées à l'endpoint de recherche (#700).
- Ajout d'un endpoint POST pour la gestion des chunks de données (#660).
- Correction de la gestion du seuil dans la recherche sémantique (#684).
- Amélioration du formatage des erreurs de configuration (#672).
- Correction du streaming des réponses du chat (#692).
- Ajout d'un healthcheck à la migration Elasticsearch (#669).
- Correction du format de requête pour l'intégration Albert (audio) (#665).

### Évolutions techniques
- Refactorisation importante des routes de l'API vers une architecture plus propre (#712, #707, #691, #658).
- Suppression de l'endpoint legacy `/v1/files` et `/v1/ocr-beta` (#698).
- Dépréciation du paramètre `k` dans l'endpoint `/v1/search` (#694).
- Dépréciation des arguments legacy du rerank (#705).
- Dépréciation de l'endpoint `/v1/proconnect` (#693).
- Consolidation des index Elasticsearch en un seul index (#667).
- Correction d'un problème de division par zéro dans le calcul rff_k pour la recherche (#687).
- Suppression du helper de registre des routes (#697).
- Correction des métriques avec plusieurs workers (#681).
- Modification du schéma des chunks (#688).
- Suppression du nom du document de l'index Elasticsearch (#686).

### Autres changements
- Mise à jour des modèles de "issue" sur GitHub (#711).
- Suppression du fichier `import_circular_diagram.md` (#699).
- Documentation de l'évolutivité d'Elasticsearch (ADR) (#668).
