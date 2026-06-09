## Changelog : pitchou (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, Pitchou a connu une refonte technique majeure avec la migration vers de nouvelles technologies (SvelteKit, Vite, pnpm, Typescript) pour améliorer la performance, la sécurité et la maintenabilité du projet. Des corrections de bugs et des améliorations fonctionnelles ont également été apportées, notamment concernant la gestion des fichiers, la synchronisation des données et l'ajout d'espèces protégées à la liste.

### Évolutions fonctionnelles
- Ajout de *Cosentinia vellea* et du *grand capricorne* à la liste des espèces protégées. [#578](https://github.com/betagouv/pitchou/issues/578) [#577](https://github.com/betagouv/pitchou/issues/577)
- Ajout de domaines *indre-et-loire* et *guyane* pour l'authentification. [#579](https://github.com/betagouv/pitchou/issues/579)
- Affichage correct du fichier "espèces impactées" après la migration vers le stockage objet. [#590](https://github.com/betagouv/pitchou/issues/590)
- Correction d'une erreur 500 lors du téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/issues/587)
- Ajout d'un bandeau d'information sur l'environnement de *staging*. [#574](https://github.com/betagouv/pitchou/issues/574)
- Fusion de la page AARRI dans la page des statistiques. [#582](https://github.com/betagouv/pitchou/issues/582)
- Ajout de liens vers les pages statistiques et budget, ainsi que d'un bouton de changement de thème dans le footer. [#581](https://github.com/betagouv/pitchou/issues/581)
- Autorisation des routes d'écriture/suppression via CAP. [#565](https://github.com/betagouv/pitchou/issues/565)
- Ajout d'un seed de développement pour permettre la connexion locale. [#563](https://github.com/betagouv/pitchou/issues/563)

### Évolutions techniques
- Migration complète vers SvelteKit (SPA) en remplacement de Fastify. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration du build system de Rollup vers Vite. [#564](https://github.com/betagouv/pitchou/issues/564)
- Migration vers le gestionnaire de paquets pnpm. [#561](https://github.com/betagouv/pitchou/issues/561)
- Migration du code vers Typescript. [#568](https://github.com/betagouv/pitchou/issues/568) [#567](https://github.com/betagouv/pitchou/issues/567)
- Amélioration de la CI en utilisant `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Migration des fichiers vers Outscale Object Storage. [#573](https://github.com/betagouv/pitchou/issues/573)
- Amélioration de la sécurité : IV aléatoire pour le chiffrement, durcissement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560) [#557](https://github.com/betagouv/pitchou/issues/557)
- Utilisation de Knex passé en paramètre pour les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)

### Autres changements
- Ajout de tests unitaires avec Vitest pour la manipulation de chaînes de caractères. [#559](https://github.com/betagouv/pitchou/issues/559)
- Ajout d'un shell de développement Nix et de la configuration Direnv. [#558](https://github.com/betagouv/pitchou/issues/558)
- Application de Prettier pour améliorer la lisibilité du code. [#555](https://github.com/betagouv/pitchou/issues/555)
- Correction de bugs liés à la synchronisation des données (doublons de décisions administratives, rattachement des pièces jointes). [#584](https://github.com/betagouv/pitchou/issues/584) [#570](https://github.com/betagouv/pitchou/issues/570)
- Correction de l'affichage du header et du footer pour correspondre aux exigences du DSFR. [#583](https://github.com/betagouv/pitchou/issues/583)
- Correction d'un bug qui réinitialisait l'état "vu" des notifications lors de la resynchronisation. [#592](https://github.com/betagouv/pitchou/issues/592)
- Correction d'un bug dans le script de seed initial. [#575](https://github.com/betagouv/pitchou/issues/575)
- Configuration du volume `pgdata` pour éviter les problèmes de permissions sous Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans le fichier Docker Compose. [#572](https://github.com/betagouv/pitchou/issues/572)
