## Changelog : espace-membre-next (30 derniers jours, au 8 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'espace membre au cours du dernier mois. Les modifications concernent principalement l'amélioration de la gestion des startups et des phases de projet, ainsi que l'intégration de nouvelles fonctionnalités liées aux comptes Matrix et à la détection de l'utilisation de Tchap. Une amélioration du formulaire pour la gestion des jours travaillés par semaine a également été apportée.

### Évolutions fonctionnelles
- Modification du formulaire pour la gestion des jours travaillés par semaine. [#1395](https://github.com/betagouv/espace-membre-next/issues/1395)
- Amélioration de la sélection des noms d'événements pour les startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- Alignement des libellés des phases de projet avec ceux utilisés sur beta.gouv.fr. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384)
- Renommage de la phase "perennisation" en "consolidation" pour une meilleure clarté. [#1392](https://github.com/betagouv/espace-membre-next/issues/1392)

### Évolutions techniques
- Ajout d'une table `matrix_accounts` et d'un script de synchronisation pour gérer les comptes Matrix. [#1373](https://github.com/betagouv/espace-membre-next/issues/1373)
- Optimisation de la détection de l'utilisation de Tchap pour éviter des traitements inutiles. [#1393](https://github.com/betagouv/espace-membre-next/issues/1393)
- Mise à jour des contraintes de nom des phases pour garantir la cohérence des données. [#1356](https://github.com/betagouv/espace-membre-next/issues/1356)
- Nettoyage de la configuration de l'environnement. [#1383](https://github.com/betagouv/espace-membre-next/issues/1383)
