## Changelog : dossierfacile-backend (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des pièces justificatives, notamment en permettant l'upload d'avis d'imposition plus récents et en corrigeant des erreurs lors de l'analyse des documents ADEME. Des modifications ont également été apportées aux informations requises concernant les locataires et les garants, et une correction a été implémentée pour éviter la duplication de documents.

### Évolutions fonctionnelles
- Possibilité de télécharger des avis d'imposition plus récents pour l'analyse.  [#1281](https://github.com/MTES-MCT/dossierfacile-backend/issues/1281)
- L'email du bénéficiaire est désormais obligatoire lors de la création d'un dossier locataire. [#1277](https://github.com/MTES-MCT/dossierfacile-backend/issues/1277)
- L'email du co-locataire est désormais obligatoire lors de la création d'un dossier locataire. [#1274](https://github.com/MTES-MCT/dossierfacile-backend/issues/1274)
- Ajout du champ email pour le garant personnel (locataire ou co-locataire). [#1273](https://github.com/MTES-MCT/dossierfacile-backend/issues/1273)
- Correction de l'analyse des erreurs génériques et inconnues pour les documents ADEME. [#1280](https://github.com/MTES-MCT/dossierfacile-backend/issues/1280)

### Évolutions techniques
- Ajout de SSL pour les logs envoyés à Logstash. [#1271](https://github.com/MTES-MCT/dossierfacile-backend/issues/1271)
- Mise à jour des dépendances du projet. [#1272](https://github.com/MTES-MCT/dossierfacile-backend/issues/1272)
- Ajout d'un index unique sur la table des documents pour éviter les doublons. [#1261](https://github.com/MTES-MCT/dossierfacile-backend/issues/1261)
- Modification de la règle de classification de la taxe foncière pour l'analyse des documents. [#1269](https://github.com/MTES-MCT/dossierfacile-backend/issues/1269)
- Correction d'un problème de logs en environnement SSL. [#1276](https://github.com/MTES-MCT/dossierfacile-backend/issues/1276)

### Autres changements
- Préparation des versions 3.5.12 et 3.5.13.
