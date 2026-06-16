## Changelog : questions-ecrites (30 derniers jours, au 2026-06-15)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données, notamment l'extraction des questions parlementaires, et l'ajout de nouvelles fonctionnalités de filtrage et d'accès aux données. L'infrastructure a également été mise à jour avec le remplacement de Qdrant par pg_vector pour le stockage des vecteurs, simplifiant ainsi le déploiement et la maintenance.

### Évolutions fonctionnelles
- Ajout d'un filtre "directions" à l'endpoint d'attribution des bureaux [#55dcce8](https://github.com/SocialGouv/questions-ecrites/commit/55dcce8).
- Ajout d'un endpoint pour récupérer les "directions" [#f1474a2](https://github.com/SocialGouv/questions-ecrites/commit/f1474a2).
- Possibilité de filtrer les attributions par `office_ids` dans `get_attributions` [#109f013](https://github.com/SocialGouv/questions-ecrites/commit/109f013).
- Extraction des questions parlementaires singulières de l'Assemblée Nationale et du Sénat [#2accd67](https://github.com/SocialGouv/questions-ecrites/commit/2accd67).
- Amélioration de l'extraction de l'objet des questions parlementaires de l'Assemblée Nationale [#a50c08a](https://github.com/SocialGouv/questions-ecrites/commit/a50c08a).
- Amélioration des identifiants des réponses [#a0e481d](https://github.com/SocialGouv/questions-ecrites/commit/a0e481d).

### Évolutions techniques
- Remplacement de Qdrant par pg_vector pour le stockage des vecteurs [#0be8c5e](https://github.com/SocialGouv/questions-ecrites/commit/0be8c5e) et [#e2bf4af](https://github.com/SocialGouv/questions-ecrites/commit/e2bf4af) [#50717c3](https://github.com/SocialGouv/questions-ecrites/commit/50717c3).
- Ajout d'un endpoint de santé (healthz) pour la surveillance de l'application [#c6e701a](https://github.com/SocialGouv/questions-ecrites/commit/c6e701a).
- Configuration de la variable d'environnement `DATABASE_URL` [#6361e73](https://github.com/SocialGouv/questions-ecrites/commit/6361e73).
- Les variables `ALBERT_BASE_URL` et `ALBERT_RERANK_MODEL` sont désormais configurables via des variables d'environnement [#00d7f60](https://github.com/SocialGouv/questions-ecrites/commit/00d7f60).
- Renommage de la variable `SOCLE_IA_API_KEY` en `PLIAGE_API_KEY` [#25bfdf7](https://github.com/SocialGouv/questions-ecrites/commit/25bfdf7).

### Autres changements
- Mise à jour de la documentation README.md et CLAUDE.md [#2552ea9](https://github.com/SocialGouv/questions-ecrites/commit/2552ea9).
- Ajout d'informations sur `kubectl` dans le README [#e096d93](https://github.com/SocialGouv/questions-ecrites/commit/e096d93).
- Suppression des clusters de questions [#c66949e](https://github.com/SocialGouv/questions-ecrites/commit/c66949e).
- Correction d'un bug lors de la récupération de la `key` depuis un JSONB [#c7ee3b1](https://github.com/SocialGouv/questions-ecrites/commit/c7ee3b1).
- Correction suite aux retours de `revu-bot` sur la PR #39 [#f93e508](https://github.com/SocialGouv/questions-ecrites/pull/39).
- Ajout d'une règle `.claude` au fichier `.gitignore` [#ff394d3](https://github.com/SocialGouv/questions-ecrites/commit/ff394d3).
