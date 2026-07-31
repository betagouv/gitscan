## Changelog : quefairedemesobjets (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la robustesse de la plateforme, notamment au niveau des déploiements et des tests. Des corrections ont été apportées pour résoudre des problèmes de synchronisation de données et de déploiement en pré-production. Des améliorations ont également été apportées à la cartographie des données et à la gestion des établissements.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la prévisualisation des pages Wagtail avec des accents dans le slug [#3195](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3195).
- Suppression du filtrage des établissements ayant un code étranger [#3216](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3216).
- L'infographie est maintenant responsive sur les petits écrans [#3179](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3179).
- Amélioration de la suggestion d'établissements à partir de la table `lien_suggestion` [#3177](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3177).
- Ajout d'actions en tâche de fond dans l'interface d'administration Django [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093).

### Évolutions techniques
- Passage aux workspaces UV pour une meilleure gestion des dépendances et des environnements [#3058](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3058).
- Mise à jour de la logique de clonage des datasets de la BAN avec un paramètre de correction [#3199](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3199).
- Refonte des modèles DBT pour une meilleure organisation [#3170](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3170).
- Amélioration de la stabilité des tests e2e et correction de la CI en échec [#3151](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3151).
- Correction de la synchronisation de la production vers la pré-production en utilisant le DSN pour la restauration [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135).
- Mise à jour de la configuration Docker pour utiliser des volumes nommés [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130).
- Restructuration des settings Django [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060).
- DAG pour enrichir les SIREN depuis les SIRET et vice-versa [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125).
- Correction des DAGs CMA et Généric [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124).

### Autres changements
- Correction d'un problème lié au lockfile empêchant le déploiement en pré-production [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133).
- Déplacement du script SQL `wagtail_french` pour résoudre un problème de déploiement Scalingo [#3134](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3134).
- Suppression temporaire de la comparaison visuelle dans les tests e2e [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136).
- Ajout d'un template pour les pages index et script de migration [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122).
- Correction d'un espace au-dessus du breadcrumb sur les pages produit [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121).
- Augmentation de la durée de rétention des sauvegardes de la webapp [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137).
- Nombreuses mises à jour de dépendances (voir les commits pour plus de détails).
