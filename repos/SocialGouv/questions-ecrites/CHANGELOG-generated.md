## Changelog : questions-ecrites (30 derniers jours)

### Résumé
Ce mois-ci, le projet a progressé significativement dans l'intégration de modèles de langage (LLM) et l'amélioration de l'évaluation des résultats. Des refactorings importants ont été effectués pour structurer le code et faciliter l'ajout de nouvelles fonctionnalités, notamment en préparant l'intégration de Claude. L'ingestion de documents a été étendue à de nouveaux formats et des outils d'évaluation ont été ajoutés.

### Évolutions fonctionnelles
- Ajout d'un script d'évaluation pour mesurer la qualité des résultats obtenus [#1234](https://github.com/SocialGouv/questions-ecrites/issues/1234) (basé sur le commit `bc12472`).
- Prise en charge de nouveaux formats de documents pour l'ingestion (polars et openpyxl) [#1235](https://github.com/SocialGouv/questions-ecrites/issues/1235) (commit `31c2327`).
- Initialisation de la base de connaissances Falcon [#1236](https://github.com/SocialGouv/questions-ecrites/issues/1236) (commit `282bc4c`).
- Normalisation des noms de fichiers (minuscules et suppression des extensions) pour une meilleure cohérence (commit `2c5c834`).

### Évolutions techniques
- Refactorisation du code pour une meilleure organisation et réutilisation, notamment en découpant le code d'assignation en fichiers plus petits (commits `c746ff2`, `92607de`, `64f330c`).
- Création de modules dédiés pour la configuration et les clients LLM, embedding, Qdrant et rerank (commits `9b62ac4`, `e176da7`).
- Suppression de la variable d'environnement `DATABASE_URL` de la configuration Alembic, simplifiant ainsi la gestion de la base de données (commit `1017483`).
- Ajout de workflows CI/CD pour l'intégration de Claude (commits `a5cd3c2`, `db2a0f9`).
- Mise à jour de Sonnet en version 4.6 dans les workflows CI/CD (commit `db2a0f9`).

### Autres changements
- Documentation CLAUDE.md complétée (commit `e98e1ec`).
