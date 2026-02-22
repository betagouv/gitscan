## Changelog : OpenGateLLM (30 derniers jours)

### Résumé
Ce mois-ci, OpenGateLLM a connu des améliorations significatives en termes de gestion des données, de simplification de l'architecture et de correction de bugs. Les utilisateurs bénéficieront d'une meilleure gestion des chunks de données, de la dépréciation de certains anciens endpoints, et d'une infrastructure plus robuste grâce à la refactorisation de l'application.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/v1/chunks` pour la gestion des chunks de données (#660).
- Dépréciation de l'endpoint legacy `/v1/files` et `/v1/ocr-beta` pour les documents (#698).
- Dépréciation de la fonctionnalité ProConnect (#693).
- Amélioration de la gestion du seuil dans la recherche (#684).
- Correction du streaming de la réponse chat pour les modèles (#692).
- Amélioration du formatage des erreurs de configuration (#672).
- Ajout d'un healthcheck à la migration Elasticsearch (#669).
- Correction du format de requête pour l'intégration Albert (audio) (#665).
- Suppression des rôles et organisations dans le playground (#666).

### Évolutions techniques
- Refactorisation de la création de l'application pour une architecture plus propre (#691).
- Refactorisation des routeurs pour une architecture plus propre (#658).
- Consolidation des index Elasticsearch en un seul index (#667).
- Modification du schéma des chunks (#688).
- Correction de la division par zéro dans le calcul `rff_k` pour la recherche, avec ajout de tests (#687).
- Suppression du nom de document de l'index Elasticsearch (#686).
- Correction de l'affichage des métriques avec plusieurs workers (#681).
- Dépréciation du paramètre `k` dans l'endpoint `/v1/search` (#694).

### Autres changements
- Suppression du fichier `import_circular_diagram.md` (#699).
- Ajout d'une documentation ADR concernant le scaling Elasticsearch (#668).
