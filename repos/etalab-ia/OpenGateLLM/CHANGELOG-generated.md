## Changelog : OpenGateLLM (30 derniers jours)

### Résumé
Ce mois-ci, OpenGateLLM a connu des améliorations significatives en termes de gestion des données (chunks, documents) et de refonte de l'architecture interne pour une meilleure maintenabilité et évolutivité. Des corrections de bugs et des dépréciations de fonctionnalités anciennes ont également été apportées pour optimiser l'expérience utilisateur et préparer le terrain pour de futures évolutions.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/v1/chunks` pour la gestion des chunks de données (#660).
- Amélioration de la gestion du seuil dans la recherche pour une meilleure pertinence des résultats (#684).
- Correction du streaming des réponses du chat pour une expérience utilisateur plus fluide (#692).
- Suppression des endpoints legacy `/v1/files` et `/v1/ocr-beta` (#698).
- Dépréciation de la fonctionnalité ProConnect (#693).
- Dépréciation du paramètre `k` dans l'endpoint `/v1/search` (#694).
- Amélioration du tri et des filtres sur les pages des routeurs et des fournisseurs dans le Playground (#664).
- Correction du format de date d'expiration lors de la création d'utilisateurs dans le Playground (#663).
- Correction du type d'ID de collection obsolète dans la recherche (#662).

### Évolutions techniques
- Refactorisation de la création de l'application pour adopter une architecture plus propre (#691).
- Refactorisation des routeurs pour une meilleure organisation et maintenabilité (#658).
- Consolidation des index Elasticsearch en un seul index pour simplifier la gestion et améliorer les performances (#667).
- Ajout d'un healthcheck au script de migration Elasticsearch (#669).
- Modification du schéma des chunks (#688).
- Correction d'une division par zéro dans le calcul `rff_k` dans la recherche (#687).
- Suppression du nom de document de l'index Elasticsearch (#686).
- Modification du format par défaut des métadonnées des documents (#685).

### Autres changements
- Suppression du fichier `import_circular_diagram.md` (#699).
- Amélioration de la lisibilité des messages d'erreur de configuration (#672).
- Documentation d'une architecture de décision relative au scaling d'Elasticsearch (#668).
- Correction du format de la requête pour l'intégration avec Albert (#665).
- Suppression de tous les rôles et organisations dans le Playground (#666).
