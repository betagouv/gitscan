## Changelog : calendars (30 derniers jours)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'application Calendars, notamment de nouvelles fonctionnalités de partage de calendriers, l'ajout de liens de confirmation de participation (RSVP) aux invitations, et des améliorations de l'interface utilisateur pour une meilleure expérience globale. Des corrections de bugs et des optimisations techniques ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de liens de confirmation de participation (RSVP) dans les emails d'invitation (#10).
- Implémentation du partage de calendriers avec une nouvelle interface utilisateur (#12).
- Ajout d'une modale d'importation pour importer des événements (#10).
- Intégration d'un bouton de visioconférence dans la modale d'événement, avec génération de lien et tests associés (#7, #8).
- Possibilité d'afficher l'URL ICS dans les emails d'invitation.
- Ajout d'une couleur par défaut pour les calendriers (#10).

### Évolutions techniques
- Ajout du support de l'architecture ARM64 pour les images Docker et mise à jour des étapes du workflow CI (#11).
- Optimisation du chargement des calendriers visibles en utilisant une seule requête SQL (#10).
- Refactorisation de la modale d'événement en composants plus petits (#7).
- Suppression des modèles `Calendar` et `CalendarShare` (#10).
- Amélioration du buildpack Scalingo et ajout d'un favicon dynamique (#10).
- Correction du CI et nettoyage général du dépôt (#12).
- Correction d'un problème de double conversion de fuseau horaire dans l'affichage du calendrier (#12).

### Autres changements
- Réorganisation de la documentation dans le dossier `docs/`.
- Correction de textes sur la page d'accueil.
- Corrections mineures de style et de formatage dans le frontend et le backend.
- Suppression des fichiers OpenSpec du suivi Git.
- Mise à jour des artefacts OpenSpec pour la correction du fuseau horaire.
- Mise à jour des compétences et commandes OpenSpec.
