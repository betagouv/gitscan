## Changelog : Docurba (30 derniers jours, au 31 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par une migration progressive des endpoints API vers Django pour améliorer la performance et la cohérence des données. Des améliorations ont également été apportées à la gestion des événements, des utilisateurs et des collectivité, ainsi que des corrections de bugs et des optimisations de performance. L'interface utilisateur a été améliorée avec la possibilité d'utiliser du markdown dans les descriptions et la gestion des liens externes.

### Évolutions fonctionnelles
- Possibilité d'utiliser du markdown dans les descriptions des événements et des procédures, avec support des liens externes [#47da726](https://github.com/MTES-MCT/Docurba/commit/47da726).
- Amélioration de l'affichage des collaborateurs (insensibilité à la casse) [#e68e8a7](https://github.com/MTES-MCT/Docurba/commit/e68e8a7).
- Migration des endpoints `/api/communes`, `/api/geo/communes`, `/api/geo/collectivites`, `/api/geo/intercommunalites` et `/api/projects/notify/shared` vers Django, améliorant ainsi la performance et la fiabilité [#fb08e75](https://github.com/MTES-MCT/Docurba/commit/fb08e75), [#f982096](https://github.com/MTES-MCT/Docurba/commit/f982096), [#3c3c42d](https://github.com/MTES-MCT/Docurba/commit/3c3c42d).
- Ajout des champs `archived_at` et `archived_by` au modèle Event pour gérer l'archivage [#b1613bc](https://github.com/MTES-MCT/Docurba/commit/b1613bc).
- Ajout des types d'événements PPLH et PPILH [#5917f55](https://github.com/MTES-MCT/Docurba/commit/5917f55).
- Ajout d'un modèle EventType et d'une configuration admin associée [#a3f28ef](https://github.com/MTES-MCT/Docurba/commit/a3f28ef).
- Ajout des champs `siren` et `code_insee` au modèle Collectivite [#d947e06](https://github.com/MTES-MCT/Docurba/commit/d947e06).
- Ajout d'un gestionnaire "Adhesion" [#ab5add6](https://github.com/MTES-MCT/Docurba/commit/ab5add6).

### Évolutions techniques
- Migration progressive vers Django pour l'API interne, incluant l'ajout de tests et l'optimisation des performances [#9aad97f](https://github.com/MTES-MCT/Docurba/commit/9aad97f), [#b941aca](https://github.com/MTES-MCT/Docurba/commit/b941aca).
- Refactoring de l'utilisation de l'API des collectivité dans le frontend, avec l'introduction d'un plugin dédié [#a0b94e9](https://github.com/MTES-MCT/Docurba/commit/a0b94e9).
- Ajout de Row Level Security (RLS) sur les modèles `core_eventtype`, `history_eventsnapshot` et `pghistory_context` pour améliorer la sécurité [#0d549a8](https://github.com/MTES-MCT/Docurba/commit/0d549a8).
- Utilisation de Syrupy pour les tests de l'API interne [#2b1215a](https://github.com/MTES-MCT/Docurba/commit/2b1215a).
- Mise à jour des dépendances : Django, ruff, syrupy, django-filter, django-datadog-logger, setuptools, pre-commit.
- Suppression des migrations "squashed" pour les utilisateurs [#4059b6b](https://github.com/MTES-MCT/Docurba/commit/4059b6b).
- Ajout d'une variable d'environnement `$ENABLE_MIGRATIONS` pour contrôler l'exécution des migrations [#ae15917](https://github.com/MTES-MCT/Docurba/commit/ae15917).
- Renommage du modèle `User` en `SupabaseUser` [#6e69dc3](https://github.com/MTES-MCT/Docurba/commit/6e69dc3).

### Autres changements
- Ajout d'un script CRON pour lier les événements aux types d'événements [#b9d4c3e](https://github.com/MTES-MCT/Docurba/commit/b9d4c3e).
- Correction du script `post_deploy` [#365d806](https://github.com/MTES-MCT/Docurba/commit/365d806).
- Mise à jour du fichier `event_types.json` [#50c58d5](https://github.com/MTES-MCT/Docurba/commit/50c58d5).
- Suppression de code inutilisé et nettoyage du code.
- Correction de bugs divers liés à l'affichage et au traitement des données.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour de la documentation.
- Correction de problèmes liés aux exports et aux tests.
- Amélioration de la performance des requêtes SQL.
- Suppression d'une ancienne vue matérialisée et ajout d'index pour la remplacer [#cca93c3](https://github.com/MTES-MCT/Docurba/commit/cca93c3).
