## Changelog : trackdechets (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par l'amélioration de la gestion des bordereaux, notamment la possibilité de transférer des documents entre des SIRET fermés et ouverts. Des corrections importantes ont été apportées au registre pour garantir la visibilité et l'exactitude des données, tout en affinant les messages d'erreur pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Gestion des SIRET** : Possibilité de transférer des bordereaux (BSFF/BSVHU) d'un SIRET fermé vers un SIRET ouvert, y compris pour les dossiers en attente de groupement [#4834](https://github.com/MTES-MCT/trackdechets/issues/4834).
- **Édition de documents** : Ajout de la possibilité de modifier la mention ADR sur un BSDA de réexpédition [#4845](https://github.com/MTES-MCT/trackdechets/issues/4845).
- **Registre et visibilité** : 
    - Correction de l'affichage du registre exhaustif (les colonnes "Nom usuel" sont désormais correctement renseignées) [#4836](https://github.com/MTES-MCT/trackdechets/issues/4836).
    - Correction de l'absence d'apparition des bordereaux BSVHU et BSFF dans le registre établissement dès la signature du producteur [#4840](https://github.com/MTES-MCT/trackdechets/issues/4840).
- **Expérience utilisateur** : 
    - Amélioration et clarification des messages d'erreur pour les détenteurs [#4847](https://github.com/MTES-MCT/trackdechets/issues/4847).
    - Affichage de messages d'erreur spécifiques lors de tentatives de transfert sur des SIRET fermés [#4837](https://github.com/MTES-MCT/trackdechets/issues/4837).
    - Mise à jour du texte informatif présent dans le bandeau de l'interface [#4841](https://github.com/MTES-MCT/trackdechets/issues/4841).

### Évolutions techniques
- **Analytique** : Identification des applications pour Matomo Beta.Gouv et simplification de la gestion du consentement (suppression de la contrainte de cookies pour Matomo) [#4843](https://github.com/MTES-MCT/trackdechets/issues/4843).
- **Sécurité et conformité** : Réactivation de l'affichage des éléments MFA (authentification multi-facteurs) et Crisp en environnements de Sandbox et de Production [#4835](https://github.com/MTES-MCT/trackdechets/issues/4835).
- **Maintenance et déploiement** : Résolution d'erreurs de build et corrections liées aux processus de mise en production.

### Autres changements
- **Nettoyage** : Suppression de lignes en doublon dans certains textes de l'interface [#4846](https://github.com/MTES-MCT/trackdechets/issues/4846).
