## Changelog : ecobalyse (30 derniers jours, au 30 juillet 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les véhicules et l'énergie, ainsi que sur l'amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités dans l'interface et l'API. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de processus pour la modélisation des véhicules électriques selon la réglementation en vigueur [#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687).
- Implémentation d'opérations d'assemblage génériques [#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683).
- Amélioration de l'affichage des ingrédients dans l'interface utilisateur [#2676](https://github.com/MTES-MCT/ecobalyse/issues/2676).
- Ajout de la possibilité de résoudre le nom complet de la région lorsque c'est possible [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658).
- Ajout de commandes API authentifiées [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653).
- Ajout d'un lien de feedback dans l'interface actuelle [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612).
- Ajout de ratios de transport routier/maritime mis à jour [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575).
- Ajout de liens de documentation configurables [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577).
- Importation de données BAFU à partir d'un export CSV Simapro [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626).
- Ajout de l'export Ecospold1 [#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316).
- Ajout de tags pour les transports réfrigérés [#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657).

### Évolutions techniques
- Utilisation de la base de données ecobalyse-data pour l'historique des scores [#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580).
- Optimisation de la vitesse de récupération de l'historique des scores [#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642).
- Refactoring pour ne pas dupliquer le schéma des processus [#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680).
- Mise à jour des dépendances npm et yarn [#2668](https://github.com/MTES-MCT/ecobalyse/issues/2668), [#2677](https://github.com/MTES-MCT/ecobalyse/issues/2677).
- Mise à jour de la dépendance Pillow [#2665](https://github.com/MTES-MCT/ecobalyse/issues/2665).
- Mise à jour de la dépendance Litestar [#2584](https://github.com/MTES-MCT/ecobalyse/issues/2584).
- Mise à jour de la dépendance Sentry-sdk [#2585](https://github.com/MTES-MCT/ecobalyse/issues/2585).
- Amélioration de la configuration pour ne référencer que les processus génériques [#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660).
- Déplacement de la suite de tests E2E vers un job planifié [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633).
- Finalisation de la fusion des dépôts de données et de frontend [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614).

### Autres changements
- Correction de bugs et avertissements dans les tests de données [#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671).
- Correction des processus alu et acier [#2679](https://github.com/MTES-MCT/ecobalyse/issues/2679).
- Correction d'un bug empêchant l'accès aux impacts détaillés [#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669).
- Ajout d'une politique de sécurité [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608).
- Nettoyage et correction de données (sorghum, rye, flaxseed, lima-bean, amaranth, plantain) [#2458](https://github.com/MTES-MCT/ecobalyse/issues/2458), [#2478](https://github.com/MTES-MCT/ecobalyse/issues/2478), [#2481](https://github.com/MTES-MCT/ecobalyse/issues/2481), [#2482](https://github.com/MTES-MCT/ecobalyse/issues/2482), [#2488](https://github.com/MTES-MCT/ecobalyse/issues/2488), [#2491](https://github.com/MTES-MCT/ecobalyse/issues/2491), [#2511](https://github.com/MTES-MCT/ecobalyse/issues/2511), [#2539](https://github.com/MTES-MCT/ecobalyse/issues/2539), [#2546](https://github.com/MTES-MCT/ecobalyse/issues/2546).
- Mise à jour des exemples de véhicules [#2629](https://github.com/MTES-MCT/ecobalyse/issues/2629), [#2641](https://github.com/MTES-MCT/ecobalyse/issues/2641).
- Ajout de la région Maghreb [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568).
- Correction du nom du composant cable [#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587).
- Mise à jour des consommations des véhicules [#2594](https://github.com/MTES-MCT/ecobalyse/issues/2594).
- Correction de la prévention de la falsification de jeton d'authentification [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600).
- Ajout du tag productmassdependent [#2579](https://github.com/MTES-MCT/ecobalyse/issues/2579).
- Changement de mix électrique par défaut vers celui de l'Inde [#1702](https://github.com/MTES-MCT/ecobalyse/issues/1702).
- Mise à jour des données et ajout du processus cff [#1708](https://github.com/MTES-MCT/ecobalyse/issues/1708).
- Upgrade des dépendances node [#1737](https://github.com/MTES-MCT/ecobalyse/issues/1737).
