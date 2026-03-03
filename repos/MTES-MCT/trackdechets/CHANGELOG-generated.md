## Changelog : trackdechets (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Trackdéchets au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de performance et des renforcements de la sécurité, notamment concernant la gestion des droits d'accès et des invitations. Des améliorations ont également été apportées aux exports de données et à la génération de documents.

### Évolutions fonctionnelles
- Possibilité d'utiliser des slashs dans l'ID lors de la recherche dans le registre [#4693](https://github.com/MTES-MCT/trackdechets/issues/4693).
- Ajout d'une date d'expiration aux hashs d'invitation pour renforcer la sécurité [#4653](https://github.com/MTES-MCT/trackdechets/issues/4653).
- Correction du nom de la destination sur le PDF du BSVHU [#4683](https://github.com/MTES-MCT/trackdechets/issues/4683).
- Correction pour afficher correctement les fiches d'établissement en dehors de l'environnement de production [#4684](https://github.com/MTES-MCT/trackdechets/issues/4684).
- Amélioration du support des fichiers d'import Excel [#4685](https://github.com/MTES-MCT/trackdechets/issues/4685).
- Correction de l'affichage du poids lors de la signature émetteur, qui affichait "nullt" [#4667](https://github.com/MTES-MCT/trackdechets/issues/4667).
- Renommage de l'opération sur la modale de signature du traitement BSDA pour une meilleure clarté [#4681](https://github.com/MTES-MCT/trackdechets/issues/4681).
- Amélioration des règles d'affichage des noms lors de l'export des données "MyCompaniesCsv/MyCompaniesXls" [#4657](https://github.com/MTES-MCT/trackdechets/issues/4657).
- Modification des règles d'inclusion lors de l'export du registre [#4673](https://github.com/MTES-MCT/trackdechets/issues/4673).
- Ajout d'un limiteur de débit (rate limiting) à l'export du registre pour éviter les abus [#4658](https://github.com/MTES-MCT/trackdechets/issues/4658).
- Affichage d'une erreur si les informations de conditionnement sont manquantes [#4665](https://github.com/MTES-MCT/trackdechets/issues/4665).
- Rend la colonne `RegistryTexsAnalysisFile.s3FileKey` unique pour éviter les accès non autorisés [#4659](https://github.com/MTES-MCT/trackdechets/issues/4659).
- Empêche l'énumération possible via la création d'une demande de droits admin [#4649](https://github.com/MTES-MCT/trackdechets/issues/4649).
- Envoi d'emails différents aux administrateurs lors d'une demande de droits d'administration [#4646](https://github.com/MTES-MCT/trackdechets/issues/4646).
- Ne pas afficher le code de signature aux chauffeurs [#4664](https://github.com/MTES-MCT/trackdechets/issues/4664).
- Ajout des intermédiaires au PDF du BSVHU [#4661](https://github.com/MTES-MCT/trackdechets/issues/4661).
- Ne pas envoyer de création de transporteur BSDA par défaut lors de la création d'un BSDA [#4663](https://github.com/MTES-MCT/trackdechets/issues/4663).
- Correction de la date de signature de l'émission sur le BSDA [#4654](https://github.com/MTES-MCT/trackdechets/issues/4654).

### Évolutions techniques
- Amélioration des indexs sur `RegistryLookup` pour optimiser les performances [#4642](https://github.com/MTES-MCT/trackdechets/issues/4642).
- Ajout de la surveillance ELU (Elasticsearch Logging Unit) [#4662](https://github.com/MTES-MCT/trackdechets/issues/4662).
- Modification/k8s (détails non fournis dans le commit) [#4666](https://github.com/MTES-MCT/trackdechets/issues/4666).

### Autres changements
- Mise à jour du Changelog [#4670](https://github.com/MTES-MCT/trackdechets/issues/4670).
- Ne pas afficher de modale d'erreur avant d'afficher une modale de signature [#4656](https://github.com/MTES-MCT/trackdechets/issues/4656).
- Correction d'un bug où l'activation d'un utilisateur était envoyée même s'il n'avait pas rejoint l'entreprise [#4647](https://github.com/MTES-MCT/trackdechets/issues/4647).
