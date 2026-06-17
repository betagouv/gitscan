## Changelog : complements-alimentaires (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la maintenance technique du projet avec de nombreuses mises à jour de dépendances. Des améliorations fonctionnelles ont été apportées à la gestion des visas, notamment l'amélioration de l'interface de modification de la décision et la persistance de cette décision lors de la navigation. Une suppression de champs inutiles a également été effectuée.

### Évolutions fonctionnelles
- Amélioration de l'interface de modification de la décision de visa : refonte du layout et pré-remplissage des valeurs. [#2948](https://github.com/betagouv/complements-alimentaires/pull/2948)
- Persistance de la décision de visa : la décision est maintenant conservée lors de la navigation dans l'application. [#2950](https://github.com/betagouv/complements-alimentaires/pull/2950)
- Suppression des champs relatifs aux plantes pour les produits non-plantes. [#2921](https://github.com/betagouv/complements-alimentaires/pull/2921)
- Correction d'un problème d'affichage du délai de réponse. [#2945](https://github.com/betagouv/complements-alimentaires/pull/2945)

### Évolutions techniques
- Mise à jour de nombreuses dépendances :
    - `numpy` (2.4.4 -> 2.4.6)
    - `cryptography` (48.0.0 -> 48.0.1)
    - `pypdf` (6.10.2 -> 6.13.0)
    - `bleach` (6.3.0 -> 6.4.0)
    - `tzdata` (2025.3 -> 2026.2)
    - `requests` (2.33.0 -> 2.34.2)
    - `packaging` (26.0 -> 26.2)
    - `sqlfluff` (4.1.0 -> 4.2.1)
    - `idna` (3.11 -> 3.15)
    - `psycopg2` (2.9.11 -> 2.9.12)
    - `pytz` (2025.2 -> 2026.2)
    - `regex` (2026.1.15 -> 2026.5.9)
- Mise à jour des dépendances frontend : `vue`, `vue-router`, `tailwindcss`, `eslint-plugin-prettier`, `vue-eslint-parser`, `webpack-bundle-tracker`, `shell-quote`, `gouvminint/vue-dsfr` et autres.
- Suppression de `ipdb` et de ses dépendances. [#2932](https://github.com/betagouv/complements-alimentaires/pull/2932)

### Autres changements
- Amélioration de l'accessibilité : audit et correction de l'utilisation de `v-for` pour utiliser des listes HTML sémantiques. [#2946](https://github.com/betagouv/complements-alimentaires/pull/2946)
- Ajustement des marges et espacement dans l'interface. [#2957](https://github.com/betagouv/complements-alimentaires/pull/2957)
- Grille de colonnes responsive dans VisaValidationSegment. [#2952](https://github.com/betagouv/complements-alimentaires/pull/2952)
