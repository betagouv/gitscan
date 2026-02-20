## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche, de l'affichage des acteurs et de la cartographie. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des efforts ont également été déployés pour optimiser les performances et la maintenance du code, ainsi que pour améliorer la qualité des données.

### Évolutions fonctionnelles
- Correction du pinpoint de la fiche acteur en mode liste pour afficher la bonne localisation et le bouton "Itinéraire" (#2550, #2414).
- Amélioration de la recherche d'objets avec l'ajout de synonymes et de variantes (#2435), puis rétractation de cette fonctionnalité en raison de problèmes (#2550).
- Ajout d'une section "comment tester" dans le template des Pull Requests pour faciliter les tests (#2520).
- Amélioration de l'affichage des acteurs inactifs et des corrections (#2522).
- Ajout de la possibilité de filtrer les acteurs sur la carte par sources (#2474).
- Correction de l'affichage du logo sur la page d'accueil en mode iframe (#2441).
- Amélioration de l'affichage des sous-catégories dans l'admin Django pour les produits (#2410).
- Ajout d'un bouton d'information à la modale des filtres en mode mobile (#2412).
- Correction de l'URL de health check du scheduler (#2434).
- Ajout d'une colonne "rapporter" dans le jeu de données open-data (#2428).

### Évolutions techniques
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance (#2523).
- Suppression de `purgecss` (#2551).
- Suppression de dépendances inutilisées (wagtail-honeypot, api-insee) (#2473).
- Mise à jour de Sites Faciles vers Sites Conformes (#2544).
- Passage sur Carte Faciles (#2429).
- Suppression de modèles Django non utilisés (Familles, Bonus) (#2513).
- Utilisation de la CLI Scaleway dans les actions GitHub (#2295).
- Mise à jour de Django vers la version 5.11 (#2519).
- Utilisation de `logger` au lieu de `logging` (#2452).
- Suppression du dossier `etl` et des anciennes tables clonées (#2461, #2462).
- Correction du script d'export de la base de données de test (#2473).
- Plusieurs mises à jour de dépendances (voir section "Autres changements").

### Autres changements
- Mises à jour de nombreuses dépendances : eslint, @iframe-resizer, astral-sh/setup-uv, @playwright/test, posthog-js, sentry-sdk, apache-airflow-providers-postgres, django-admin-sortable2, @fullhuman/postcss-purgecss, parcel, prettier, astral-sh/ruff-action, dbt-postgres, @types/node, boto3, sphinxcontrib-mermaid, postcss-nesting, @hotwired/turbo.
- Correction de l'affichage des icônes du générateur d'infotri (#2548).
- Ajout de composants sites conformes manquants (#2545).
- Correction de bugs visuels (centrage sur la homepage, espacements sur les fiches produit) (#2499).
- Suppression de la variante touch n drag de la fiche acteur en mobile (#2515).
- Ajout d'un saut de ligne dans le texte d'intro du widget info-tri (#2455).
- Correction d'une faute d'orthographe sur le widget info-tri (#2442).
- Modification des textes et hyperliens du contenu info-tri (#2440).
- Ajout de tests pour l'affichage de l'acteur en mode liste (#2521).
- Suppression de la librairie `tqdm` qui n'est plus utilisée (#2542).
- Comparaison SIREN et SIRET des acteurs (#2524).
- Ajout d'un script de déploiement (#2377a17).
- Correction de la définition du `map_container_id` sur les cartes sur mesure (#2408).
- Amélioration de la gestion du mode debug de PostHog (#2406).
- Correction d'un problème d'alignement de l'infotri (#2411).
- Rendre le nom de l'acteur cliquable en mode liste (#2413).
- Suppression du contenu de la description si égale aux consignes d'accès (#2517).
- Ajout d'un revert pour la recherche objet du header (#2471).
- Correction du problème du pinpoint home qui s'affiche sans qu'on le souhaite (#2472).
- Suppression de la variante touch n drag de la fiche acteur en mobile (#2515).
- Restauration de la base de données locale avec les données de preprod (#2453).
