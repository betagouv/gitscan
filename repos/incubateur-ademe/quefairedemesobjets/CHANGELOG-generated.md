## Changelog : quefairedemesobjets (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la plateforme, notamment en production, avec des corrections de déploiement et des optimisations de la base de données. Des travaux ont également été réalisés sur l'enrichissement des données et l'amélioration des processus de synchronisation. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la prévisualisation des pages Wagtail avec des accents dans le slug [#3195](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3195).
- Ajout d'actions en tâche de fond dans l'interface d'administration Django pour plus de flexibilité [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093).
- Amélioration de la stabilité des tests e2e, notamment en corrigeant un problème lié au lockfile [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122) et [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133).
- Ajout d'un template pour les pages index et script de migration [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122).
- Correction de l'affichage du breadcrumb sur les pages produit [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121).

### Évolutions techniques
- Modification de la logique de clone pour permettre ou non l'exécution d'une commande DBT de consolidation [#3169](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3169).
- Utilisation de workspaces UV pour améliorer l'environnement de développement [#3058](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3058).
- Refactorisation des settings Django pour une meilleure organisation [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060).
- Mise à jour des volumes Docker pour utiliser des named volumes, améliorant la gestion et la portabilité [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130).
- Amélioration de la gestion des DAGs Airflow, notamment en limitant l'historique et en corrigeant des erreurs [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095), [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124), [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125) et [#3101](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3101).
- Correction de la synchronisation de la base de données en production vers la pré-production [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135).
- Optimisation du script de restauration de la base de données sample [#3090](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3090).
- Amélioration de la gestion des relations et des localisations dans les DataFrames partagés entre les jobs d'un DAG [#3092](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3092).

### Autres changements
- Mise à jour de la documentation d'onboarding concernant les accès aux données [#3094](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3094).
- Ajout d'un paramètre pour corriger les datasets de la BAN [#3199](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3199).
- Correction d'un problème de comparaison visuelle dans les tests e2e [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136).
- Augmentation de la durée de rétention des backups de la webapp [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137).
- Commandes pour réparer les Suggestions avec des données de localisation incorrectes [#3097](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3097).
- Nombreuses mises à jour de dépendances pour assurer la sécurité et la performance du projet.
