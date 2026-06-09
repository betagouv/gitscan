## Changelog : vao (30 derniers jours, au 8 juin 2026)

### Résumé
Ce changelog couvre une période d'amélioration continue pour VAO, avec un focus important sur la correction de bugs, l'accessibilité (RGAA) et l'amélioration de l'expérience utilisateur, notamment dans les formulaires d'agrément et de demande de séjour. Des efforts ont également été déployés pour améliorer la couverture des tests et la robustesse de l'application.

### Évolutions fonctionnelles
- **Agrément :**
    - Amélioration du workflow de renouvellement d'agrément, notamment la correction d'un problème de rafraîchissement et l'ajout de validations. [#1335](https://github.com/SocialGouv/vao/issues/1335)
    - Ajout de la possibilité de retourner à l'étape précédente lors de la correction d'un agrément dans Fusager. [#1348](https://github.com/SocialGouv/vao/issues/1348)
    - Mise à jour des statuts d'agrément dans Fusager. [#1353](https://github.com/SocialGouv/vao/issues/1353)
    - Correction du chemin de téléchargement des documents dans le back-office. [#1327](https://github.com/SocialGouv/vao/issues/1327)
    - Ajout de contrôles pour les représentants légaux. [#1399](https://github.com/SocialGouv/vao/issues/1399)
- **Demande de séjour :**
    - Envoi du code OTP par email pour l'authentification. [#1361](https://github.com/SocialGouv/vao/issues/1361)
    - Correction des validations des fichiers liés aux séjours et aux bilans. [#1320](https://github.com/SocialGouv/vao/issues/1320)
- **Accessibilité (RGAA) :**
    - Améliorations significatives de l'accessibilité des étapes de renouvellement d'agrément et des formulaires, incluant l'ajout de *fieldset*, de labels et la correction de problèmes de contraste. [#1336](https://github.com/SocialGouv/vao/issues/1336), [#1347](https://github.com/SocialGouv/vao/issues/1347), [#1351](https://github.com/SocialGouv/vao/issues/1351), [#1354](https://github.com/SocialGouv/vao/issues/1354), [#1382](https://github.com/SocialGouv/vao/issues/1382), [#1386](https://github.com/SocialGouv/vao/issues/1386), [#1395](https://github.com/SocialGouv/vao/issues/1395)
- **Back-office :**
    - Amélioration du scrolling sur les onglets des agréments. [#1394](https://github.com/SocialGouv/vao/issues/1394)

### Évolutions techniques
- Amélioration de la configuration des tests Jest et des timeouts pour les conteneurs. [#1366](https://github.com/SocialGouv/vao/issues/1366)
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de la configuration de build TypeScript.
- Amélioration de la couverture des tests d'intégration. [#1315](https://github.com/SocialGouv/vao/issues/1315)
- Correction de problèmes liés à la configuration de l'environnement de développement et des tests. [#1373](https://github.com/SocialGouv/vao/issues/1373)
- Correction de problèmes liés à la configuration des tests E2E. [#1364](https://github.com/SocialGouv/vao/issues/1364), [#1365](https://github.com/SocialGouv/vao/issues/1365)
- Correction de problèmes de fiabilité signalés par SonarQube. [#1319](https://github.com/SocialGouv/vao/issues/1319)

### Autres changements
- Mise à jour de diverses dépendances (axios, ts-jest, multer, @aws-sdk/client-s3, nuxt).
- Nettoyage et factorisation du code.
- Correction de problèmes mineurs et amélioration de la documentation.
- Mise à jour des chemins d'accès dans le script d'initialisation de la base de données. [#1324](https://github.com/SocialGouv/vao/issues/1324)
