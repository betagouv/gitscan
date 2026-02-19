## Changelog : histologe (30 derniers jours)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans le suivi des dossiers, la gestion des signalements et des notifications. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Des améliorations ont été apportées à l'interconnexion avec SISH et à la gestion des partenaires.

### Évolutions fonctionnelles
- Ajout de la qualification "Saleté" dans les signalements (#5371).
- Possibilité pour les usagers d'envoyer des messages après la réouverture d'un signalement clôturé (#5320).
- Amélioration de la réorganisation des données et du design dans les détails de dossier du suivi usager (#5324).
- Ajout du choix de bâtiment pour les usagers saisissant une adresse manuellement (#5341).
- Ajout du nom du partenaire ayant saisi un signalement professionnel (#5380).
- Possibilité de filtrer les dossiers sans activité partenaire sur le statut de l'affectation pour un agent (#5325).
- Simplification de la création de périmètre pour les partenaires (#5287).
- Ajout de la nature du parc dans la liste des signalements (#5311).
- Amélioration de la gestion des e-mails en échec (correction de bugs) (#5373).
- Passage sur un nouveau système de messages de confirmation/erreur pour les visites (#5265).
- Ajout d'un rappel automatique pour le suivi mensuel dans la démarche accélérée (#5304).
- Modification des informations de l'agence dans les détails du dossier de suivi usager (#5355).
- Ajout de la division du menu SA en deux parties (#5392).
- Ajout d'une fonctionnalité pour bloquer l'envoi d'emails aux usagers lorsque le logement est vacant (#5310).
- Ajout d'une fonctionnalité pour notifier également les agents et un email générique pour les abandons de procédure (#5335).
- Implémentation d'un cron pour les rappels d'injonctions de signalement (#5322).

### Évolutions techniques
- Exécution du cron de synchronisation des fichiers bucket S3 via un service jobless (#5261).
- Organisation des nouveaux fichiers S3 par année/mois pour optimiser les synchronisations (#5331).
- Mise à jour des dépendances (phpunit) (#5343).
- Mise à jour de la version de lodash (#5338).
- Ajout des linter JS dans la CI (#5424).
- Suppression des dépréciations (#5422).
- Ajout d'informations sur le territoire pour l'accès à l'API (#5334).
- Mise à jour de la documentation de l'API v1.3.0 (#5190).
- Correction de la soumission multiple de formulaires (#5248).
- Amélioration de l'accessibilité pour les connexions SI externes (#5259).
- Correction de bugs liés aux réactions aux formulaires (#5313).
- Ajout de skiplinks pour passer les filtres et la liste (#5377).
- Amélioration du filtrage des signalements et injonctions (#5360).
- Limitation du sélecteur de construction dans le frontend (#5451).
- Suppression des sous-domaines dans le service secours (#5425).
- Correction d'un bug lié à la notification de visite pour un partenaire externe (#5430).
- Nettoyage de la configuration de l'API (#5401).
- Réinitialisation du formulaire dans une modale après une soumission réussie sans rechargement de la page (#5429).
- Correction de bugs sur les visites (#5435, #5434).
- Correction du mail de notification lors de la suppression d'un SA (#5452).

### Autres changements
- Ajout de données "Profil Occupant" (#5329).
- Ajout de catégories de suivis pour la gestion des interventions depuis SISH (#5333).
- Ajout d'un événement Matomo pour la démarche accélérée (#5366).
- Ajout d'une option pour la réponse du bailleur (#5269).
- Suppression des autocomplete dans les checkbox de recherche (#5406).
- Ajout de tests et corrections pour l'envoi d'événements Matomo (#5342, #5354).
- Correction de l'envoi des notifications lorsque des éléments sont supprimés (#5383, #5394).
- Ajout de la gestion des suivis arrêtés et de main-levée simultanément (#5362).
- Mise à jour de Webpack (#5407).
- Ajout de la gestion des tags triés par libellé (#4981, #5381).
- Suppression de la recherche de paramètres lors de la désactivation d'un utilisateur (#5420, #5423).
- Ajout d'une URI à la liste bloquée lors de la maintenance (#5418, #5421).
- Correction d'erreurs de redirections après actions (#5314).
- Ajout d'un formulaire multi-étape pour le service secours (#5398).
- Revue des notifications tiers déclarant pro (#5405).
- Ajout de la gestion des connexions SI externes (#5259).
