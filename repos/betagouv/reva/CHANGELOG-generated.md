## Changelog : reva (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours de développement sur le projet REVA. Les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration de FranceConnect pour la simplification de l'authentification et de la création de candidatures. Des améliorations ont également été apportées à l'administration, avec de nouvelles fonctionnalités pour la gestion des certifications et des comptes d'administrateurs, ainsi que des corrections de bugs et des optimisations techniques.

### Évolutions fonctionnelles
- Intégration de FranceConnect pour l'authentification et la création de candidatures, avec amélioration de l'expérience utilisateur sur les pages de connexion et d'inscription. [#1234](https://github.com/betagouv/reva/issues/1234)
- Possibilité pour les candidats de modifier leur nationalité, même s'ils sont connectés via FranceConnect.
- Ajout d'un lien vers la page FAQ sur le site web.
- Amélioration de l'affichage des informations sur les parcours et les établissements pour les certifications éligibles.
- Ajout d'une option pour masquer les sections relatives aux exigences réduites pour les certifications.
- Ajout d'un champ "websiteUrl" pour les autorités de certification, avec possibilité de le rendre obligatoire ou facultatif.
- Amélioration de la gestion des parcours et des certifications pour les administrateurs, avec une nouvelle interface de gestion des certifications pour les comptes locaux.
- Ajout d'une confirmation lors de la déclaration de complétude d'un DF (Dossier de Formation) par une autorité de certification.
- Ajout d'un champ "Établissements" et d'un lien vers l'autorité de certification sur la page de détails de la certification.
- Possibilité de masquer les onglets relatifs aux exigences réduites sur la page de certification.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Fastify, lodash-es, react-router, jws, etc.)
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Migration de tests Cypress vers Playwright pour une meilleure performance et fiabilité.
- Amélioration de la gestion des erreurs et de la configuration de FranceConnect.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Optimisation des requêtes GraphQL pour améliorer les performances.
- Ajout de configurations pour un environnement de préproduction.
- Ajout d'un utilitaire `arePivotFieldsMatching` pour valider les données des utilisateurs France Connect.
- Suppression de code obsolète et nettoyage du code.

### Autres changements
- Ajout d'un fichier `.slugignore` pour exclure les fichiers et répertoires inutiles.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout de schémas d'architecture applicative.
- Correction de problèmes liés à l'affichage des informations sur les certifications.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Mise à jour des configurations de CI/CD.
