## Changelog : quefairedemesobjets (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse de l'infrastructure, notamment la gestion des sauvegardes et la synchronisation des données entre les environnements. Des corrections ont également été apportées pour améliorer la qualité des données et l'expérience utilisateur, en particulier sur l'interface infotri et dans l'administration de l'application. L'architecture des DAGs pour le traitement des données a été revue et optimisée.

### Évolutions fonctionnelles
- Correction de la preview Wagtail qui buggait avec des accents dans le slug. [#3195](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3195)
- Suppression du filtrage des établissements ayant un code étranger. [#3216](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3216)
- L'infotri est maintenant responsive sur les petits écrans. [#3179](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3179)
- Ajout d'actions en tâche de fond dans l'interface d'administration Django. [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093)
- Amélioration de la suggestion d'objets basée sur la table `lien_suggestion`. [#3177](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3177)

### Évolutions techniques
- Passage aux workspaces uv pour la gestion des dépendances et des environnements. [#3058](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3058)
- Refonte de la logique de clonage des datasets de la BAN avec un paramètre de correction. [#3199](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3199)
- Modification de la logique des DAGs pour l'enrichissement des SIREN et SIRET. [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125)
- Correction et réorganisation des DAGs CMA et Généric. [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124)
- Amélioration de la synchronisation entre les environnements de production et de pré-production via l'utilisation de DSN. [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135)
- Utilisation de la fonction `chain` au lieu de l'opérateur `>>` pour une meilleure lisibilité et maintenabilité du code Airflow. [#3178](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3178)
- Mise à jour de la configuration Docker pour utiliser des volumes nommés. [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130)
- Suppression des tables temporaires après l'action principale dans les DAGs. [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095)

### Autres changements
- Augmentation de la durée de rétention des backups de la webapp. [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137)
- Désactivation temporaire des tests de comparaison visuelle e2e. [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136)
- Correction de la CI en cas d'échec des tests e2e. [#3151](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3151)
- Nombreuses mises à jour de dépendances (linting, tests, build tools, etc.).
