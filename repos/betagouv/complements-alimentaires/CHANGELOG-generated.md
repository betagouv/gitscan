## Changelog : complements-alimentaires (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur pour la gestion des décisions de visa, notamment en permettant la persistance de la décision lors de la navigation et en améliorant l'affichage des champs. Des corrections et des optimisations ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Amélioration de l'interface de modification de la décision de visa : pré-remplissage des valeurs et adaptation du layout pour une meilleure expérience utilisateur. [#2947](https://github.com/betagouv/complements-alimentaires/pull/2947)
- La décision de visa est maintenant persistée lors de la navigation, évitant la perte de données. [#2959](https://github.com/betagouv/complements-alimentaires/pull/2959)
- Correction d'un bug empêchant l'affichage du délai de réponse. [#2945](https://github.com/betagouv/complements-alimentaires/pull/2945)
- Suppression de l'affichage de la section "partie de la plante" pour les produits qui ne sont pas des plantes. [#2921](https://github.com/betagouv/complements-alimentaires/pull/2921)

### Évolutions techniques
- Suppression de l'utilisation de `ipdb` et ajout des dépendances manquantes. [#2932](https://github.com/betagouv/complements-alimentaires/pull/2932)
- Mises à jour de plusieurs dépendances :
    - `arabic-reshaper` (3.0.0 -> 3.0.1)
    - `babel/core` (7.29.0 -> 7.29.7)
    - `babel/eslint-parser` (7.29.0 -> 7.29.7)
    - `cryptography` (48.0.0)
    - `express` et `qs` (dans /frontend)
    - `github/codeql-action`
    - `gouvminint/vue-dsfr` (8.17.0)
    - `idna` (3.11 -> 3.15)
    - `lxml` (6.1.0 -> 6.1.1)
    - `pypdf` (6.10.2 -> 6.11.0)
    - `pytz` (2025.2 -> 2026.2)
    - `psycopg2` (2.9.11 -> 2.9.12)
    - `regex` (2026.1.15 -> 2026.5.9)
    - `requests` (2.33.0 -> 2.34.2)
    - `sentry-sdk` (2.58.0 -> 2.60.0)
    - `sqlfluff` (4.1.0 -> 4.2.1)
    - `tailwindcss` (4.2.4 -> 4.3.0)
    - `vue` (3.5.33 -> 3.5.34)
    - `vue-router` (5.0.6 -> 5.0.7)
    - `webpack-bundle-tracker`

### Autres changements
- Audit de l'utilisation de `v-for` dans le frontend pour identifier les composants qui devraient utiliser des listes HTML.
- Ajustement des marges et espacement dans l'interface utilisateur. [#2942](https://github.com/betagouv/complements-alimentaires/pull/2942)
- Grille de colonnes responsive dans VisaValidationSegment. [#2946](https://github.com/betagouv/complements-alimentaires/pull/2946)
