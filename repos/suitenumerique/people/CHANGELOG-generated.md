## Changelog : people (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des boîtes aux lettres et la correction de bugs liés à l'importation et à l'utilisation de dimail. Des corrections de sécurité ont également été apportées, notamment des mises à jour de dépendances. L'authentification via liens de connexion pour les boîtes aux lettres a été implémentée, améliorant ainsi la sécurité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Les liens de connexion sont désormais envoyés aux boîtes aux lettres au lieu des mots de passe, améliorant la sécurité. [#1108](https://github.com/suitenumerique/people/issues/1108)
- Amélioration du message d'erreur lorsque aucune adresse e-mail secondaire n'est disponible.
- Correction de l'envoi du code de connexion à l'URL dimail incorrecte.
- Correction du suivi des redirections depuis dimail.
- Correction d'un bug empêchant l'importation de boîtes aux lettres fonctionnelles.

### Évolutions techniques
- Passage à mailboxes v2 pour l'importation.
- Mise à jour de la bibliothèque urllib3 vers la version 2.7.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de Django vers la version 6.0.5 pour corriger une vulnérabilité de sécurité.
- Mise à jour de Pillow vers la version 12.2.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de pytest vers la version 9.0.3 pour corriger une vulnérabilité de sécurité.
- Mise à jour de next vers les versions 15.5.15 et 15.5.18 pour corriger des vulnérabilités de sécurité.
- Correction d'un problème de possible élévation de privilèges lors de l'invitation.
- Correction d'un bug lié à la gestion des slashs dans les endpoints dimail.

### Autres changements
- Mise à jour des chaînes de caractères traduits (i18n).
- Amélioration du message "pas d'alias" sur la vue domaine (front-end).
- Mise à jour de la documentation concernant dimail.
- Correction d'un bug dans le menu de profil concernant la langue actuelle.
- Suppression de la bordure du conteneur dans l'interface utilisateur.
