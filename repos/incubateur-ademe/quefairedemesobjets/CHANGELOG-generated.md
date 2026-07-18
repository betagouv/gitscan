## Changelog : quefairedemesobjets (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance de la plateforme, notamment au niveau des pipelines de données et des déploiements. Des corrections ont été apportées pour résoudre des problèmes de CI/CD et de synchronisation des bases de données. Des améliorations d'accessibilité et de l'expérience utilisateur ont également été intégrées, ainsi que des optimisations pour la recherche et la gestion des données.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité au clavier avec des focus plus clairs et des outlines pour l'autocomplete [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073).
- Amélioration du positionnement de l'autocomplete dans l'iframe de recherche [#2854](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2854).
- Ajout d'un panneau de débogage du score de recherche pour les utilisateurs bêta [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852).
- Ajout d'un template pour les pages index et script de migration [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122).
- Réduction de la duplication dans les Makefiles [#3089](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3089).
- Amélioration de la gestion des suggestions avec correction des coordonnées géographiques incorrectes [#3097](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3097).
- Ajout d'actions en tâche de fond dans l'admin Django [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093).

### Évolutions techniques
- Mise à jour des pipelines Airflow pour enrichir les données SIREN à partir des SIRET et vice-versa [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125).
- Correction des DAGs CMA et Généric [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124).
- Amélioration de la stabilité des tests e2e et correction de la CI en échec [#3151](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3151).
- Mise à jour du script de restore de la base de données sample pour plus d'efficacité [#3090](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3090).
- Utilisation de named volumes dans le fichier docker-compose.yml [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130).
- Restructuration des settings Django pour une meilleure organisation [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060).
- Amélioration de la gestion des connexions à la base de données pour éviter les timeouts [#3074](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3074).
- Correction d'un problème de lockfile empêchant le déploiement en preprod [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133).
- Déplacement du script SQL wagtail_french pour résoudre les problèmes de déploiement Scalingo [#3134](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3134).
- Implémentation d'environnements de preview [#3065](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3065).
- Mise en place d'un processus de review régulière des comptes Django et Airflow [#3070](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3070).

### Autres changements
- Documentation mise à jour concernant les accès à donner ou retirer [#3077](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3077).
- Augmentation de la durée de rétention des backups de la webapp [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137).
- Désactivation temporaire de la comparaison visuelle e2e [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136).
- Correction d'un espace au-dessus du breadcrumb sur les pages produit [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121).
- Correction de la synchro prod > preprod en utilisant le DSN au lieu de Docker [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135).
- Amélioration de la gestion des relations et des locations dans les dataframes partagées entre les jobs d'un DAG [#3092](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3092).
- Limitation du contenu sur la version iframe de l'assistant [#3013](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3013).
- Suppression des tables temporaires après l'action principale dans Airflow [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095).
- Diverses mises à jour de dépendances (bleach, dbt-postgres, msgpack, dompurify, etc.).
