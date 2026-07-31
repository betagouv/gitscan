## Changelog : Docurba (30 derniers jours, au 30 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par une migration progressive de l'API vers Django pour améliorer la performance et la cohérence des données. Des améliorations ont également été apportées à la gestion des événements, des collectivités et des utilisateurs, ainsi que des corrections de bugs et des optimisations de sécurité. L'interface utilisateur a été améliorée avec la prise en charge du markdown pour les descriptions et la gestion des liens.

### Évolutions fonctionnelles
- Ajout de la possibilité d'utiliser le markdown dans les descriptions des procédures et des événements, avec support des liens externes. [#f8c91f3](https://github.com/MTES-MCT/Docurba/commit/f8c91f3)
- Amélioration de l'affichage des collaborateurs, insensible à la casse. [#e68e8a7](https://github.com/MTES-MCT/Docurba/commit/e68e8a7)
- Correction de l'export des communes, assurant la gestion correcte des listes de codes SIREN longues. [#8104fc2](https://github.com/MTES-MCT/Docurba/commit/8104fc2)
- Ajout des types d'événements PPLH et PPILH. [#5917f55](https://github.com/MTES-MCT/Docurba/commit/5917f55)
- Ajout de la gestion des utilisateurs avec un modèle `User` associé à un profil. [#de55e2e](https://github.com/MTES-MCT/Docurba/commit/de55e2e), [#b496f50](https://github.com/MTES-MCT/Docurba/commit/b496f50)
- Ajout du SIREN aux collectivités via l'API interne Django. [#d947e06](https://github.com/MTES-MCT/Docurba/commit/d947e06)
- Ajout de la gestion des groupes et membres pour les collectivités via l'API interne Django. [#91ee156](https://github.com/MTES-MCT/Docurba/commit/91ee156)

### Évolutions techniques
- Migration progressive des endpoints `/api/communes`, `/api/geo/communes`, `/api/geo/collectivites`, `/api/geo/intercommunalites` et `/api/projects/notify/shared` vers Django pour une meilleure performance et maintenance. [#fb08e75](https://github.com/MTES-MCT/Docurba/commit/fb08e75), [#f982096](https://github.com/MTES-MCT/Docurba/commit/f982096), [#f2dea1b](https://github.com/MTES-MCT/Docurba/commit/f2dea1b), [#d687eba](https://github.com/MTES-MCT/Docurba/commit/d687eba), [#3c3c42d](https://github.com/MTES-MCT/Docurba/commit/3c3c42d)
- Refactoring de l'utilisation de l'API des collectivités pour utiliser un plugin dédié. [#a0b94e9](https://github.com/MTES-MCT/Docurba/commit/a0b94e9), [#d4eee06](https://github.com/MTES-MCT/Docurba/commit/d4eee06), [#1556ee2](https://github.com/MTES-MCT/Docurba/commit/1556ee2)
- Ajout de Row Level Security (RLS) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context` pour renforcer la sécurité. [#0d549a8](https://github.com/MTES-MCT/Docurba/commit/0d549a8)
- Mise à jour de l'infrastructure pour utiliser Node.js v26. [#0f3d354](https://github.com/MTES-MCT/Docurba/commit/0f3d354)
- Ajout d'un mécanisme pour activer/désactiver les migrations via la variable d'environnement `$ENABLE_MIGRATIONS`. [#ae15917](https://github.com/MTES-MCT/Docurba/commit/ae15917)
- Amélioration des tests Django avec l'ajout de Syrupy et l'utilisation de snapshots. [#358667b](https://github.com/MTES-MCT/Docurba/commit/358667b), [#2e3d1c5](https://github.com/MTES-MCT/Docurba/commit/2e3d1c5), [#b8962ee](https://github.com/MTES-MCT/Docurba/commit/b8962ee)
- Correction de plusieurs problèmes de performance et de N+1 queries dans l'API Django. [#952a9e5](https://github.com/MTES-MCT/Docurba/commit/952a9e5), [#b8fb698](https://github.com/MTES-MCT/Docurba/commit/b8fb698)

### Autres changements
- Ajout d'un script CRON pour lier les événements aux types d'événements. [#b9d4c3e](https://github.com/MTES-MCT/Docurba/commit/b9d4c3e)
- Correction du script de déploiement. [#365d806](https://github.com/MTES-MCT/Docurba/commit/365d806)
- Mise à jour des types d'événements. [#50c58d5](https://github.com/MTES-MCT/Docurba/commit/50c58d5), [#1a5c06a](https://github.com/MTES-MCT/Docurba/commit/1a5c06a)
- Suppression des migrations écrasées pour les utilisateurs. [#4059b6b](https://github.com/MTES-MCT/Docurba/commit/4059b6b)
- Suppression des fichiers de configuration Django du dépôt. [#b8962ee](https://github.com/MTES-MCT/Docurba/commit/b8962ee)
- Ajout du modèle `EventType` et de sa configuration dans l'admin Django. [#a3f28ef](https://github.com/MTES-MCT/Docurba/commit/a3f28ef), [#e95e270](https://github.com/MTES-MCT/Docurba/commit/e95e270), [#b962e35](https://github.com/MTES-MCT/Docurba/commit/b962e35)
