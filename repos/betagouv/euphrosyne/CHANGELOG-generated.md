## Changelog : euphrosyne (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Euphrosyne au cours des 30 derniers jours. Les principales évolutions concernent la mise à jour de la version de Django, l'amélioration de la gestion des participations (validation, affichage), la refactorisation de la gestion du stockage de fichiers avec Azure, et des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. De nombreuses dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction d'un bug dans l'affichage des participations distantes, permettant d'accéder à l'édition des informations. (#1720)
- Ajout d'une validation pour empêcher la création de participations avec la même adresse email pour l'employeur et l'utilisateur. (#1719)
- Normalisation des noms de personnes et d'employeurs (capitalisation). (#1718)
- Implémentation de la possibilité d'exempter un employeur lors de la création d'une participation, en se basant sur son identifiant ROR. (#1716)
- Amélioration du style du dropdown pour la sélection d'institutions. (#1717)
- Ajout de la gestion de l'ID de template pour les goodflags et logging en cas d'absence. (#1704, #1705)
- Correction d'un problème où le processus de signature électronique pouvait échouer. (#1703)

### Évolutions techniques
- Mise à jour de Django en version 6.0.2, incluant des corrections de sécurité et des améliorations de performance. (#1736, #1619)
- Refactorisation de la gestion du stockage de fichiers avec l'utilisation de `BlobStorageClient` et `FileshareStorageClient` pour une meilleure intégration avec Azure. (#1706)
- Mise en place d'un mécanisme de gestion des erreurs et de retries pour les processus de signature électronique.
- Ajout de l'application de règles de Content Security Policy (CSP) pour renforcer la sécurité. (#1734)
- Intégration de Sentry pour le frontend, permettant de suivre et de diagnostiquer les erreurs côté client. (#1734)
- Mise à jour de nombreuses dépendances :
    - `drf-spectacular` (0.28.0 -> 0.29.0)
    - `@typescript-eslint/eslint-plugin` (8.54.0)
    - `prettier` (3.8.0 -> 3.8.1)
    - `mini-css-extract-plugin` (2.9.4 -> 2.10.0)
    - `css-minimizer-webpack-plugin` (7.0.2 -> 7.0.4)
    - `vitest` (4.0.17 -> 4.0.18)
    - `sentry-sdk` (2.45.0 -> 2.52.0)
    - `@azure/storage-blob` (12.29.1 -> 12.30.0)
    - `@sentry/browser` (10.34.0 -> 10.36.0 -> 10.37.0)
    - `@types/react`
    - `@types/react-dom`
    - `react-dom` (19.2.3)
    - `fast-xml-parser` (5.2.5 -> 5.3.4)
    - `purgecss-webpack-plugin` (7.0.2 -> 8.0.0)
    - `@isaacs/brace-expansion` (5.0.0 -> 5.0.1)
    - `social-auth-app-django` (5.5.1 -> 5.7.0)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et configurations.
- Correction de styles CSS spécifiques à Django. (#1736)
- Amélioration de la gestion des timeouts pour certaines tâches asynchrones.
- Correction de la version de React et React-DOM pour assurer la compatibilité. (#1705)
