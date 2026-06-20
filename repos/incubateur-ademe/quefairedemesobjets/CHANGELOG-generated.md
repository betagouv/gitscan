## Changelog : quefairedemesobjets (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de l'accessibilité. Des corrections de bugs et des optimisations techniques ont également été apportées, ainsi qu'une migration vers Airflow v3 pour la gestion des tâches. De nombreuses mises à jour de dépendances ont été réalisées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Amélioration du positionnement de l'autocomplete dans l'iframe de recherche [#2854](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2854).
- Réduction des marges sur le fil d'ariane des pages produit [#2993](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2993).
- Limitation du contenu affiché dans la version iframe de l'assistant [#3013](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3013).
- Ajout d'un panneau de débogage du score de recherche pour les utilisateurs en version beta [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852).
- Affichage de la famille d'un objet dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2827).
- Correction d'une erreur 500 sur l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
- Amélioration de l'accessibilité (RGAA) avec correction de non-conformités bloquantes et mineures [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777), [#2794](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2794).
- Ajout d'un A/B test pour la carte/liste par défaut sur les pages produit en mode mobile [#2795](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2795).
- Correction du bouton "Voir la fiche" en mode liste [#2868](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2868).
- Correction d'un problème d'encodage des propositions de service après la migration vers Airflow v3 [#2870](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2870).

### Évolutions techniques
- Migration vers Airflow v3 pour la gestion des tâches et des workflows [#2832](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2832).
- Adaptation de la chaîne CI/CD à la nouvelle version du CLI Scaleway [#2855](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2855).
- Amélioration de la gestion des connexions à la base de données pour éviter les timeouts [#3074](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3074).
- Utilisation de `django_setup_full` dans les fonctions pour une meilleure initialisation [#3075](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3075).
- Processus de revue régulière des comptes Django et Airflow [#3070](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3070).
- Calcul du sample de la base de données Webapp à partir de la production [#3069](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3069).
- Correction de l'ordre des intervalles lors du traitement des données [#2988](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2988).
- Amélioration du regroupement des dépendances avec Dependabot [#3059](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3059).
- Suppression des espaces autour des adresses email [#3014](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3014).
- Mise à jour de la documentation pour la sécurité et les Agents IA [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495).
- Empêcher l'indexation de la preprod par une variable d'environnement [#3017](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3017).

### Autres changements
- Ajout de documentation pour la sécurité et les Agents IA [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495).
- Diverses mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.
- Correction de problèmes liés à la compilation des fichiers .map en production [#3074](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3074).
