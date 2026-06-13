## Changelog : pitchou (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé une refonte technique majeure de l'application, passant de Fastify et Rollup à SvelteKit et Vite, et adoptant pnpm comme gestionnaire de paquets.  Ces changements visent à améliorer la performance, la maintenabilité et l'expérience de développement. Des corrections de bugs et des améliorations fonctionnelles ont également été apportées, notamment concernant la gestion des fichiers, la synchronisation des données et l'ajout d'espèces protégées à la liste.

### Évolutions fonctionnelles
- Ajout de *Cosentinia vellea* et du *grand capricorne* à la liste des espèces protégées. [#578](https://github.com/betagouv/pitchou/issues/578) [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout de domaines *indre-et-loire* et *guyane* pour l'authentification. [#579](https://github.com/betagouv/pitchou/issues/579)
- Correction de l'affichage des fichiers espèces impactées après la migration vers le stockage objet. [#590](https://github.com/betagouv/pitchou/issues/590)
- Correction d'une erreur 500 lors du téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/issues/587)
- Ajout d'un bandeau d'information sur l'environnement de *staging*. [#574](https://github.com/betagouv/pitchou/issues/574)
- Fusion de la page *aarri* dans la page des statistiques. [#582](https://github.com/betagouv/pitchou/issues/582)
- Ajout de liens vers les pages statistiques et budget, ainsi que d'un bouton de changement de thème dans le pied de page. [#581](https://github.com/betagouv/pitchou/issues/581)
- Autorisation des routes d'écriture et de suppression via CAP. [#565](https://github.com/betagouv/pitchou/issues/565)
- Correction pour éviter de réinitialiser l'état "vu" des notifications lors de la resynchronisation. [#592](https://github.com/betagouv/pitchou/issues/592)
- Correction pour éviter les décisions administratives en double lors de la synchronisation. [#584](https://github.com/betagouv/pitchou/issues/584)
- Correction pour rattacher les pièces jointes du pétitionnaire partagées entre les dossiers. [#570](https://github.com/betagouv/pitchou/issues/570)
- Correction pour gérer le cas où l'entreprise est nulle lors de la synchronisation. [#569](https://github.com/betagouv/pitchou/issues/569)

### Évolutions techniques
- Refonte de l'application avec migration vers SvelteKit (SPA) et suppression de Fastify. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration du système de build de Rollup vers Vite. [#564](https://github.com/betagouv/pitchou/issues/564)
- Adoption de pnpm comme gestionnaire de paquets. [#561](https://github.com/betagouv/pitchou/issues/561)
- Migration du code vers TypeScript. [#568](https://github.com/betagouv/pitchou/issues/568) [#567](https://github.com/betagouv/pitchou/issues/567)
- Migration des fichiers vers Outscale Object Storage. [#573](https://github.com/betagouv/pitchou/issues/573)
- Amélioration de la CI en utilisant `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Amélioration de la sécurité : IV aléatoire pour le chiffrement et durcissement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560) [#557](https://github.com/betagouv/pitchou/issues/557)
- Ajout de tests unitaires avec Vitest. [#559](https://github.com/betagouv/pitchou/issues/559)
- Configuration de `prettier` pour améliorer la lisibilité du code. [#555](https://github.com/betagouv/pitchou/issues/555)
- Utilisation de volumes nommés pour `pgdata` dans Docker pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans Docker. [#572](https://github.com/betagouv/pitchou/issues/572)
- Correction de l'utilisation de `knex` dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)

### Autres changements
- Renommage des "évènements traqués" en "évènements suivis" dans la documentation.
- Création d'une documentation expliquant le suivi des interactions utilisateurs. [#586](https://github.com/betagouv/pitchou/issues/586)
- Mise à jour de la mise en page de l'en-tête et du pied de page pour respecter les exigences du DSFR. [#583](https://github.com/betagouv/pitchou/issues/583)
- Ajout d'un shell de développement Nix et de la configuration Direnv. [#558](https://github.com/betagouv/pitchou/issues/558)
