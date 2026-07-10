## Changelog : fondation (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'architecture frontale avec une migration vers une approche "feature-first", des corrections de bugs et des améliorations de l'expérience utilisateur, notamment concernant la gestion des fichiers et des rapports officiels. Des mises à jour de sécurité et de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la sélection de fichiers désactivés dans l'interface. [#466](https://github.com/betagouv/fondation/issues/466)
- Amélioration de la gestion des fichiers dans les rapports officiels : suppression des fichiers sans issue et modification de l'introduction des fichiers suspendus. [#462](https://github.com/betagouv/fondation/issues/462), [#463](https://github.com/betagouv/fondation/issues/463)
- Possibilité d'attacher des fichiers à une nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Amélioration de l'affichage des commentaires dans les fichiers de nomination. [#408](https://github.com/betagouv/fondation/issues/408)
- Remplacement du modal "magistrat" par un panneau latéral pour une meilleure expérience utilisateur. [#439](https://github.com/betagouv/fondation/issues/439)
- Correction d'un bug lié au titre du président dans l'introduction. [#465](https://github.com/betagouv/fondation/issues/465)
- Correction de l'affichage des agendas dans les rapports officiels. [#478](https://github.com/betagouv/fondation/issues/478)
- Correction d'un problème de synchronisation des données des rapports officiels. [#402](https://github.com/betagouv/fondation/issues/402)
- Correction de l'affichage du nom de l'agenda dans le sélecteur de rapports officiels. [#401](https://github.com/betagouv/fondation/issues/401)
- Cas particulier géré pour CC PARIS. [#450](https://github.com/betagouv/fondation/issues/450)

### Évolutions techniques
- Migration des tests E2E de l'API vers un package dédié. [#441](https://github.com/betagouv/fondation/issues/441)
- Migration vers Vitest pour les tests unitaires. [#437](https://github.com/betagouv/fondation/issues/437)
- Refactoring important de l'architecture frontale vers une approche "feature-first" pour une meilleure organisation et maintenabilité du code. [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433), [#428](https://github.com/betagouv/fondation/issues/428), [#431](https://github.com/betagouv/fondation/issues/431), [#430](https://github.com/betagouv/fondation/issues/430), [#429](https://github.com/betagouv/fondation/issues/429), [#427](https://github.com/betagouv/fondation/issues/427)
- Ajout de "index barrels" pour une meilleure organisation des imports dans le code partagé. [#440](https://github.com/betagouv/fondation/issues/440)
- Mise à jour de plusieurs dépendances, incluant des correctifs de sécurité pour `piscina`, `react-router` et `vite`. [#435](https://github.com/betagouv/fondation/issues/435), [#423](https://github.com/betagouv/fondation/issues/423), [#422](https://github.com/betagouv/fondation/issues/422)
- Suppression de dépendances inutilisées. [#456](https://github.com/betagouv/fondation/issues/456)
- Mise à jour de NestJS. [#452](https://github.com/betagouv/fondation/issues/452)
- Mise à jour de S3. [#454](https://github.com/betagouv/fondation/issues/454)
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Remplacement de l'espacement Tailwind par l'espacement DSFR.
- Ajout d'un test d'acceptation pour la documentation. [#399](https://github.com/betagouv/fondation/issues/399)

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) pour l'architecture "feature-first" du frontend. [#434](https://github.com/betagouv/fondation/issues/434)
- Mise à jour de la structure des composants partagés. [#412](https://github.com/betagouv/fondation/issues/412)
- Suppression des migrations inutiles. [#443](https://github.com/betagouv/fondation/issues/443)
- Ajout d'un composant `NewTable` virtualisé pour l'affichage de tableaux de données. [#442](https://github.com/betagouv/fondation/issues/442)
- Déplacement des colonnes de transparence vers une table spécifique. [#445](https://github.com/betagouv/fondation/issues/445)
- Correction de l'indexation `archivedAt` dans le schéma de session. [#415](https://github.com/betagouv/fondation/issues/415)
- Autorisation de positions actuelles de nomination inconnues. [#416](https://github.com/betagouv/fondation/issues/416)
- Configuration de l'outil de formatage `oxfmt` dans VSCode. [#406](https://github.com/betagouv/fondation/issues/406)
