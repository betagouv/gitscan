## Changelog : quefairedemesobjets (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance de la plateforme, notamment au niveau des pipelines de données (Airflow, DBT) et de l'infrastructure. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, en particulier concernant la recherche et l'accessibilité. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la compatibilité.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité : amélioration de la navigation au clavier et du focus sur les panneaux, ajout d'outlines pour l'autocomplete, et amélioration des infotrips. [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073)
- Correction d'un bug : résolution de doublons dans les résultats de recherche lorsque le terme recherché correspondait à une variante. [#3090](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3090)
- Correction d'un bug : correction du bouton "Voir la fiche" en mode liste. [#2868](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2868)
- Ajout d'un panneau de débogage pour le score de recherche pour les utilisateurs en version beta. [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852)
- Mise à jour de la documentation d'onboarding concernant les accès. [#3094](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3094)
- Ajout d'une commande pour réparer les Suggestions avec des mauvaises coordonnées géographiques. [#3097](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3097)
- Ajout d'une commande pour aligner les propositions de service. [#2866](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2866)

### Évolutions techniques
- Optimisation des timeouts Nginx pour améliorer la réactivité. [#3091](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3091)
- Augmentation de la rétention des logs DAG dans Airflow à 15 jours. [#3101](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3101)
- Amélioration de la gestion des relations et des localisations dans les jobs Airflow. [#3092](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3092)
- Refactorisation pour éviter l'utilisation de sources non-basiques dans les modèles DBT. [#3072](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3072)
- Amélioration de la gestion des connexions à la base de données pour éviter les timeouts. [#3074](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3074)
- Suppression des espaces autour des adresses email. [#3014](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3014)
- Mise en place d'un processus de revue régulière des comptes Django et Airflow. [#3070](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3070)
- Suppression de l'environnement Airflow et modification des noms d'environnements. [#2872](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2872)
- Désactivation de la compilation des fichiers `.map` en production. [#2921](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2921)
- Amélioration de la gestion des erreurs et de la robustesse des pipelines de données.
- Réduction de la duplication dans les Makefile. [#3089](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3089)

### Autres changements
- Mise à jour de la documentation pour la sécurité et les Agents IA. [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495)
- De nombreuses mises à jour de dépendances ont été intégrées pour améliorer la sécurité et la stabilité.
- Amélioration de la configuration de Dependabot pour inclure toutes les dépendances. [#2874](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2874)
- Ajout de variables d'environnement pour contrôler l'indexation par les moteurs de recherche. [#3017](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3017)
- Amélioration du groupage des dépendances dans Dependabot. [#3059](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3059)
- Amélioration de la gestion des erreurs dans les scripts de restauration de la base de données. [#3090](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3090)
