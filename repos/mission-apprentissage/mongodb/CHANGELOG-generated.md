## Changelog : mongodb (30 derniers jours, au 08 juillet 2026)

### Résumé
Ce changelog présente les récentes modifications apportées à l'infrastructure MongoDB de la Mission Apprentissage. Les changements incluent une rotation de secret pour une sécurité accrue, la correction d'un problème lié à un token, et une simplification de la structure du dépôt en supprimant des sous-modules obsolètes.

### Évolutions fonctionnelles
- Correction du token `TOKEN_MNA_SHARED` [#issue à investiguer]

### Évolutions techniques
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` pour simplifier la gestion du dépôt et réduire sa complexité. [#issue à investiguer]
- Mise à jour du sous-module `.bin/shared`.
- Rotation du secret principal SOPS pour renforcer la sécurité de l'infrastructure.

### Autres changements
- Aucun changement significatif à signaler.
