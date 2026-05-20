## Changelog : quefairedemesobjets (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la cartographie des acteurs du réemploi et de la réparation, l'amélioration de la qualité des données via un modèle de déduplication, et la mise à jour de l'infrastructure technique. Des améliorations ont également été apportées au tracking et à l'expérience utilisateur, notamment sur la page de recherche et la carte.

### Évolutions fonctionnelles
- Amélioration de la carte : affichage de la mini carte sur mobile dans la fiche détaillée [#2797](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2797).
- Correction de l'affichage dupliqué du nom dans les résultats de recherche (Vélovélo) [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- Ajout du tracking des clics sur les résultats de recherche [#2722](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2722).
- Possibilité de clusteriser les résultats par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- Ajout d'une source générique configurable pour répondre à des besoins spécifiques [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).
- Ajout de filtres pour affiner les résultats : `has_correction` [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801) et suggestions groupées [#2796](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2796).
- Correction de tests e2e suite à des mises à jour de dépendances [#2806](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2806) et [#2736](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2736).
- Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2749).

### Évolutions techniques
- Migration vers Airflow V3 [#2568](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2568).
- Mise à jour de plusieurs dépendances (Django, psycopg, protobufjs, etc.).
- Amélioration de la gestion des erreurs et des retries pour les health checks [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- Refonte du tracking avec l'implémentation de `pageView` et d'événements [#2721](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2721).
- Première itération d'un modèle de Machine Learning pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2727).
- Calcul des différences de propositions de service entre un acteur et sa révision [#2539](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2539).

### Autres changements
- Mise à jour de la base de données `db_mapping.json` [#2829](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2829).
- Suppression de fichiers inutiles [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2756).
- Mise à jour des sites conformes [#2825](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2825).
