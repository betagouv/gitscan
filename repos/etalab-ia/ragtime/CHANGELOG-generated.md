## Changelog : ragtime (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet ragtime a connu des changements importants, notamment un renommage complet du projet de "rag-facile" à "ragtime".  Des améliorations significatives ont été apportées à la gestion des collections via l'interface en ligne de commande (CLI), ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'authentification et l'installation.

### Évolutions fonctionnelles
- Ajout d'une gestion complète des collections via la CLI, permettant de créer, modifier et supprimer des collections de documents. [#98a0c04](https://github.com/etalab-ia/ragtime/commit/98a0c04e2c72df20c6b3b8059a9311445de8d606)
- L'assistant agentique et la commande `ragtime learn` ont été supprimés.
- Amélioration du processus d'installation : l'outil affiche désormais les prochaines étapes après la configuration initiale au lieu de démarrer automatiquement le serveur de développement. [#aa27c6a](https://github.com/etalab-ia/ragtime/commit/aa27c6a92b98471d73342c09b468e8a9c50a9cc7)
- L'authentification Chainlit est désormais conditionnelle à la configuration de Supabase. [#2d59249](https://github.com/etalab-ia/ragtime/commit/2d592496d9e940ea9e804849918d789c53119a02)
- Amélioration de la gestion des tests pour les collections activées/désactivées. [#198a31e](https://github.com/etalab-ia/ragtime/commit/198a31e2d24115a0d7f96c8f189c25e6fbb76edf)

### Évolutions techniques
- Renommage du projet de "rag-facile" à "ragtime" dans tout le code et la documentation. [#15a1969](https://github.com/etalab-ia/ragtime/commit/15a1969d67e8f79a79c99d3138381c888287d386)
- Mise à jour de la configuration `wt.toml` pour utiliser `pre-start` au lieu de `post-create` (déprécié). [#fe0ddbd](https://github.com/etalab-ia/ragtime/commit/fe0ddbd)
- Ajout de dépendances `supabase` et `asyncpg` pour Chainlit lors de l'installation. [#2ea3d88](https://github.com/etalab-ia/ragtime/commit/2ea3d882a9b94ad1d5cdbdc44fcb98523fd69d22)
- Amélioration de la gestion des répertoires `src` existants lors de la génération de l'application autonome. [#da51390](https://github.com/etalab-ia/ragtime/commit/da51390821b67f530e9f4a66dd2a290da4398d8a)
- Utilisation d'une invite de mot de passe pour la saisie de la clé API lors de l'installation. [#5f1e12d](https://github.com/etalab-ia/ragtime/commit/5f1e12d81f3effa582714d0f642650ce265782a6), [#f613f6f](https://github.com/etalab-ia/ragtime/commit/f613f6f275506ca8884d064085eb09caa128e840)
- Support des tests PR dans le workflow `install.sh`. [#ff88374](https://github.com/etalab-ia/ragtime/commit/ff88374aa50113119af8986cb04dc318124ba84e)

### Autres changements
- Mise à jour des packages de l'espace de travail vers la version 0.25.0 et activation de l'installation automatique dans `.prototools`. [#b88e69b](https://github.com/etalab-ia/ragtime/commit/b88e69b)
- Ajout de `.ragtime/` à `.gitignore`. [#59cbe0b](https://github.com/etalab-ia/ragtime/commit/59cbe0b)
- Correction de l'art ASCII de RAGTIME dans le README et le banner. [#78913bc](https://github.com/etalab-ia/ragtime/commit/78913bcc4c9437513a17cacf27ff979046890a85), [#c8376d2](https://github.com/etalab-ia/ragtime/commit/c8376d2f7c5b0356bdd5470869ff1206692e73b3)
