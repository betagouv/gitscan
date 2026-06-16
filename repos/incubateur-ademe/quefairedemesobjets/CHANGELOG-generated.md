## Changelog : quefairedemesobjets (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité du site, la correction de bugs liés à la recherche et à l'affichage des données, ainsi que la mise à niveau de l'infrastructure technique avec la migration vers Airflow v3 et la mise à jour de nombreuses dépendances. Des améliorations ont également été apportées à l'interface d'administration et à la gestion des données.

### Évolutions fonctionnelles

*   Correction d'un bug empêchant l'affichage correct du bouton "Voir la fiche" en mode liste. [#2868](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2868)
*   Amélioration de l'affichage de la famille d'un objet dans les résultats de recherche pour tous les utilisateurs. [#2827](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2827)
*   Ajout d'une légende à la carte dans l'administration des groupes de suggestions.
*   Correction d'une erreur 500 lors de l'import des synonymes de recherche (page vélo). [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853)
*   Implémentation d'un A/B test pour l'affichage par défaut des pages produit en mode mobile (carte ou liste). [#2795](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2795)
*   Correction de problèmes d'encodage des propositions de service suite à la migration vers Airflow v3. [#2870](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2870)
*   Correction d'un problème lié au tri des intervalles dans Airflow v3. [#2991](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2991)
*   Ajout de documentation concernant la sécurité et les Agents IA. [#2495](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2495)

### Évolutions techniques

*   Migration vers Airflow v3. [#2568](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2568)
*   Mise à jour de nombreuses dépendances (Django, Airflow, boto3, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
*   Suppression des espaces autour des emails pour une meilleure conformité. [#3014](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3014)
*   Empêchement de l'indexation de l'environnement de pré-production par une variable d'environnement. [#3017](https://github.com/incubateur-ademe/quefiredemesobjets/issues/3017)
*   Mise à jour de la CLI Scaleway dans la supply chain. [#2856](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2856)
*   Amélioration de la gestion des groupes de dépendances avec Dependabot. [#2981](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2981)

### Autres changements

*   Améliorations de l'accessibilité RGAA : correction de non-conformités bloquantes et mineures. [#2777](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2777), [#2794](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2794)
*   Utilisation du nouvel autocomplete pour le champ adresse de la carte. [#2793](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2793)
*   Mise à jour de la base de données `db_mapping.json`. [#2829](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2829)
*   Correction d'un problème où une recherche synonyme était conservée lors de la navigation. [#2826](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2826)
*   Correction d'une erreur lors de la purge des `IndexEntry` orphelines.
*   Amélioration de la conformité aux maquettes.
*   Ajout de commentaires et de tests assistés par LLM.
*   Ajout de paramètres UTM.
*   Amélioration de la gestion des actions applicables à un ensemble de `SuggestionGroupe`.
*   Correction d'un problème avec les float dans l'interface Airflow v3.
*   Ajout d'une commande pour aligner les propositions de service. [#2866](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2866)
