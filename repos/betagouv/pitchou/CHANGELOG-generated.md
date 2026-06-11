## Changelog : pitchou (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, Pitchou a connu une refonte technique majeure avec la migration vers de nouvelles technologies (SvelteKit, Vite, pnpm, Typescript) pour améliorer la performance, la sécurité et la maintenabilité de la plateforme. Des améliorations significatives ont également été apportées au stockage des fichiers, à la synchronisation des données et à l'interface utilisateur, notamment avec l'ajout de nouvelles statistiques et de liens utiles.

### Évolutions fonctionnelles
- Ajout de nouvelles espèces protégées à la liste CNPN : *Cosentinia vellea* et le grand capricorne. [#578](https://github.com/betagouv/pitchou/issues/578) [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout de domaines autorisés pour l'authentification : Indre-et-Loire et Guyane. [#579](https://github.com/betagouv/pitchou/issues/579)
- Affichage correct du fichier "espèces impactées" après la migration vers le nouveau stockage. [#590](https://github.com/betagouv/pitchou/issues/590)
- Correction d'une erreur 500 lors du téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/issues/587)
- Ajout d'un bandeau d'information sur l'environnement de staging. [#574](https://github.com/betagouv/pitchou/issues/574)
- Ajout de liens vers les statistiques, le budget et le bouton de thème dans le footer. [#581](https://github.com/betagouv/pitchou/issues/581)
- Fusion de la page aarri dans la page des statistiques. [#582](https://github.com/betagouv/pitchou/issues/582)
- Correction d'un bug qui réinitialisait l'état "vu" des notifications lors de la resynchronisation. [#592](https://github.com/betagouv/pitchou/issues/592)
- Correction pour éviter les décisions administratives en double lors de la synchronisation. [#584](https://github.com/betagouv/pitchou/issues/584)
- Correction pour rattacher les pièces jointes aux dossiers lors de la synchronisation. [#570](https://github.com/betagouv/pitchou/issues/570)

### Évolutions techniques
- Migration complète vers SvelteKit (SPA) en remplacement de Fastify. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration du build system de Rollup vers Vite. [#564](https://github.com/betagouv/pitchou/issues/564)
- Migration vers TypeScript pour une meilleure typage et maintenabilité du code. [#568](https://github.com/betagouv/pitchou/issues/568) [#567](https://github.com/betagouv/pitchou/issues/567)
- Passage à pnpm comme gestionnaire de paquets. [#561](https://github.com/betagouv/pitchou/issues/561)
- Migration des fichiers vers Outscale Object Storage. [#573](https://github.com/betagouv/pitchou/issues/573)
- Amélioration de la CI avec l'utilisation de `just` en local et dans les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Renforcement de la sécurité avec un IV aléatoire pour le chiffrement et durcissement de la connexion et du code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560) [#557](https://github.com/betagouv/pitchou/issues/557)
- Utilisation de volumes nommés pour `pgdata` dans Docker pour éviter les problèmes de permissions. [#571](https://github.com/betagouv/pitchou/issues/571)

### Autres changements
- Documentation sur le suivi des interactions utilisateurs ajoutée. [#586](https://github.com/betagouv/pitchou/issues/586)
- Correction de la documentation pour renommer "évènements traqués" en "événements suivis". [#586](https://github.com/betagouv/pitchou/issues/586)
- Ajout de tests unitaires avec Vitest pour la manipulation de chaînes de caractères. [#559](https://github.com/betagouv/pitchou/issues/559)
- Ajout d'un shell de développement Nix et de la configuration Direnv. [#558](https://github.com/betagouv/pitchou/issues/558)
- Application de Prettier pour améliorer la cohérence du code. [#555](https://github.com/betagouv/pitchou/issues/555)
- Suppression du service tooling dans le fichier docker-compose. [#572](https://github.com/betagouv/pitchou/issues/572)
- Correction de l'utilisation de `knex` dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)
- Mise à jour du header et du footer pour respecter les exigences de la DSFR. [#583](https://github.com/betagouv/pitchou/issues/583)
