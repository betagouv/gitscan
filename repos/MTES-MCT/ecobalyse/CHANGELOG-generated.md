## Changelog : ecobalyse (30 derniers jours, au 30 juillet 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les véhicules et l'énergie, ainsi que sur l'amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités dans l'interface et l'API. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de processus pour la modélisation selon la réglementation des véhicules électriques ([#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622)).
- Intégration de processus prenant en compte le kilométrage pour la phase d'utilisation des véhicules ([#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619)).
- Implémentation d'opérations d'assemblage génériques ([#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683)).
- Possibilité de résoudre le nom complet de la région lorsque c'est possible dans l'explorateur ([#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658)).
- Ajout d'un bouton unique pour ajouter un article de production ([#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664)).
- Ajout d'un lien de feedback dans l'application ([#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)).
- Ajout de la possibilité d'exporter des données Ecospold1 ([#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316)).
- Ajout de tags "transporté refroidi" pour les données ([#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657)).
- Amélioration de la gestion des transformations avec des valeurs par défaut pertinentes ([#2636](https://github.com/MTES-MCT/ecobalyse/issues/2636)).
- Ajout de commandes API authentifiées ([#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653)).
- Correction de l'affichage des impacts détaillés ([#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669)).

### Évolutions techniques
- Utilisation de la base de données ecobalyse-data pour l'historique des scores ([#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580)).
- Optimisation de la vitesse de chargement de l'historique des scores ([#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642)).
- Refactorisation pour ne référencer que les processus génériques dans config.json ([#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660)).
- Déplacement de la suite de tests E2E vers une tâche planifiée ([#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633)).
- Finalisation de la fusion des dépôts de données et de frontend ([#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614)).
- Correction de la configuration des processus pour éviter les duplications ([#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680)).
- Correction du calcul du score total dans food1 ([#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655)).
- Mise à jour des processus pour l'alu et l'acier ([#2679](https://github.com/MTES-MCT/ecobalyse/issues/2679)).
- Correction des avertissements dans les tests de données ([#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671)).
- Ajout de processus pour les "autres matériaux" des VE ([#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687)).

### Autres changements
- Mise à jour des ingrédients de poisson et ajout d'ingrédients secondaires ([#2676](https://github.com/MTES-MCT/ecobalyse/issues/2676)).
- Ajout d'une politique de sécurité ([#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608)).
- Nettoyage des données de base des ingrédients et des alias ([#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604)).
- Renommage des activités à créer et de Custom ([#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601)).
- Correction du nom des composants de câble ([#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587)).
- Mise à jour des exemples de véhicules ([#2629](https://github.com/MTES-MCT/ecobalyse/issues/2629)).
- Mise à jour des exemples Veli ([#2616](https://github.com/MTES-MCT/ecobalyse/issues/2616)).
- Mise à jour des dépendances npm et yarn ([#2668](https://github.com/MTES-MCT/ecobalyse/issues/2668), [#2677](https://github.com/MTES-MCT/ecobalyse/issues/2677)).
- Mise à jour de la dépendance Pillow ([#2665](https://github.com/MTES-MCT/ecobalyse/issues/2665)).
- Upgrade des dépendances node ([#1737](https://github.com/MTES-MCT/ecobalyse/issues/1737)).
