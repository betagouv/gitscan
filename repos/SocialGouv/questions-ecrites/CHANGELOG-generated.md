## Changelog : questions-ecrites (30 derniers jours, au 22/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'optimisation des performances de recherche et la fiabilisation de l'ingestion des données. Les recherches de questions similaires sont désormais plus rapides et plus robustes grâce à une meilleure gestion des index vectoriels. La gestion des structures administratives (bureaux et directions) a également été affinée pour garantir une meilleure précision dans l'attribution des données.

### Évolutions fonctionnelles
- **Amélioration de l'ingestion** : Les téléchargements de données peuvent désormais reprendre là où ils s'étaient arrêtés au lieu de recommencer intégralement.
- **Gestion des bureaux et directions** : Amélioration de la synchronisation et de la reconnaissance des structures administratives (bureaux/directions) à partir des données MIN15.
- **Retours utilisateurs** : Ajout d'un champ de commentaire pour enrichir les retours de correction ([#59](https://github.com/SocialGouv/questions-ecrites/issues/59)).

### Évolutions techniques
- **Optimisation de la recherche vectorielle (pgvector)** :
  - Amélioration des performances via l'utilisation d'index HNSW partiels pour accélérer les recherches par bureau ou direction.
  - Renforcement de la compatibilité et de la détection de version de l'extension `pgvector`.
  - Création de la table `question_similar_cache` pour accélérer l'affichage des résultats similaires.
- **Intelligence Artificielle & Reranking** :
  - Optimisation du processus de "reranking" par l'envoi des documents à l'API Albert par lots (batching), améliorant la stabilité et la vitesse.
  - Meilleure gestion des erreurs et des timeouts lors des appels de calcul de similarité.
- **Base de données & Performance** :
  - Matérialisation de la vue `question_attributions_all` pour optimiser les requêtes de jointure.
  - Sécurisation et robustesse des migrations de base de données (Alembic), notamment sur les procédures de retour en arrière (downgrade).
- **Infrastructure & CI/CD** :
  - Simplification de l'architecture : suppression de Qdrant, `pgvector` étant désormais l'unique moteur de stockage vectoriel.
  - Correction des pipelines de déploiement via ArgoCD.
  - Optimisation de la consommation mémoire lors de l'ingestion des données du Sénat pour éviter les plantages.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant les mécanismes de scan itératif.
- **CI/CD** : Mise à jour de la gestion des tags pour les jobs de backfill.
