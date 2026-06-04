## Changelog : jeveuxaider-back (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la fiabilité de la plateforme, notamment au niveau de la synchronisation des données avec Airtable et des requêtes statistiques. Des améliorations ont également été apportées à la gestion des missions et des organisations, ainsi qu'à la gestion des notifications et des abonnements.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des missions depuis Airtable : prise en compte des missions supprimées et ajout d'une commande pour synchroniser une seule mission supprimée [#192].
- Filtrage des organisations par ID lors de la synchronisation Airtable [#191].
- Ajout d'un bandeau d'email destinataire dans les notifications [#189].
- Les structures peuvent maintenant se désinscrire de manière autonome des notifications [#172].
- Possibilité de filtrer les notes pour exclure les entrées de l'utilisateur actuel [#180].
- Application du filtre "adultes uniquement" de manière cohérente sur le marketplace [#199].

### Évolutions techniques
- Optimisation des requêtes statistiques : ajout d'index, refactoring des jointures et des conditions pour améliorer la performance et la lisibilité [#181, #182, #184, #186].
- Refactoring de la gestion de l'état de participation et suppression du code obsolète `actingAs` [#191].
- Utilisation de l'opérateur `ilike` pour des recherches moins strictes [#106].
- Amélioration de la logique de synchronisation des missions pour exclure les missions non pertinentes en fonction de leur état et de leurs notes [#190].
- Refactoring du code pour la gestion des rôles (rolables.fonction) [#194].
- Suppression d'un filtre de département inutilisé dans les invitations [#183].

### Autres changements
- Ajout de paramètres `autovacuum` et d'index pour la table `activity_log` afin d'améliorer les performances [#188].
- Mise à jour de plusieurs dépendances Symfony (routing, http-kernel, mailer, mime) [#198, #197, #196, #195].
- Mise à jour de la librairie phpseclib [#183].
