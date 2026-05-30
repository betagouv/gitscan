## Changelog : calendars (30 derniers jours, au 29 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment la possibilité de réorganiser les calendriers et des corrections de bugs concernant l'encodage des caractères CalDAV, la sélection de la langue et la déconnexion. La gestion du déplacement d'événements entre calendriers a également été améliorée.

### Évolutions fonctionnelles
- Possibilité de réorganiser l'ordre des calendriers dans l'interface utilisateur, tant pour les utilisateurs que dans l'administration.  [#56](https://github.com/suitenumerique/calendars/issues/56)
- Correction d'un bug empêchant l'encodage correct des caractères spéciaux lors de la synchronisation CalDAV. [#817cc41](https://github.com/suitenumerique/calendars/commit/817cc41)
- Correction du flux de sélection de la langue et du processus de déconnexion. [#8902f75](https://github.com/suitenumerique/calendars/commit/8902f75)
- Amélioration du déplacement d'événements entre différents calendriers. [#52](https://github.com/suitenumerique/calendars/issues/52)

### Évolutions techniques
- Aucune évolution technique majeure à signaler durant cette période.

### Autres changements
- La favicon est maintenant chargée à partir d'un fichier d'asset au lieu d'un SVG inline. (présent dans le changelog existant)
- Ajout du support de la plateforme ARM64 pour la construction des images Docker. (présent dans le changelog existant)
