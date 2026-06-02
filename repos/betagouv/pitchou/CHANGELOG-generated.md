## Changelog : pitchou (30 derniers jours, au 1er juin 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé une refonte technique majeure de l'application, passant de Fastify et Rollup à SvelteKit et Vite, avec l'objectif d'améliorer les performances et l'expérience de développement. Des améliorations de sécurité ont également été apportées, ainsi que des corrections de bugs et l'ajout d'une espèce protégée à la liste.

### Évolutions fonctionnelles
- Ajout du grand capricorne à la liste des espèces protégées dans le cadre du CPNP. [#578](https://github.com/betagouv/pitchou/issues/578)
- Ajout d'un bandeau d'information sur l'environnement de staging pour une meilleure identification. [#574](https://github.com/betagouv/pitchou/issues/574)
- Autorisation des routes d'écriture et de suppression via CAP. [#565](https://github.com/betagouv/pitchou/issues/565)
- Correction de la synchronisation des dossiers pour gérer correctement les entreprises nulles. [#569](https://github.com/betagouv/pitchou/issues/569)
- Correction du rattachement des pièces jointes du pétitionnaire partagées entre les dossiers. [#570](https://github.com/betagouv/pitchou/issues/570)

### Évolutions techniques
- Refonte complète de l'application : migration de Fastify vers SvelteKit (SPA) pour une meilleure performance et expérience utilisateur. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration de Rollup vers Vite pour améliorer la vitesse de build. [#564](https://github.com/betagouv/pitchou/issues/564)
- Passage à pnpm pour la gestion des dépendances. [#561](https://github.com/betagouv/pitchou/issues/561)
- Amélioration du CI en utilisant `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Amélioration de la sécurité : utilisation d'un IV aléatoire pour le chiffrement et renforcement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560), [#557](https://github.com/betagouv/pitchou/issues/557)
- Passage de `pgdata` en volume nommé dans Docker pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans Docker. [#572](https://github.com/betagouv/pitchou/issues/572)

### Autres changements
- Ajout de tests avec Vitest pour la fonction `manipulationStrings`. [#559](https://github.com/betagouv/pitchou/issues/559)
- Ajout d'un shell de développement Nix et de la configuration Direnv. [#558](https://github.com/betagouv/pitchou/issues/558)
- Ajout et application de Prettier pour améliorer la cohérence du code. [#555](https://github.com/betagouv/pitchou/issues/555)
- Correction de la seed script et de l'origine. [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout d'un seed de développement pour l'authentification locale. [#563](https://github.com/betagouv/pitchou/issues/563)
- Correction de l'utilisation de Knex dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)
