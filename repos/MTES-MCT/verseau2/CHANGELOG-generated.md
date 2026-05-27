## Changelog : verseau2 (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives en termes de fonctionnalités d'export de données, de visualisation, et de gestion des bilans. Des corrections ont également été apportées pour améliorer la stabilité et la configuration de l'application, notamment en environnement de développement et de déploiement.

### Évolutions fonctionnelles
- Ajout d'un graphique pour visualiser les mesures [#88](https://github.com/MTES-MCT/verseau2/issues/88).
- Implémentation de l'export CSV pour les données [#82](https://github.com/MTES-MCT/verseau2/issues/82).
- Ajout de nouvelles colonnes au bilan, améliorant la richesse des données présentées [#72](https://github.com/MTES-MCT/verseau2/issues/72).
- Gestion des dates de début et de fin pour les bilans, avec un nouvel endpoint dédié aux paramètres [#84](https://github.com/MTES-MCT/verseau2/issues/84).
- Les rapports sont désormais envoyés même en cas d'erreur [#76](https://github.com/MTES-MCT/verseau2/issues/76).
- Correction du tri des résultats SQL [#89](https://github.com/MTES-MCT/verseau2/issues/89).
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement [#74](https://github.com/MTES-MCT/verseau2/issues/74).

### Évolutions techniques
- Ajout d'un service d'authentification mock avec gestion, facilitant les tests et le développement [#85](https://github.com/MTES-MCT/verseau2/issues/85).
- Ajout de la gestion CORS pour les déploiements frontend/backend [#83](https://github.com/MTES-MCT/verseau2/issues/83).
- Amélioration de la structure des types et des services dans le backend [#81](https://github.com/MTES-MCT/verseau2/issues/81).
- Refactoring des méthodes de détail dans `MasaProvider`.
- Amélioration de la gestion des requêtes pour les API REST MASA.
- Mise à jour de la dépendance `axios` vers la version 1.16 [#66](https://github.com/MTES-MCT/verseau2/issues/66).
- Configuration du serveur pour Docker.
- Ajout de la configuration pour le reverse proxy [#73](https://github.com/MTES-MCT/verseau2/issues/73).

### Autres changements
- Correction d'une erreur lors du déploiement de `sync-pg` [#87](https://github.com/MTES-MCT/verseau2/issues/87).
- Correction d'une erreur `ERR_PNPM_ABORTED_REMOVE_MODULES_DIR_NO_TTY` en environnement de développement [#6bf89b5](https://github.com/MTES-MCT/verseau2/commit/6bf89b5).
- Ajout de la configuration du gestionnaire de paquets et des moteurs [#179](https://github.com/MTES-MCT/verseau2/issues/179).
- Correction de la restauration de la base de données PostgreSQL en local [#86](https://github.com/MTES-MCT/verseau2/issues/86).
- Correction de l'URL de redirection Nginx [#80](https://github.com/MTES-MCT/verseau2/issues/80).
- Désactivation temporaire de la synchronisation de la base de données [#78](https://github.com/MTES-MCT/verseau2/issues/78).
- Fix des règles ESLint et gestion des erreurs [#75](https://github.com/MTES-MCT/verseau2/issues/75).
- Amélioration de la documentation et des commandes dans `AGENTS.md`.
- Correction du trim des adresses email dans les requêtes [#70](https://github.com/MTES-MCT/verseau2/issues/70).
- Correctif recette [#71](https://github.com/MTES-MCT/verseau2/issues/71).
