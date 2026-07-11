## Changelog : vao (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les agréments, notamment pour les nouveaux agréments et les renouvellements. Des corrections d'accessibilité (RGAA) ont été apportées, ainsi que des améliorations sur les flux de connexion et la gestion des documents. Des travaux ont également été réalisés sur l'infrastructure et la sécurité.

### Évolutions fonctionnelles
- Amélioration du flux de premier agrément, incluant des étapes et des confirmations : [#1479](https://github.com/SocialGouv/vao/issues/1479), [#1475](https://github.com/SocialGouv/vao/issues/1475), [#1471](https://github.com/SocialGouv/vao/issues/1471), [#1472](https://github.com/SocialGouv/vao/issues/1472), [#1463](https://github.com/SocialGouv/vao/issues/1463)
- Ajout de la possibilité de modifier la date de fin d'un agrément dans l'espace administrateur (EIG) : [#1452](https://github.com/SocialGouv/vao/issues/1452)
- Amélioration de la gestion des documents joints et des messages affichés après le dépôt : [#1407](https://github.com/SocialGouv/vao/issues/1407), [#1406](https://github.com/SocialGouv/vao/issues/1406)
- Ajout de la possibilité de renvoyer le code OTP et amélioration de la validation de la connexion : [#1396](https://github.com/SocialGouv/vao/issues/1396)
- Ajout de textes de CGU et de sensibilisation EIG : [#1417](https://github.com/SocialGouv/vao/issues/1417), [#1418](https://github.com/SocialGouv/vao/issues/1418)
- Amélioration de l'affichage et de la gestion des informations de transport : [#1442](https://github.com/SocialGouv/vao/issues/1442)

### Évolutions techniques
- Corrections d'accessibilité (RGAA) sur plusieurs pages : page de login, page de création de compte, étapes de renouvellement, page "mon agrément" : [#1474](https://github.com/SocialGouv/vao/issues/1474), [#1477](https://github.com/SocialGouv/vao/issues/1477), [#1440](https://github.com/SocialGouv/vao/issues/1440), [#1391](https://github.com/SocialGouv/vao/issues/1391), [#1428](https://github.com/SocialGouv/vao/issues/1428)
- Mise en place d'un *feature flag* pour la gestion du code OTP : [#1409](https://github.com/SocialGouv/vao/issues/1409)
- Amélioration de la gestion des erreurs et des validations côté serveur : [#1458](https://github.com/SocialGouv/vao/issues/1458)
- Optimisation des ressources PostgreSQL en production : [#1363](https://github.com/SocialGouv/vao/issues/1363), [#1362](https://github.com/SocialGouv/vao/issues/1362)

### Autres changements
- Publication de la version 1.28.1 en préproduction : [#1462](https://github.com/SocialGouv/vao/issues/1462)
- Publication de la version 1.28.0 en préproduction : [#1422](https://github.com/SocialGouv/vao/issues/1422)
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajustements des tests et de la configuration.
- Correction de problèmes liés à la date et aux messages internes : [#1460](https://github.com/SocialGouv/vao/issues/1460), [#1446](https://github.com/SocialGouv/vao/issues/1446)
