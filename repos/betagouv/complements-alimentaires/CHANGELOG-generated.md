## Changelog : complements-alimentaires (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité du site, la correction de bugs et la mise à jour des dépendances. Des améliorations ont été apportées à la gestion des fichiers, à la navigation et à la conformité aux normes RGAA.  Une nouvelle fonctionnalité permet également la modification des déclarations sans entreprises mandatées.

### Évolutions fonctionnelles
- Possibilité de modifier les déclarations sans entreprises mandatées. [#2734](https://github.com/betagouv/complements-alimentaires/pull/2734)
- Amélioration de la gestion des erreurs de validation des fichiers.
- Amélioration de la navigation avec un fil d'Ariane plus visible sur mobile.
- Amélioration de la structure des pages d'historique et des collaborateurs pour une meilleure accessibilité.
- Amélioration de l'accessibilité des tableaux et des champs de formulaire.
- Correction d'erreurs sur le v-model. [#2797](https://github.com/betagouv/complements-alimentaires/pull/2797)

### Évolutions techniques
- Mise à jour de la version de PostgreSQL dans les workflows GitHub pour une meilleure stabilité et sécurité. [#2736](https://github.com/betagouv/complements-alimentaires/pull/2736)
- Mise à jour de plusieurs dépendances : Django, Pytest, Faker, NumPy, PyPDF, reportlab, vue-router, vue-eslint-parser, postcss, etc. (mises à jour automatiques via Dependabot)
- Refactoring du code pour supprimer des variables inutilisées.
- Mise à jour de la configuration ESLint.
- Correction d'une régression introduite par une mise à jour ESLint.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Corrections mineures de style et de formatage.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Mise à jour des dépendances de développement.
- Ajout d'une validation du type MIME pour les pièces jointes des déclarations.
- Suppression de code obsolète.
