## Changelog : quefairedemesobjets (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et de la performance de la plateforme, notamment au niveau des pipelines de données et du déploiement. Des corrections ont été apportées pour résoudre des problèmes de déploiement et de synchronisation des données, et l'accessibilité a été améliorée. Des optimisations ont également été réalisées sur le processus de restauration de la base de données et la gestion des comptes utilisateurs.

### Évolutions fonctionnelles
- Ajout d'actions en tâche de fond dans l'interface d'administration Django pour une meilleure gestion des données. [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093)
- Amélioration du positionnement de l'autocomplétion en iframe dans la recherche. [#2854](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2854)
- Ajout d'un panneau de débogage pour le score de recherche pour les utilisateurs en version bêta. [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852)
- Amélioration de l'accessibilité du site, notamment au niveau du focus clavier et des infobulles. [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073)
- Ajout d'un template pour les pages index et script de migration. [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122)
- Correction d'un problème d'espace au-dessus du fil d'ariane sur les pages produit. [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121)

### Évolutions techniques
- Mise à jour de la configuration Docker pour utiliser des volumes nommés, améliorant la gestion et la portabilité des données. [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130)
- Correction de problèmes de synchronisation entre la production et la pré-production, notamment en utilisant le DSN pour la restauration de la base de données. [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135)
- Amélioration de la stabilité des tests end-to-end (e2e). [#3021](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3021)
- Restructuration des paramètres Django pour une meilleure organisation et maintenabilité. [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060)
- Mise en place d'un processus de revue régulière des comptes Django et Airflow pour renforcer la sécurité. [#3070](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3070)
- Correction de problèmes liés au lockfile empêchant le déploiement en pré-production. [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133)
- Déplacement du script SQL `wagtail_french` pour débloquer le déploiement Scalingo. [#3134](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3134)
- Amélioration de la gestion des relations et des localisations dans les DataFrames partagées entre les tâches d'un DAG. [#3092](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3092)
- Mise à jour des scripts pour enrichir les SIREN à partir des SIRET et vice versa. [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125)
- Correction des DAGs CMA et Généric. [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124)
- Optimisation du script de restauration de la base de données sample. [#3090](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3090)
- Correction des scripts pour permettre leur exécution par cohorte. [#3097](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3097)
- Mise à jour de la documentation d'onboarding concernant les accès. [#3094](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3094)
- Suppression des tables temporaires après l'action principale dans Airflow. [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095)

### Autres changements
- Réduction de la duplication dans les Makefiles. [#3089](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3089)
- Désactivation temporaire de la comparaison visuelle e2e. [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136)
- Augmentation de la durée de rétention des sauvegardes de la webapp. [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137)
- Empêcher l'indexation de la pré-production par une variable d'environnement. [#3017](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3017)
- Suppression des espaces autour des emails. [#3014](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3014)
- Ajout de documentation pour la sécurité et les Agents IA. [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495)
- Nombreuses mises à jour de dépendances.
