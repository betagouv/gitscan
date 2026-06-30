## Changelog : domifa (30 derniers jours, au 29 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections de bugs et améliorations de la sécurité, notamment concernant l'authentification, la gestion des utilisateurs et la protection contre les attaques. Des améliorations ont également été apportées à la gestion des organismes et à l'expérience utilisateur, notamment sur le portail usager.

### Évolutions fonctionnelles
- Ajout de la possibilité de spécifier "autre" comme type d'organisme et raison.
- Amélioration de la gestion des utilisateurs bloqués : suppression de la possibilité de les éditer.
- Ajout de filtres pour la recherche des utilisateurs supprimés.
- Amélioration de la gestion des téléchargements avec ajout d'un blocage.
- Ajout de statistiques sur les sessions utilisateurs.
- Correction du formulaire de mot de passe et du texte associé.
- Correction de l'affichage des alertes de warning.
- Correction de l'affichage du caractère arobase (@) dans les textes.
- Correction du test du portail usager.
- Ajout de titres et de pages manquantes.

### Évolutions techniques
- Mise en place d'une table IP pour la gestion des accès.
- Ajout d'un filtre HTTP.
- Ajout d'un filtre d'exception.
- Ajout de tests unitaires et correction de tests existants.
- Ajout de logs pour les échecs de connexion.
- Correction de problèmes de linting.
- Ajout d'un testeur de mail générique.
- Correction potentielle d'une vulnérabilité de type "CodeQL / Type confusion through parameter tampering".
- Ajout de mailing via tipimail.
- Correction de la gestion des boutons en OTP.

### Autres changements
- Suppression de la fabrique sociale.
- Correction de la construction de l'application frontend.
- Correction de typages.
- Mise à jour de la configuration du portail.
