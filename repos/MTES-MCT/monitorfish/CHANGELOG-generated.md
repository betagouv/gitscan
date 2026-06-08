## Changelog : monitorfish (30 derniers jours, au 4 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la surveillance AIS, avec l'intégration de données de position en temps réel et l'affichage des navires sur la carte. Des corrections et des améliorations ont également été apportées à la gestion des préavis, des signalements INN, des unités de contrôle et des ventes, ainsi que des optimisations techniques et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout du champ `is_under_jdp` à la table `analytics_missions` pour une meilleure analyse des missions. [#5162](https://github.com/MTES-MCT/monitorfish/issues/5162)
- Amélioration des filtres dans la liste des signalements INN pour une recherche plus efficace. [#5151](https://github.com/MTES-MCT/monitorfish/issues/5151)
- Ajout de la possibilité de mettre à jour facilement les signalements INN créés dans Navpro. [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113)
- Ajout d'une recherche par "type" et "base" lors de la création d'une nouvelle unité de contrôle. [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110)
- Ré-ajout des champs liés aux espèces dans le formulaire manuel de préavis en cas de non-débarquement. [#5088](https://github.com/MTES-MCT/monitorfish/issues/5088)
- Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers). [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108)
- Ajout de la mention "Préavis zéro" dans l'objet des emails de notification. [#5104](https://github.com/MTES-MCT/monitorfish/issues/5104)
- Intégration de l'affichage des navires AIS sur la carte, avec des informations sur leur type, leur destination et leur position récente. [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090)
- Ajout d'un filtre pour les navires absents dans la liste des signalements INN.
- Amélioration du comportement des filtres pour les rapports.
- Possibilité de rechercher des navires directement depuis la barre de recherche et de zoomer sur leur position.
- Ajout d'un indicateur visuel pour les navires identifiés comme étant en infraction (CFR).

### Évolutions techniques
- Mise à jour des dépendances backend : Spring Boot 4, Security 7, Flyway 12, Ktor 3.5. [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146)
- Mise à jour de TimescaleDB et PostGIS. [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096)
- Amélioration de la gestion des erreurs lors du chargement des cartes Sentry.
- Correction d'un test flaky sur la pipeline CI/CD. [#5148](https://github.com/MTES-MCT/monitorfish/issues/5148)
- Ajout de variables d'environnement pour Kafka et la génération de certificats. [#5115](https://github.com/MTES-MCT/monitorfish/issues/5115)
- Harmonisation du composant Dialog dans l'interface utilisateur. [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144)
- Correction de bugs et amélioration de la robustesse des tests.
- Optimisation de la lecture des coordonnées WKT pour l'affichage des données AIS.
- Mise en place d'un workflow de mise à jour de la base de données.

### Autres changements
- Correction de libellés et de tests dans l'interface utilisateur.
- Ajout d'un README pour la génération du fichier .p12. [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123)
- Ajout d'une bannière d'erreur en cas d'échec de l'upload de fichiers. [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091)
- Ajout d'une bannière d'environnement pour l'intégration continue. [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024)
- Mise à jour de la documentation et du code pour améliorer la lisibilité et la maintenabilité.
