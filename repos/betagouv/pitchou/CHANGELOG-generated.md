## Changelog : pitchou (30 derniers jours, au 6 juin 2026)

### Résumé
Ce mois-ci, Pitchou a connu une refonte technique majeure avec la migration vers SvelteKit et Vite, améliorant ainsi les performances et la maintenabilité du projet. Des corrections de bugs ont été apportées, notamment concernant le téléchargement de documents et la synchronisation des dossiers. De nouvelles espèces protégées ont été ajoutées à la liste. Enfin, des améliorations de sécurité et de l'infrastructure ont été implémentées.

### Évolutions fonctionnelles
- Ajout de nouvelles espèces protégées à la liste CNPN : *Cosentinia vellea* et le grand capricorne. [#578](https://github.com/betagouv/pitchou/issues/578), [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout de domaines autorisés pour l'authentification : Indre-et-Loire et Guyane. [#579](https://github.com/betagouv/pitchou/issues/579)
- Ajout d'un bandeau d'information sur l'environnement de staging pour une meilleure identification. [#574](https://github.com/betagouv/pitchou/issues/574)
- Fusion de la page AARRI dans la page des statistiques pour une vue d'ensemble consolidée. [#582](https://github.com/betagouv/pitchou/issues/582)
- Ajout de liens vers les pages statistiques et budget, ainsi qu'un bouton de changement de thème dans le footer. [#581](https://github.com/betagouv/pitchou/issues/581)
- Correction d'une erreur 500 lors du téléchargement de documents. [#587](https://github.com/betagouv/pitchou/issues/587)
- Correction de problèmes liés à la synchronisation des dossiers, notamment pour éviter les doublons de décisions administratives et rattacher les pièces jointes partagées. [#584](https://github.com/betagouv/pitchou/issues/584), [#570](https://github.com/betagouv/pitchou/issues/570)

### Évolutions techniques
- Migration complète vers SvelteKit (SPA) et suppression de Fastify, modernisant l'architecture frontend. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration du système de build de Rollup vers Vite pour des performances améliorées. [#564](https://github.com/betagouv/pitchou/issues/564)
- Migration vers TypeScript pour une meilleure typage et maintenabilité du code. [#568](https://github.com/betagouv/pitchou/issues/568), [#567](https://github.com/betagouv/pitchou/issues/567)
- Passage à pnpm pour la gestion des dépendances, optimisant l'installation et la gestion des paquets. [#561](https://github.com/betagouv/pitchou/issues/561)
- Migration des fichiers vers Outscale Object Storage pour une meilleure scalabilité et fiabilité. [#573](https://github.com/betagouv/pitchou/issues/573)
- Amélioration du CI/CD en utilisant `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Amélioration de la sécurité avec un IV aléatoire pour le chiffrement et un durcissement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560), [#557](https://github.com/betagouv/pitchou/issues/557)

### Autres changements
- Ajout d'un seed de développement pour permettre la connexion locale avec un compte prédéfini. [#563](https://github.com/betagouv/pitchou/issues/563)
- Configuration de `pgdata` en volume nommé dans Docker pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans le fichier Docker Compose. [#572](https://github.com/betagouv/pitchou/issues/572)
- Ajout de Prettier pour formater automatiquement le code et améliorer la cohérence. [#555](https://github.com/betagouv/pitchou/issues/555)
- Ajout de tests unitaires avec Vitest pour la fonction `manipulationStrings`. [#559](https://github.com/betagouv/pitchou/issues/559)
- Ajout d'un shell de développement Nix et de la configuration Direnv pour un environnement de développement reproductible. [#558](https://github.com/betagouv/pitchou/issues/558)
- Correction de l'utilisation de `knex` dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)
- Amélioration de la gestion des erreurs et des logs.
