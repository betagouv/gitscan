## Changelog : calendars (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'améliorations significatives, notamment une refonte de la gestion des RSVP, une meilleure sécurité dans le traitement des données CalDAV, et une migration technique importante du frontend de Next.js vers Vite. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une expérience utilisateur plus fluide.

### Évolutions fonctionnelles
- **RSVP :** Refonte complète des modèles d'emails et de pages de confirmation de participation, avec correction de bugs associés [#60](https://github.com/suitenumerique/calendars/issues/60).
- **RSVP :** Amélioration de la confirmation de participation directement depuis l'interface utilisateur [#60](https://github.com/suitenumerique/calendars/issues/60).
- **Calendriers :** Possibilité de réorganiser les calendriers dans l'interface, avec des corrections d'administration et de mise en page [#56](https://github.com/suitenumerique/calendars/issues/56).
- **Déplacement d'événements :** Correction d'un bug empêchant le déplacement d'événements entre différents calendriers [#52](https://github.com/suitenumerique/calendars/issues/52).
- **Langue et déconnexion :** Correction de bugs concernant la sélection de la langue et le processus de déconnexion.

### Évolutions techniques
- **Frontend :** Migration du framework frontend de Next.js vers Vite pour améliorer les performances et l'expérience de développement [#63](https://github.com/suitenumerique/calendars/issues/63).
- **CalDAV :** Renforcement de la sécurité du traitement des données ICS (iCalendar) [#59](https://github.com/suitenumerique/calendars/issues/59).
- **CalDAV :** Suppression de la librairie `tsdav` et refactorisation du chemin réseau pour une meilleure gestion des requêtes CalDAV [#58](https://github.com/suitenumerique/calendars/issues/58).
- **SabreDAV :** Fixation des dépendances Composer et retour à la version principale de SabreDAV pour bénéficier des dernières corrections et fonctionnalités [#61](https://github.com/suitenumerique/calendars/issues/61).
- **Encodage :** Correction de l'encodage des caractères spéciaux lors de l'importation de données CalDAV.

### Autres changements
- Aucun changement significatif à signaler dans cette catégorie.
