## Changelog : ecobalyse (30 derniers jours, au 4 août 2026)

### Résumé
Ce mois-ci, ecobalyse a considérablement enrichi ses capacités de modélisation, notamment pour le secteur des véhicules électriques et la gestion des processus de transport. L'expérience utilisateur a été améliorée par de nouveaux outils de manipulation de données et une interface plus intuitive, tandis que la sécurité et l'automatisation des processus de calcul ont été renforcées.

### Évolutions fonctionnelles
- **Modélisation et données** : 
    - Extension des processus pour les véhicules électriques (normes, consommation, phase d'usage) [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622) [#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687) [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619) [#2594](https://github.com/MTES-MCT/ecobalyse/issues/2594).
    - Gestion avancée des transports (étiquettes de refroidissement, transport pré-assemblage) [#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657) [#2654](https://github.com/MTES-MCT/ecobalyse/issues/2654) [#2616](https://github.com/MTES-MCT/ecobalyse/issues/2616).
    - Nouveaux formats d'import/export (EcoSpold1, BAFU via Simapro) [#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316) [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626).
    - Corrections de données (aluminium, acier, diesel, calcul de score alimentaire) [#2679](https://github.com/MTES-MCT/ecobalyse/issues/2679) [#2641](https://github.com/MTES-MCT/ecobalyse/issues/2641) [#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655) [#2676](https://github.com/MTES-MCT/ecobalyse/issues/2676).
- **Expérience utilisateur (UX/UI)** : 
    - Implémentation des opérations d'assemblage [#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683) et de nouvelles transformations avec valeurs par défaut [#2636](https://github.com/MTES-MCT/ecobalyse/issues/2636).
    - Améliorations de l'interface (étiquettes contextuelles [#2632](https://github.com/MTES-MCT/ecobalyse/issues/2632), bouton d'ajout rapide [#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664), résolution des noms de régions [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658), lien de feedback [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)).
    - Correction de l'affichage des graphiques en mode sombre [#2690](https://github.com/MTES-MCT/ecobalyse/issues/2690).
- **Sécurité** : 
    - Renforcement de la politique de sécurité [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608) et sécurisation des jetons d'authentification [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600).
    - Mise à disposition de commandes API authentifiées [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653) et restriction d'accès aux impacts détaillés [#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669).

### Évolutions techniques
- **Architecture et Performance** : 
    - Optimisation de la vitesse de l'historique des scores [#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642) et migration vers une base de données dédiée [#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580).
    - Fusion des dépôts data et front-end [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614) et refactorisation des schémas de processus pour éviter les duplications [#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680).
- **Automatisation et Tests** : 
    - Automatisation de l'historique des scores via GitHub Cron [#2609](https://github.com/MTES-MCT/ecobalyse/issues/2609) et déplacement de la suite de tests E2E vers des tâches planifiées [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633).
    - Correction des avertissements dans les tests de données [#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671).
- **Maintenance** : 
    - Mise à jour d'Elm [#2638](https://github.com/MTES-MCT/ecobalyse/issues/2638) et nettoyage structurel du code (renommage de composants et nettoyage des ingrédients) [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604) [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601) [#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587).

### Autres changements
- Amélioration de la gestion de la configuration pour limiter les références aux processus génériques [#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660) [#2627](https://github.com/MTES-MCT/ecobalyse/issues/2627).
