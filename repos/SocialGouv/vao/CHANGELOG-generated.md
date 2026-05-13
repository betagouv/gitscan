## Changelog : vao (30 derniers jours, au 12 mai 2026)

### Résumé
Ce changelog présente les évolutions récentes de VAO, le système d'information pour la dématérialisation des procédures de séjours pour personnes handicapées. Les dernières mises à jour se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office (BO) et l'administration des agréments, notamment en corrigeant des problèmes d'accessibilité, de validation de formulaires et de gestion des fichiers. Des améliorations techniques ont également été apportées, notamment concernant les tests et l'initialisation de la base de données.

### Évolutions fonctionnelles
- **Agrément :** Amélioration de la gestion des fichiers lors du renouvellement des agréments [#1295](https://github.com/SocialGouv/vao/issues/1295).
- **Agrément :** Ajout de la possibilité de gérer les statuts "A_CORRIGER" des agréments dans le back-office [#1390](https://github.com/SocialGouv/vao/issues/1390).
- **Agrément :** Ajout de l'envoi de mails de confirmation pour les demandes d'agrément [#1286](https://github.com/SocialGouv/vao/issues/1286).
- **Interface utilisateur :** Corrections d'accessibilité (RGAA) sur les étapes 1 et 3 du processus d'agrément [#1281](https://github.com/SocialGouv/vao/issues/1281), [#1284](https://github.com/SocialGouv/vao/issues/1284), [#1296](https://github.com/SocialGouv/vao/issues/1296).
- **Formulaires :** Corrections de validation et d'affichage sur les étapes 2, 3 et 4 du processus d'agrément [#1272](https://github.com/SocialGouv/vao/issues/1272), [#1279](https://github.com/SocialGouv/vao/issues/1279), [#1258](https://github.com/SocialGouv/vao/issues/1258), [#1259](https://github.com/SocialGouv/vao/issues/1259).
- **Back-office :** Amélioration de l'affichage des dates et des informations relatives aux agréments [#1333](https://github.com/SocialGouv/vao/issues/1333).
- **Fusager :** Ajout de fonctionnalités pour la gestion des JDMA et des messages [#1266](https://github.com/SocialGouv/vao/issues/1266), [#1273](https://github.com/SocialGouv/vao/issues/1273).

### Évolutions techniques
- **Tests :** Amélioration de la couverture des tests d'intégration et ajout de tests frontend au CI [#1305](https://github.com/SocialGouv/vao/issues/1305), [#1307](https://github.com/SocialGouv/vao/issues/1307), [#1309](https://github.com/SocialGouv/vao/issues/1309), [#1315](https://github.com/SocialGouv/vao/issues/1315), [#1317](https://github.com/SocialGouv/vao/issues/1317), [#1319](https://github.com/SocialGouv/vao/issues/1319).
- **Base de données :** Refonte du processus d'initialisation de la base de données avec l'ajout d'un Dockerfile dédié et correction des chemins [#1304](https://github.com/SocialGouv/vao/issues/1304), [#1324](https://github.com/SocialGouv/vao/issues/1324).
- **CI/CD :** Corrections et améliorations des actions de build de l'image database-init.
- **Code :** Refactoring et passage en TypeScript de certaines parties du code.

### Autres changements
- Correction de coquilles et amélioration de la lisibilité du code.
- Suppression de branches inutiles.
- Mise à jour de la documentation.
- Amélioration de la gestion des erreurs et des logs.
