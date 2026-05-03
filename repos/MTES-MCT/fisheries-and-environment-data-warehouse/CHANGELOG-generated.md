## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données et la correction de bugs liés aux requêtes et aux références réglementaires. Des ajustements ont été apportés aux données de patrouille et aux missions, ainsi qu'à la gestion des conflits d'exécution des tâches planifiées.

### Évolutions fonctionnelles
- Correction d'un bug dans les données de réglementations h3 [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Amélioration des données de patrouille [#193](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/193).
- Ajout de données relatives aux Plans d'Action Maritime (PAM) [#192](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/192).

### Évolutions techniques
- Refactorisation de la clause `FROM` dans les requêtes relatives aux missions [#194](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/194).
- Résolution de conflits d'exécution des tâches planifiées pour éviter les chevauchements [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Correction d'un bug lié au type de géométrie [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Ajout de dépendances (DEP messages) [#188](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/188).

### Autres changements
- Préparation pour le déploiement (bump de version) [#196](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/196).
- Revert d'une modification précédente concernant l'ajout de références réglementaires en raison d'un problème rencontré [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
