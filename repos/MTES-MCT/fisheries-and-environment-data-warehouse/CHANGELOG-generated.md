## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 15 avril 2026)

### Résumé
Ce changelog fait le point sur les améliorations apportées à l'entrepôt de données dédié aux pêches et à l'environnement marin. Les récentes mises à jour se concentrent sur l'ajout de nouvelles données (références réglementaires, missions interservices, COE/COX), la correction de bugs liés à la géométrie et aux conflits d'exécution des tâches, ainsi que des ajustements de l'infrastructure et des dépendances.

### Évolutions fonctionnelles
- Ajout de références réglementaires aux données [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Intégration de données relatives aux missions interservices dans les exports de patrouille [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186).
- Ajout des champs mois et année aux données de patrouille [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186).
- Ajout des données COE (Comité des pêches et des élevages) et COX (Conseil des pêches et des élevages) [#178](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/178).
- Ajout d'un champ "statut" à la table des activités [#188](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/188).

### Évolutions techniques
- Correction d'un bug lié au type de géométrie [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Résolution des conflits d'exécution des tâches (flows Prefect) [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Mise à jour de la version de Trivy (outil d'analyse de vulnérabilités) [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186).
- Désactivation temporaire du workflow Trivy.
- Ajout de messages DEP (Data Engineering Pipeline) pour faciliter le suivi des processus.

### Autres changements
- Mise à jour du fichier `.trivyignore` pour ignorer certains éléments lors de l'analyse de vulnérabilités.
- Intégration des dernières modifications du dépôt principal (gitlab-sml.din.developpement-durable.gouv.fr).
- Rétractation temporaire de la fusion de la pull request #191 en raison d'un bug corrigé par la suite.
