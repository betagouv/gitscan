## Changelog : trackdechets (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à trackdechets au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs sur les PDF des BSVHU, l'import Excel et l'affichage des informations, ainsi que des améliorations de la sécurité, de la gestion des droits et de l'export des données. Plusieurs optimisations ont également été apportées à l'interface utilisateur et à la gestion des bordereaux.

### Évolutions fonctionnelles
- Correction du nom de la destination sur le PDF des BSVHU (#4683)
- Amélioration du support des fichiers d'import Excel (#4685)
- Affichage correct des informations des transporteurs étrangers lors de la réouverture d'un BSDA (#4644)
- Correction de l'affichage du poids sur les bordereaux signés (#4667)
- Renommage de l'opération sur la modale de signature du traitement BSDA (#4681)
- Ajout d'une expiration sur les hash d'invitation pour renforcer la sécurité (#4653)
- Affichage des intermédiaires sur le PDF du BSVHU (#4661)
- Correction de la date de signature de l'émission sur le BSDA (#4654)
- Amélioration des règles d'affichage du nom lors de l'export des entreprises (#4657)
- Modification des règles d'inclusion à l'export du registre (#4673)
- Ajout d'un rate limiting à l'export du registre pour éviter les abus (#4658)
- Affichage d'une erreur de conditionnement si l'information est manquante (#4665)
- Rendre la colonne RegistryTexsAnalysisFile.s3FileKey unique pour éviter les accès non autorisés (#4659)
- Correction du statut "En attente de traitement" pour tous les bordereaux (#4648)
- Changement des règles de traçabilité DND/TEXS selon les types d'établissements (#4643)

### Évolutions techniques
- Ajout de monitoring ELU (#4662)
- Amélioration des indexs sur RegistryLookup pour optimiser les performances (#4642)
- Suppression de l'énumération possible via la création d'une demande de droits admin (#4649)
- Nettoyage des transporteurs avant la sauvegarde d'un BSDA (#4663)
- Suppression de l'envoi systématique de `createBsdaTransporter` lors de la création d'un BSDA (#4660)
- Mise à jour du changelog (#4670)
- Modification de la logique d'envoi des emails aux administrateurs lors d'une demande de droits (#4646)
- Ne pas envoyer `isActive` si l'utilisateur n'a pas rejoint l'entreprise (#4647)

### Autres changements
- Correction d'un bug empêchant l'affichage des fiches établissement hors environnement de production (#4684)
- Correction d'un bug empêchant l'affichage de la modale d'erreur avant la modale de signature (#4656)
- Modification du k8s (#4666)
