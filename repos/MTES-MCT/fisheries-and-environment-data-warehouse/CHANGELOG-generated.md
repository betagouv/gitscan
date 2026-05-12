## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 11 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'entrepôt de données dédié aux pêches et à l'environnement marin au cours du dernier mois. Les principales évolutions concernent l'ajout de nouveaux indicateurs de surveillance, des corrections de requêtes et des améliorations de la gestion des données, notamment pour les missions de patrouille et les données PAM (Plateforme d'Acquisition de données Marine).

### Évolutions fonctionnelles
- Ajout d'indicateurs relatifs aux missions PAM (Plateforme d'Acquisition de données Marine) [#202](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/202).
- Ajout d'un indicateur comptant le nombre de navires reconnus [#204](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/204).
- Ajout d'heures de surveillance [#201](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/201).
- Ajout de données relatives aux excp [#199](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/199).
- Ajout de références réglementaires [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Amélioration des données de patrouille [#198](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/198) et [#193](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/193).
- Ajout de données PAM [#190](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/190).

### Évolutions techniques
- Optimisation des requêtes pour l'API de patrouille, ne requérant que les missions PAM nécessaires [#200](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/200).
- Correction de la clause FROM dans la requête des missions [#194](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/194).
- Correction d'un bug lié au type de géométrie [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Gestion des dates nulles et saut de chargement si les données sont vides [#200](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/200).
- Correction d'un bug sur regulations_h3 [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Rétractation d'une précédente fusion pour correction [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).

### Autres changements
- Mise à jour de la version pour le déploiement [#196](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/196).
- Correction d'une faute de frappe dans le nom d'une colonne [#203](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/203).
