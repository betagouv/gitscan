## Changelog : calendars (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs et l'amélioration de la gestion des calendriers et des canaux CalDAV. Les utilisateurs bénéficieront d'une expérience plus fluide lors du déplacement d'événements, de la sélection de la langue et de la déconnexion. Des améliorations ont également été apportées à la sécurité et à la configuration des canaux CalDAV.

### Évolutions fonctionnelles
- Correction du déplacement d'événements entre les calendriers. [#52](https://github.com/suitenumerique/calendars/issues/52)
- Amélioration de la sélection de la langue et du processus de déconnexion.
- Modification du format du mot de passe des canaux CalDAV pour une meilleure sécurité. [#51](https://github.com/suitenumerique/calendars/issues/51)
- Ajout de scopes et de niveaux de scope aux canaux CalDAV, avec une interface utilisateur améliorée pour une gestion plus fine des permissions. [#50](https://github.com/suitenumerique/calendars/issues/50)
- Possibilité de convertir des calendriers individuels en "mailboxes" CalDAV. [#49](https://github.com/suitenumerique/calendars/issues/49)

### Évolutions techniques
- Séparation des mailbox et des principals individuels dans SabreDAV pour une meilleure organisation.

### Autres changements
- Le favicon est maintenant chargé à partir d'un fichier asset plutôt que d'un SVG en ligne.
- Ajout du support de la plateforme ARM64 pour les builds d'images Docker.
