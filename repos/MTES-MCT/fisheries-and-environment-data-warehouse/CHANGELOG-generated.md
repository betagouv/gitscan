## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration et de la qualité des données, notamment concernant les missions interservices, les patrouilles et les références réglementaires. Des corrections de bugs et des ajustements ont été apportés pour assurer la fiabilité des données et des pipelines.

### Évolutions fonctionnelles
- Ajout de la prise en charge des missions interservices [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186).
- Ajout des mois et années aux données [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186).
- Ajout d'un champ "statut" à la table des activités [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Ajout des références réglementaires aux données [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Amélioration des données de patrouille (maj et redémarrage des exports) [#186](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/186), [#193](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/193).
- Ajout de messages DEP (Données Environnementales Partagées) [#188](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/188).
- Ajout de PAM (probablement un nouveau type de données ou de processus, plus d'informations seraient nécessaires) [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).

### Évolutions techniques
- Refactorisation de la clause FROM dans la requête des missions pour optimiser la performance.
- Correction d'un bug sur les réglementations h3 [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
- Correction d'un bug lié au type de géométrie [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Résolution des conflits de planification des exécutions de pipeline (flow runs) [#189](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/189).
- Mise à jour de la configuration de Trivy (outil d'analyse de vulnérabilités) et désactivation temporaire du workflow Trivy.
- Intégration des modifications du dépôt GitLab (fusion de la branche 'main') [#194](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/194).

### Autres changements
- Mise à jour du fichier `.trivyignore`.
- Rétrogradation d'une fusion précédente (réintégration de l'ajout des références réglementaires après une correction) [#191](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/191).
