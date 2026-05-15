## Changelog : vao (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à VAO au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'expérience utilisateur, notamment sur les formulaires d'agrément et la gestion des documents, ainsi que des optimisations techniques et des corrections de sécurité. Des améliorations ont également été apportées à l'initialisation de la base de données et aux tests.

### Évolutions fonctionnelles
- **Agrément :** Correction du défilement des onglets dans le back-office ([#1325](https://github.com/SocialGouv/vao/issues/1325)).
- **Agrément :** Amélioration de la validation des agréments et gestion des statuts (A_CORRIGER) ([#1327](https://github.com/SocialGouv/vao/issues/1327), [#1313](https://github.com/SocialGouv/vao/issues/1313)).
- **Documents :** Correction de l'upload des documents pour le renouvellement des agréments ([#1320](https://github.com/SocialGouv/vao/issues/1320), [#1384](https://github.com/SocialGouv/vao/issues/1384)).
- **Documents :** Ajout de la gestion des fichiers obligatoires et des contraintes sur les documents ([#1385](https://github.com/SocialGouv/vao/issues/1385)).
- **Adresse :** Correction du formattage de l'adresse à l'étape 3 du processus ([#1282](https://github.com/SocialGouv/vao/issues/1282), [#1085](https://github.com/SocialGouv/vao/issues/1085)).
- **Accessibilité :** Amélioration de l'accessibilité des boutons et labels ([#1281](https://github.com/SocialGouv/vao/issues/1281), [#1084](https://github.com/SocialGouv/vao/issues/1084)).
- **Confirmation d'agrément :** Implémentation de l'envoi d'emails de confirmation pour les demandes d'agrément ([#1286](https://github.com/SocialGouv/vao/issues/1286), [#1149](https://github.com/SocialGouv/vao/issues/1149)).
- **Fusager :** Modifications et transmission des agréments ([#1306](https://github.com/SocialGouv/vao/issues/1306), [#1318](https://github.com/SocialGouv/vao/issues/1318), [#1392](https://github.com/SocialGouv/vao/issues/1392)).
- **Fusager :** Ajout de la liste des JDMA ([#1268](https://github.com/SocialGouv/vao/issues/1268)).

### Évolutions techniques
- **Tests :** Ajout et amélioration des tests d'intégration et frontend ([#1307](https://github.com/SocialGouv/vao/issues/1307), [#1309](https://github.com/SocialGouv/vao/issues/1309), [#1315](https://github.com/SocialGouv/vao/issues/1315)).
- **CI/CD :** Corrections pour les tests E2E en CI ([#1328](https://github.com/SocialGouv/vao/issues/1328)).
- **Base de données :** Refonte du processus d'initialisation de la base de données avec l'ajout d'un Dockerfile dédié ([#1304](https://github.com/SocialGouv/vao/issues/1304), [#1324](https://github.com/SocialGouv/vao/issues/1324)).
- **Refactoring :** Passage de certaines parties du code en TypeScript pour une meilleure maintenabilité ([#1385](https://github.com/SocialGouv/vao/issues/1385)).
- **Sécurité :** Correction de vulnérabilités identifiées par SonarQube ([#1319](https://github.com/SocialGouv/vao/issues/1319)).
- **Authentification :** Correction de la déconnexion et du refresh token ([#1310](https://github.com/SocialGouv/vao/issues/1310)).

### Autres changements
- Amélioration de la couverture des tests.
- Corrections de style et de code.
- Mise à jour de la documentation.
