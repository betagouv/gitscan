## Changelog : quefairedemesobjets (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité du site, la correction de bugs et l'optimisation de la recherche. Des mises à jour de dépendances importantes ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme. Des améliorations de l'infrastructure et du pipeline CI/CD ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité au clavier, notamment pour le focus des panneaux et l'autocomplétion. [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073)
- Ajout d'un panneau de débogage du score de recherche pour les utilisateurs en version bêta. [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852)
- Correction d'un bug empêchant l'affichage correct du terme recherché dans la fiche détaillée en mode iframe. [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853)
- Correction d'un bug lié aux doublons dans les résultats de recherche. [#3076](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3076)
- Amélioration de l'affichage de la famille de produits dans les résultats de recherche. [#2827](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2827)
- Ajout de la légende à la carte dans l'administration des groupes de suggestions. [#2858](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2858)

### Évolutions techniques
- Mise à jour de l'infrastructure Airflow : passage à la version 3 et correction de problèmes d'encodage. [#2870](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2870), [#2991](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2991)
- Amélioration du processus de review des comptes Django et Airflow pour renforcer la sécurité. [#3070](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3070)
- Refonte du processus de build et de déploiement avec des regroupements de dépendances plus efficaces. [#3059](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3059)
- Mise à jour de nombreuses dépendances (Django, Airflow, psycopg, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance. (Voir les nombreux commits dependabot)
- Correction de problèmes liés à la gestion des intervalles de temps dans le traitement des données. [#2822](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2822)
- Amélioration de la gestion des connexions à la base de données pour éviter les timeouts. [#3074](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3074)

### Autres changements
- Ajout de documentation concernant la sécurité et l'utilisation d'Agents IA. [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495)
- Suppression des espaces autour des adresses e-mail dans le code. [#3014](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3014)
- Mise à jour des fichiers de lock Terragrunt après le déploiement de Airflow v3 en production. [#2856](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2856)
- Suppression de l'environnement Airflow et modification des noms des environnements. [#2872](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2872)
- Ajout de variables d'environnement pour empêcher l'indexation de la pré-production par les moteurs de recherche. [#3017](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3017)
