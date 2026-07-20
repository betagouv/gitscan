## Changelog : quefairedemesobjets (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de la plateforme, notamment au niveau des pipelines de données et des déploiements. Des corrections ont été apportées pour stabiliser les tests et les environnements de pré-production. Des optimisations ont également été réalisées sur la gestion des données et l'accessibilité.

### Évolutions fonctionnelles
- Ajout d'actions en tâche de fond dans l'interface d'administration Django pour faciliter certaines opérations. [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093)
- Amélioration de l'accessibilité au clavier : focus du panneau, outline de l'autocomplétion et infobulle. [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073)
- Ajout d'un template pour les pages index et script de migration. [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122)
- Correction d'un problème empêchant le déploiement en pré-production. [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133)

### Évolutions techniques
- Mise à jour des volumes Docker pour utiliser des "named volumes" pour une meilleure gestion et portabilité. [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130)
- Refonte de la structure des settings Django pour une meilleure organisation et maintenabilité. [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060)
- Ajout d'environnements de preview pour faciliter les tests et la revue des modifications. [#3065](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3065)
- Correction de la synchronisation de la base de données entre la production et la pré-production. [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135)
- DAG pour enrichir les SIREN depuis les SIRET et vice-versa. [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125)
- Correction des DAG CMA et Généric. [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124)
- Amélioration de la stabilité des tests e2e. [#3021](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3021)
- Correction de la CI en échec pour les tests e2e. [#3151](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3151)
- Mise en place d'un mécanisme pour ne supprimer les tables temporaires qu'après l'action principale dans les DAG Airflow. [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095)
- Augmentation de la durée de rétention des backups de la webapp. [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137)
- Augmentation des timeouts Nginx. [#3091](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3091)

### Autres changements
- Mise à jour de la documentation d'onboarding concernant les accès à donner ou retirer. [#3094](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3094)
- Ajout de commandes pour réparer les Suggestions avec des données de localisation incorrectes. [#3097](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3097)
- Sérialisation et désérialisation des relations et locations dans les DataFrames partagés entre les tâches d'un DAG. [#3092](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3092)
- Réduction de la duplication dans les Makefiles. [#3089](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3089)
- Diverses mises à jour de dépendances.
- Désactivation temporaire de la comparaison visuelle e2e. [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136)
