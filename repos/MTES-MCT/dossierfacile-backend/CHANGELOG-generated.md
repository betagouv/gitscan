## Changelog : dossierfacile-backend (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances de recherche de propriétaires et locataires, l'ajout de règles de classification de résidence, et des corrections pour l'interface opérateur (BO). Des améliorations ont également été apportées à la gestion des sessions utilisateur et à la génération de PDF.

### Évolutions fonctionnelles
- **Interface Opérateur (BO):** Les opérateurs peuvent désormais retraiter les documents des locataires après un refus, facilitant ainsi la correction et la validation des dossiers.  [#1241](https://github.com/MTES-MCT/dossierfacile-backend/issues/1241) et [#1242](https://github.com/MTES-MCT/dossierfacile-backend/issues/1242)
- **Recherche:** Optimisation de la recherche de locataires et de propriétaires pour une meilleure performance.
- **Classification de résidence:** Ajout de règles de classification de résidence pour une catégorisation plus précise. [#1247](https://github.com/MTES-MCT/dossierfacile-backend/issues/1247)
- **Gestion des PDF:** Correction d'un problème de dépassement de texte sur les PDF lors de l'ajout de messages personnalisés longs. [#1243](https://github.com/MTES-MCT/dossierfacile-backend/issues/1243)
- **Séparation des rôles:** Dissociation de la jointure locataire du rôle principal dans l'interface opérateur. [#1249](https://github.com/MTES-MCT/dossierfacile-backend/issues/1249)

### Évolutions techniques
- **Performance:** Ajout d'index sur la colonne email (en minuscules) dans la table `user_account` pour améliorer les performances des requêtes.
- **Session Management:** Implémentation de Redis pour persister les sessions utilisateur en cas de redémarrage du back-office (BO). [#1239](https://github.com/MTES-MCT/dossierfacile-backend/issues/1239)
- **Analyse de commentaires:** Refonte de la méthode d'analyse des commentaires. [#1245](https://github.com/MTES-MCT/dossierfacile-backend/issues/1245)
- **Capacités LLM:** Ajout d'une compétence SQL pour améliorer les capacités SQL du LLM (Large Language Model). [#1246](https://github.com/MTES-MCT/dossierfacile-backend/issues/1246)
- **Anonymisation:** Suppression de la colonne `json_profile` de la table `tenant_log` pour faciliter l'anonymisation des données. [#1238](https://github.com/MTES-MCT/dossierfacile-backend/issues/1238)
- **Correction IA Document:** Correction du type de retour de l'IA pour les documents 2D inconnus. [#1237](https://github.com/MTES-MCT/dossierfacile-backend/issues/1237)
- **Optimisation BO:** Optimisation de l'appel à l'API de prévisualisation de fichiers dans le back-office. [#1236](https://github.com/MTES-MCT/dossierfacile-backend/issues/1236)

### Autres changements
- Mises à jour de version : 3.5.7, 3.5.8 et 3.5.10.
