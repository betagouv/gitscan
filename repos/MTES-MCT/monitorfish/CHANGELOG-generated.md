## Changelog : monitorfish (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du suivi des navires, notamment avec l'intégration des données AIS (Automatic Identification System) pour afficher les positions des navires sur la carte. Des corrections et améliorations ont également été apportées aux préavis, aux signalements et à l'interface utilisateur, notamment pour la gestion des infractions et des informations sur les navires.

### Évolutions fonctionnelles
- **AIS :** Intégration de l'affichage des navires via le système AIS sur la carte, avec la possibilité de rechercher et de zoomer sur les navires AIS.  Les dernières positions AIS sont maintenant mises à jour via la pipeline.
- **Préavis :**
    - Ajout de la mention "zéro" dans les emails, PDF et SMS pour les préavis nuls.
    - Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers).
    - Possibilité de filtrer les préavis par type "préavis zéro".
    - Suppression des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis.
- **Signalements :**
    - Possibilité d'ajouter plusieurs NATINF (nature d'infraction) à un signalement.
    - Possibilité de faire des signalements "en lots" pour les infractions INN.
- **Fiche navire :** Amélioration de l'interface utilisateur pour les modalités de contact sur l'onglet identité.
- **Catégories d'infraction :** Ajout de la catégorie d'infraction NATINF 22204.
- **Gestion des unités :** Ajout d'une recherche dans les menus "type" et "base" lors de la création d'une nouvelle unité.

### Évolutions techniques
- **Kafka :** Ajout d'une variable d'environnement `CERT_FOLDER` pour la configuration de Kafka. Désactivation de Kafka par défaut.
- **Base de données :** Mise à jour de TimescaleDB et PostGIS.
- **Backend :** Mise à jour des dépendances non majeures.
- **Tests :** Ajout et correction de tests Cypress et backend.
- **Docker :** Modifications de la configuration Docker pour la gestion de Kafka et de la base de données.
- **Migrations :** Corrections et ajouts de migrations de base de données.

### Autres changements
- Correction de bugs divers dans l'interface utilisateur (favicon, positionnement des boîtes à outils sur la carte).
- Amélioration de la documentation et des commentaires.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de la bannière d'environnement d'intégration.
- Correction de l'affichage des coordonnées WKT pour les données AIS.
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers.
- Correction de l'affichage des raisons de vérification des préavis.
- Ajout de la gestion de la validité des périodes pour les signalements.
- Suppression de configurations AIS inutiles.
- Correction de l'affichage des noms de navires.
- Ajout de la longueur des navires dans les positions AIS.
- Ajout d'un filtre pour exclure les navires avec un CFR (Common Fisheries Register).
- Ajout de la gestion des types de positions (VMS, AIS) dans la base de données.
- Correction de l'affichage des infoboxes lors de l'ouverture d'un rapport IUU.
- Amélioration des tests pour les formulaires de signalement.
- Correction de problèmes liés à la construction de ReadTheDocs.
