## Changelog : trackdechets (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à trackdechets au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de la gestion des BSDD (Bon de Suivi Déchet), des BSDA (Bon de Suivi Déchet d'Autorisation) et des registres, ainsi que des corrections de bugs et des optimisations de l'interface utilisateur. Des améliorations ont également été apportées aux filtres et à la gestion des établissements.

### Évolutions fonctionnelles
- Possibilité de sélectionner les parcelles sur un plan lors de la création d'un BSDD. [#4691](https://github.com/MTES-MCT/trackdechets/issues/4691)
- Ajout d'un filtre avancé "Contact" sur le tableau de bord. [#4671](https://github.com/MTES-MCT/trackdechets/issues/4671)
- Ajout de l'annulation d'export registre en cours, avec documentation de l'IHM. [#4696](https://github.com/MTES-MCT/trackdechets/issues/4696)
- Affichage du BSPAOH dans l'onglet "Pour action" lorsqu'il est au statut PARTIALLY_REFUSED. [#4676](https://github.com/MTES-MCT/trackdechets/issues/4676)
- Conversion des poids sur export registre BSFF en tonnes. [#4675](https://github.com/MTES-MCT/trackdechets/issues/4675)
- Ajouts de filtres avancés sur le siret émetteur, transporteur, entreprise de travaux, destination. [#4686](https://github.com/MTES-MCT/trackdechets/issues/4686)
- Suppression des informations de chantier si un BSDA n'est plus un BSDA de Collecte sur un chantier. [#4669](https://github.com/MTES-MCT/trackdechets/issues/4669)
- Renommage de la page établissement. [#4680](https://github.com/MTES-MCT/trackdechets/issues/4680)
- Correction sur le PDF du BSVHU, avec le bon nom pour la destination. [#4683](https://github.com/MTES-MCT/trackdechets/issues/4683)
- Amélioration sur le support de fichiers d'import Excel. [#4685](https://github.com/MTES-MCT/trackdechets/issues/4685)
- Correction pour afficher correctement les poids lors de la signature émetteur (ne pas afficher "nullt"). [#4667](https://github.com/MTES-MCT/trackdechets/issues/4667)
- Renommage de l'opération sur la modale de signature du traitement BSDA. [#4681](https://github.com/MTES-MCT/trackdechets/issues/4681)
- Correction pour autoriser les slashs dans l'ID registre. [#4693](https://github.com/MTES-MCT/trackdechets/issues/4693) et [#4695](https://github.com/MTES-MCT/trackdechets/issues/4695)
- Permettre une révision du code famille. [#4692](https://github.com/MTES-MCT/trackdechets/issues/4692)
- Les "Installation de valorisation de terres et sédiments" peuvent être visées sur des BSDD de déchets non-dangereux. [#4704](https://github.com/MTES-MCT/trackdechets/issues/4704)
- Corriger wording consistence BSPAOH. [#4705](https://github.com/MTES-MCT/trackdechets/issues/4705)
- Fix pickupSite for bsda. [#4710](https://github.com/MTES-MCT/trackdechets/issues/4710)

### Évolutions techniques
- Querying de l'API geo.gouv.fr depuis le backend pour éviter des problèmes de CORS. [#4703](https://github.com/MTES-MCT/trackdechets/issues/4703)
- Correction du schéma Prisma. [#4702](https://github.com/MTES-MCT/trackdechets/issues/4702)
- Suppression de l'action Sentry GH car elle ne fonctionne pas. [#4700](https://github.com/MTES-MCT/trackdechets/issues/4700)
- Ajout d'une expiration sur les hash d'invitation pour renforcer la sécurité. [#4653](https://github.com/MTES-MCT/trackdechets/issues/4653)
- Changement de la logique du rate limiting pour éviter de bloquer des usages légitimes. [#4689](https://github.com/MTES-MCT/trackdechets/issues/4689)
- Résolution de conflits sur readableId de BSD suite. [#4674](https://github.com/MTES-MCT/trackdechets/issues/4674)
- Rappatriement des hotfix de master > dev. [#4698](https://github.com/MTES-MCT/trackdechets/issues/4698)

### Autres changements
- Mise à jour du schéma d'architecture du README. [#4668](https://github.com/MTES-MCT/trackdechets/issues/4668)
- Ajout de codes groupement à la révision BSDASRI. [#4688](https://github.com/MTES-MCT/trackdechets/issues/4688)
- Remonter le message d'erreur sur le sélecteur d'établissement émetteur BSDA. [#4687](https://github.com/MTES-MCT/trackdechets/issues/4687)
- Afficher un premier transporteur vide dans l'IHM registre. [#4677](https://github.com/MTES-MCT/trackdechets/issues/4677)
- Fix tests. [#4682](https://github.com/MTES-MCT/trackdechets/issues/4682)
