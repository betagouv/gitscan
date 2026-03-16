## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration du moteur de recherche, la correction de bugs et la mise à jour des dépendances pour assurer la stabilité et la performance de la plateforme. Des améliorations ont également été apportées à l'administration et à l'intégration de nouveaux services comme Sites Conformes. Des efforts ont été déployés pour optimiser les données et les processus de clonage de tables.

### Évolutions fonctionnelles
- Amélioration du moteur de recherche avec l'ajout de synonymes et de variantes pour une recherche plus pertinente [#2435](https://github.com/incubateur-ademe/quefairedemesobjets/pull/2435).
- Correction d'un bug empêchant la redirection vers les acteurs affichés [#2514](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2514).
- Correction de l'affichage des icônes dans le générateur d'infotri [#2543](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2543).
- Mise à jour de l'intégration avec Sites Conformes (anciennement Sites Faciles) [#2544](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2544), [#2585](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2585).
- Correction d'une erreur de géolocalisation sur Chrome [#2596](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2596).
- Amélioration des tests e2e pour une meilleure couverture et fiabilité [#2588](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2588), [#2595](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2595).
- Correction de la fonctionnalité de redirection de l'admin Django vers Wagtail [#2589](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2589).
- Mise à jour de Wagtailmenus et Django [#2578](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2578).
- Correction de bugs sur le moteur de recherche dans l'administration [#2584](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2584) et [#2591](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2591).

### Évolutions techniques
- Mise à jour de Django vers la version 6.0 [#2588](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2588).
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance [#2523](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2523).
- Création de DAGs Airflow pour cloner les tables des liens de succession d'entreprise [#2579](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2579).
- Suppression de modèles DBT obsolètes et alignement des noms par convention [#2576](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2576).
- Correction du notebook de clustering pour la localisation et le type d'acteur [#2610](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2610).
- Ajout d'un notebook pour générer des suggestions de cluster à partir d'un CSV [#2609](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2609).
- Amélioration de la vitesse de la CI/CD [#2583](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2583).
- Suppression de la librairie `tqdm` non utilisée [#2542](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2542).
- Correction des permissions de la CD [#2571](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2571).
- Suppression de purgecss [#2551](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2551).

### Autres changements
- Mise à jour de la documentation pour le déploiement des containers Scaleway [#2468](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2468).
- Renommage de LVAO en "Que faire de mes objets et déchets" [#2600](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2600).
- Mise à jour de la documentation pour la résolution de la CI [#2570](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2570).
- Correction pour ne pas valider les formulaires Wagtail sans validateur [#2607](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2607).
- Correction pour ne pas collecter les identifiants des dataframes vides [#2602](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2602).
- Mise à jour de l'URL des objets de type Source [#2608](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2608).
- Mise à jour de l'ordre d'affichage : réparation avant réemploi [#2603](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2603).
- Correction pour ne pas souligner les liens dans l'admin [#2601](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2601).
- Correction de la détection des corrections affichées avec des acteurs inactifs [#2522](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2522).
- Mise à jour de diverses dépendances (eslint, playwright, posthog-js, sentry-sdk, apache-airflow-providers-postgres, django-admin-sortable2, etc.).
