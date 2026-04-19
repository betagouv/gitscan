## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'enrichissement des données avec l'ajout de références réglementaires et de données sur les activités de contrôle des pêches (patrols). Des corrections de bugs et des améliorations de la robustesse des pipelines ont également été apportées.

### Évolutions fonctionnelles
- Ajout de références réglementaires aux données, améliorant la traçabilité et le contexte des informations. [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191)
- Intégration de données relatives aux missions interservices de contrôle des pêches. [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186)
- Ajout des champs "mois" et "année" aux données de patrols. [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186)
- Ajout d'un champ "statut" à la table des activités. [#178](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/178)
- Ajout des données COE et COX. [#178](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/178)

### Évolutions techniques
- Correction d'un bug lié au type de géométrie. [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189)
- Résolution de conflits potentiels dans la planification des exécutions des pipelines. [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189)
- Mise à jour de la version de Trivy (outil d'analyse de vulnérabilités).
- Ajout de messages DEP (Data Engineering Pipeline) pour améliorer la traçabilité. [#188](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/188)
- Suppression temporaire du workflow Trivy en raison de problèmes.
- Correction d'un bug sur les réglementations H3.

### Autres changements
- Mise à jour du fichier `.trivyignore`.
- Intégration des dernières modifications du dépôt amont (gitlab-sml.din.developpement-durable.gouv.fr).
