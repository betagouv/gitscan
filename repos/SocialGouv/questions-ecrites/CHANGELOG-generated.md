## Changelog : questions-ecrites (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative dans l'ingestion et le traitement des questions écrites parlementaires. De nouvelles fonctionnalités ont été implémentées pour télécharger et traiter les questions des Assemblées Nationale et Sénat, y compris les questions plus anciennes. Des améliorations ont également été apportées à la performance et à la structure des données, ainsi qu'à l'intégration avec les services Socle IA et Qdrant. Une API FastAPI a été ajoutée pour exposer les attributions des questions.

### Évolutions fonctionnelles
- Ajout d'une API FastAPI avec un endpoint pour les attributions de questions. [#0135e82](https://github.com/SocialGouv/questions-ecrites/commit/0135e82)
- Implémentation de l'attribution des questions aux différents bureaux. [#14529d9](https://github.com/SocialGouv/questions-ecrites/commit/14529d9)
- Possibilité de télécharger et d'ingérer les questions des Assemblées Nationale et du Sénat à partir de leurs endpoints respectifs. [#2a3c187](https://github.com/SocialGouv/questions-ecrites/commit/2a3c187)
- Prise en charge de l'ingestion de questions anciennes de l'Assemblée Nationale. [#5103c3e](https://github.com/SocialGouv/questions-ecrites/commit/5103c3e)
- Prise en charge de l'ingestion de questions anciennes du Sénat. [#f52368e](https://github.com/SocialGouv/questions-ecrites/commit/f52368e)
- Extraction des réponses dans une table dédiée. [#0af58e4](https://github.com/SocialGouv/questions-ecrites/commit/0af58e4)
- Ajout du champ "objet" de la question dans la base de données PostgreSQL. [#bb3e31f](https://github.com/SocialGouv/questions-ecrites/commit/bb3e31f)
- Ajout de clients pour les services web de Réponse. [#f4d0834](https://github.com/SocialGouv/questions-ecrites/commit/f4d0834)
- Ajout d'un script pour identifier les similarités entre les questions. [#42003db](https://github.com/SocialGouv/questions-ecrites/commit/42003db)

### Évolutions techniques
- Refactorisation de l'algorithme de clustering pour améliorer les performances. [#252be4f](https://github.com/SocialGouv/questions-ecrites/commit/252be4f)
- Ajout de checkpoints lors de l'ingestion des questions pour gérer les erreurs. [#3bc2275](https://github.com/SocialGouv/questions-ecrites/commit/3bc2275)
- Simplification de la structure des tables de clustering en les fusionnant en une seule. [#a5a1b1f](https://github.com/SocialGouv/questions-ecrites/commit/a5a1b1f)
- Suppression du champ "is_social" de la base de données des questions. [#05e783d](https://github.com/SocialGouv/questions-ecrites/commit/05e783d)
- Ajout d'indices sur la table `questions` pour optimiser les requêtes. [#489f2df](https://github.com/SocialGouv/questions-ecrites/commit/489f2df)
- Implémentation d'un système de limitation de débit (TokenBucketRateLimiter). [#be2a6dd](https://github.com/SocialGouv/questions-ecrites/commit/be2a6dd)
- Sauvegarde des clusters de similarité dans la base de données. [#3b550ac](https://github.com/SocialGouv/questions-ecrites/commit/3b550ac)

### Autres changements
- Ajout de commandes de dump de la base de données dans le Makefile. [#d61cc2b](https://github.com/SocialGouv/questions-ecrites/commit/d61cc2b)
- Suppression de code inutilisé. [#c31882d](https://github.com/SocialGouv/questions-ecrites/commit/c31882d)
- Simplification du README pour l'ingestion de données opendata. [#56836ad](https://github.com/SocialGouv/questions-ecrites/commit/56836ad)
- Mise à jour de la documentation CLAUDE.md pour l'utilisation de Falcon MCP. [#cdb3139](https://github.com/SocialGouv/questions-ecrites/commit/cdb3139) et [#e94460e](https://github.com/SocialGouv/questions-ecrites/commit/e94460e)
- Suppression de Falcon de la documentation CLAUDE.md. [#f1d84ad](https://github.com/SocialGouv/questions-ecrites/commit/f1d84ad)
