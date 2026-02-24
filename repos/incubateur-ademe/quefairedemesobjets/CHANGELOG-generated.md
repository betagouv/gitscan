## Changelog : quefairedemesobjets (30 derniers jours)

### Résumé
Les dernières mises à jour de "Que faire de mes objets" se concentrent sur l'amélioration de la qualité des données, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de la cartographie et de l'interface. Des optimisations techniques ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un test e2e qui échouait suite à une migration de fiches vêtements (#2554).
- Correction des icônes du générateur d'infotri (#2548).
- Correction de l'affichage du pinpoint et du bouton "Itinéraire" sur la fiche acteur en mode liste (#2551, #2414).
- Amélioration de l'affichage des acteurs inactifs dans les corrections (#2522).
- Ajout de la possibilité de filtrer les acteurs par sources dans l'export Open-Data (#2428).
- Correction d'un problème où le pinpoint de la fiche acteur en mode liste n'affichait pas la bonne localisation (#2551).
- Amélioration du header avec le logo en mode iframe (#2398, #2458).
- Ajout de meta tags Wagtail sur la page d'accueil (#2457).
- Correction de fautes d'orthographe et amélioration des textes et hyperliens du widget info-tri (#2442, #2440).
- Restauration de la base de données locale avec les données de preprod (#2453).
- Correction du script d'export de la base de données de test (#2473).

### Évolutions techniques
- Refactorisation des tables `exposure_stats` pour faciliter la maintenance (#2523).
- Comparaison SIREN et SIRET des acteurs (#2524).
- Suppression de `purgecss` (#2551).
- Suppression de modèles Wagtail non utilisés (Familles, Bonus) (#2436).
- Suppression du dossier etl et des anciennes tables clonées (#2461, #2462).
- Utilisation de la CLI Scaleway dans les actions GitHub (#2295).
- Utilisation de `logger` au lieu de `logging` (#2452).
- Passage sur Carte Faciles (#2429).
- Upgrade de Django en version 5.11 (#2519).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour de nombreuses dépendances : `ajv`, `@fullhuman/postcss-purgecss`, `@iframe-resizer/child`, `@iframe-resizer/parent`, `@playwright/test`, `@types/node`, `apache-airflow-providers-amazon`, `apache-airflow-providers-postgres`, `astral-sh/ruff-action`, `astral-sh/setup-uv`, `boto3`, `django-admin-sortable2`, `djangoql`, `eslint`, `hotwired/turbo`, `lodash`, `orjson`, `parcel`, `postcss-nesting`, `prettier`, `protobuf`, `posthog-js`, `ruff`, `sentry-sdk`, `sphinxcontrib-mermaid`, `uv`.
- Ajout d'un saut de ligne dans le texte d'intro du widget info-tri (#2455).
- Ajout d'une colonne "rapporter" dans le jeu de données Open-Data (#2428).
- Ajout de sections "comment tester" dans les templates de Pull Request (#2520).
- Suppression de la lib `tqdm` (#2542).
- Correction d'un revert de la fonctionnalité de synonymes dans le moteur de recherche (#2550).
- Ajout d'un script de déploiement (#2517).
- Revert d'une modification du pied de page de l'assistant en iframe (#2525).
- Proposition pour tagger différemment les versions à déployer en preprod (#2494).
- Suppression du contenu de la description si égale aux consignes d'accès (#2517).
- Ajout d'indicateurs de qualité de données (#2464).
- Correction de l'URL de health check du scheduler (#2434).
- Interprétation des colonnes Facebook et Instagram quand la colonne website n'est pas disponible (#2439).
- Ne pas filtrer les anciens acteurs de LVAO dans Open-Data (#2432).
- Ne pas filtrer le CP et la Ville des acteurs à domicile (#2512).
- Calcul du taux d'acteur empilés vs la date (#2500).
- Calcul de la distance à la solution la plus proche par geste (#2487).
- Nettoyage de fonction et champs inutilisés (#2489).
- Suppression de la variante touch n drag de la fiche acteur en mobile (#2515).
- Correction visuelle : centrage sur la homepage, espacements sur les fiches produit (#2499).
- Ajout de composants sites conformes manquants (#2545).
- Correctifs Infotri : script, icône (#2543).
- Mise à jour de Sites Faciles > Sites Conformes (#2544).
- Suppression de purgecss (#2551).
- Correction des icônes du générateur d'infotri (#2458).
- Suppression de la variante touch n drag de la fiche acteur en mobile (#2515).
