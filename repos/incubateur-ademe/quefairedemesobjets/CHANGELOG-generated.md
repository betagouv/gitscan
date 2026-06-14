## Changelog : quefairedemesobjets (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de l'accessibilité. Une migration majeure vers Airflow v3 a été entreprise pour moderniser l'infrastructure de traitement des données. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles

*   **Recherche :**
    *   Correction d'une erreur 500 sur l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
    *   Correction d'un bug où les doublons apparaissaient dans les résultats de recherche lorsque le terme recherché correspondait à une variante. [#2826](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2826)
    *   Affichage de la famille du produit dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2827).
    *   Amélioration de l'autocomplete pour le champ adresse sur la carte [#2793](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2793).
*   **Accessibilité :**
    *   Corrections des non-conformités RGAA mineures [#2794](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2794) et corrections des retours bloquants RGAA [#2777](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2777).
*   **Interface utilisateur :**
    *   Correction du bouton "Voir la fiche" en mode liste (régression) [#2868](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2868).
    *   Ajout d'une légende à la carte dans l'administration des suggestion groupe.
    *   A/B test du mode carte/liste par défaut sur les pages produit en mobile [#2795](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2795).
*   **Données :**
    *   Mise à jour des données "Sites Conformes" [#2825](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2825).
    *   Mise à jour de la base de données de mapping [#2829](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2829).

### Évolutions techniques

*   **Infrastructure :**
    *   Migration vers Airflow v3 pour moderniser le pipeline de données [#2568](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2568).
    *   Adaptation de la chaîne CI/CD à la version v1 du CLI Scaleway [#2855](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2855).
    *   Suppression de l'environnement Airflow précédent et modification des noms d'environnement [#2872](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2872).
*   **Dépendances :**
    *   Mise à jour de nombreuses dépendances (Django, Airflow, psycopg, etc.) pour améliorer la sécurité et la stabilité.
*   **Divers :**
    *   Amélioration de la gestion des groupes de dépendances dans Dependabot [#2981](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2981).
    *   Correction pour gérer correctement les float dans l'interface Airflow v3 [#2991](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2991).
    *   Commande pour aligner les propositions de service [#2866](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2866).
    *   Correction pour éviter qu'une recherche synonyme ne soit conservée lors de la navigation.

### Autres changements

*   Encodage et décodage en JSON de la clé `DF_PARENTS_CHOOSE_DATA` [#2992](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2992).
*   Ajout de tests et de commentaires assistés par LLM [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853).
*   Ajout de `utm` pour le suivi des campagnes.
*   Amélioration de la conformité aux maquettes [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853).
*   Purge des `IndexEntry` orphelines avec une commande et lors des builds CI [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853).
*   Correction d'un bug lié à la mention du terme recherché sur la fiche.
*   Renommage de certains éléments de code.
*   Améliorations diverses du code.
*   Mise à jour du fichier de lock Terragrunt après déploiement de Airflow v3 en production.
*   Correction de la version de la CLI Scaleway dans la supply chain.
*   Correction de la compilation des fichiers `.map` en production.
