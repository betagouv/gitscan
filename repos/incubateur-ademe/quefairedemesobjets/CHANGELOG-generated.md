## Changelog : quefairedemesobjets (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la migration vers Airflow v3, l'amélioration de l'accessibilité du site, et l'ajout de nouvelles fonctionnalités pour la recherche et la gestion des données, notamment concernant les propositions de services et les sources de données. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Recherche :** Correction d'une erreur 500 lors de l'import des synonymes de recherche pour la page vélo [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
- **Affichage des résultats de recherche :** Affichage de la famille de l'objet dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2827).
- **Carte :** Ajout d'une légende à la carte dans l'administration des suggestion groupe [#1ac3667](https://github.com/incubateur-ademe/quefairedemesobjets/commit/1ac3667).
- **Carte (Mobile) :** Affichage de la mini carte sur mobile dans la fiche détaillée [#2797](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2797).
- **A/B Testing :** Mise en place d'un A/B test pour choisir le mode d'affichage par défaut (carte/liste) sur les pages produit en version mobile [#2795](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2795).
- **Sources de données :** Ajout d'une source de données générique configurable pour répondre à des besoins spécifiques [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).
- **SuggestionGroupe :** Amélioration de la gestion des corrections sur les groupes de suggestions [#2802](https://github.com/incubateur-ademe/quefairedemesobjets/commit/6aaaa26).
- **SuggestionGroupe :** Ajout de filtres pour les suggestion groupe ayant des corrections [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801).

### Évolutions techniques
- **Airflow :** Migration vers Airflow v3 [#2568](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2568) et adaptation du pipeline de données pour cette nouvelle version [#2832](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2832).
- **Scaleway CLI :** Mise à jour de la version de la CLI Scaleway dans la chaîne de déploiement [#2856](https://github.com/incubateur-ademe/quefairedemesobjets/commit/1d8e874).
- **Accessibilité :** Corrections pour améliorer l'accessibilité du site selon les normes RGAA, incluant des corrections bloquantes [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777) et mineures [#2794](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2794).
- **Autocomplete :** Utilisation d'un nouveau composant d'autocomplétion pour le champ adresse de la carte [#2793](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2793).
- **Propositions de service :** Correction d'un problème d'encodage des propositions de service suite à la migration vers Airflow v3 [#2870](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2870).
- **Calcul de différences :** Implémentation du calcul des différences entre les propositions de service et leurs révisions [#2539](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2539).

### Autres changements
- **Documentation :** Mise à jour des sites conformes [#2825](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2825).
- **Nettoyage de code :** Suppression de fichiers inutiles [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- **Tests :** Correction de tests e2e [#2806](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2806).
- **Configuration :** Mise à jour du fichier de lock Terragrunt après le déploiement de Airflow v3 en production [#cf33deb](https://github.com/incubateur-ademe/quefairedemesobjets/commit/cf33deb).
- **Migration :** Ajout d'une migration manquante [#cd330de](https://github.com/incubateur-ademe/quefairedemesobjets/commit/cd330de).
