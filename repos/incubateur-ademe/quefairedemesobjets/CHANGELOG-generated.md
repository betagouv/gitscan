## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la qualité du code, la correction de bugs et l'optimisation des performances, notamment au niveau du moteur de recherche et de l'administration. Des améliorations ont également été apportées à l'infrastructure et aux tests, ainsi qu'à la documentation pour faciliter le déploiement. Une migration vers Django 6.0 a été effectuée, avec un rollback ultérieur dû à des problèmes d'interface.

### Évolutions fonctionnelles
- Amélioration du moteur de recherche avec prise en compte des synonymes et variantes pour des résultats plus pertinents. [#2435](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2435)
- Correction d'un bug empêchant l'affichage correct des acteurs en mode liste. [#2521](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2521)
- Correction de l'affichage des icônes dans le générateur d'infotri. [#2543](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2543)
- Correction d'une erreur de géolocalisation sur Chrome. [#2596](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2596)
- Correction de bugs et améliorations des tests e2e pour une meilleure stabilité. [#2595](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2595) et [#2598](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2598)
- Correction du script de génération de la base de données de test. [#2592](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2592)
- Mise à jour de Sites Faciles vers Sites Conformes pour bénéficier de nouvelles fonctionnalités et corrections. [#2585](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2585) et [#2586](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2586)
- Amélioration de l'administration avec des corrections et des ajouts pour faciliter la gestion du contenu. [#2584](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2584)
- La fonctionnalité de redirection de l'admin Django vers Wagtail est de nouveau fonctionnelle. [#2589](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2589)

### Évolutions techniques
- Mise à jour de Django en version 6.0 (rollback effectué en raison de problèmes d'interface). [#2588](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2588)
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance. [#2523](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2523)
- Suppression de code obsolète (modèle dbt). [#2576](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2576)
- Ajout d'un DAG Airflow pour cloner les tables des liens de succession d'entreprise. [#2579](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2579)
- Amélioration de la vitesse de la CI/CD. [#2583](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2583)
- Suppression de PurgeCSS. [#2551](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2551)
- Ajout d'espace de stockage pour supporter les DAG de clone de Annuaire Entreprise. [#2577](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2577)

### Autres changements
- Mise à jour de la documentation pour le déploiement des containers Scaleway. [#2468](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2468)
- Ajout d'une section "comment tester" dans le template des pull requests. [#2520](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2520)
- Proposition de nouvelle stratégie de tagging pour les versions de déploiement. [#2494](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2494)
- Correction du notebook de clustering pour la localisation et le type d'acteur. [#2610](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2610)
- Création d'un notebook pour générer des suggestions de cluster à partir d'un CSV. [#2609](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2609)
- Correction de la validation des formulaires Wagtail. [#2607](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2607)
- Correction de l'export de l'URL des objets de type Source. [#2608](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2608)
- Suppression de l'affichage des identifiants dans les dataframes vides. [#2602](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2602)
- Modification du titre pour afficher la réparation avant le réemploi. [#2603](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2603)
- Renommage de LVAO en "Que faire de mes objets et déchets". [#2600](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2600)
- Suppression du soulignement des liens dans l'admin. [#2601](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2601)
- Correction de l'affichage des acteurs inactifs. [#2522](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2522)
- Suppression de la variante touch n drag de la fiche acteur en mobile. [#2515](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2515)
