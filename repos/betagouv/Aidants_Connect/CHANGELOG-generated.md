## Changelog : Aidants_Connect (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration d'un nouveau tunnel d'intégration pour les référents utilisant l'authentification par OTP (One-Time Password), permettant une meilleure expérience pour la connexion via application mobile. Des corrections de tests et des ajustements d'interface ont également été réalisés.

### Évolutions fonctionnelles
- Implémentation d'un tunnel d'intégration OTP pour les référents, incluant les pages de bienvenue, de téléchargement de l'application, de scan du QR code et de félicitations. [#1785](https://github.com/betagouv/Aidants_Connect/issues/1785)
- Ajout d'un bouton de fermeture sur toutes les pages du tunnel OTP.
- Possibilité de renvoyer le texte sur les pages du tunnel OTP.
- Implémentation de la méthode POST pour la fermeture du tunnel OTP, avec protection CSRF et gestion appropriée des sessions.
- Introduction d'une nouvelle clé de session pour le dispositif TOTP afin d'éviter les conflits avec d'autres flux.

### Évolutions techniques
- Refactorisation de la page de félicitations du tunnel OTP pour supprimer les espaces blancs inutiles et mettre à jour les assertions des tests.
- Correction des tests France Connect. [#1783](https://github.com/betagouv/Aidants_Connect/issues/1783)
- Correction de la largeur des panneaux sur les différentes pages du tunnel.
- Suppression du texte "prochaines étapes" sur les pages du tunnel.
