## Changelog : dossierfacile-backend (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et des performances du backend, ainsi que sur l'ajout de nouvelles fonctionnalités pour les opérateurs du back-office, notamment concernant le traitement des dossiers et la gestion des accès. Des optimisations ont également été apportées à la recherche de propriétaires et locataires.

### Évolutions fonctionnelles
- Les opérateurs du back-office peuvent désormais relancer le traitement des documents d'un dossier après un refus [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241), [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242).
- Ajout d'un point de terminaison pour télécharger les documents d'un dossier avec des limitations de débit personnalisées [#1252](https://github.com/MTES-MCT/dossierfacile-backend/issues/1252).
- Amélioration de la gestion des droits d'accès des opérateurs dans le back-office, avec vérification des permissions lors des actions sur les dossiers, les partages d'appartement et les fichiers [#1254](https://github.com/MTES-MCT/dossierfacile-backend/issues/1254).
- Mise à jour des labels de taxe dans le back-office [#1248](https://github.com/MTES-MCT/dossierfacile-backend/issues/1248).
- Ajout d'un endpoint e2e pour simuler le rejet d'un dossier par un opérateur [#1258](https://github.com/MTES-MCT/dossierfacile-backend/issues/1258).
- Ajout d'un fichier `agents.md` pour documenter les agents [#1253](https://github.com/MTES-MCT/dossierfacile-backend/issues/1253).

### Évolutions techniques
- Optimisation de la requête pour la récupération paginée des locataires à archiver.
- Amélioration de la recherche de propriétaires et de locataires pour de meilleures performances.
- Ajout d'index sur la colonne email (en minuscules) pour accélérer les recherches.
- Refonte de la transaction pour la tâche d'archivage des locataires [#1255](https://github.com/MTES-MCT/dossierfacile-backend/issues/1255).
- Correction d'un problème de concurrence pouvant empêcher la création d'un locataire [#1257](https://github.com/MTES-MCT/dossierfacile-backend/issues/1257).
- Correction d'un bug empêchant la déconnexion des utilisateurs du back-office [#1256](https://github.com/MTES-MCT/dossierfacile-backend/issues/1256).
- Ajout de Redis pour persister la session utilisateur du back-office en cas de redémarrage [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239).
- Amélioration de la méthode d'analyse des commentaires [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245).
- Ajout de compétences SQL pour améliorer les capacités du LLM [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246).
- Ajout de règles de classification de résidence [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247).

### Autres changements
- Correction d'un débordement PDF pour les messages personnalisés longs [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243).
- Mise à jour de la version à V3.5.10 et V3.5.11.
- Amélioration de la documentation et revue du code.
