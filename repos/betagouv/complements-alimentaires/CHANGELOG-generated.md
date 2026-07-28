## Changelog : complements-alimentaires (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la mise à jour des dépendances du projet, assurant ainsi sa sécurité et sa stabilité. Une amélioration fonctionnelle a été apportée concernant la gestion des visas pour certains articles.

### Évolutions fonctionnelles
- Amélioration de la gestion des visas pour les articles 16 et 18. [#2997-visa-approval](https://github.com/betagouv/complements-alimentaires/pull/2997)

### Évolutions techniques
- Mise à jour de nombreuses dépendances Python (Django, django-filter, django-viewflow, pillow, sentry-sdk, tzlocal, uritools, pandas, regex, pikepdf, django-webpack-loader) vers leurs dernières versions stables.
- Mise à jour des dépendances npm/yarn du frontend (body-parser, prettier, vue, websocket-driver, svgo, fast-uri, postcss, @tailwindcss/postcss).
- Mise à jour des actions GitHub utilisées pour le CI/CD.

### Autres changements
- Correction de tests suite à l'implémentation de la gestion des visas.
- Ajout de validations côté backend pour la gestion des visas.
