## Changelog : monitorfish (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration du suivi des navires avec l'intégration des données AIS, des corrections de bugs et des améliorations de l'interface utilisateur. Des améliorations ont également été apportées à la gestion des préavis et des signalements, notamment pour les cas de non-débarquement et les préavis "zéro". Enfin, des mises à jour de l'infrastructure et des dépendances ont été réalisées.

### Évolutions fonctionnelles
- **AIS :** Intégration de l'affichage des navires sous AIS sur la carte, avec récupération des dernières positions et informations associées (type de navire, destination, etc.). Possibilité de rechercher des navires AIS directement depuis la barre de recherche. [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090)
- **Préavis :**
    - Ajout de la mention "zéro" dans les notifications (mails, SMS, PDF) en cas de préavis nul. [#4981](https://github.com/MTES-MCT/monitorfish/issues/4981)
    - Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers). [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108)
    - Invalidation automatique des préavis "zéro" BFT ou SWO créés il y a plus de 24 heures. [#5069](https://github.com/MTES-MCT/monitorfish/issues/5069)
- **Signalements INN :** Simplification de la mise à jour des signalements par le pôle INN, en lien avec Navpro. [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113)
- **Unités :** Ajout d'une recherche par type et base lors de la création d'une nouvelle unité. [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110)
- **Coordonnées :** Correction d'un bug dans la longitude lors de la saisie des coordonnées. [#5106](https://github.com/MTES-MCT/monitorfish/issues/5106)
- **Catégories d'infractions :** Correction d'un bug dans le flux de gestion des catégories d'infractions. [#5082](https://github.com/MTES-MCT/monitorfish/issues/5082)
- **Environnement :** Ajout d'une bannière indiquant l'environnement d'intégration. [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024)
- **Upload :** Affichage d'une bannière d'erreur en cas d'échec d'upload. [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091)

### Évolutions techniques
- **Kafka :** Ajout de la configuration et des variables d'environnement nécessaires pour l'intégration de Kafka, notamment pour la réception des données AIS. [#5115](https://github.com/MTES-MCT/monitorfish/issues/5115), [#5118](https://github.com/MTES-MCT/monitorfish/issues/5118)
- **Base de données :** Mise à jour de TimescaleDB et PostGIS. [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096)
- **Docker :** Ajout de variables d'environnement manquantes et corrections de la configuration Docker Compose.
- **Tests :** Amélioration et correction de nombreux tests (Cypress, Jest).
- **Dépendances :** Mise à jour des dépendances backend. [#5064](https://github.com/MTES-MCT/monitorfish/issues/5064)
- **Lecture coordonnées WKT :** Correction de la lecture des coordonnées WKT. [#5125](https://github.com/MTES-MCT/monitorfish/issues/5125)

### Autres changements
- Ajout d'un README pour la génération du certificat .p12. [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123)
- Mise à jour des dernières positions par la pipeline. [#5127](https://github.com/MTES-MCT/monitorfish/issues/5127)
- Correction de l'icône de favicon. [#5114](https://github.com/MTES-MCT/monitorfish/issues/5114)
- Suppression de configurations AIS inutilisées.
- Nettoyage du code et correction de typos.
- Amélioration de la gestion des erreurs et des messages d'information.
