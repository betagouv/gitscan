## Changelog : calendars (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'application Calendars, notamment l'ajout de fonctionnalités de partage de calendriers, de liens de confirmation de participation (RSVP) et d'importation d'événements. L'interface utilisateur a également été améliorée, et des corrections ont été apportées pour optimiser les performances et la stabilité de l'application. De plus, le support de l'architecture ARM64 a été ajouté pour les images Docker.

### Évolutions fonctionnelles
- Ajout de liens de confirmation de participation (RSVP) dans les emails d'invitation aux événements [#10](https://github.com/suitenumerique/calendars/issues/10).
- Implémentation du partage de calendriers avec une nouvelle interface utilisateur et suppression de la terminologie "agenda" [#12](https://github.com/suitenumerique/calendars/issues/12).
- Ajout d'une fonctionnalité d'importation d'événements via un modal dédié.
- Ajout d'un bouton de visioconférence dans le modal d'événement, avec génération d'un lien [#8](https://github.com/suitenumerique/calendars/issues/8).
- Ajout d'un backend pour la gestion des "Entitlements" avec support pour Deploy Center [#31](https://github.com/suitenumerique/calendars/issues/31).
- Ajout d'une couleur par défaut pour les calendriers.

### Évolutions techniques
- Ajout du support de l'architecture ARM64 pour les images Docker et amélioration du workflow CI [#11](https://github.com/suitenumerique/calendars/issues/11).
- Refactoring du `EventModal` en composants de section pour une meilleure organisation du code [#7](https://github.com/suitenumerique/calendars/issues/7).
- Optimisation de la récupération des calendriers visibles en utilisant une seule requête et en les affichant de manière plus efficace [#12](https://github.com/suitenumerique/calendars/issues/12).
- Suppression des modèles `Calendar` et `CalendarShare` pour simplifier la structure des données [#12](https://github.com/suitenumerique/calendars/issues/12).
- Ajout d'un buildpack Scalingo et d'une favicon dynamique.
- Amélioration du CI et nettoyage général du code [#12](https://github.com/suitenumerique/calendars/issues/12).

### Autres changements
- Réorganisation de la documentation dans le dossier `docs/` [#12](https://github.com/suitenumerique/calendars/issues/12).
- Corrections de textes sur la page d'accueil.
- Corrections mineures de style et de formatage du code.
- Ajout de tests pour la fonctionnalité de visioconférence.
- Extraction de l'URL ICS et affichage dans les emails d'invitation.
