## Changelog : people (30 derniers jours, au 11 mai 2026)

### Résumé
Les récentes mises à jour de l'application People se concentrent sur l'amélioration de l'intégration avec dimail, notamment en passant à la version 2 de mailboxes et en envoyant des liens de connexion plutôt que des mots de passe. Des corrections de sécurité et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Passage à mailboxes v2 pour l'importation depuis dimail, améliorant la compatibilité et la stabilité.
- Envoi de liens de connexion au lieu de mots de passe lors de l'utilisation de dimail, renforçant la sécurité.
- Amélioration du message d'erreur affiché lorsqu'il n'y a pas d'adresse email secondaire.
- Export des informations de contact du domaine depuis l'interface d'administration.
- Correction d'un bug où le code de connexion était envoyé à une URL dimail incorrecte.
- Correction d'un bug empêchant l'importation de certaines boîtes aux lettres fonctionnelles depuis dimail.
- Amélioration de l'affichage du message "pas d'alias" dans la vue des domaines.
- Correction de l'affichage de la langue actuelle dans le menu de profil [#1108].
- Suppression de la bordure du conteneur dans l'interface utilisateur [#1107].

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5 (incluant des correctifs de sécurité).
- Mise à jour de Pillow vers la version 12.2.0 (correctif de sécurité).
- Mise à jour de pytest vers la version 9.0.3 (correctif de sécurité).
- Mise à jour de next vers la version 15.5.15 (correctif de sécurité).
- Correction d'une possible escalade de privilèges lors de l'invitation d'utilisateurs.
- Correction d'un bug empêchant l'accès aux rôles attendus lors de la création d'invitations par email.
- Correction d'un bug lié à la gestion des majuscules/minuscules lors de la recherche d'emails existants.

### Autres changements
- Mise à jour des chaînes de caractères traduites pour l'internationalisation.
- Documentation mise à jour concernant l'utilisation de dimail.
