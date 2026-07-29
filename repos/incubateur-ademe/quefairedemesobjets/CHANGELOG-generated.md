## Changelog : quefairedemesobjets (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité de la plateforme, la correction de bugs et l'amélioration des processus de déploiement. Des travaux ont également été réalisés sur l'enrichissement des données et l'optimisation des pipelines de traitement.

### Évolutions fonctionnelles
- Suppression du filtrage des établissements avec un code étranger [#3216](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3216).
- Correction d'un bug empêchant la prévisualisation des pages Wagtail avec des accents dans le slug [#3195](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3195).
- Ajout d'actions en tâche de fond dans l'interface d'administration Django [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093).
- Correction d'un problème lié à l'espace au-dessus du fil d'Ariane sur les pages produit [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121).
- Ajout d'un template pour les pages index et script de migration [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122).

### Évolutions techniques
- Modification de la logique de clonage des données pour lancer (ou non) une commande DBT de consolidation [#3169](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3169).
- Utilisation de la fonction `chain` au lieu de l'opérateur `>>` pour une meilleure lisibilité du code [#3178](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3178).
- Première version de suggestion basée sur la table `lien_suggestion` [#3177](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3177).
- Restructuration des modèles DBT [#3170](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3170).
- Utilisation des workspaces uv [#3058](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3058).
- Passage des volumes Docker en named volumes pour une meilleure gestion [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130).
- Correction de la synchronisation entre la production et la pré-production en utilisant le DSN pour la restauration [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135).
- Amélioration de la stabilité des tests e2e [#3021](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3021).
- Restructuration des settings Django [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060).
- Mise à jour des dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour régulière des dépendances du projet (Python, JavaScript, etc.) via Dependabot et Renovate.
- Ajout d'un paramètre pour corriger les datasets de la BAN [#3199](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3199).
- Augmentation de la durée de rétention des sauvegardes de la webapp [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137).
- Désactivation temporaire de la comparaison visuelle dans les tests e2e [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136).
- Correction d'un problème de lockfile empêchant le déploiement en pré-production [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133).
- Déplacement du script SQL `wagtail_french` pour résoudre un problème de déploiement Scalingo [#3134](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3134).
- Ajout de la conservation de 15 jours d'historique de DAG dans Airflow [#3101](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3101).
- Suppression des tables temporaires après l'action principale [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095).
- DAG pour enrichir les SIREN depuis les SIRET et réciproquement [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125).
- Correction des DAGs CMA et Généric [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124).
