## Changelog : drive (30 derniers jours, au 24 juin 2026)

### Résumé
Les dernières mises à jour de Drive se concentrent sur l'amélioration de la conversion de fichiers, notamment avec l'intégration de OnlyOffice, et l'ajout de la possibilité d'exporter des dossiers entiers. Des améliorations ont également été apportées à la gestion des utilisateurs, avec l'introduction d'un système de réconciliation de comptes, et à la robustesse générale de l'application, avec des corrections de bugs et des optimisations de sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers sous forme d'archive ZIP. [#cd7bebf](https://github.com/suitenumerique/drive/commit/cd7bebf)
- Implémentation d'un système de réconciliation de comptes utilisateurs, permettant de gérer les comptes orphelins ou erronés. [#9995a2a](https://github.com/suitenumerique/drive/commit/9995a2a)
- Possibilité de convertir des fichiers pendant qu'ils sont en cours d'analyse. [#3587826](https://github.com/suitenumerique/drive/commit/3587826)
- Ajout de la prise en charge de l'upload de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout de boutons d'appel à l'action (CTA) pour les fichiers et dossiers publics, différenciés selon l'authentification de l'utilisateur. [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f)
- Amélioration de l'interface utilisateur pour afficher l'état de conversion des fichiers. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)

### Évolutions techniques
- Intégration de OnlyOffice pour la conversion de fichiers, avec gestion des requêtes signées via JWT. [#5149283](https://github.com/suitenumerique/drive/commit/5149283)
- Mise à jour des dépendances PyJWT et cryptography pour corriger des failles de sécurité. [#630209f](https://github.com/suitenumerique/drive/commit/630209f)
- Amélioration de la gestion des erreurs et des états lors de l'upload de fichiers. [#caa1dbc](https://github.com/suitenumerique/drive/commit/caa1dbc)
- Optimisation du streaming des fichiers exportés depuis S3. [#dd7b20b](https://github.com/suitenumerique/drive/commit/dd7b20b)
- Correction du healthcheck de Collabora pour fonctionner sans curl. [#2d16361](https://github.com/suitenumerique/drive/commit/2d16361)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)

### Autres changements
- Amélioration de la documentation et des guidelines de contribution. [#1843036](https://github.com/suitenumerique/drive/commit/1843036)
- Clarification et amélioration de la cohérence de la documentation README. [#f53d80d](https://github.com/suitenumerique/drive/commit/f53d80d)
- Ajout de tests E2E pour le workflow de conversion. [#302bff1](https://github.com/suitenumerique/drive/commit/302bff1)
- Documentation de l'environnement de conversion OnlyOffice. [#350a482](https://github.com/suitenumerique/drive/commit/350a482)
- Suppression de colonnes `numchild` obsolètes du modèle `Item`. [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c)
