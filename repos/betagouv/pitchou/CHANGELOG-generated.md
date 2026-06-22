## Changelog : pitchou (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé d'importantes améliorations techniques pour moderniser l'architecture de Pitchou, notamment une migration vers un monorepo, l'adoption de nouvelles technologies comme SvelteKit et Vite, et le passage au stockage des fichiers sur Outscale Object Storage. Des améliorations fonctionnelles ont également été apportées, notamment pour le suivi des statistiques AARRI et la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'un bouton pour télécharger les événements utilisateurs pour les statistiques AARRI. [#590](https://github.com/betagouv/pitchou/pulls/590)
- Amélioration de la section évolution des indicateurs AARRI dans les statistiques. [#597](https://github.com/betagouv/pitchou/pulls/597)
- Ajout d'une page administrateur listant les utilisateurs avec leur niveau AARRI. [#591](https://github.com/betagouv/pitchou/pulls/591)
- Migration de la liste des espèces protégées vers une table en base de données. [#589](https://github.com/betagouv/pitchou/pulls/589)
- Ajout de *Cosentinia vellea* et du grand capricorne à la liste des espèces protégées. [#578](https://github.com/betagouv/pitchou/pulls/578)
- Ajout de domaines *indre-et-loire* et *guyane* pour l'authentification. [#579](https://github.com/betagouv/pitchou/pulls/579)
- Ajout d'une page d'erreur 404 personnalisée. [#596](https://github.com/betagouv/pitchou/pulls/596)
- Suppression des liens vers les démarches numériques dans les avis d'expert. [#5554cde](https://github.com/betagouv/pitchou/commit/5554cde)

### Évolutions techniques
- Refactorisation du dépôt en monorepo. [#593](https://github.com/betagouv/pitchou/pulls/593) et [#595](https://github.com/betagouv/pitchou/pulls/595)
- Migration des fichiers vers Outscale Object Storage. [#573](https://github.com/betagouv/pitchou/pulls/573)
- Migration de Svelte vers SvelteKit (SPA) et suppression de Fastify. [#566](https://github.com/betagouv/pitchou/pulls/566)
- Migration de Rollup vers Vite pour l'optimisation du build. [#564](https://github.com/betagouv/pitchou/pulls/564)
- Passage à pnpm pour la gestion des dépendances. [#561](https://github.com/betagouv/pitchou/pulls/561)
- Migration progressive vers TypeScript. [#568](https://github.com/betagouv/pitchou/pulls/568) et [#567](https://github.com/betagouv/pitchou/pulls/567)
- Amélioration de la CI en utilisant just en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/pulls/562)

### Autres changements
- Correction du format du fichier CSV téléchargé pour les statistiques AARRI. [#dc5b93c](https://github.com/betagouv/pitchou/commit/dc5b93c)
- Renommage des "évènements traqués" en "événements suivis" dans la documentation. [#9b70848](https://github.com/betagouv/pitchou/commit/9b70848)
- Création d'une documentation expliquant le suivi des interactions utilisateurs. [#586](https://github.com/betagouv/pitchou/pulls/586)
- Correction d'un problème empêchant le reset de l'état "vu" des notifications lors de la synchronisation. [#592](https://github.com/betagouv/pitchou/pulls/592)
- Correction de l'affichage du fichier des espèces impactées après la migration vers le stockage objet. [#590](https://github.com/betagouv/pitchou/pulls/590)
- Correction d'une erreur 500 lors du téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/pulls/587)
- Correction des retours d'erreur et de la suppression de décisions. [#588](https://github.com/betagouv/pitchou/pulls/588)
- Correction d'un problème de doublons de décisions administratives lors de la synchronisation. [#584](https://github.com/betagouv/pitchou/pulls/584)
- Ajustement de la mise en page de l'en-tête et du pied de page pour respecter les exigences du DSFR. [#583](https://github.com/betagouv/pitchou/pulls/583)
- Fusion de la page AARRI dans la page des statistiques. [#582](https://github.com/betagouv/pitchou/pulls/582)
- Ajout de liens vers les pages des statistiques, du budget et du bouton de thème dans le pied de page. [#581](https://github.com/betagouv/pitchou/pulls/581)
- Ajout d'un seed de développement pour permettre la connexion locale. [#563](https://github.com/betagouv/pitchou/pulls/563)
- Configuration du volume nommé pgdata dans Docker pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/pulls/571)
- Suppression du service tooling dans Docker. [#572](https://github.com/betagouv/pitchou/pulls/572)
- Ajout d'un bandeau sur l'environnement de staging. [#574](https://github.com/betagouv/pitchou/pulls/574)
- Correction de la gestion des entreprises nulles lors de la synchronisation. [#569](https://github.com/betagouv/pitchou/pulls/569)
- Correction du rattachement des pièces jointes pétitionnaire partagées entre les dossiers. [#570](https://github.com/betagouv/pitchou/pulls/570)
- Amélioration de la sécurité en utilisant un IV aléatoire pour le chiffrement. [#560](https://github.com/betagouv/pitchou/pulls/560)
- Correction d'un problème de seed. [#575](https://github.com/betagouv/pitchou/pulls/575)
