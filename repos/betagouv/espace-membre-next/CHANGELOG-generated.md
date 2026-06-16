## Changelog : espace-membre-next (30 derniers jours, au 15 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'espace membre au cours du dernier mois. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur pour la gestion des startups et des phases, ainsi que l'ajout de fonctionnalités liées à la synchronisation des comptes Matrix. Une fonctionnalité de parrainage a été supprimée.

### Évolutions fonctionnelles
- Modification du formulaire pour la saisie des jours travaillés par semaine pour les membres. [#1395](https://github.com/betagouv/espace-membre-next/issues/1395)
- Correction de l'affichage des noms d'événements pour les startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- Alignement des libellés des phases avec ceux utilisés sur beta.gouv.fr pour une meilleure cohérence. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384)
- Amélioration de la détection de l'utilisation de Tchap, avec une optimisation pour éviter des vérifications inutiles. [#1393](https://github.com/betagouv/espace-membre-next/issues/1393)

### Évolutions techniques
- Ajout d'une table `matrix_accounts` et d'un script de synchronisation pour les comptes Matrix. [#1373](https://github.com/betagouv/espace-membre-next/issues/1373)
- Renommage de la phase "perennisation" en "consolidation" pour plus de clarté. [#1392](https://github.com/betagouv/espace-membre-next/issues/1392)
- Mise à jour des contraintes de nom des phases dans la base de données. [#1356](https://github.com/betagouv/espace-membre-next/issues/1356)
- Nettoyage de la configuration de l'environnement. [#1383](https://github.com/betagouv/espace-membre-next/issues/1383)

### Autres changements
- Suppression de toutes les fonctionnalités liées au parrainage. [#1404](https://github.com/betagouv/espace-membre-next/issues/1404)
