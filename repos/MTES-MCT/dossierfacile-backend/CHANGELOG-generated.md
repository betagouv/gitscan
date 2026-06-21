## Changelog : dossierfacile-backend (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la robustesse du backend, ainsi que sur l'ajout de nouvelles fonctionnalités pour les opérateurs du back-office, notamment concernant le traitement des dossiers et la gestion des accès. Des optimisations ont également été apportées à la recherche de propriétaires et de locataires.

### Évolutions fonctionnelles
- Ajout d'un endpoint E2E pour simuler le rejet d'un dossier par un opérateur. [#1258](https://github.com/MTES-MCT/dossierfacile-backend/issues/1258)
- Les opérateurs du back-office peuvent maintenant retravailler les documents d'un dossier après un refus. [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242) et [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241)
- Ajout d'un endpoint pour télécharger les documents d'un dossier avec des limites de débit personnalisées. [#1252](https://github.com/MTES-MCT/dossierfacile-backend/issues/1252)
- Vérification des permissions d'accès des opérateurs lors d'actions sur les dossiers, les partages d'appartement et les fichiers. [#1254](https://github.com/MTES-MCT/dossierfacile-backend/issues/1254)
- Mise à jour des labels de taxe dans le back-office. [#1248](https://github.com/MTES-MCT/dossierfacile-backend/issues/1248)
- Ajout de règles de classification de résidence. [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247)
- Amélioration de la gestion des sessions utilisateurs dans le back-office grâce à l'utilisation de Redis. [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239)
- Correction d'un bug empêchant la déconnexion des utilisateurs du back-office. [#1256](https://github.com/MTES-MCT/dossierfacile-backend/issues/1256)
- Correction d'un problème de dépassement de capacité sur les PDF lors de l'ajout de messages personnalisés longs. [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243)

### Évolutions techniques
- Optimisation de la requête pour la récupération paginée des locataires à archiver.
- Refonte de la transaction pour la tâche d'archivage des locataires. [#1255](https://github.com/MTES-MCT/dossierfacile-backend/issues/1255)
- Optimisation de la recherche de propriétaires et de locataires.
- Ajout d'index sur la colonne email (en minuscules) pour améliorer les performances des recherches.
- Amélioration de la méthode d'analyse des commentaires. [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245)
- Ajout de compétences SQL pour améliorer les capacités du LLM. [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246)
- Correction d'une course critique potentielle lors de la création de locataires. [#1257](https://github.com/MTES-MCT/dossierfacile-backend/issues/1257)

### Autres changements
- Création d'un premier fichier `agents.md`. [#1253](https://github.com/MTES-MCT/dossierfacile-backend/issues/1253)
- Suppression de la dépendance entre la jointure de locataire et le principal dans le back-office. [#1249](https://github.com/MTES-MCT/dossierfacile-backend/issues/1249)
- Mises à jour de version (V3.5.10 et V3.5.11).
- Améliorations diverses et corrections de code suite à des revues de code.
