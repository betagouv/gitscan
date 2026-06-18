## Changelog : quefairedemesobjets (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la recherche et l'accessibilité. Des corrections de bugs et des mises à jour de dépendances ont également été réalisées pour assurer la stabilité et la sécurité de la plateforme. Une migration vers Airflow v3 a été entreprise et est en cours de finalisation.

### Évolutions fonctionnelles
- Amélioration de la recherche : correction d'une erreur 500 lors de l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
- Affichage de la famille de produits dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2827).
- Correction du bouton "Voir la fiche" en mode liste sur les pages produit (correction d'une régression) [#2868](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2868).
- Ajout d'une légende à la carte dans l'administration des suggestion groupe.
- Mise à jour des données "Sites Conformes" [#2825](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2825).
- Amélioration de l'affichage des propositions de service depuis la migration vers Airflow v3 [#2870](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2870).

### Évolutions techniques
- Migration vers Airflow v3 en cours : adaptation du code et de l'infrastructure pour supporter la nouvelle version d'Airflow [#2568](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2568) et [#2832](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2832).
- Mise à jour de nombreuses dépendances : plusieurs bibliothèques et frameworks ont été mis à jour vers leurs dernières versions stables (Django, Airflow, PostgreSQL, React, etc.).
- Amélioration de la gestion des environnements et des variables d'environnement pour la preprod et la production.
- Optimisation du processus de purge des IndexEntry orphelines pour améliorer les performances de la recherche.
- Refonte de la configuration de la supply chain pour utiliser la version v1 du CLI Scaleway.
- Suppression des espaces autour des emails dans le code.
- Correction de problèmes d'encodage des propositions de service.

### Autres changements
- Amélioration de l'accessibilité (RGAA) : corrections de non-conformités mineures et implémentation de nouvelles fonctionnalités pour améliorer l'accessibilité de la plateforme [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777) et [#2794](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2794).
- Ajout de documentation pour la sécurité et les Agents IA [#2495](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2495).
- Ajout de tests LLM-assistés.
- Modification du nom d'un libellé ("En savoir plus sur ce site" -> "En savoir plus sur cet outil") [#3018](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3018).
- Ajout d'un header `X-Robots-Tag` pour améliorer le référencement.
- Groupement des dépendances de Dependabot pour une meilleure gestion.
- Suppression de l'environnement Airflow et modification du nom des environnements.
- Mise à jour des fichiers de lock Terragrunt après le déploiement d'Airflow v3 en production.
- Ajout de variables d'environnement pour contrôler le comportement de l'indexation.
- Correction de l'utilisation des paramètres `dry_run` et `use_legacy` dans les DAG Airflow.
