## Changelog : calendars (30 derniers jours, au 13 novembre 2026)

### Résumé
Cette période est marquée par la publication de la version 0.2.0. Les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur (gestion des calendriers partagés, interface mobile et personnalisation de l'affichage) et sur un renforcement de la localisation (gestion des langues). La stabilité de l'infrastructure et la sécurité des droits d'accès ont également été consolidées.

### Évolutions fonctionnelles
- **Gestion des calendriers et partage**
  - Possibilité de masquer un calendrier ou de quitter un calendrier partagé [#119](https://github.com/suitenumerique/calendars/issues/119) [#110](https://github.com/suitenumerique/calendars/issues/110).
  - Amélioration du partage : support de la sélection multiple d'utilisateurs [#132](https://github.com/suitenumerique/calendars/issues/132) et envoi automatique d'invitations pour les participants ajoutés ultérieurement [#153](https://github.com/suitenumerique/calendars/issues/153).
  - Nouveaux privilèges pour les administrateurs de boîtes mail, permettant la suppression de calendriers [#73](https://github.com/suitenumerique/calendars/issues/73) [#130](https://github.com/suitenumerique/calendars/issues/130).
  - Protection contre la suppression accidentelle de calendriers gérés par synchronisation [#109](https://github.com/suitenumerique/calendars/issues/109).

- **Interface et Expérience Utilisateur (UX)**
  - Optimisation des formulaires : verrouillage de l'édition lors de la sauvegarde [#161](https://github.com/suitenumerique/calendars/issues/161) et saisie de listes d'emails dans le champ participant [#158](https://github.com/suitenumerique/calendars/issues/158).
  - Améliorations visuelles : repositionnement des boutons RSVP [#156](https://github.com/suitenumerique/calendars/issues/156), affichage de l'heure de fin sur les événements [#120](https://github.com/suitenumerique/calendars/issues/120) et mémorisation de la dernière vue du calendrier [#121](https://github.com/suitenumerique/calendars/issues/121).
  - Refonte du design des emails d'invitation [#125](https://github.com/suitenumerique/calendars/issues/125).
  - Améliorations mobiles : correction de la mise en page du menu latéral [#122](https://github.com/suitenumerique/calendars/issues/122).

- **Localisation et Authentification**
  - Amélioration globale de la gestion des langues (sélecteur, pages RSVP, gestion des erreurs API) [#106](https://github.com/suitenumerique/calendars/issues/106) [#141](https://github.com/suitenumerique/calendars/issues/141) [#138](https://github.com/suitenumerique/calendars/issues/138) [#131](https://github.com/suitenumerique/calendars/issues/131).
  - Support du "silent login" pour les utilisateurs disposant déjà d'une session SSO [#98](https://github.com/suitenumerique/calendars/issues/98).

- **Corrections de bugs**
  - Sécurisation de l'import d'événements via la vérification des droits d'écriture [#143](https://github.com/suitenumerique/calendars/issues/143).
  - Correction de la gestion des RSVP : empêche la restauration d'événements annulés [#113](https://github.com/suitenumerique/calendars/issues/113) et correction des dates d'exception (EXDATE) [#134](https://github.com/suitenumerique/calendars/issues/134).

### Évolutions techniques
- **Infrastructure et Backend**
  - Mise à jour des environnements : passage à PHP 8.5.12 [#101](https://github.com/suitenumerique/calendars/issues/101) et rafraîchissement des images de base et des certificats CA [#100](https://github.com/suitenumerique/calendars/issues/100).
  - Ajout d'un healthcheck pour l'image backend [#150](https://github.com/suitenumerique/calendars/issues/150).
  - Mise à jour du serveur Caddy vers la version 2.11.9 [#149](https://github.com/suitenumerique/calendars/issues/149).
  - Optimisation de l'infrastructure : suppression de la tâche cron de sauvegarde PostgreSQL sur Scalingo [#147](https://github.com/suitenumerique/calendars/issues/147).

- **Frontend et Build**
  - Compatibilité étendue : support de Chromium 109 et transition vers `npm` pour la gestion des dépendances frontend [#96](https://github.com/suitenumerique/calendars/issues/96).

- **Tests**
  - Ajustement de la version de `pytest` pour résoudre des problèmes de concurrence lors de l'exécution des tests.

### Autres changements
- Publication de la version 0.2.0 [#148](https://github.com/suitenumerique/calendars/issues/148).
- Mise à jour de la documentation (ajout d'images au README et correction d'informations obsolètes) [#102](https://github.com/suitenumerique/calendars/issues/102) [#105](https://github.com/suitenumerique/calendars/issues/105).
