## Changelog : ragtime (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec un changement de nom de "rag-facile" à "ragtime".  De nouvelles fonctionnalités de gestion de collections ont été ajoutées via l'interface en ligne de commande (CLI), permettant aux utilisateurs de créer, modifier et supprimer des collections de documents. Des corrections de bugs ont également été apportées, notamment concernant l'authentification et la configuration initiale.

### Évolutions fonctionnelles
- Ajout d'une interface en ligne de commande (CLI) complète pour la gestion des collections : création, modification et suppression. [#98a0c04](https://github.com/etalab-ia/ragtime/commit/98a0c04e2c72df20c6b3b8059a9311445de8d606) et [#809140d](https://github.com/etalab-ia/ragtime/commit/809140d80bb383c6827e39fb42d4a9dc2e1fbeec)
- Amélioration de la configuration initiale : affichage des prochaines étapes au lieu du démarrage automatique du serveur de développement. [#aa27c6a](https://github.com/etalab-ia/ragtime/commit/aa27c6a92b98471d73342c09b468e8a9c50a9cc7)
- Demande de mot de passe pour la saisie de la clé API lors de la configuration initiale. [#5f1e12d](https://github.com/etalab-ia/ragtime/commit/5f1e12d81f3effa582714d0f642650ce265782a6) et [#f613f6f](https://github.com/etalab-ia/ragtime/commit/f613f6f275506ca8884d064085eb09caa128e840)

### Évolutions techniques
- Changement de nom du projet de "rag-facile" à "ragtime". [#15a1969](https://github.com/etalab-ia/ragtime/commit/15a1969d67e8f79a79c99d3138381c888287d386)
- Suppression de l'agentic harness et de la commande `ragtime learn`. [#609e987](https://github.com/etalab-ia/ragtime/commit/609e987a767687ccf687d5f881787b0ef9761440)
- Correction de tests pour confirmer au lieu d'abandonner. [#713e88a](https://github.com/etalab-ia/ragtime/commit/713e88aa417f43a88646bcbb632f9f94a3f111ed)
- Gestion des codes ANSI dans les tests d'activation/désactivation des collections. [#198a31e](https://github.com/etalab-ia/ragtime/commit/198a31e2d24115a0d7f96c8f189c25e6fbb76edf)
- Ajout des dépendances `supabase` et `asyncpg` pour Chainlit lors de la configuration. [#2ea3d88](https://github.com/etalab-ia/ragtime/commit/2ea3d882a9b94ad1d5cdbdc44fcb98523fd69d22)
- Gestion des répertoires `src` existants lors de la génération de l'installation autonome. [#da51390](https://github.com/etalab-ia/ragtime/commit/da51390821b67f530e9f4a66dd2a290da4398d8a)
- Support des tests PR dans le workflow `install.sh`. [#ff88374](https://github.com/etalab-ia/ragtime/commit/ff88374aa50113119af8986cb04dc318124ba84e)
- Correction de l'authentification conditionnelle à la configuration de Supabase. [#2d59249](https://github.com/etalab-ia/ragtime/commit/2d592496d9e940ea9e804849918d789c53119a02)

### Autres changements
- Correction de la bannière ASCII art RAGTIME. [#78913bc](https://github.com/etalab-ia/ragtime/commit/78913bcc4c9437513a17cacf27ff979046890a85) et [#c8376d2](https://github.com/etalab-ia/ragtime/commit/c8376d2f7c5b0356bdd5470869ff1206692e73b3)
