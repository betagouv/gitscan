## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la stabilité et des performances de la plateforme, notamment en mettant à jour Django et en optimisant le moteur de recherche. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, en particulier sur la carte et l'interface d'administration. Des améliorations ont également été apportées à la gestion des données et à l'infrastructure de déploiement.

### Évolutions fonctionnelles
- Correction d'une erreur de géolocalisation sur Chrome [#2596](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2596).
- Amélioration du moteur de recherche, notamment avec l'ajout de synonymes et de variantes pour une recherche plus pertinente [#2569](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2569) et [#2591](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2591).
- Correction du script de génération de la base de données de test [#2592](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2592).
- La fonctionnalité de redirection de l'administration Django vers Wagtail est de nouveau fonctionnelle [#2589](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2589).
- Amélioration de l'affichage des acteurs à domicile, ne filtrant plus sur le code postal et la ville [#2512](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2512).
- Correction de l'affichage du pied de page de l'assistant en iframe [#2516](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2516).
- Calcul du taux d'acteur empilés en fonction de la date [#2500](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2500).
- Le type d'acteur renvoyé par la CMA est maintenant correctement identifié comme "artisan" [#2496](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2496).
- Calcul de la distance à la solution la plus proche par geste [#2487](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2487).

### Évolutions techniques
- Mise à jour de Django vers la version 6.0 [#2588](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2588).
- Amélioration de la vitesse de la CI/CD [#2583](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2583).
- Mise à jour de Sites Faciles vers Sites Conformes [#2585](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2585) et [#2544](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2544).
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance [#2523](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2523).
- Suppression de modèles inutilisés (Familles, Bonus) [#2513](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2513).
- Suppression de purgecss [#2551](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2551).
- Mise à jour de nombreuses dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour de la documentation pour le déploiement des containers Scaleway [#2468](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2468).
- Ajout d'espace de stockage pour supporter les DAG de clone de l'Annuaire Entreprise [#2577](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2577).
- Correction des DAGs de clone de table à partir de fichiers geodata [#2575](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2575).
- Mise à jour de plusieurs dépendances : `actions/download-artifact`, `dbt-common`, `svgo`, `minimatch`, `@fullhuman/postcss-purgecss`, `eslint-config-love`, `prettier`, `astral-sh/ruff-action`, `ruff`, `docker/login-action`, `@iframe-resizer/parent`, `@iframe-resizer/child`, `maplibre-gl`, `apache-airflow-providers-amazon`, `django-debug-toolbar`, `orjson`, `apache-airflow-providers-postgres`, `ajv`, `posthog-js`, `sentry-sdk` (mises à jour automatiques par Dependabot).
- Ajout de tests de non-régression [#2527](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2527).
- Ré-organisation du code [#2546](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2546).
- Suppression de la lib `tqdm` qui n'est plus utilisée [#2542](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2542).
- Ajout d'un script de déploiement [#2517](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2517).
- Amélioration des tests e2e [#2595](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2595) et correction de tests e2e [#2598](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2598) et [#2336](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2336).
