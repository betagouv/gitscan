## Changelog : dossierfacile-backend (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'espace administrateur (BO), l'optimisation des performances de recherche et l'ajout de nouvelles fonctionnalités pour le traitement des documents et la gestion des sessions utilisateurs. Des corrections ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Les opérateurs du BO peuvent désormais relancer le traitement des documents d'un locataire après un refus. [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241) et [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242)
- Un nouveau point de terminaison a été ajouté pour télécharger les documents d'un dossier de candidature (DFC) avec des limitations de débit personnalisées. [#1252](https://github.com/MTES-MCT/dossierfacile-backend/issues/1252)
- Amélioration de la recherche des propriétaires et des locataires pour une meilleure performance.
- Ajout de règles de classification de la résidence. [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247)
- Ajout d'une compétence SQL pour améliorer les capacités SQL du LLM. [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246)
- Correction d'un problème de dépassement de capacité sur les PDF lors de l'ajout de messages personnalisés longs. [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243)
- Ajout d'un fichier `agents.md` pour documenter les agents. [#1253](https://github.com/MTES-MCT/dossierfacile-backend/issues/1253)
- Amélioration de la vérification des permissions d'accès des opérateurs dans le BO lors de la réalisation d'actions sur un locataire/partage d'appartement et un fichier. [#1254](https://github.com/MTES-MCT/dossierfacile-backend/issues/1254)
- Mise à jour du label de taxe dans le BO. [#1248](https://github.com/MTES-MCT/dossierfacile-backend/issues/1248)

### Évolutions techniques
- Ajout de Redis pour préserver la session utilisateur dans le BO lors d'un redémarrage. [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239)
- Optimisation de la méthode d'analyse des commentaires. [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245)
- Ajout d'index sur la base de données pour améliorer les performances, notamment sur l'email des utilisateurs.
- Refonte de la vue matérialisée `latest_operator`. [#1251](https://github.com/MTES-MCT/dossierfacile-backend/issues/1251)
- Dissociation de la jointure locataire du principal. [#1249](https://github.com/MTES-MCT/dossierfacile-backend/issues/1249)
- Correction du type de retour de l'IA pour les documents 2DDOC inconnus. [#1237](https://github.com/MTES-MCT/dossierfacile-backend/issues/1237)

### Autres changements
- Suppression de la colonne `json_profile` de la table `tenant_log` pour l'anonymisation. [#1238](https://github.com/MTES-MCT/dossierfacile-backend/issues/1238)
- Publication des versions 3.5.8 et 3.5.10.
- Correction pour éviter d'appeler l'API de prévisualisation de fichier inutilement dans le BO. [#1236](https://github.com/MTES-MCT/dossierfacile-backend/issues/1236)
