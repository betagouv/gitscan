## Changelog : OpenGateRAG-Next (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois-ci, OpenGateRAG-Next a franchi une étape majeure de sa restructuration. Le projet se concentre désormais sur une gestion robuste des "collections" de données via une nouvelle API, permettant de créer, consulter et modifier des ensembles de données de manière structurée. Pour gagner en efficacité et en clarté, une partie du code ancien et du composant Elasticsearch a été supprimée au profit d'une architecture plus moderne et simplifiée basée sur PostgreSQL.

### Évolutions fonctionnelles
- **Gestion complète des collections via API** : Implémentation du cycle de vie des collections (création, récupération avec filtres de nom et de visibilité, consultation par ID et mise à jour) [#2, #3, #4, #5].
- **Gestion des quotas** : Mise en place d'une limite de stockage par défaut de 10 millions de tokens pour les nouveaux utilisateurs [#15](https://github.com/etalab-ia/OpenGateRAG-Next/issues/15).

### Évolutions techniques
- **Refonte de l'architecture métier** : Introduction d'une structure basée sur les UseCases, les ports et les repositories pour les collections et les utilisateurs, améliorant la modularité.
- **Migration de la persistance** : Passage à une gestion via PostgreSQL et optimisation du schéma de données (suppression des anciennes clés étrangères).
- **Nettoyage de l'infrastructure** : Suppression du code hérité (legacy) et d'Elasticsearch pour alléger le système.
- **Amélioration de la qualité logicielle** : 
    - Mise en place de tests unitaires et d'intégration.
    - Intégration de tests de bout en bout (E2E) contre les dernières versions d'OpenGateLLM [#18](https://github.com/etalab-ia/OpenGateRAG-Next/issues/18).
    - Correction de la gestion des clés API dans les scripts de test E2E [#16](https://github.com/etalab-ia/OpenGateRAG-Next/issues/16).
- **Optimisation du code** : Centralisation de la configuration du logging et réorganisation des utilitaires vers la couche infrastructure.

### Autres changements
- **Documentation** : Mise à jour des guides sur les agents, des conventions de tests et de la documentation de référence pour l'API.
- **Maintenance** : Nettoyage des configurations et des dépendances inutilisées.
