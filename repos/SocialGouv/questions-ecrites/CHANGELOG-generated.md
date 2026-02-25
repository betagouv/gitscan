## Changelog : questions-ecrites (30 derniers jours)

### Résumé
Ce projet a connu des avancées significatives au cours des dernières semaines, notamment dans la préparation à l'intégration de Claude, un modèle de langage. Des améliorations ont été apportées à la structure du code, à la gestion de la configuration et à l'ajout de nouvelles fonctionnalités pour l'évaluation des résultats. L'objectif est d'améliorer la capacité du système à associer les questions sans réponse aux experts appropriés.

### Évolutions fonctionnelles
- Ajout d'un script d'évaluation pour mesurer la qualité des résultats (#bc12472).
- Normalisation des noms de fichiers (minuscules et suppression des extensions) pour une meilleure cohérence (#2c5c834).
- Ajout de clients pour interagir avec le LLM, les embeddings, Qdrant et le reranker (#e176da7).

### Évolutions techniques
- Refactorisation du code pour une meilleure organisation et réutilisation (#c746ff2, #92607de, #64f330c).
- Déplacement du code commun dans le package `qe` (#64f330c).
- Suppression de la variable d'environnement `DATABASE_URL` de la configuration Alembic (#1017483).
- Centralisation de la gestion de la configuration dans un module dédié (#9b62ac4).
- Ajout des dépendances `polars` et `openpyxl` pour de nouvelles fonctionnalités (#31c2327).
- Intégration des workflows CI/CD pour Claude (#a5cd3c2, #db2a0f9).

### Autres changements
- Documentation initiale pour l'intégration de Claude (#e98e1ec).
- Initialisation du projet (#a1b06aa).
