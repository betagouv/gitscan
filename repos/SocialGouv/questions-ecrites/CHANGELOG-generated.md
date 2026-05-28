## Changelog : questions-ecrites (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des évolutions significatives concernant la recherche sémantique et l'attribution des questions. L'architecture a été refactorée pour utiliser `pg_vector` à la place de `qdrant` pour le stockage des embeddings, améliorant ainsi la performance et la simplicité de l'infrastructure. De nouvelles fonctionnalités ont été ajoutées pour permettre la recherche sémantique et le filtrage par direction.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour la recherche sémantique, permettant de retrouver des questions similaires en fonction de leur contenu. [#7cbeb76](https://github.com/SocialGouv/questions-ecrites/commit/7cbeb76)
- Ajout d'un filtre par "direction" sur l'endpoint d'attribution des questions aux services. [#55dcce8](https://github.com/SocialGouv/questions-ecrites/commit/55dcce8)
- Ajout d'un endpoint pour récupérer la liste des directions. [#f1474a2](https://github.com/SocialGouv/questions-ecrites/commit/f1474a2)
- Possibilité d'intégrer des embeddings (représentations vectorielles) dans les réponses. [#5c2d135](https://github.com/SocialGouv/questions-ecrites/commit/5c2d135), [#1d925c3](https://github.com/SocialGouv/questions-ecrites/commit/1d925c3), [#d66a225](https://github.com/SocialGouv/questions-ecrites/commit/d66a225), [#36dfc27](https://github.com/SocialGouv/questions-ecrites/commit/36dfc27)
- Ajout d'un endpoint de santé (`healthz`) pour faciliter la surveillance de l'application. [#c6e701a](https://github.com/SocialGouv/questions-ecrites/commit/c6e701a)

### Évolutions techniques
- Refactorisation de l'architecture pour utiliser `pg_vector` pour le stockage des embeddings, remplaçant `qdrant`. [#0be8c5e](https://github.com/SocialGouv/questions-ecrites/commit/0be8c5e)
- Ajout de la dépendance `pgvector` pour supporter l'utilisation de `pg_vector`. [#50717c3](https://github.com/SocialGouv/questions-ecrites/commit/50717c3)
- Configuration de l'URL de la base de données via la variable d'environnement `DATABASE_URL`. [#6361e73](https://github.com/SocialGouv/questions-ecrites/commit/6361e73)
- Correction d'une erreur lors de la récupération de la clé depuis un objet JSONB. [#c7ee3b1](https://github.com/SocialGouv/questions-ecrites/commit/c7ee3b1)
- Corrections suite aux retours de la revue de code (PR). [#62b8f91](https://github.com/SocialGouv/questions-ecrites/commit/62b8f91), [#1a2ae94](https://github.com/SocialGouv/questions-ecrites/commit/1a2ae94)

### Autres changements
- Mise à jour de la documentation `CLAUDE.md` et `README.md`. [#2552ea9](https://github.com/SocialGouv/questions-ecrites/commit/2552ea9)
