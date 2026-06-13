## Changelog : calendars (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives, notamment une refonte de la gestion des RSVP, un renforcement de la sécurité du traitement des données ICS, et une migration technique majeure du frontend vers Vite pour une meilleure performance et expérience de développement. Des améliorations de l'interface utilisateur, comme le réordonnancement des calendriers, ont également été apportées.

### Évolutions fonctionnelles
- **RSVP :** Amélioration significative du processus de confirmation de participation (RSVP) avec une refonte des modèles d'emails et de pages, permettant une confirmation directement depuis l'interface utilisateur. [#60](https://github.com/suitenumerique/calendars/issues/60)
- **RSVP :** Factorisation du code de composition des emails pour les RSVP, permettant une utilisation commune entre les envois par SMTP et par Messages. [#64](https://github.com/suitenumerique/calendars/issues/64)
- **Calendriers :** Possibilité de réordonner les calendriers dans l'interface utilisateur, offrant une meilleure organisation et personnalisation. [#56](https://github.com/suitenumerique/calendars/issues/56)
- **Interface utilisateur :** Corrections et améliorations diverses de l'interface utilisateur et de la mise en page, notamment dans l'administration. [#56](https://github.com/suitenumerique/calendars/issues/56)

### Évolutions techniques
- **Frontend :** Migration du frontend de Next.js vers Vite, pour améliorer les performances et l'expérience de développement. [#63](https://github.com/suitenumerique/calendars/issues/63)
- **CalDAV :** Suppression de la librairie `tsdav` et refactorisation du chemin réseau pour une meilleure gestion des données CalDAV. [#58](https://github.com/suitenumerique/calendars/issues/58)
- **CalDAV :** Renforcement de la sécurité du traitement des données ICS pour prévenir les vulnérabilités. [#59](https://github.com/suitenumerique/calendars/issues/59)
- **Dépendances :** Fixation des versions des dépendances Composer pour assurer la stabilité et la compatibilité avec l'upstream SabreDAV. [#61](https://github.com/suitenumerique/calendars/issues/61)

### Autres changements
- Préparation de la version 0.1.0.
- Corrections et améliorations mineures diverses.
