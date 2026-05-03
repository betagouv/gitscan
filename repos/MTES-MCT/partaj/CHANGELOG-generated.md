## Changelog : partaj (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des pièces jointes (appendices) et la notification des co-demandeurs lors de l'envoi d'une saisine. Des optimisations internes et des corrections de bugs ont également été apportées pour améliorer la stabilité et la qualité du code.

### Évolutions fonctionnelles
- Amélioration de la fonctionnalité de gestion des pièces jointes : ajout des appendices aux publications et correction de problèmes liés à leur affichage et à leur enregistrement. [#10](https://github.com/MTES-MCT/partaj/issues/10)
- Les co-demandeurs sont désormais notifiés lorsqu'une saisine leur est envoyée. [#N732](https://github.com/MTES-MCT/partaj/issues/N732)

### Évolutions techniques
- Synchronisation des versions de PostgreSQL, Elasticsearch et Django pour assurer la cohérence de l'infrastructure.
- Suppression d'imports inutiles pour alléger le code et améliorer sa lisibilité.
- Ajout de tests pour la fonctionnalité de referral.

### Autres changements
- Préparation du déploiement sur l'environnement de staging.
- Correction de la formulation concernant les appendices.
- Amélioration du lien envoyé par email lors de la notification.
