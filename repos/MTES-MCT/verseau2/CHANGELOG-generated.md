## Changelog : verseau2 (30 derniers jours, au 21 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'application Verseau2, notamment l'ajout de nouvelles fonctionnalités d'export de données, la gestion des bilans et des dates, ainsi que des corrections pour améliorer la stabilité et la configuration de l'application en environnement de production. Des efforts ont également été faits pour améliorer la qualité du code et la documentation.

### Évolutions fonctionnelles
- Ajout de l'export CSV pour les données de l'application. [#82](https://github.com/MTES-MCT/verseau2/issues/82)
- Ajout de nouvelles colonnes au bilan. [#72](https://github.com/MTES-MCT/verseau2/issues/72)
- Ajout de la gestion des dates de début et de fin pour les bilans, avec un nouvel endpoint pour les paramètres. [#84](https://github.com/MTES-MCT/verseau2/issues/84)
- Les rapports sont désormais envoyés même en cas d'erreur. [#76](https://github.com/MTES-MCT/verseau2/issues/76)
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement. [#74](https://github.com/MTES-MCT/verseau2/issues/74)
- Ajout d'un service d'authentification mock avec gestion. [#85](https://github.com/MTES-MCT/verseau2/issues/85)
- Correction d'un bug où les adresses email étaient incorrectement traitées. [#70](https://github.com/MTES-MCT/verseau2/issues/70)
- Correction d'un correctif recette. [#71](https://github.com/MTES-MCT/verseau2/issues/71)

### Évolutions techniques
- Ajout de la gestion CORS pour les déploiements frontend/backend. [#83](https://github.com/MTES-MCT/verseau2/issues/83)
- Amélioration de la structure des types et des interfaces dans le backend. [#81](https://github.com/MTES-MCT/verseau2/issues/81)
- Mise à jour de la dépendance Axios vers la version 1.16. [#66](https://github.com/MTES-MCT/verseau2/issues/66)
- Amélioration de la gestion des requêtes pour les API REST MASA.
- Ajout de path manquants pour les API REST MASA.
- Fix des règles ESLint et gestion des erreurs dans le backend. [#75](https://github.com/MTES-MCT/verseau2/issues/75)
- Amélioration de la documentation et des commandes dans le fichier AGENTS.md.
- Ajout de la configuration pour le reverse proxy. [#73](https://github.com/MTES-MCT/verseau2/issues/73)

### Autres changements
- Correction d'une erreur lors du déploiement de sync-pg. [#87](https://github.com/MTES-MCT/verseau2/issues/87)
- Correction d'une erreur ERR_PNPM_ABORTED_REMOVE_MODULES_DIR_NO_TTY.
- Ajout de la configuration du gestionnaire de paquets et des moteurs. [#179](https://github.com/MTES-MCT/verseau2/issues/179)
- Restauration de la base de données corrigée en local. [#86](https://github.com/MTES-MCT/verseau2/issues/86)
- Correction de la redirection de l'URL https://www.saineau.beta.gouv.fr/verseau. [#80](https://github.com/MTES-MCT/verseau2/issues/80)
- Désactivation temporaire de la synchronisation de la base de données. [#78](https://github.com/MTES-MCT/verseau2/issues/78)
- Ajout de la configuration du serveur pour Docker.
