## Changelog : questions-ecrites (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, le projet a fait des avancées significatives dans l'exposition des données et l'amélioration de la recherche. Une API FastAPI a été implémentée, permettant d'accéder aux questions écrites et à leurs attributions. De plus, la possibilité d'intégrer des réponses sémantiques a été ajoutée, ouvrant la voie à des fonctionnalités de recherche plus performantes.

### Évolutions fonctionnelles
- Ajout d'un endpoint d'API pour la recherche sémantique. [#1234](https://github.com/SocialGouv/questions-ecrites/issues/1234) (implémentation en cours)
- Ajout d'un endpoint d'API pour les attributions aux différents bureaux. [#1234](https://github.com/SocialGouv/questions-ecrites/issues/1234)
- Possibilité d'intégrer des réponses (embeddings) pour améliorer la recherche et le reranking.
- Attribution des questions aux bureaux concernés.

### Évolutions techniques
- Implémentation d'une API REST avec FastAPI et Uvicorn.
- Refactorisation de la structure de l'API pour une meilleure organisation et maintenabilité.

### Autres changements
- Correction de commentaires issus de la revue de code sur l'implémentation de l'API.
