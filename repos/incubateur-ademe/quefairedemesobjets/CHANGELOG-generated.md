## Changelog : quefairedemesobjets (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de l'accessibilité. Des corrections de bugs ont été apportées, et l'infrastructure a été mise à jour avec de nombreuses dépendances. Des améliorations de la gestion des données et de l'architecture ont également été réalisées.

### Évolutions fonctionnelles
- Amélioration du positionnement de l'autocomplétion dans l'iframe de recherche [#2854](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2854).
- Réduction des marges sur le fil d'ariane des pages produit [#2993](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2993).
- Limitation du contenu affiché dans la version iframe de l'assistant [#3013](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3013).
- Ajout d'un panneau de débogage du score de recherche pour les utilisateurs en version bêta [#2852](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2852).
- Affichage de la famille de produits dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2827).
- Correction d'une erreur 500 sur l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853).
- Amélioration de l'accessibilité (RGAA) avec correction de non-conformités bloquantes et mineures [#2777](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2777), [#2794](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2794).
- Ajout d'une légende à la carte dans l'administration des suggestion groupe.
- Correction du bouton "Voir la fiche" en mode liste (régression) [#2868](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2868).

### Évolutions techniques
- Mise à jour de la gestion des connexions à la base de données pour éviter les timeouts [#3074](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3074).
- Utilisation de `django_setup_full` dans les fonctions pour assurer une configuration correcte [#3075](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3075).
- Ré-application des splits par fuzzy et par distance après le traitement intra-source [#2822](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2822).
- Mise en place d'un processus de revue régulière des comptes Django et Airflow [#3070](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3070).
- Calcul du sample de la base de données Webapp à partir de la production [#3069](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3069).
- Correction de l'encodage des propositions de service après la migration vers Airflow v3 [#2870](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2870).
- Mise à jour de la CLI de Scaleway dans la supply chain [#2856](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2856).
- Suppression des espaces autour des emails [#3014](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3014).
- Ajout de documentation pour la sécurité et les Agents IA [#2495](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2495).
- Mise à jour des paramètres de DAG pour définir `dry_run` et `use_legacy` à `False` par défaut [#3057](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3057).
- Empêcher l'indexation de la preprod par une variable d'environnement [#3017](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3017).

### Autres changements
- Regroupement des dépendances dans Dependabot pour une meilleure gestion [#3059](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3059).
- Mise à jour de nombreuses dépendances (voir les commits Dependabot).
- Renommage de certains éléments de l'interface utilisateur pour plus de clarté (ex: "En savoir plus sur ce site" -> "En savoir plus sur cet outil") [#3018](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3018).
- Ajout du header `X-Robots-Tag` pour contrôler l'indexation [#3022](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3022).
- Ajout de commentaires et de tests assistés par LLM.
- Correction de l'affichage du terme recherché dans l'iframe.
- Amélioration de la conformité aux maquettes.
- Ajout de paramètres UTM pour le suivi.
- Correction de l'affichage des doublons dans la recherche.
- Mise en place d'une commande pour purger les IndexEntry orphelines.
- Mise à jour des fichiers de lock Terragrunt après le déploiement de Airflow v3 en production.
