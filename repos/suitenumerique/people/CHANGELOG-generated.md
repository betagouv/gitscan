## Changelog : people (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration avec dimail, la sécurité et l'expérience utilisateur. Les utilisateurs bénéficient d'une meilleure gestion des invitations et des liens de connexion, ainsi que de corrections de bugs pour une utilisation plus fluide. Des améliorations de sécurité ont également été apportées, notamment la correction d'une potentielle élévation de privilèges et la mise à jour de dépendances vulnérables.

### Évolutions fonctionnelles
- Les invitations envoient désormais des liens de connexion au lieu de mots de passe, améliorant la sécurité et la simplicité d'accès.
- Amélioration du message d'erreur lorsque l'utilisateur n'a pas d'adresse email secondaire.
- L'export des informations de contact du domaine est maintenant disponible dans l'interface d'administration.
- Correction de l'affichage de la langue actuelle dans le menu de profil [#1108].
- Suppression de la bordure du conteneur dans l'interface utilisateur [#1107].
- Possibilité de rafraîchir les invitations expirées.

### Évolutions techniques
- Passage à la version v2 des boîtes aux lettres (mailboxes) pour l'importation depuis dimail.
- Correction d'un bug qui empêchait l'importation des boîtes aux lettres fonctionnelles depuis dimail.
- Correction d'un bug qui envoyait le code de connexion à une URL dimail incorrecte.
- Correction d'une potentielle élévation de privilèges lors de l'invitation d'utilisateurs.
- Mise à jour de la dépendance `dimail` vers la version v0.6.5.
- Mise à jour de la dépendance `pillow` vers la version 12.2.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `pytest` vers la version 9.0.3 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `next` vers la version 15.5.15 pour corriger une vulnérabilité de sécurité.

### Autres changements
- Mise à jour des chaînes de caractères traduites pour l'internationalisation.
- Amélioration du message affiché lorsqu'il n'y a pas d'alias sur la page du domaine.
- Ajout d'informations de contact du domaine à l'export.
- Correction d'un bug empêchant l'importation des boîtes aux lettres fonctionnelles depuis dimail.
