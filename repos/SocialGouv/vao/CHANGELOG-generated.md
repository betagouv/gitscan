## Changelog : vao (30 derniers jours, au 17 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité (RGAA) et de la robustesse de l'application, notamment au niveau de la gestion des agréments et des renouvellements. Des corrections de bugs et des optimisations de la gestion des fichiers et des dates ont également été apportées. L'authentification a été renforcée avec l'ajout de fonctionnalités liées à la vérification en deux étapes (OTP).

### Évolutions fonctionnelles
- **Authentification:** Ajout de la possibilité de renvoyer le code OTP et de valider la connexion avec le code OTP [#1396]. Implémentation de la mémorisation du code OTP [#1408]. Ajout d'un système de tentatives pour le code OTP [#1387].
- **Agréments:** Amélioration de la gestion des statuts des agréments [#1405]. Possibilité de retourner un agrément après correction dans Fusager [#1402]. Correction d'un bug empêchant le rafraîchissement des agréments en renouvellement [#1335].
- **Documents:** Normalisation des noms de fichiers uploadés en supprimant les caractères spéciaux [#1389]. Correction de problèmes liés à l'affichage des documents joints [#1406, #1420].
- **Expérience utilisateur:** Correction de messages contradictoires affichés lors du dépôt de fichiers de complétude [#1407]. Amélioration de l'accessibilité (RGAA) sur plusieurs étapes du processus, notamment pour les représentants légaux et les certificats [#1336, #1347, #1354].
- **Envoi d'emails:** Prise en charge de l'envoi d'emails lors de la prise en charge d'un dossier [#1400].
- **Fusager:** Correction d'un bug lié au bouton "activer" dans Fusager lorsque le SIRET est identique [#1352, #1390, #1419].

### Évolutions techniques
- **Infrastructure:** Augmentation des ressources CPU et mémoire pour la base de données PostgreSQL en production et pré-production [#1362, #1363].
- **Dépendances:** Mise à jour de plusieurs dépendances : NestJS, Nodemailer, Knex, Axios, ts-jest, multer, nuxt [#1373, #1374, #1375, #1376, #1377, #1392, #1393, #1394].
- **Tests:** Amélioration de la couverture de tests et correction de tests E2E défaillants [#1341, #1344, #1349, #1350]. Ajout de tests pour la gestion des ressources PostgreSQL [#1399].
- **Sécurité:** Implémentation d'un mécanisme de "fail closed" pour l'antivirus [#1413].
- **Code:** Refactoring et nettoyage du code, notamment pour la gestion des erreurs et la duplication de code.
- **CI/CD:** Amélioration de la configuration de la CI/CD.

### Autres changements
- Ajout de validateurs EIG pour le back-office [#1418].
- Mise à jour de la documentation et des textes d'information (CGU, sensibilisation EIG) [#1410, #1411, #1417].
- Correction de problèmes liés à la configuration ESLint et TypeScript.
- Suppression de la catégorie de fichier "MOTIVATION".
- Ajout de feature flags pour certaines fonctionnalités (OTP).
- Amélioration de la gestion des erreurs et des validations.
