## Changelog : calendars (30 derniers jours, au 20 avril 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'intégration avec les canaux CalDAV et l'ajout de nouvelles fonctionnalités liées aux boîtes aux lettres et aux invitations. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant l'envoi d'invitations et l'affichage de l'interface.

### Évolutions fonctionnelles
- **Canaux CalDAV :** Ajout de scopes pour les canaux CalDAV, amélioration de l'interface utilisateur et modification du format du mot de passe CalDAV. [#50](https://github.com/suitenumerique/calendars/issues/50) et [#51](https://github.com/suitenumerique/calendars/issues/51)
- **Boîtes aux lettres :** Intégration avec Messages pour les boîtes aux lettres. [#46](https://github.com/suitenumerique/calendars/issues/46)
- **Invitations :** Correction d'un bug empêchant l'envoi d'invitations depuis la boîte aux lettres sélectionnée.
- **Callbacks :** Simplification de la logique des URLs de callback. [#47](https://github.com/suitenumerique/calendars/issues/47)
- **Calendriers :** Possibilité de mettre à niveau des calendriers individuels en boîtes aux lettres.

### Évolutions techniques
- **SabreDAV :** Séparation de la boîte aux lettres et des principaux utilisateurs dans SabreDAV. [#49](https://github.com/suitenumerique/calendars/issues/49)
- **Interface utilisateur :** Masquage de la case à cocher "disponibilités" dans la modale d'édition en fonction d'un flag de fonctionnalité.
- **Affichage :** Correction de plusieurs problèmes d'affichage et amélioration de la verbosité des logs.

### Autres changements
- Aucun changement significatif à signaler.
