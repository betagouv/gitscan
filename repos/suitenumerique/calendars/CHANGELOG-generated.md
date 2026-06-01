## Changelog : calendars (30 derniers jours, au 30 mai 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment la possibilité de réorganiser les calendriers et des corrections de bugs concernant l'encodage des caractères CalDAV, la sélection de la langue et la gestion des événements. Une refactorisation importante a également été effectuée pour supprimer une dépendance CalDAV obsolète.

### Évolutions fonctionnelles
- Possibilité de réorganiser les calendriers via l'interface utilisateur, avec des ajustements correspondants dans l'administration et la mise en page. [#56](https://github.com/suitenumerique/calendars/issues/56)
- Correction d'un bug empêchant l'encodage correct des caractères spéciaux lors de la synchronisation CalDAV. [#817cc41](https://github.com/suitenumerique/calendars/commit/817cc41)
- Correction du flux de sélection de la langue et de la déconnexion. [#8902f75](https://github.com/suitenumerique/calendars/commit/8902f75)
- Correction d'un bug empêchant le déplacement d'événements entre les calendriers. [#52](https://github.com/suitenumerique/calendars/issues/52)

### Évolutions techniques
- Suppression de la librairie `tsdav` et refactorisation du chemin réseau CalDAV pour simplifier et améliorer la maintenance. [#58](https://github.com/suitenumerique/calendars/issues/58)

### Autres changements
- Aucun changement significatif à signaler.
