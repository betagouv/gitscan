## Changelog : trackdechets (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à trackdechets au cours du dernier mois. Les utilisateurs bénéficieront d'une expérience améliorée grâce à de nouvelles fonctionnalités de filtrage, à la possibilité de sélectionner des parcelles sur un plan pour les BSDD, et à des corrections de bugs concernant l'affichage et l'export des données. Des améliorations techniques ont également été apportées pour la sécurité, la performance et la gestion des erreurs.

### Évolutions fonctionnelles
- Possibilité de sélectionner les parcelles sur un plan lors de la création d'un BSDD. [#4691](https://github.com/MTES-MCT/trackdechets/issues/4691)
- Ajout d'un filtre avancé "Contact" sur le tableau de bord. [#4671](https://github.com/MTES-MCT/trackdechets/issues/4671)
- Ajout de filtres avancés sur le siret émetteur, transporteur, entreprise de travaux et destination. [#4686](https://github.com/MTES-MCT/trackdechets/issues/4686)
- Renommage de la page "établissement" pour une meilleure clarté. [#4680](https://github.com/MTES-MCT/trackdechets/issues/4680)
- Amélioration sur le support de fichiers d'import Excel. [#4685](https://github.com/MTES-MCT/trackdechets/issues/4685)
- Affichage du BSPAOH dans l'onglet "Pour action" lorsqu'il est au statut PARTIALLY_REFUSED. [#4676](https://github.com/MTES-MCT/trackdechets/issues/4676)
- Conversion des poids sur l'export registre BSFF en tonnes. [#4675](https://github.com/MTES-MCT/trackdechets/issues/4675)
- Affichage d'un premier transporteur vide dans l'IHM registre. [#4677](https://github.com/MTES-MCT/trackdechets/issues/4677)
- Ajout de l'annulation d'export registre en cours et documentation de l'IHM. [#4696](https://github.com/MTES-MCT/trackdechets/issues/4696)
- Ajout de codes groupement à la révision BSDASRI. [#4688](https://github.com/MTES-MCT/trackdechets/issues/4688)
- Remontée du message d'erreur sur le sélecteur d'établissement émetteur BSDA. [#4687](https://github.com/MTES-MCT/trackdechets/issues/4687)

### Évolutions techniques
- Ajout d'une expiration sur les hash d'invitation pour renforcer la sécurité. [#4653](https://github.com/MTES-MCT/trackdechets/issues/4653)
- Suppression de l'action Sentry GitHub Actions car elle ne fonctionnait pas. [#4700](https://github.com/MTES-MCT/trackdechets/issues/4700)
- Correction du schéma Prisma. [#4702](https://github.com/MTES-MCT/trackdechets/issues/4702)
- Ajout d'un rate limiting à l'export de registre pour éviter les abus. [#4658](https://github.com/MTES-MCT/trackdechets/issues/4658)
- Rendre la colonne RegistryTexsAnalysisFile.s3FileKey unique pour éviter des accès non-autorisés. [#4659](https://github.com/MTES-MCT/trackdechets/issues/4659)
- Correction de la logique du rate limiting pour éviter de bloquer des usages légitimes. [#4689](https://github.com/MTES-MCT/trackdechets/issues/4689)

### Autres changements
- Correction pour autoriser le slash dans les identifiants registre. [#4693](https://github.com/MTES-MCT/trackdechets/issues/4693) et [#4695](https://github.com/MTES-MCT/trackdechets/issues/4695)
- Correction pour afficher le poids réceptionné dans l'aperçu du BSDA même s'il est égal à zéro. [#4678](https://github.com/MTES-MCT/trackdechets/issues/4678)
- Tolérance pour les anciens BSDA qui n'ont pas de quantité refusée. [#4682](https://github.com/MTES-MCT/trackdechets/issues/4682)
- Correction du nom de la destination sur le PDF du BSVHU. [#4683](https://github.com/MTES-MCT/trackdechets/issues/4683)
- Suppression des informations de chantier si un BSDA n'est plus un BSDA de Collecte sur un chantier. [#4669](https://github.com/MTES-MCT/trackdechets/issues/4669)
- Mise à jour du Changelog. [#4670](https://github.com/MTES-MCT/trackdechets/issues/4670)
- Publication de la version MEP 2026.02.1. [#4672](https://github.com/MTES-MCT/trackdechets/issues/4672)
- Modification des règles d'inclusion à l'export du registre. [#4673](https://github.com/MTES-MCT/trackdechets/issues/4673)
- Ajout d'un affichage des noms aux exports MyCompaniesCsv/MyCompaniesXls. [#4657](https://github.com/MTES-MCT/trackdechets/issues/4657)
- Correction de conflits sur readableId de BSD suite. [#4674](https://github.com/MTES-MCT/trackdechets/issues/4674)
- Correction de tests. [#4681](https://github.com/MTES-MCT/trackdechets/issues/4681) et [#4679](https://github.com/MTES-MCT/trackdechets/issues/4679)
- Correction d'un bug d'affichage "nullt" pour les poids non renseignés. [#4667](https://github.com/MTES-MCT/trackdechets/issues/4667)
- Rappatriement des hotfix de master vers dev. [#4698](https://github.com/MTES-MCT/trackdechets/issues/4698)
