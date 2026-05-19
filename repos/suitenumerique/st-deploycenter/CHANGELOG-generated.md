## Changelog : st-deploycenter (30 derniers jours, au 18 mai 2026)

### Résumé
Cette version apporte des améliorations concernant la gestion des droits d'accès, notamment pour les calendriers et les transferts de données. Des corrections ont également été apportées pour assurer la fiabilité de l'export des données vers datagouv et l'optimisation des performances lors du chargement des organisations.

### Évolutions fonctionnelles
- Ajout d'un droit d'accès pour les calendriers, avec une refactorisation pour une gestion plus générique des droits. [#41e1f31](https://github.com/suitenumerique/st-deploycenter/commit/41e1f31)
- Restriction de l'accès aux transferts de données aux abonnements actifs. [#2a53f29](https://github.com/suitenumerique/st-deploycenter/commit/2a53f29)
- Affichage de la raison pour laquelle un utilisateur n'a pas le droit de télécharger des données. [#1d26fb7](https://github.com/suitenumerique/st-deploycenter/commit/1d26fb7)

### Évolutions techniques
- Optimisation du chargement des organisations pour éviter de charger toutes les données en une seule fois. [#60b646b](https://github.com/suitenumerique/st-deploycenter/commit/60b646b)
- Nettoyage des métriques obsolètes au niveau de l'organisation après leur récupération. [#bc523ee](https://github.com/suitenumerique/st-deploycenter/commit/bc523ee)
- Correction du nom du champ "status" lors de l'export vers datagouv. [#163f086](https://github.com/suitenumerique/st-deploycenter/commit/163f086)
- Correction pour éviter d'exporter les opérateurs en test ou nouveaux sans statut vers datagouv. [#e75df90](https://github.com/suitenumerique/st-deploycenter/commit/e75df90)
- L'export des jeux de données vers datagouv est maintenant effectué toutes les 4 heures. [#7f32820](https://github.com/suitenumerique/st-deploycenter/commit/7f32820)

### Autres changements
- Correction de tests. [#4360642](https://github.com/suitenumerique/st-deploycenter/commit/4360642)
