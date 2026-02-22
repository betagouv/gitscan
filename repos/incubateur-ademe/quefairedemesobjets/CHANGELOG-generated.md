## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Les dernières mises à jour de QueFaireDeMesObjets se concentrent sur l'amélioration de la qualité des données, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche, de la cartographie et de l'affichage des acteurs. Des efforts ont également été faits pour moderniser l'infrastructure et les dépendances du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct de la localisation et du bouton "Itinéraire" sur la fiche acteur en mode liste (#2414).
- Amélioration de la recherche d'objets avec l'ajout de synonymes et de variantes (#2435), puis rétractation suite à des problèmes (#2550).
- Correction de l'affichage des icônes du générateur d'infotri (#2548).
- Amélioration de la gestion des corrections et des sources de données pour les acteurs (#2456, #2459, #2460).
- Ajout de la possibilité de filtrer les acteurs par sources sur la carte (#2474).
- Correction du pinpoint home qui s'affichait sans qu'on le souhaite (#2472).
- Passage de la recherche objet du header en version DSFR (#2257) puis rétractation (#2471).
- Amélioration du footer avec le style DSFR et l'ajout des logos et du bouton "En savoir plus" (#2397).
- Ajout d'un saut de ligne dans le texte d'intro du widget info-tri (#2455) et correction d'une faute d'orthographe (#2442).
- Modification du pied de page de l'assistant en iframe (#2516) puis restauration (#2525).

### Évolutions techniques
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance (#2523).
- Suppression de `purgecss` (#2551) et de la librairie `tqdm` (#2542).
- Comparaison SIREN et SIRET des acteurs (#2524).
- Mise à jour de Sites Faciles vers Sites Conformes (#2544).
- Suppression de modèles Wagtail non utilisés (Familles, Bonus) (#2436).
- Utilisation de la CLI Scaleway dans les actions GitHub (#2295).
- Passage à Django 5.11 (#2519).
- Mise à jour de nombreuses dépendances (voir section "Autres changements").
- Ajout d'un script de déploiement (#2377).

### Autres changements
- Mise à jour de plusieurs dépendances : eslint, @iframe-resizer, astral-sh/setup-uv, @playwright/test, posthog-js, sentry-sdk, apache-airflow-providers-postgres, django-admin-sortable2, @fullhuman/postcss-purgecss, parcel, prettier, astral-sh/ruff-action, dbt-postgres, @types/node, boto3, sphinxcontrib-mermaid, apache-airflow-providers-amazon, postcss-nesting, @hotwired/turbo.
- Ajout de tests pour l'affichage des acteurs en mode liste (#2521).
- Ajout d'une section "comment tester" dans le template des Pull Requests (#2520).
- Amélioration de la définition du referrer de PostHog (#2407).
- Suppression de l'API INSEE (#2498).
- Nettoyage de code et suppression de fichiers inutilisés (#2461, #2462, #2491).
- Ajout d'indicateurs de qualité de données (#2464).
- Correction du script d'export de la base de données de test (#2473).
- Ajout de la colonne "rapporter" dans le jeu de données open-data (#2428).
- Correction de l'URL de health check du scheduler (#2434).
- Ajout de la gestion des styles du diff via des classes CSS (#2454).
- Utilisation de `logger` au lieu de `logging` (#2452).
- Restauration de la base de données locale avec les données de preprod (#2453).
- Suppression du dossier `etl` (#2461).
- Suppression des anciennes tables clonées (#2462).
- Correction des tests e2e suite à une migration de fiche vêtement (#2554).
