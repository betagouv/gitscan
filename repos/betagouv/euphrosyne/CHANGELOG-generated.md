## Changelog : euphrosyne (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout de nouvelles fonctionnalités pour la gestion des certifications et des données, ainsi que sur l'amélioration de la sécurité et de la robustesse de la plateforme. De nombreuses mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du système.

### Évolutions fonctionnelles
- Ajout d'une image de machine virtuelle pour la tomographie. [#1941](https://github.com/betagouv/euphrosyne/pull/1941)
- Amélioration de l'export CSV des utilisateurs ayant passé une certification. [#6600b34](https://github.com/betagouv/euphrosyne/commit/6600b34)
- Ajout d'une protection pour les origines autorisées lors des requêtes de données. [#8ec9518](https://github.com/betagouv/euphrosyne/commit/8ec9518)
- Ajout de la possibilité d'exporter en CSV la liste des utilisateurs ayant obtenu une certification. [#5bbbcee](https://github.com/betagouv/euphrosyne/commit/5bbbcee)
- Ajout d'une action pour l'impersonation d'administrateur. [#be2f0fd](https://github.com/betagouv/euphrosyne/commit/be2f0fd)
- Correction d'une vulnérabilité d'injection dans l'export CSV des certifications. [#11f152e](https://github.com/betagouv/euphrosyne/commit/11f152e)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, Sentry SDK, IPython, ts-loader, @typescript-eslint/eslint-plugin, axios, vitest, docutils, opensearch-py, webpack, gunicorn, types-markdown, black. Ces mises à jour visent à améliorer la sécurité, la performance et la stabilité de l'application.
- Mise à jour de la version de TypeScript et des types React.
- Mise à jour des stubs Django.

### Autres changements
- Aucune documentation ou configuration n'a été modifiée.
