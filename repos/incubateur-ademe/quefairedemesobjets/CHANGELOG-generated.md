## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la qualité des données, la correction de bugs affectant l'expérience utilisateur et l'optimisation de l'infrastructure. Des améliorations ont été apportées à la recherche d'objets, à l'affichage des acteurs sur la carte, et à l'export des données. Plusieurs mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration du moteur de recherche avec prise en compte des synonymes et variantes pour une meilleure pertinence des résultats [#2569](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2569).
- Correction de l'affichage du pinpoint (localisation) sur la fiche acteur en mode liste, affichant désormais la bonne localisation et le bouton "Itinéraire" [#2414](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2414).
- Amélioration de la gestion des corrections et des sources de données, avec affichage de colonnes dédiées [#2456](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2456) et [#2459](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2459).
- Ajout de la possibilité de filtrer les acteurs sur la carte par sources [#2474](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2474).
- Correction du problème du pinpoint home qui s'affichait sans qu'on le souhaite [#2472](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2472).
- Passage de la recherche d'objet dans le header à la version DSFR [#2257](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2257).
- Suppression de l'export des adresses pour les acteurs uniquement domiciliés [#2460](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2460).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Wagtailmenus, Django, ajv, eslint, playwright, posthog-js, sentry-sdk, apache-airflow-providers-amazon, djangoql, pillow, boto3, @iframe-resizer/child, @parcel/watcher-linux-x64-glibc, astral-sh/setup-uv, maplibre-gl, ruff, docker/build-push-action, docker/login-action, release-drafter/release-drafter, minimatch.
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance [#2523](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2523).
- Suppression de code inutilisé : modèles Familles et Bonus, librairie tqdm [#2542](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2542) et [#2551](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2551).
- Mise à jour de la documentation pour le déploiement des containers Scaleway [#2468](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2468).
- Ajout d'espace de stockage pour supporter les DAG de clone de l'Annuaire Entreprise [#2577](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2577).
- Correction des DAGs de clone de table à partir de fichiers geodata [#2575](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2575).
- Utilisation de la CLI Scaleway dans les GitHub Actions [#2295](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2295).
- Suppression des dossiers et anciennes tables clonées [#2461](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2461) et [#2462](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2462).
- Ajout d'un script de déploiement [#2517](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2517).

### Autres changements
- Ajout de tests de non-régression [#2527](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2527).
- Réorganisation du code [#2546](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2546).
- Correction des permissions de la CD [#2571](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2571).
- Publication de la documentation et résolution de la CI [#2570](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2570).
- Ajout de la section "comment tester" dans le template des Pull Requests [#2520](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2520).
- Proposition pour tagger différemment les versions à déployer en preprod [#2494](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2494).
- Ajout d'un test pour l'affichage de l'acteur en mode liste [#2521](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2521).
- Correction d'un test e2e qui échouait après la migration d'une fiche vêtement vers Wagtail [#2554](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2554).
- Suppression de purgecss [#2551](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2551).
- Correction des icônes du générateur d'infotri [#2548](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2548).
- Comparaison SIREN et SIRET de Acteur et révision [#2524](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2524).
- Ajout de composants sites conformes manquants [#2545](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2545).
- Correctifs Infotri : script, icône [#2543](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2543).
- Détection des corrections affichées avec des acteurs inactifs [#2522](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2522).
- Mise à jour de Sites Faciles vers Sites Conformes [#2544](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2544).
- Correction d'un revert précédent [#2550](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2550).
