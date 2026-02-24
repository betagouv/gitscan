## Changelog : OpenGateLLM (30 derniers jours)

### Résumé
Ce mois-ci, OpenGateLLM a connu une refonte importante de son architecture interne pour une meilleure organisation et maintenabilité. De nouvelles fonctionnalités ont été ajoutées pour la gestion des chunks de données, et des améliorations ont été apportées à la recherche et à l'indexation Elasticsearch. Plusieurs points d'accès (endpoints) ont été dépréciés en vue de simplifier l'API.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/v1/chunks` pour la gestion des chunks de données (#660).
- Amélioration de la gestion du seuil dans la recherche (#684).
- Correction du streaming de réponses pour les modèles de chat (#692).
- Suppression des rôles et organisations dans le playground (#666).
- Correction du format de requête pour l'intégration Albert dans le module audio (#665).
- Refactorisation des endpoints des providers (#696).

### Évolutions techniques
- Refactorisation de la création de l'application pour adopter une architecture plus propre (#691).
- Refactorisation des routeurs pour une meilleure organisation (#658).
- Consolidation des index Elasticsearch en un seul index (#667).
- Dépréciation du paramètre `k` dans l'endpoint `/v1/search` (#694).
- Dépréciation des anciens endpoints `/v1/files` et `/v1/ocr-beta` (#698).
- Dépréciation de la fonctionnalité ProConnect (#693).
- Correction d'une division par zéro dans le calcul `rff_k` pour la recherche (#687).
- Suppression du nom du document de l'index Elasticsearch (#686).
- Ajout d'un healthcheck au script de migration Elasticsearch (#669).
- Correction des métriques avec plusieurs workers (#681).

### Autres changements
- Suppression du fichier `import_circular_diagram.md` (#699).
- Documentation d'une architecture de décision (ADR) concernant le scaling d'Elasticsearch (#668).
- Amélioration du formatage des erreurs de configuration (#672).
- Modification du schéma des chunks (#688).
- Modification des métadonnées par défaut pour les documents (#685).
