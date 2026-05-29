## Changelog : quefairedemesobjets (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité du site, la correction de bugs et l'amélioration de la gestion des données, notamment en préparation de la migration vers Airflow v3. Des optimisations ont également été apportées à la recherche et à l'affichage des résultats.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité du site, notamment avec la correction de non-conformités RGAA bloquantes et mineures [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777).
- Utilisation d'un nouvel autocomplète pour le champ adresse sur la carte, améliorant l'expérience utilisateur [#2793](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2793).
- Correction d'une erreur 500 lors de l'import des synonymes de recherche sur la page vélo [#2853](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2853).
- Ajout d'un A/B test pour l'affichage par défaut de la carte ou de la liste sur les pages produit en version mobile [#2795](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2795).
- Affichage de la famille de l'objet dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2827).
- Ajout d'une légende à la carte dans l'administration des suggestion groupe [#1ac3667](https://github.com/incubateur-ademe/quefiredemesobjets/commit/1ac3667).
- Suppression du bouton "Infos" obsolète sur la carte [#2759](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2759).
- Possibilité de clusteriser les résultats par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2728).
- Ajout d'une nouvelle source générique configurable pour répondre à des besoins spécifiques [#2466](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2466).

### Évolutions techniques
- Préparation et migration vers Airflow v3 [#2568](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2568) et [#2832](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2832).
- Mise à jour du fichier de lock Terragrunt après le déploiement de Airflow v3 en production [#cf33deb](https://github.com/incubateur-ademe/quefiredemesobjets/commit/cf33deb).
- Correction des actions applicables à un ensemble de SuggestionGroupe [#d0e6376](https://github.com/incubateur-ademe/quefiredemesobjets/commit/d0e6376).
- Adaptation de la chaîne CI/CD GitHub à la version v1 du CLI Scaleway [#2855](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2855).
- Correction d'un problème de tests e2e [#2806](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2806).

### Autres changements
- Mise à jour de la base de données `db_mapping.json` [#2829](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2829).
- Suppression d'un fichier inutile [#2823](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2823).
- Diverses mises à jour de dépendances (Django, PyJWT, psycopg, etc.). Ces mises à jour sont effectuées via Dependabot et Renovate et visent à maintenir la sécurité et la stabilité du projet.
- Correction d'un problème empêchant la conservation d'une recherche synonyme lors de la navigation [#2826](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2826).
- Ajout de filtres `has_correction` et amélioration du filtre existant pour les suggestion groupe avec suggestion unitaire [#2801](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2801) et [#2796](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2796).
- Amélioration de la gestion des retries pour les health checks [#2763](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2763).
