## Changelog : monitorfish (30 derniers jours, au 22 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la cartographie et du suivi des navires, notamment avec l'intégration des données AIS. Des corrections et des améliorations ont également été apportées à la gestion des préavis, des signalements et des infractions, ainsi qu'à l'interface utilisateur pour une meilleure expérience. Des mises à jour de l'infrastructure et des dépendances ont également été réalisées.

### Évolutions fonctionnelles
- **Cartographie et suivi des navires :** Affichage des navires sous AIS avec récupération des positions AIS via l'API et intégration dans la carte. Possibilité de rechercher des navires AIS et de zoomer sur leur position.
- **Préavis :**
    - Ajout de la mention "zéro" dans les mails, PDF et SMS pour les préavis à zéro.
    - Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers).
    - Filtrage des préavis par type "préavis 0".
    - Suppression des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis.
- **Signalements :**
    - Possibilité de faire des signalements "en lots" (plusieurs NATINF).
    - Ajout du nombre de navires aux signalements INN.
- **Infractions :**
    - Ajout de la catégorie d'infraction NATINF 22204 (RUN FLOW).
    - Affichage des infractions sous forme de tags dans le formulaire de signalement.
- **Fiche navire :** Amélioration de l'interface utilisateur des modalités de contact.
- **Unités :** Ajout d'une recherche dans les menus "type" et "base" lors de la création d'une nouvelle unité.

### Évolutions techniques
- **Kafka :** Ajout d'une variable d'environnement `CERT_FOLDER` pour la configuration de Kafka.  Kafka n'est plus activé par défaut.
- **Base de données :** Mise à jour de TimescaleDB et PostGIS.
- **Tests :** Ajout et correction de tests Cypress pour assurer la qualité du code.
- **Infrastructure :** Amélioration du workflow de déploiement de la base de données.
- **Dépendances :** Mise à jour des dépendances backend non majeures.
- **Docker :** Ajout de la variable d'environnement `CERT_FOLDER` dans les fichiers docker-compose.
- **Correction de bugs :** Diverses corrections de bugs et améliorations de la performance.

### Autres changements
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires et documentation.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de problèmes d'affichage et de mise en page.
- Ajout d'une bannière d'erreur pour les échecs de téléchargement.
- Mise en avant de l'environnement d'intégration avec une bannière.
- Correction d'un problème d'overflow masquant la toolbox d'infraction.
- Correction d'un bug dans le flow des catégories d'infractions.
- Ajout de la possibilité d'ajouter plusieurs NATINF à un signalement.
- Correction de problèmes de tests et d'assertions.
- Ajout d'un favicon.
