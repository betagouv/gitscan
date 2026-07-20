## Changelog : ecobalyse (30 derniers jours, au 2026-07-17)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données (notamment pour les véhicules et l'alimentation), l'amélioration de l'expérience utilisateur (notamment dans l'explorateur et les détails des processus) et des corrections de bugs pour assurer la stabilité et la fiabilité de la plateforme. Des améliorations techniques ont également été apportées, notamment en matière de sécurité et de gestion des dépendances.

### Évolutions fonctionnelles
- L'explorateur affiche désormais le nom complet de la région lorsque possible. [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658)
- Ajout de commandes API authentifiées pour une intégration plus sécurisée. [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653)
- Amélioration du calcul du score total pour les données "food1". [#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655)
- Ajout de la possibilité d'importer des données BAFU à partir d'un export CSV Simapro. [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626)
- Ajout de processus pour la modélisation selon la réglementation EV (véhicules électriques). [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622)
- Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules. [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619)
- Ajout d'un lien de feedback pour les utilisateurs. [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)
- Ajout d'une politique de sécurité. [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608)
- Ajout de plusieurs exemples d'articles alimentaires. [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553)
- Amélioration de l'affichage des impacts dans les détails des objets/véhicules. [#2567](https://github.com/MTES-MCT/ecobalyse/issues/2567)
- Ajout de matériaux d'emballage pour les objets et les véhicules. [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555)
- Ajout de la possibilité de filtrer les processus invisibles dans le calculateur générique. [#2537](https://github.com/MTES-MCT/ecobalyse/issues/2537)

### Évolutions techniques
- Finalisation de la fusion des dépôts de données et de frontend. [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614)
- Mise à jour des dépendances Litestar, sentry-sdk et des dépendances de développement.
- Déplacement de la suite de tests E2E vers une tâche planifiée. [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633)
- Amélioration de la gestion de la configuration et rechargement après réception des processus détaillés. [#2627](https://github.com/MTES-MCT/ecobalyse/issues/2627)
- Refactorisation du fichier de transport et génération hors ligne. [#2535](https://github.com/MTES-MCT/ecobalyse/issues/2535)
- Utilisation de HTTP pour le chargement des données. [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416)
- Correction d'une faille de sécurité empêchant la falsification du token d'authentification. [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600)
- Mise à jour des dépendances Elm. [#2638](https://github.com/MTES-MCT/ecobalyse/issues/2638)

### Autres changements
- Nettoyage du code des données (base_ingredients et alias). [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604)
- Renommage des activités et de la classe Custom. [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601)
- Déplacement de l'historique des scores vers une tâche cron GitHub. [#2609](https://github.com/MTES-MCT/ecobalyse/issues/2609)
- Définition d'un seuil minimal de différence de 0.1% pour la table des différences. [#2607](https://github.com/MTES-MCT/ecobalyse/issues/2607)
- Mise à jour des exemples de véhicules. [#2457](https://github.com/MTES-MCT/ecobalyse/issues/2457)
- Ajout d'une région "Maghreb". [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)
- Mise à jour des ratios de transport routier/maritime. [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575)
- Ajout de liens de documentation configurables. [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577)
- Diverses mises à jour de données et corrections de LCI (Life Cycle Inventory).
- Correction de noms de composants. [#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587)
- Suppression de processus obsolètes. [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
