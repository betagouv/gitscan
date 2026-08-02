## Changelog : trackdechets (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA), ainsi que par des corrections et des évolutions fonctionnelles concernant la gestion des bordereaux de déchets, notamment en cas de changement de SIRET et d'erreurs de saisie. Des améliorations ont également été apportées à l'interface utilisateur et à la conformité légale.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier la mention ADR d'un BSDA de réexpédition. [#4845](https://github.com/MTES-MCT/trackdechets/issues/4845)
- Permet de transférer les bordereaux d'un SIRET fermé vers un SIRET ouvert. [#4834](https://github.com/MTES-MCT/trackdechets/issues/4834)
- Affichage d'un message d'erreur clair si le SIRET est fermé lors du transfert d'un BSFF. [#4837](https://github.com/MTES-MCT/trackdechets/issues/4837)
- Mise à jour du texte du bandeau d'information. [#4841](https://github.com/MTES-MCT/trackdechets/issues/4841)
- Ajout des champs "Conditionnement : (Nombre, Type et Volume)" pour tous les bordereaux. [#4825](https://github.com/MTES-MCT/trackdechets/issues/4825)
- Implémentation de l'authentification multi-facteurs (MFA) : activation, récupération de compte via code, et amélioration du wording. [#4826](https://github.com/MTES-MCT/trackdechets/issues/4826), [#4827](https://github.com/MTES-MCT/trackdechets/issues/4827), [#4830](https://github.com/MTES-MCT/trackdechets/issues/4830)
- Intégration des Mentions Légales et de la Politique de confidentialité en page WEB. [#4833](https://github.com/MTES-MCT/trackdechets/issues/4833)
- Correction d'un bug empêchant la modification des informations de contact du destinataire après signature de l'émetteur. [#4829](https://github.com/MTES-MCT/trackdechets/issues/4829)

### Évolutions techniques
- Mise à jour de Matomo pour identifier les applications concernées par Matomo Beta.Gouv. [#4843](https://github.com/MTES-MCT/trackdechets/issues/4843)
- Suppression de l'utilisation de cookies pour Matomo.
- Correction d'erreurs de build et refactoring du code.
- Changement du type de la quantité (quantity) de `Int` à `String`.
- Suppression de Crisp des cookies. [#4822](https://github.com/MTES-MCT/trackdechets/issues/4822)
- Correction d'un problème d'apparition des BSVHU & BSFF dans le registre établissement après signature du producteur. [#4840](https://github.com/MTES-MCT/trackdechets/issues/4840)

### Autres changements
- Changelog mis à jour pour la MEP du 28/07/2026. [#4842](https://github.com/MTES-MCT/trackdechets/issues/4842)
- Correction de doublons dans le texte.
- Correction de messages d'erreur pour le détenteur. [#4847](https://github.com/MTES-MCT/trackdechets/issues/4847)
- Colonnes "Nom usuel" vides pour tous les acteurs dans le registre exhaustif. [#4836](https://github.com/MTES-MCT/trackdechets/issues/4836)
- Réactivation de l'affichage des éléments MFA et Crisp en environnement Sandbox et Production. [#4835](https://github.com/MTES-MCT/trackdechets/issues/4835)
