## Changelog : questions-ecrites (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec le remplacement du vecteur store Qdrant par pg_vector, offrant ainsi une intégration plus directe avec la base de données PostgreSQL.  De nouvelles fonctionnalités ont été ajoutées, notamment un point de terminaison de recherche sémantique et la possibilité d'intégrer des embeddings (représentations vectorielles) des réponses.  Des améliorations ont également été apportées à l'API et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison pour la recherche sémantique, permettant des recherches plus pertinentes basées sur le sens des questions. [#7cbeb76](https://github.com/SocialGouv/questions-ecrites/pulls/7cbeb76)
- Ajout d'un point de terminaison `healthz` pour vérifier l'état de santé de l'application. [#c6e701a](https://github.com/SocialGouv/questions-ecrites/pulls/c6e701a)
- Possibilité d'intégrer des embeddings des réponses pour améliorer la recherche et l'analyse. [#5c2d135](https://github.com/SocialGouv/questions-ecrites/pulls/5c2d135), [#1d925c3](https://github.com/SocialGouv/questions-ecrites/pulls/1d925c3), [#d66a225](https://github.com/SocialGouv/questions-ecrites/pulls/d66a225), [#36dfc27](https://github.com/SocialGouv/questions-ecrites/pulls/36dfc27)
- Ajout d'un point de terminaison pour récupérer les directions. [#f1474a2](https://github.com/SocialGouv/questions-ecrites/pulls/f1474a2)

### Évolutions techniques
- Remplacement de Qdrant par pg_vector pour le stockage des vecteurs, simplifiant l'architecture et l'intégration avec PostgreSQL. [#0be8c5e](https://github.com/SocialGouv/questions-ecrites/pulls/0be8c5e)
- Ajout de la dépendance `pgvector` pour supporter l'utilisation de pg_vector. [#50717c3](https://github.com/SocialGouv/questions-ecrites/pulls/50717c3)
- Refactorisation de la structure de l'API pour intégrer les nouvelles fonctionnalités. [#7cbeb76](https://github.com/SocialGouv/questions-ecrites/pulls/7cbeb76)
- Configuration de l'URL de la base de données via la variable d'environnement `DATABASE_URL`. [#6361e73](https://github.com/SocialGouv/questions-ecrites/pulls/6361e73)
- Correction d'un problème de récupération de la clé depuis un objet JSONB. [#c7ee3b1](https://github.com/SocialGouv/questions-ecrites/pulls/c7ee3b1)
- Résolution des commentaires suite à la revue de la pull request. [#62b8f91](https://github.com/SocialGouv/questions-ecrites/pulls/62b8f91), [#1a2ae94](https://github.com/SocialGouv/questions-ecrites/pulls/1a2ae94)

### Autres changements
- Mise à jour de la documentation `CLAUDE.md` et `README.md`. [#2552ea9](https://github.com/SocialGouv/questions-ecrites/pulls/2552ea9)
