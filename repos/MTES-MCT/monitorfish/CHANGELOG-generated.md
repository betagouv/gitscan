## Changelog : monitorfish (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la prise en charge des données AIS (Automatic Identification System) pour le suivi des navires, des corrections de bugs et des améliorations de l'interface utilisateur. Des efforts ont également été déployés pour améliorer la gestion des préavis de pêche et la gestion des unités.

### Évolutions fonctionnelles
- **AIS :** Intégration de l'affichage des navires sous AIS sur la carte, avec récupération des dernières positions et informations associées. Possibilité de rechercher des navires AIS directement depuis la barre de recherche.
- **Signalements INN :** Simplification de la mise à jour des signalements par le pôle INN via une intégration avec Navpro [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113).
- **Préavis :**
    - Ajout de la mention "zéro" dans les notifications (mails, SMS, PDF) en cas de préavis de pêche nul [#4981](https://github.com/MTES-MCT/monitorfish/issues/4981).
    - Ajout de la raison de vérification d'un préavis (note, signalement, port état tiers) [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108).
    - Invalidations automatiques des préavis zéro BFT ou SWO créés il y a plus de 24 heures [#5069](https://github.com/MTES-MCT/monitorfish/issues/5069).
- **Unités :** Possibilité de rechercher par type et base lors de la création d'une nouvelle unité [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110).
- **Gestion des infractions :** Correction d'un bug dans le workflow des catégories d'infractions [#5082](https://github.com/MTES-MCT/monitorfish/issues/5082).
- **Dates de fin de signalement :** Rendre obligatoire la date de fin des signalements et proposer des options de fin [#5079](https://github.com/MTES-MCT/monitorfish/issues/5079).
- **Uploads :** Affichage d'une bannière d'erreur en cas d'échec d'un upload [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091).
- **Environnement :** Ajout d'une bannière indiquant l'environnement (intégration) [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024).

### Évolutions techniques
- **Kafka :** Ajout de la configuration et des variables d'environnement nécessaires pour Kafka, incluant la gestion des certificats.
- **Base de données :** Mise à jour de TimescaleDB et PostGIS.
- **Docker :** Améliorations de la configuration Docker, incluant l'ajout de variables d'environnement et la gestion des certificats.
- **Tests :** Ajout et correction de tests Cypress et Jest.
- **Cartographie :** Correction de bugs liés à l'affichage des coordonnées WKT et au positionnement des boîtes d'outils de la carte.
- **API :** Ajout d'APIs pour récupérer les positions AIS.
- **Refactoring :** Diverses corrections et améliorations du code, notamment pour la gestion des dates et des types de données.

### Autres changements
- Ajout d'un README pour la génération des certificats (.p12) [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123).
- Mise à jour des dépendances.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de configurations inutilisées.
- Amélioration des messages d'erreur.
