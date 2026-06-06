## Changelog : monitorfish (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, monitorfish a bénéficié d'améliorations significatives en termes de gestion des données AIS, de correction de bugs et d'expérience utilisateur. Des améliorations ont été apportées à la gestion des signalements, des préavis et des unités de contrôle, ainsi que des mises à jour techniques pour améliorer la stabilité et la performance de la plateforme. L'intégration de nouvelles versions de dépendances clés a également été effectuée.

### Évolutions fonctionnelles
- **Signalements INN :** Amélioration des filtres dans la liste des signalements pour une recherche plus précise [#5151](https://github.com/MTES-MCT/monitorfish/issues/5151).
- **Signalements INN :** Possibilité de mettre à jour facilement les signalements pour lesquels une fiche a été créée dans Navpro [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113).
- **Préavis :** Ajout de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers) [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108).
- **Préavis :** Ajout de la mention "Préavis zéro" dans l'objet du mail [#5104](https://github.com/MTES-MCT/monitorfish/issues/5104).
- **Unités :** Ajout d'une recherche par "type" et "base" lors de la création d'une nouvelle unité de contrôle [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110).
- **Formulaire PNO :** Ré-ajout des champs liés aux espèces dans le formulaire manuel en cas de non-débarquement [#5088](https://github.com/MTES-MCT/monitorfish/issues/5088).
- **Formulaire PNO :** Les champs liés à la pêche sont maintenant optionnels dans le formulaire manuel de déclaration de non-débarquement [#5088](https://github.com/MTES-MCT/monitorfish/issues/5088).
- **Cartographie :** Affichage des navires sous AIS (nécessite la configuration de la variable d'environnement correspondante) [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090).
- **Interface utilisateur :** Harmonisation du composant Dialog pour une expérience utilisateur plus cohérente [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144).
- **Interface utilisateur :** Mise en avant de l'environnement d'intégration avec une bannière d'information [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024).
- **Interface utilisateur :** Correction de l'étiquette "Drone" [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144).
- **Interface utilisateur :** Affichage d'une bannière d'erreur en cas d'échec de l'upload [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091).

### Évolutions techniques
- **Backend :** Mise à jour des dépendances Spring Boot 4, Security 7, Flyway 12 et Ktor 3.5 [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146).
- **Backend :** Correction d'un test flaky sur la pipeline [#5148](https://github.com/MTES-MCT/monitorfish/issues/5148).
- **Backend :** Correction de la lecture des coordonnées WKT pour l'affichage des positions AIS [#5125](https://github.com/MTES-MCT/monitorfish/issues/5125).
- **Backend :** Ajout du champ `is_under_jdp` à la table `analytics_missions` [#5162](https://github.com/MTES-MCT/monitorfish/issues/5162).
- **Base de données :** Mise à jour de TimescaleDB et PostGIS [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096).
- **Kafka :** Ajout de variables d'environnement manquantes pour Kafka et configuration de l'intégration Kafka dans Docker Compose [#5118](https://github.com/MTES-MCT/monitorfish/issues/5118).
- **Tests :** Ajout de tests Cypress pour la fonctionnalité AIS [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090).
- **CI/CD :** Modification du workflow CI/CD pour Sentry afin de continuer l'upload des source maps en cas d'erreur [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146).
- **Docker :** Ajout d'un README pour la génération du fichier .p12 [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123).

### Autres changements
- **Documentation :** Ajout d'un README pour la génération du fichier .p12 [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123).
- **Code :** Nettoyage et refactoring de divers composants de l'interface utilisateur.
- **Code :** Correction de bugs mineurs et améliorations de la performance.
- **Code :** Ajout d'un type pour `controlResource` [#5145](https://github.com/MTES-MCT/monitorfish/issues/5145).
- **Code :** Ajout de l'infraction manquante [#5145](https://github.com/MTES-MCT/monitorfish/issues/5145).
