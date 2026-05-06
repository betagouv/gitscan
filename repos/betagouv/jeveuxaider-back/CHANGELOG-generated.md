## Changelog : jeveuxaider-back (30 derniers jours, au 5 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au backend de la plateforme "Je veux aider" au cours du dernier mois. Les évolutions se concentrent sur l'optimisation des performances, l'amélioration de l'expérience utilisateur pour la gestion des missions et des logs d'activité, ainsi que des corrections de bugs pour assurer la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un filtre pour exclure les propres entrées de l'utilisateur dans les notes des missions. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Implémentation d'une pagination simple pour les logs d'activité, améliorant la navigation et la performance. [#176](https://github.com/betagouv/jeveuxaider-back/issues/176)
- Ajout d'une commande pour fermer les missions pour mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/issues/174)
- Correction d'un bug empêchant l'ouverture de missions dupliquées pour mineurs basées sur les paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/issues/173)
- Amélioration du message de bienvenue dans la notification "Association à une structure validée". [#171](https://github.com/betagouv/jeveuxaider-back/issues/171)
- Gestion des erreurs améliorée lors de l'acceptation d'une invitation. [#170](https://github.com/betagouv/jeveuxaider-back/issues/170)
- Correction de la gestion de la suppression de missions et de structures en état "Brouillon" depuis Airtable.

### Évolutions techniques
- Ajout d'index partiels aux tables `activity_log` et `participations` pour optimiser les performances des requêtes. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175)
- Refactorisation : Suppression des missions passées de la tâche `ApiEngagementExportMissionsJob`. [#169](https://github.com/betagouv/jeveuxaider-back/issues/169)
- Refactorisation : Suppression de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`. [#166](https://github.com/betagouv/jeveuxaider-back/issues/166)
- Implémentation d'une base de données réplica pour améliorer la performance et la disponibilité. [#164](https://github.com/betagouv/jeveuxaider-back/issues/164)
- Correction : Ajout des noms d'activité manquants dans le mapping des activités de mission. [#168](https://github.com/betagouv/jeveuxaider-back/issues/168)

### Autres changements
- Évolutions liées à France Travail. [#166](https://github.com/betagouv/jeveuxaider-back/issues/166)
- Mise à jour de la librairie `laravel/passport` vers la version 13.7.1. [#167](https://github.com/betagouv/jeveuxaider-back/issues/167)
- Mise à jour de la librairie `phpoffice/phpspreadsheet` vers la version 1.30.4. [#177](https://github.com/betagouv/jeveuxaider-back/issues/177)
- Mise à jour de la librairie `phpseclib/phpseclib` vers la version 3.0.51. [#169](https://github.com/betagouv/jeveuxaider-back/issues/169)
