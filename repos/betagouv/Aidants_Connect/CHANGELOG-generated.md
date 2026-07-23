## Changelog : Aidants_Connect (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration d'un tunnel d'intégration pour les référents utilisant l'application mobile avec authentification OTP (One-Time Password). Cela inclut un nouveau parcours utilisateur pour l'onboarding, avec des pages de bienvenue, de téléchargement de l'application, de scan de QR code et de confirmation. Des corrections de tests et des améliorations de l'interface ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un tunnel d'intégration pour les référents utilisant l'application mobile avec OTP, guidant l'utilisateur à travers les étapes de configuration :
  - Page de bienvenue
  - Instructions de téléchargement de l'application
  - Scan du QR code
  - Page de confirmation ([#1785](https://github.com/betagouv/Aidants_Connect/issues/1785))
- Implémentation de la possibilité de fermer le tunnel OTP avec une méthode POST, incluant la protection CSRF et la gestion des sessions.
- Ajout d'un bouton de fermeture du tunnel OTP sur toutes les pages.

### Évolutions techniques
- Refactoring de la page de confirmation pour supprimer les espaces inutiles et mettre à jour les assertions des tests pour le flux du tunnel OTP.
- Introduction d'une nouvelle clé de session pour le dispositif TOTP afin d'éviter les conflits avec d'autres flux.
- Correction des tests France Connect ([#1783](https://github.com/betagouv/Aidants_Connect/issues/1783)).
- Ajustement de la largeur des panneaux sur les différentes pages du tunnel.
- Suppression du texte "prochaines étapes".

### Autres changements
- Aucun changement significatif à signaler.
