## Changelog : calendars (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives, notamment une refonte de la gestion des RSVP (réponses à une invitation), un renforcement de la sécurité du traitement des données CalDAV, et une migration technique majeure du frontend vers Vite pour de meilleures performances. Des améliorations de l'interface utilisateur, comme le réordonnancement des calendriers, ont également été apportées.

### Évolutions fonctionnelles
- **RSVP (Réponses aux invitations):**
    - Refonte complète des modèles d'emails et de pages RSVP, avec correction de bugs associés. [#64](https://github.com/suitenumerique/calendars/issues/64)
    - Possibilité de répondre directement aux invitations depuis l'interface utilisateur. [#60](https://github.com/suitenumerique/calendars/issues/60)
- **Calendriers:**
    - Ajout de la fonctionnalité de réordonnancement des calendriers dans l'interface utilisateur. [#56](https://github.com/suitenumerique/calendars/issues/56)
    - Corrections d'erreurs d'encodage des caractères spéciaux lors de la synchronisation CalDAV. [#817cc41](https://github.com/suitenumerique/calendars/commit/817cc41)
- **Sécurité:**
    - Renforcement de la sécurité du traitement des données ICS (iCalendar) pour prévenir les vulnérabilités. [#59](https://github.com/suitenumerique/calendars/issues/59)

### Évolutions techniques
- **Frontend:**
    - Migration du frontend de Next.js vers Vite, pour améliorer les performances et l'expérience de développement. [#63](https://github.com/suitenumerique/calendars/issues/63)
- **CalDAV:**
    - Suppression de la librairie `tsdav` et refactorisation du chemin réseau pour une meilleure gestion de la synchronisation CalDAV. [#58](https://github.com/suitenumerique/calendars/issues/58)
    - Fixation des dépendances Composer et retour à la version principale de SabreDAV pour une meilleure stabilité. [#61](https://github.com/suitenumerique/calendars/issues/61)
- **RSVP:**
    - Factorisation du code de composition des emails entre SMTP et Messages pour une meilleure maintenabilité. [#64](https://github.com/suitenumerique/calendars/issues/64)

### Autres changements
- Corrections et améliorations de l'interface d'administration et de la mise en page générale. [#56](https://github.com/suitenumerique/calendars/issues/56)
