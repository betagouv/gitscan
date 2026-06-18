## Changelog : espace-membre-next (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des informations sur les startups et les phases de leurs projets, ainsi que sur l'ajout de fonctionnalités liées aux comptes Matrix. Des corrections ont également été apportées pour aligner les libellés et améliorer la détection de l'utilisation de Tchap. Enfin, des éléments liés au parrainage ont été supprimés.

### Évolutions fonctionnelles
- Modification du formulaire pour la saisie des jours travaillés par semaine pour les membres. [#1395](https://github.com/betagouv/espace-membre-next/issues/1395)
- Amélioration de la sélection des noms d'événements pour les startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- Alignement des libellés des phases de projet avec ceux utilisés sur beta.gouv.fr pour une meilleure cohérence. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384)
- Amélioration de la détection de l'utilisation de Tchap, avec une optimisation pour éviter des vérifications inutiles. [#1393](https://github.com/betagouv/espace-membre-next/issues/1393)

### Évolutions techniques
- Ajout d'une table `matrix_accounts` et d'un script de synchronisation pour gérer les comptes Matrix. [#1373](https://github.com/betagouv/espace-membre-next/issues/1373)
- Renommage de la phase "perennisation" en "consolidation" pour plus de clarté. [#1392](https://github.com/betagouv/espace-membre-next/issues/1392)

### Autres changements
- Suppression de toutes les fonctionnalités liées au parrainage. [#1404](https://github.com/betagouv/espace-membre-next/issues/1404)
