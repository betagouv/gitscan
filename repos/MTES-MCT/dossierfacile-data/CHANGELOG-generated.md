## Changelog : dossierfacile-data (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations au suivi des opérations réalisées sur DossierFacile. Plus précisément, elle ajoute un nouveau type d'action enregistrée et corrige un problème lié à la gestion des identifiants de locataires (tenant_id) lors de la recherche d'applications. Ces changements permettent un suivi plus précis de l'utilisation de la plateforme et améliorent la robustesse du système.

### Évolutions fonctionnelles
- Ajout d'un nouveau type d'action enregistrée dans le suivi des opérations : `APPLICATION_SEARCHED` [#71](https://github.com/MTES-MCT/dossierfacile-data/issues/71).
- Correction d'un bug permettant d'accepter une valeur nulle pour l'identifiant du locataire (`tenant_id`) lors de l'enregistrement d'une action de type `APPLICATION_SEARCHED` [#72](https://github.com/MTES-MCT/dossierfacile-data/issues/72).

### Évolutions techniques
Aucune évolution technique significative à signaler.

### Autres changements
Aucun autre changement à signaler.
