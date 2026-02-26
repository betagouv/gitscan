## Changelog : histologe (30 derniers jours)

### Résumé
Les dernières mises à jour d'histologe améliorent l'expérience utilisateur et la gestion des signalements, notamment en ajoutant de nouvelles fonctionnalités pour le suivi des dossiers, la gestion des notifications et l'interconnexion avec SISH. Des améliorations techniques ont également été apportées pour optimiser les performances et la maintenance de l'application.

### Évolutions fonctionnelles
- Ajout du choix de bâtiment pour les usagers saisissant une adresse manuellement dans le formulaire de signalement (#5341).
- Possibilité d'ajouter des communes dans le back-office (#5367).
- Amélioration du filtre des signalements avec injonction (#5360).
- Ajout de la qualification "Saleté" dans les signalements (#5371).
- Ajout de la donnée "Profil Occupant" dans le front et back-office (#5329).
- Ajout du nom du partenaire ayant saisi un signalement professionnel dans la fiche signalement (#5380).
- Modification de l'affichage des informations de l'agence dans le suivi usager - détails dossier (#5355).
- Réorganisation des données et du design dans le suivi usager - détails dossier (#5324).
- Ajout de la possibilité de poursuivre une procédure (#5426).
- Ajout d'un filtre par code INSEE dans la liste des signalements via l'API (#5468).
- Ajout de la date de réaffectation dans l'API (#5464).
- Ajout de skiplinks pour faciliter la navigation dans les listes et filtres (#5377).
- Amélioration de la gestion des e-mails en échec (#5373).
- Suppression des alertes immédiates dans les notifications (#5356).
- Ajout de la qualification Saleté (#5371).
- Ajout de la qualification Saleté (#5371).
- Correction d'un bug empêchant l'envoi de notifications lors de la suppression d'un SA (#5452).
- Correction d'un bug lié à la valeur de la source de création de signalement (#5484).
- Correction d'une exception Doctrine lors de l'utilisation de Sentry (#5476).
- Correction de bugs sur les visites (#5435, #5434).
- Correction du formulaire pro pour la revue des notifications tiers déclarant pro (#5405).

### Évolutions techniques
- Mise à jour des dépendances (phpunit) (#5343).
- Mise à jour des dépendances (webpack) (#5407).
- Mise à jour des dépendances npm (#5478).
- Exécution du cron de synchronisation des fichiers bucket S3 via un service jobless (#5261).
- Organisation des nouveaux fichiers S3 par année/mois pour optimiser les synchronisations (#5331).
- Ajout de linter JS dans la CI (#5424).
- Ajout d'informations sur le territoire pour l'accès à l'API (#5334).
- Suppression de l'autocomplétion du composant de recherche par checkbox (#5406).
- Nettoyage de la configuration de l'API (#5401).
- Limitation du sélecteur de construction du front-office (#5450).
- Ajout d'un événement Matomo pour la démarche accélérée (#5366).
- Automatisation de l'envoi du rappel au bailleur sans réponse dans la démarche accélérée (#5387).
- Ajout de catégories de suivis pour la gestion des interventions depuis SISH (#5333).

### Autres changements
- Ajout de la documentation de l'API v1.3.0 (#5190).
- Suppression de dépréciations (#5422).
- Correction de l'envoi des événements Matomo (#5342).
- Correction du reset du formulaire dans une modale après une soumission réussie sans rechargement de page (#5429).
- Suppression d'une option de données vides (#5439).
- Ajout de données explicites pour la source de création de signalement (#5431).
- Ajout de la gestion des suivis arrêtés et arrêtés de main-levée même lorsqu’ils sont reçus simultanément (#5362).
- Mise à jour des tests unitaires (phpunit) (#5350).
- Fusion de la branche `main` dans `develop` (#5450, #5430, #5400, #5342, #5190).
