## Changelog : trackdechets (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à trackdechets au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de performance et des ajustements de la logique métier, notamment concernant la gestion des bordereaux de déchets (BSDA, BSVHU, BSFF) et la gestion des droits d'accès.

### Évolutions fonctionnelles
- Correction d'un bug sur le PDF du BSVHU, où le nom de la destination était incorrect (#4683).
- Correction d'un problème d'affichage de la fiche établissement hors environnement de production (#4684).
- Amélioration du support des fichiers d'import Excel (#4685).
- Correction de l'affichage du poids lors de la signature émetteur, qui affichait "nullt" lorsqu'aucun poids n'était renseigné (#4667).
- Renommage de l'opération sur la modale de signature du traitement BSDA pour plus de clarté (#4681).
- Application des règles d'affichage de nom aux exports MyCompaniesCsv/MyCompaniesXls (#4657).
- Modification des règles d'inclusion à l'export du registre (#4673).
- Ajout d'un rate limiting à l'export du registre pour éviter les problèmes de performance (#4658).
- Affichage d'une erreur de conditionnement si l'information est manquante (#4665).
- Rendre la colonne RegistryTexsAnalysisFile.s3FileKey unique pour éviter les accès non autorisés (#4659).
- Plus d'énumération possible via la création d'une demande de droits admin, renforçant la sécurité (#4649).
- Envoi de mails différents aux administrateurs lors d'une demande de droits d'accès (#4646).
- Suppression de l'affichage du code de signature aux chauffeurs, améliorant la confidentialité (#4664).
- Ajout des intermédiaires au PDF du BSVHU (#4661).
- Amélioration des indexs sur RegistryLookup pour optimiser les performances (#4642).
- Correction de la date de signature de l'émission sur le BSDA (#4654).
- Correction de l'affichage des informations du transporteur étranger sur un BSDA ré-ouvert (#4644).
- Correction de l'affichage du statut "En attente de traitement" pour tous les bordereaux (#4648).
- Ajout du mode de traitement sur le PDF d'un BSFF (#4624).
- Affichage des bons lots entrants dans le cadre 10 des PDFs des BSVHUs (#4625).
- Le champ destinationReceptionRefusedWeight est désormais obligatoire sur le BSDA (#4638).
- Modification des règles de traçabilité DND/TEXS selon les types d'établissements (#4643).
- Ne pas envoyer de createBsdaTransporter par défaut à la création d'un BSDA (#4663).

### Évolutions techniques
- Ajout d'un monitoring ELU pour une meilleure surveillance de l'application (#4662).
- Nettoyage du code et refactoring pour améliorer la maintenabilité.
- Modification de la gestion des transporteurs avant la sauvegarde d'un BSDA.

### Autres changements
- Mise à jour du Changelog (#4670).
- Correction de problèmes d'affichage sur les petits écrans (#4650).
- Correction d'un problème d'affichage de modales d'erreurs avant les modales de signature (#4656).
- Correction d'un problème d'affichage du header (#4666).
