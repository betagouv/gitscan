## Changelog : trackdechets (30 derniers jours, au 29 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la gestion des bordereaux (BSDA, BSFF, BSVHU), notamment concernant la modification des mentions ADR et la gestion des transferts liés à des SIRET fermés. La visibilité des données dans le registre a été renforcée et l'expérience utilisateur a été affinée via des messages d'erreur plus explicites.

### Évolutions fonctionnelles
- **Gestion des bordereaux** : 
    - Possibilité de modifier la mention ADR d'un BSDA de réexpédition ([#4845](https://github.com/MTES-MCT/trackdechets/issues/4845)).
    - Possibilité de transférer des bordereaux depuis un SIRET fermé ([#4834](https://github.com/MTES-MCT/trackdechets/issues/4834)).
- **Registre et visibilité des données** : 
    - Correction de l'absence d'apparition des documents BSVHU et BSFF dans le registre établissement immédiatement après la signature du producteur ([#4840](https://github.com/MTES-MCT/trackdechets/issues/4840)).
    - Résolution du problème des colonnes "Nom usuel" vides pour les acteurs dans le registre exhaustif ([#4836](https://github.com/MTES-MCT/trackdechets/issues/4836)).
- **Expérience utilisateur** : 
    - Amélioration des messages d'erreur destinés aux détenteurs ([#4847](https://github.com/MTES-MCT/trackdechets/issues/4847)) et lors des tentatives de transfert vers un SIRET fermé ([#4837](https://github.com/MTES-MCT/trackdechets/issues/4837)).
    - Mise à jour du texte informatif dans le bandeau de la plateforme ([#4841](https://github.com/MTES-MCT/trackdechets/issues/4841)).
    - Suppression de lignes en doublon dans certains textes de l'interface ([#4846](https://github.com/MTES-MCT/trackdechets/issues/4846)).

### Évolutions techniques
- **Analytique** : 
    - Identification de l'application pour le suivi via Matomo Beta.Gouv ([#4843](https://github.com/MTES-MCT/trackdechets/issues/4843)).
    - Simplification de la gestion du consentement suite à la suppression du besoin de cookies pour Matomo.
- **Maintenance et déploiement** : 
    - Corrections liées au processus de build et déploiement de la mise en production du 28/07/2026.

### Autres changements
- Mise à jour de la documentation du changelog.
