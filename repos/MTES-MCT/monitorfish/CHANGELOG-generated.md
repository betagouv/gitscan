## Changelog : monitorfish (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration du suivi des navires, notamment avec l'intégration des données AIS (Automatic Identification System) permettant de visualiser les positions des navires en temps réel. Des améliorations ont également été apportées à la gestion des signalements, des préavis et des infractions, ainsi qu'à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- **Suivi des navires :** Intégration de l'affichage des navires sous AIS, avec affichage des positions récentes et possibilité de recherche. [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090)
- **Signalements :**
    - Possibilité d'ajouter plusieurs NATINF (nature d'infraction) à un signalement. [#5048](https://github.com/MTES-MCT/monitorfish/issues/5048)
    - Possibilité de créer des signalements "en lots". [#5053](https://github.com/MTES-MCT/monitorfish/issues/5053)
- **Préavis :**
    - Ajout de la mention "zéro" dans les mails, PDF et SMS pour les préavis nuls. [#4981](https://github.com/MTES-MCT/monitorfish/issues/4981)
    - Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers). [#5033](https://github.com/MTES-MCT/monitorfish/issues/5033)
    - Retrait des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis. [#5050](https://github.com/MTES-MCT/monitorfish/issues/5050)
- **Unités :** Ajout d'une recherche dans les menus "type" et "base" lors de la création d'un nouveau moyen. [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110)
- **Fiche navire :** Ajustements de l'interface utilisateur pour les modalités de contact. [#5051](https://github.com/MTES-MCT/monitorfish/issues/5051)
- **Catégories d'infractions :** Ajout de la catégorie d'infraction NATINF 22204 (RUN FLOW). [#5056](https://github.com/MTES-MCT/monitorfish/issues/5056)
- **Environnement :** Ajout d'une bannière indiquant l'environnement (intégration). [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024) et [#5105](https://github.com/MTES-MCT/monitorfish/issues/5105)

### Évolutions techniques
- **Kafka :** Ajout de la variable d'environnement `CERT_FOLDER` pour Kafka. [#5115](https://github.com/MTES-MCT/monitorfish/issues/5115)
- **Base de données :** Mise à jour de TimescaleDB et PostGIS. [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096)
- **Tests :** Ajout de tests Cypress pour les nouvelles fonctionnalités AIS.
- **Docker :** Ajout de la configuration des certificats dans les images Docker.
- **Backend :** Mise à jour des dépendances non majeures. [#5064](https://github.com/MTES-MCT/monitorfish/issues/5064)
- **CI/CD :** Améliorations du workflow de déploiement de la base de données.

### Autres changements
- Correction de bugs divers dans l'interface utilisateur (favicon, positionnement des boîtes d'outils de la carte). [#5114](https://github.com/MTES-MCT/monitorfish/issues/5114)
- Corrections de typos et améliorations de la lisibilité du code.
- Amélioration de la gestion des erreurs lors de l'upload de fichiers. [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091)
- Diverses corrections et optimisations du code.
- Mise à jour de la documentation.
