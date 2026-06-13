## Changelog : questions-ecrites (30 derniers jours, au 2026-06-12)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives concernant l'ingestion des questions parlementaires, notamment la prise en charge des questions singulières de l'Assemblée Nationale et du Sénat.  Des filtres supplémentaires ont été ajoutés pour affiner les recherches et l'attribution des questions, et l'infrastructure a été modifiée pour utiliser pg_vector à la place de qdrant pour la gestion des vecteurs.

### Évolutions fonctionnelles
- Ajout d'un filtre par "directions" sur l'endpoint d'attribution des questions aux services [#55dcce8](https://github.com/SocialGouv/questions-ecrites/commit/55dcce8).
- Ajout d'un endpoint pour récupérer les "directions" [#f1474a2](https://github.com/SocialGouv/questions-ecrites/commit/f1474a2).
- Possibilité de filtrer par `office_ids` dans l'endpoint `get_attributions` [#109f013](https://github.com/SocialGouv/questions-ecrites/commit/109f013).
- Prise en charge de l'extraction des questions singulières de l'Assemblée Nationale et du Sénat [#2accd67](https://github.com/SocialGouv/questions-ecrites/commit/2accd67).
- Correction de l'extraction de l'objet à partir des balises `<analyses><analyse>` modernes dans l'ingestion des questions de l'Assemblée Nationale [#a50c08a](https://github.com/SocialGouv/questions-ecrites/commit/a50c08a).
- Correction de la récupération de la `key` à partir du JSONB [#c7ee3b1](https://github.com/SocialGouv/questions-ecrites/commit/c7ee3b1).

### Évolutions techniques
- Remplacement de qdrant par pg_vector pour la gestion des vecteurs [#0be8c5e](https://github.com/SocialGouv/questions-ecrites/commit/0be8c5e) et mise à jour de la configuration correspondante [#e2bf4af](https://github.com/SocialGouv/questions-ecrites/commit/e2bf4af).
- Ajout de la dépendance `pgvector` [#50717c3](https://github.com/SocialGouv/questions-ecrites/commit/50717c3).
- Les variables d'environnement `ALBERT_BASE_URL` et `ALBERT_RERANK_MODEL` sont maintenant configurables via des variables d'environnement [#00d7f60](https://github.com/SocialGouv/questions-ecrites/commit/00d7f60).
- Renommage de la variable d'environnement `SOCLE_IA_API_KEY` en `PLIAGE_API_KEY` [#25bfdf7](https://github.com/SocialGouv/questions-ecrites/commit/25bfdf7).
- Ajout d'un endpoint de santé (`healthz`) pour la surveillance de l'application [#c6e701a](https://github.com/SocialGouv/questions-ecrites/commit/c6e701a).
- Ajout de la variable d'environnement `DATABASE_URL` [#6361e73](https://github.com/SocialGouv/questions-ecrites/commit/6361e73).

### Autres changements
- Suppression des clusters de questions [#c66949e](https://github.com/SocialGouv/questions-ecrites/commit/c66949e).
- Mise à jour de la documentation (README.md et CLAUDE.md) [#2552ea9](https://github.com/SocialGouv/questions-ecrites/commit/2552ea9).
- Ajout d'informations sur `kubectl` dans le README [#e096d93](https://github.com/SocialGouv/questions-ecrites/commit/e096d93).
- Correction de feedback revu-bot sur la PR #39 [#f93e508](https://github.com/SocialGouv/questions-ecrites/commit/f93e508).
- Ajout d'une règle pour ignorer le fichier `.claude` dans le contrôle de version [#ff394d3](https://github.com/SocialGouv/questions-ecrites/commit/ff394d3).
