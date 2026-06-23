## Changelog : complements-alimentaires (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur pour la gestion des décisions de visa, notamment en permettant la persistance et le pré-remplissage des données. Des corrections d'accessibilité ont également été apportées. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Amélioration de l'interface de modification de la décision de visa :
  - Permet de conserver la décision de visa lors de la navigation. [#2950](https://github.com/betagouv/complements-alimentaires/pull/2950)
  - Pré-remplissage des valeurs de l'instruction pour la modification côté visa.
  - Ajustement des marges et de l'espacement pour une meilleure lisibilité.
- Correction d'un bug empêchant l'affichage du délai de réponse. [#2952](https://github.com/betagouv/complements-alimentaires/pull/2952)
- Suppression des champs relatifs aux plantes pour les produits qui n'en sont pas. [#2921](https://github.com/betagouv/complements-alimentaires/pull/2921)
- Amélioration de la grille de colonnes dans la section VisaValidationSegment pour une meilleure réactivité.

### Évolutions techniques
- Mises à jour de nombreuses dépendances :
  - `numpy` (2.4.4 -> 2.4.6)
  - `cryptography` (48.0.0 -> 48.0.1)
  - `pypdf` (6.11.0 -> 6.13.0)
  - `sentry-sdk` (2.58.0 -> 2.60.0)
  - `pre-commit` (4.5.1 -> 4.6.0)
  - `sqlfluff` (4.2.0 -> 4.2.1)
  - `arabic-reshaper` (3.0.0 -> 3.0.1)
  - `packaging` (26.0 -> 26.2)
  - `requests` (2.33.0 -> 2.34.2)
  - `lxml` (6.1.0 -> 6.1.1)
  - `pyhanko-certvalidator` (0.30.1 -> 0.31.1)
  - `vue-router` (5.0.6 -> 5.0.7)
  - `vue` (3.5.34 -> 3.5.35)
  - `webpack-bundle-tracker`
- Mises à jour des actions GitHub et des outils de développement (eslint, babel, etc.).
- Mise à jour de la librairie de composants Vue DSFR (8.17.0).

### Autres changements
- Amélioration de l'accessibilité : Audit des utilisations de `v-for` pour identifier les composants qui devraient être des listes. [#2946](https://github.com/betagouv/complements-alimentaires/pull/2946)
- Corrections et mises à jour de la configuration du projet.
