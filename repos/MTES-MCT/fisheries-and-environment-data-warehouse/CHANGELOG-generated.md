## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'entrepôt de données au cours du dernier mois. Les modifications se concentrent principalement sur l'ajout de nouveaux indicateurs et l'optimisation des requêtes liées aux missions de surveillance, améliorant ainsi la capacité à analyser les données de pêche et d'environnement marin. Des corrections et des refactorisations ont également été effectuées pour améliorer la qualité et la performance du système.

### Évolutions fonctionnelles
- Ajout de nouveaux indicateurs liés aux missions PAM (surveillance des activités de pêche) : nombre de cibles contrôlées, heures de surveillance.
- Ajout du nombre de navires reconnus.
- Ajout d'une gestion des dates nulles pour éviter les erreurs de chargement de données.
- Ajout d'une exception pour améliorer la robustesse du système [#206](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/206).
- Correction d'une colonne dans les données de patrouille [#198](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/198).
- Correction d'une erreur dans les requêtes de missions [#194](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/194).

### Évolutions techniques
- Optimisation des requêtes pour l'API de patrouille afin de ne requêter que les missions PAM pertinentes [#201](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/201).
- Refactorisation de la clause FROM dans la requête des missions pour améliorer la lisibilité et la maintenance [#194](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/194).
- Correction d'une virgule manquante dans le DDL [#203](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/203).

### Autres changements
- Mise à jour de la version pour le déploiement [#196](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/196).
