## Changelog : calendars (30 derniers jours)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'une refonte majeure de l'interface utilisateur, notamment au niveau de l'affichage des événements et de la gestion des calendriers. De nouvelles fonctionnalités ont été ajoutées, comme l'importation de calendriers, les liens de confirmation de participation aux invitations, et le partage de calendriers. Des améliorations significatives ont également été apportées à la compatibilité et à la performance de l'application.

### Évolutions fonctionnelles
- Ajout de liens de confirmation de participation (RSVP) dans les emails d'invitation (#10).
- Possibilité de partager des calendriers avec d'autres utilisateurs.
- Ajout d'une fonctionnalité d'importation de calendriers (#10).
- Amélioration de l'affichage des événements et ajout de nouvelles fonctionnalités à la modale d'événement.
- Ajout de la génération de liens de visioconférence dans les événements (#8).
- Amélioration de l'expérience utilisateur du calendrier (Scheduler) avec une nouvelle interface et des performances optimisées.
- Ajout d'un logo dynamique pour les calendriers.
- Ajout d'une bannière d'accueil.

### Évolutions techniques
- Ajout du support de l'architecture ARM64 pour les images Docker (#11).
- Refonte de l'architecture frontend avec une meilleure organisation des composants et des types.
- Implémentation d'un service CalDAV pour la synchronisation avec des calendriers externes.
- Ajout de tests Playwright et Cypress pour améliorer la qualité du code et la couverture des tests.
- Amélioration de la gestion des timezones et correction d'un bug lié à la double conversion.
- Ajout de plugins SabreDAV pour améliorer la compatibilité et les fonctionnalités.
- Optimisation des requêtes à la base de données pour améliorer les performances.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de la configuration et des outils de développement (OpenSpec).

### Autres changements
- Correction de textes sur la page d'accueil.
- Nettoyage du code et suppression de composants inutilisés.
- Mise à jour de la documentation du projet.
- Correction de bugs mineurs et améliorations de la stabilité.
- Suppression de modèles de calendriers inutiles.
- Ajout de variables d'environnement pour la configuration CalDAV.
- Ajout de modèles d'emails pour les invitations.
