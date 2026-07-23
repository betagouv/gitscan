## Changelog : ecobalyse (30 derniers jours, au 2026-07-22)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration des données, l'ajout de fonctionnalités pour les véhicules et les objets, et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées, notamment pour la performance et la sécurité.

### Évolutions fonctionnelles
- Ajout de l'exportation des données au format Ecospold1 [#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316).
- Amélioration de l'interface utilisateur pour l'ajout d'éléments de production uniques [#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664).
- Restriction de l'accès aux impacts détaillés pour certains utilisateurs [#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669).
- Résolution du nom complet de la région dans l'explorateur [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658).
- Ajout de commandes API authentifiées [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653).
- Possibilité d'activer le refroidissement des transports lorsque disponible [#2654](https://github.com/MTES-MCT/ecobalyse/issues/2654).
- Correction du calcul du score total pour les aliments [#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655).
- Ajout de données pour la modélisation selon la réglementation EV [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622).
- Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619).
- Ajout d'un lien de feedback [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612).
- Ajout d'une politique de sécurité [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608).
- Ajout de plusieurs exemples d'articles alimentaires [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563).
- Ajout de données pour les matériaux d'emballage pour les objets et les véhicules [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555).
- Ajout de ratios actualisés pour le transport routier et maritime [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575).
- Ajout de liens de documentation configurables [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577).
- Ajout de données BAFU importées depuis un export CSV Simapro [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626).

### Évolutions techniques
- Optimisation de la vitesse d'historique des scores [#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642).
- Finalisation de la fusion des dépôts de données et de front-end [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614).
- Amélioration de la configuration pour ne référencer que les processus génériques [#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660).
- Mise à jour des dépendances Litestar et sentry-sdk.
- Déplacement de la suite de tests E2E vers un job planifié [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633).
- Refactorisation du chargement des données en utilisant HTTP [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416).
- Correction d'une faille de sécurité empêchant la falsification du token d'authentification [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600).

### Autres changements
- Correction des avertissements des tests de données [#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671).
- Mises à jour des exemples de véhicules [#2457](https://github.com/MTES-MCT/ecobalyse/issues/2457).
- Améliorations de l'interface utilisateur et corrections de bugs mineurs.
- Nettoyage du code et des données.
- Mises à jour des données LCI pour divers produits agricoles.
- Ajout d'une région "Maghreb" [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568).
- Correction de l'Euro norm dans l'exemple diesel [#2641](https://github.com/MTES-MCT/ecobalyse/issues/2641).
- Ajout de tags "transporté refroidi" [#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657).
- Correction de l'ordre des transformations [#2537](https://github.com/MTES-MCT/ecobalyse/issues/2537).
- Suppression de processus obsolètes.
- Amélioration de la documentation.
