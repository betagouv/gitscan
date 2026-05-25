## Changelog : oidc2fer (30 derniers jours, au 22 mai 2026)

### Résumé
Cette version apporte des améliorations à la gestion des identifiants SIRET et corrige un problème de sensibilité à la casse pour l'attribut `eduPersonAffiliation`. Ces changements améliorent la compatibilité et la précision de l'identification des établissements d'enseignement supérieur. La version 1.0.14 a été déployée en production.

### Évolutions fonctionnelles
- Correction : L'attribut `eduPersonAffiliation` est maintenant comparé sans tenir compte de la casse, améliorant ainsi la compatibilité avec certains fournisseurs d'identité. [#41](https://github.com/proconnect-gouv/oidc2fer/pull/41)
- Ajout : Ajout de nouvelles entités à la correspondance SIRET, notamment pour EURECOM.
- Ajout : Ajout d'autres entités à la correspondance SIRET.

### Évolutions techniques
- Déploiement : La version 1.0.14 a été déployée en production.
- Publication : Publication de la version 1.0.14.

### Autres changements
Aucun autre changement significatif à signaler.
