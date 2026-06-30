## Changelog : complements-alimentaires (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la maintenance et la mise à jour des dépendances du projet, notamment les librairies JavaScript utilisées en frontend (React, Vue.js) et les librairies Python. Une suppression de la librairie BeautifulSoup4 a également été effectuée. Ces mises à jour visent à améliorer la sécurité, la stabilité et les performances de l'application.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle majeure n'a été déployée durant cette période.

### Évolutions techniques
- **Suppression de BeautifulSoup4:** La librairie BeautifulSoup4 et ses dépendances ont été supprimées du projet. [#2977](https://github.com/betagouv/complements-alimentaires/pull/2977)
- **Mise à jour des dépendances:** De nombreuses dépendances ont été mises à jour vers leurs dernières versions stables, incluant :
    - Python : `pypdf`, `redis`, `cryptography`, `bleach`, `sentry-sdk`, `identify`, `pre-commit`, `numpy`, `tzdata`, `sqlfluff`
    - JavaScript (frontend) : `vue`, `vue-router`, `eslint-plugin-prettier`, `vue-eslint-parser`, `babel/core`, `shell-quote`, `launch-editor`, `webpack-bundle-tracker`, `@gouvminint/vue-dsfr`
    - GitHub Actions : `actions/checkout`, `github/codeql-action`

### Autres changements
Aucun autre changement significatif n'a été apporté durant cette période.
