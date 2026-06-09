## Changelog : calendars (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives, notamment une refonte de la gestion des RSVP (réponses à une invitation), un renforcement de la sécurité pour l'importation de données CalDAV, et une migration technique majeure du frontend de Next.js vers Vite pour une meilleure performance et expérience de développement. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **RSVP :** Amélioration significative de la gestion des RSVP, incluant une refonte des modèles d'emails et de pages, permettant une confirmation de participation directement depuis l'interface utilisateur. [#60](https://github.com/suitenumerique/calendars/issues/60)
- **Gestion des calendriers :** Possibilité de réorganiser les calendriers dans l'interface utilisateur, avec des corrections d'interface et d'administration associées. [#56](https://github.com/suitenumerique/calendars/issues/56)
- **CalDAV :** Renforcement de la sécurité lors de la manipulation des données ICS importées via CalDAV. [#59](https://github.com/suitenumerique/calendars/issues/59)
- **Langue et déconnexion :** Correction des flux de sélection de la langue et de déconnexion. [#8902f75](https://github.com/suitenumerique/calendars/commit/8902f75f6151530444131766c962a6f215f63f8f)

### Évolutions techniques
- **Frontend :** Migration du frontend de Next.js vers Vite pour améliorer les performances et l'expérience de développement. [#63](https://github.com/suitenumerique/calendars/issues/63)
- **CalDAV :** Suppression de la librairie `tsdav` et refactorisation du chemin réseau pour une meilleure gestion des requêtes CalDAV. [#58](https://github.com/suitenumerique/calendars/issues/58)
- **Dépendances :** Fixation des versions des dépendances Composer pour assurer la stabilité et retour à la version principale de SabreDAV. [#61](https://github.com/suitenumerique/calendars/issues/61)
- **RSVP :** Factorisation du code de composition des emails entre SMTP et Messages pour une meilleure maintenabilité. [#64](https://github.com/suitenumerique/calendars/issues/64)

### Autres changements
- Correction de l'encodage des caractères spéciaux lors de l'importation CalDAV. [#817cc41](https://github.com/suitenumerique/calendars/commit/817cc41779316b69a14a020987d04698d49a519b)
