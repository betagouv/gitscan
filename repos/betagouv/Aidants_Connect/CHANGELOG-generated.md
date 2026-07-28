## Changelog : Aidants_Connect (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration d'un tunnel d'intégration pour les référents utilisant une application mobile avec authentification à deux facteurs (OTP), ainsi que sur l'amélioration de la gestion des informations relatives aux organisations (SIRET) lors de l'export de données. Des corrections de tests France Connect ont également été apportées.

### Évolutions fonctionnelles
- **Tunnel d'intégration OTP pour les référents:** Ajout d'un parcours d'intégration guidé pour les référents utilisant une application mobile avec authentification à deux facteurs (QR code, téléchargement de l'application, etc.) [#1785](https://github.com/betagouv/Aidants_Connect/issues/1785).
- **Gestion des SIRET:**
    - Ajout de champs pour le nettoyage des numéros SIRET lors de l'export global des données [#1802](https://github.com/betagouv/Aidants_Connect/issues/1802).
    - Ajout d'un champ pour sauvegarder les numéros SIRET invalides [#1799](https://github.com/betagouv/Aidants_Connect/issues/1799).
    - Ajout d'un champ pour sauvegarder les doublons de numéros SIRET et modification de l'interface d'administration des organisations [#1800](https://github.com/betagouv/Aidants_Connect/issues/1800).
- **API FNE:** Modifications et implémentation de l'API FNE [#1801](https://github.com/betagouv/Aidants_Connect/issues/1801).

### Évolutions techniques
- **Tests France Connect:** Correction des tests liés à l'authentification via France Connect [#1783](https://github.com/betagouv/Aidants_Connect/issues/1783).
- **Sécurité OTP:** Implémentation de la méthode POST pour la suppression du tunnel OTP, avec ajout de protections CSRF et gestion des sessions.
- **Refactoring template:** Refactoring du template de la page de félicitations pour supprimer les espaces inutiles et mettre à jour les assertions des tests pour le flux OTP.
- **Gestion des sessions OTP:** Introduction d'une nouvelle clé de session pour le dispositif TOTP afin d'éviter les conflits avec d'autres flux.
- **Améliorations visuelles tunnel OTP:** Corrections de la largeur des panneaux et suppression du texte "prochaines étapes" sur les différentes pages du tunnel OTP.

### Autres changements
- Aucun changement significatif à signaler.
