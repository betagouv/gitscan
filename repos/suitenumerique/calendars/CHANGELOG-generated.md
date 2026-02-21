## Changelog : calendars (30 derniers jours)

### Résumé
Ce mois-ci, l'application Calendars a bénéficié d'une refonte majeure de l'interface utilisateur, notamment du calendrier et de la gestion des événements. De nouvelles fonctionnalités ont été ajoutées, comme l'importation de calendriers, les invitations à des événements avec liens de réponse, et le partage de calendriers. Des améliorations significatives ont également été apportées à l'infrastructure et aux tests pour assurer une meilleure stabilité et performance.

### Évolutions fonctionnelles
- Ajout de liens de réponse (RSVP) dans les invitations par email (#10).
- Possibilité de partager des calendriers avec d'autres utilisateurs.
- Ajout d'une fonctionnalité d'importation de calendriers (#10).
- Amélioration de l'affichage des événements et de l'interface modale associée.
- Ajout de la génération de liens de visioconférence dans les événements (#8).
- Amélioration de l'expérience utilisateur du Scheduler, avec des performances optimisées.
- Ajout d'un logo dynamique pour les calendriers.
- Ajout de la prise en charge de l'importation d'événements via ICS.

### Évolutions techniques
- Ajout du support de l'architecture ARM64 pour les images Docker (#11).
- Refonte de l'architecture frontend avec une meilleure organisation des composants.
- Amélioration de la qualité du code React et optimisation des performances.
- Mise à jour des dépendances et refactoring du code pour une meilleure maintenabilité.
- Ajout de tests Playwright et Cypress pour une couverture de test plus complète.
- Amélioration de l'intégration avec SabreDAV, notamment pour la gestion des invitations et des abonnements.
- Ajout de nouvelles classes et plugins SabreDAV pour la normalisation des participants et la gestion des abonnements.
- Optimisation des requêtes à la base de données pour améliorer la performance du chargement des calendriers.
- Ajout de variables d'environnement pour la configuration de CalDAV.

### Autres changements
- Suppression de modèles de données Calendar et CalendarShare.
- Suppression de code et de composants inutilisés.
- Mise à jour de la documentation du projet.
- Correction de bugs mineurs liés à la conversion de fuseaux horaires.
- Amélioration du style et du formatage du code.
- Mise à jour des thèmes et des tokens de design Cunningham.
- Nettoyage du code et suppression de fichiers de suivi Git inutiles.
