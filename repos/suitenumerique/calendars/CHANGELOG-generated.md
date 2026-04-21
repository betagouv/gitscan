## Changelog : calendars (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives concernant la gestion des canaux CalDAV, l'intégration avec des services de messagerie, et le partage d'événements. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur globale.

### Évolutions fonctionnelles
- **Canaux CalDAV :** Amélioration de l'interface utilisateur et ajout de niveaux de permission pour les canaux CalDAV [#50](https://github.com/suitenumerique/calendars/issues/50).
- **Partage d'événements :** Introduction de différents niveaux de partage avec des corrections d'interface utilisateur correspondantes [#41](https://github.com/suitenumerique/calendars/issues/41).
- **Intégration avec Messages :** Ajout de l'intégration avec des services de messagerie pour une meilleure communication autour des événements [#46](https://github.com/suitenumerique/calendars/issues/46).
- **Envoi d'invitations :** Correction d'un bug empêchant l'envoi d'invitations depuis la boîte de réception sélectionnée [#42](https://github.com/suitenumerique/calendars/issues/42).
- **URL de rappel :** Simplification de la logique des URL de rappel (callbacks) [#47](https://github.com/suitenumerique/calendars/issues/47).
- **Gestion des boîtes de réception :** Amélioration de la gestion des boîtes de réception et des principaux utilisateurs dans SabreDAV [#49](https://github.com/suitenumerique/calendars/issues/49). Possibilité de transformer des calendriers en boîtes de réception.

### Évolutions techniques
- **Audit :** Ajout de champs d'audit pour suivre les modifications apportées aux canaux et aux utilisateurs [#42](https://github.com/suitenumerique/calendars/issues/42).
- **Tests :** Correction de tests aléatoires (flaky tests) [#43](https://github.com/suitenumerique/calendars/issues/43).
- **Linting :** Correction des erreurs de linting [#44](https://github.com/suitenumerique/calendars/issues/44).
- **Format du mot de passe :** Modification du format du mot de passe des canaux CalDAV [#51](https://github.com/suitenumerique/calendars/issues/51).

### Autres changements
- Correction de plusieurs problèmes mineurs avant la première publication [#45](https://github.com/suitenumerique/calendars/issues/45).
- Correction de divers problèmes d'affichage et amélioration de la verbosité des logs.
- Masquage de la case à cocher "disponibilités" en fonction d'un indicateur de fonctionnalité.
