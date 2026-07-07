## Changelog : fondation (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des agendas et des fichiers, ainsi que sur des refactorings importants pour moderniser l'architecture du projet et améliorer sa maintenabilité. Des corrections de bugs et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Correction de l'affichage et du fonctionnement de la sélection des fichiers d'agenda. [#451](https://github.com/betagouv/fondation/issues/451)
- Amélioration de la gestion des fichiers liés aux nominations, avec la possibilité de joindre des fichiers. [#407](https://github.com/betagouv/fondation/issues/407)
- Correction de l'affichage des noms d'agenda dans la liste des plans. [#391](https://github.com/betagouv/fondation/issues/391)
- Correction du comportement de l'importation Lolfi, notamment pour la mise à jour des identifiants de fichiers. [#417](https://github.com/betagouv/fondation/issues/417)
- Amélioration de la synchronisation des données des rapports officiels. [#402](https://github.com/betagouv/fondation/issues/402)
- Correction de l'affichage des fichiers suspendus dans les rapports officiels. [#396](https://github.com/betagouv/fondation/issues/396)
- Ajout d'une gestion spécifique pour les cas particuliers de "CC PARIS". [#400](https://github.com/betagouv/fondation/issues/400)
- Ajout d'un indicateur de commentaire pour les fichiers de nomination. [#408](https://github.com/betagouv/fondation/issues/408)
- Ajout d'un panneau latéral pour remplacer la modale magistrat. [#439](https://github.com/betagouv/fondation/issues/439)
- Amélioration de la gestion des positions actuelles des nominations. [#416](https://github.com/betagouv/fondation/issues/416)

### Évolutions techniques
- Migration des tests vers Vitest pour améliorer la performance et la maintenabilité. [#437](https://github.com/betagouv/fondation/issues/437)
- Refactoring important de l'architecture front-end vers une approche "feature-first" pour une meilleure organisation du code et une plus grande modularité. [#434](https://github.com/betagouv/fondation/issues/434)
- Déplacement des tests E2E de l'API vers un package dédié. [#441](https://github.com/betagouv/fondation/issues/441)
- Suppression des dépendances inutilisées. [#456](https://github.com/betagouv/fondation/issues/456)
- Mise à jour de plusieurs dépendances, incluant des correctifs de sécurité pour `piscina` et `react-router`. [#435](https://github.com/betagouv/fondation/issues/435), [#423](https://github.com/betagouv/fondation/issues/423)
- Utilisation de tokens de couleurs DSFR au lieu de couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Refactoring pour utiliser l'ingestion Lolfi pour les données de test. [#398](https://github.com/betagouv/fondation/issues/398)
- Suppression de la migration conditionnelle. [#410](https://github.com/betagouv/fondation/issues/410)

### Autres changements
- Documentation : Ajout d'un ADR pour l'architecture front-end "feature-first". [#434](https://github.com/betagouv/fondation/issues/434)
- Amélioration de la configuration de Renovate pour éviter les problèmes de mémoire. [#420](https://github.com/betagouv/fondation/issues/420)
- Mise à jour de la documentation README. [#392](https://github.com/betagouv/fondation/issues/392)
- Ajout d'une proposition de structure pour les composants partagés. [#412](https://github.com/betagouv/fondation/issues/412)
- Mise à jour des dépendances et épinglage des versions pour plus de stabilité. [#424](https://github.com/betagouv/fondation/issues/424)
- Ajout de la gestion des priorités automatiques. [#414](https://github.com/betagouv/fondation/issues/414)
- Déplacement des colonnes de transparence vers une table spécifique. [#445](https://github.com/betagouv/fondation/issues/445)
- Suppression de l'utilisation de dsft avec des unités. [#403](https://github.com/betagouv/fondation/issues/403)
- Correction du wording du badge de documentation. [#389](https://github.com/betagouv/fondation/issues/389)
- Ajout d'un bouton JDMA conditionné au rôle de l'utilisateur. [#388](https://github.com/betagouv/fondation/issues/388)
- Correction de la configuration du préfixe de commit Renovate. [#393](https://github.com/betagouv/fondation/issues/393)
