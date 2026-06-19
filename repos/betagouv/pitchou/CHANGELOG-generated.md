## Changelog : pitchou (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la performance, de la sécurité et de l'expérience utilisateur de Pitchou. Les principales évolutions incluent la migration des fichiers vers un nouvel hébergement (Outscale Object Storage), une refonte technique majeure vers SvelteKit et TypeScript, et des améliorations significatives des statistiques AARRI et de la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'un bouton pour télécharger les données utilisateurs pour les statistiques AARRI. [#596](https://github.com/betagouv/pitchou/issues/596)
- Amélioration de la section "évolution des indicateurs" dans les statistiques AARRI. [#597](https://github.com/betagouv/pitchou/issues/597)
- Ajout d'une page d'administration utilisateurs avec indication du niveau AARRI. [#591](https://github.com/betagouv/pitchou/issues/591)
- Migration de la liste des espèces protégées vers une table en base de données, améliorant la performance et la maintenabilité. [#589](https://github.com/betagouv/pitchou/issues/589)
- Correction des retours d'erreur et de la suppression de décisions. [#588](https://github.com/betagouv/pitchou/issues/588)
- Ajout de nouvelles espèces protégées à la liste (Cosentinia vellea, grand capricorne). [#578](https://github.com/betagouv/pitchou/issues/578)
- Ajout de domaines "indre-et-loire" et "guyane" pour l'authentification. [#579](https://github.com/betagouv/pitchou/issues/579)
- Ajout d'un bandeau d'information sur l'environnement de staging. [#574](https://github.com/betagouv/pitchou/issues/574)
- Correction d'un problème empêchant le téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/issues/587)
- Correction d'un bug qui réinitialisait l'état "vu" des notifications lors de la synchronisation. [#592](https://github.com/betagouv/pitchou/issues/592)
- Affichage correct du fichier espèces impactées après la migration vers l'object storage. [#590](https://github.com/betagouv/pitchou/issues/590)

### Évolutions techniques
- Migration complète vers SvelteKit (SPA) et suppression de Fastify, améliorant la performance et la structure du projet. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration vers TypeScript pour une meilleure maintenabilité et robustesse du code. [#568](https://github.com/betagouv/pitchou/issues/568) et [#567](https://github.com/betagouv/pitchou/issues/567)
- Migration des fichiers vers Outscale Object Storage pour une meilleure scalabilité et réduction des coûts. [#573](https://github.com/betagouv/pitchou/issues/573)
- Refonte du système de build avec l'utilisation de Vite au lieu de Rollup. [#564](https://github.com/betagouv/pitchou/issues/564)
- Passage à pnpm pour la gestion des dépendances. [#561](https://github.com/betagouv/pitchou/issues/561)
- Amélioration de la CI/CD avec l'utilisation de `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Amélioration de la sécurité : ajout d'un IV aléatoire pour le chiffrement et renforcement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560) et [#557](https://github.com/betagouv/pitchou/issues/557)
- Ajout de tests unitaires avec Vitest. [#559](https://github.com/betagouv/pitchou/issues/559)

### Autres changements
- Documentation sur le suivi des événements utilisateurs. [#586](https://github.com/betagouv/pitchou/issues/586)
- Amélioration de la conformité du header et footer aux standards DSFR. [#583](https://github.com/betagouv/pitchou/issues/583)
- Fusion de la page AARRI dans la page statistiques générale. [#582](https://github.com/betagouv/pitchou/issues/582)
- Ajout de liens vers les pages statistiques et budget dans le footer, ainsi qu'un bouton de changement de thème. [#581](https://github.com/betagouv/pitchou/issues/581)
- Correction du script de seed pour la base de données. [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout d'un seed de développement pour permettre la connexion locale. [#563](https://github.com/betagouv/pitchou/issues/563)
- Configuration du volume `pgdata` pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans le fichier docker-compose. [#572](https://github.com/betagouv/pitchou/issues/572)
- Ajout et application de Prettier pour le formatage du code. [#555](https://github.com/betagouv/pitchou/issues/555)
- Ajout d'un dev shell Nix et de la configuration Direnv. [#558](https://github.com/betagouv/pitchou/issues/558)
- Correction de l'utilisation du paramètre `knex` dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)
- Correction de la gestion des entreprises nulles lors de la synchronisation. [#569](https://github.com/betagouv/pitchou/issues/569)
- Rattachement des pièces jointes partagées entre les dossiers lors de la synchronisation. [#570](https://github.com/betagouv/pitchou/issues/570)
