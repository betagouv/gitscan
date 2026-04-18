## Changelog : zero-logement-vacant (30 derniers jours, au 2026-04-14)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des campagnes, des propriétaires et des logements, ainsi que sur des corrections de bugs et des optimisations techniques. L'ajout de nouvelles fonctionnalités, comme l'export des destinataires de campagne et l'amélioration des filtres, vise à faciliter le travail des agents de l'administration. Des efforts importants ont également été réalisés pour renforcer la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter la liste des destinataires d'une campagne. [#1710](https://github.com/MTES-MCT/zero-logement-vacant/pull/1710)
- Amélioration de l'affichage des informations sur les propriétaires (rang, droits de propriété). [#1726](https://github.com/MTES-MCT/zero-logement-vacant/pull/1726)
- Ajout d'une notification lors de la création d'une campagne ou de la suppression d'un groupe. [#1751](https://github.com/MTES-MCT/zero-logement-vacant/pull/1751)
- Correction de l'affichage des noms de filtres de périmètre. [#1757](https://github.com/MTES-MCT/zero-logement-vacant/pull/1757)
- Correction du libellé de l'onglet "Évolutions". [#1758](https://github.com/MTES-MCT/zero-logement-vacant/pull/1758)
- Ajout d'un avertissement concernant les données sensibles lors du téléchargement de documents et de la saisie de notes. [#1703](https://github.com/MTES-MCT/zero-logement-vacant/pull/1703)
- Correction de l'affichage des pourcentages avec une décimale. [#1751](https://github.com/MTES-MCT/zero-logement-vacant/pull/1751)

### Évolutions techniques
- Refactorisation importante du code lié à la gestion des périmètres et des droits d'accès, notamment pour l'intégration avec Portail DF. [#1649](https://github.com/MTES-MCT/zero-logement-vacant/pull/1649)
- Mise en place de triggers pour précalculer le nombre de logements et de propriétaires par groupe, améliorant ainsi les performances. [#1750](https://github.com/MTES-MCT/zero-logement-vacant/pull/1750)
- Amélioration de la gestion des erreurs et de la robustesse du code.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité. [#1764](https://github.com/MTES-MCT/zero-logement-vacant/pull/1764)
- Amélioration de la couverture des tests unitaires et d'intégration.
- Utilisation de `p-memoize` pour optimiser les appels à l'API Geo.
- Refactorisation de la gestion des utilisateurs et des établissements.
- Migration vers une architecture plus modulaire avec l'introduction de "factories" pour la création d'objets de test et de données. [#1767](https://github.com/MTES-MCT/zero-logement-vacant/pull/1767)
- Amélioration de la configuration et de l'environnement de développement avec l'intégration de Worktrunk. [#1748](https://github.com/MTES-MCT/zero-logement-vacant/pull/1748)

### Autres changements
- Documentation de l'implémentation des "factories". [#1771](https://github.com/MTES-MCT/zero-logement-vacant/pull/1771)
- Ajout d'un plan pour l'exploration de l'EETL et l'implémentation d'un pipeline de propriétaires. [#1771](https://github.com/MTES-MCT/zero-logement-vacant/pull/1771)
- Suppression de code mort et de configurations inutilisées.
- Correction de problèmes de SonarCloud.
- Amélioration de la configuration des pipelines CI/CD.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de nouvelles variables d'environnement pour la configuration.
- Correction de problèmes liés à l'affichage des images.
- Correction de problèmes liés à la gestion des droits d'accès.
- Correction de problèmes liés à l'exportation des données.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à la synchronisation des données avec Cerema.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des logs.
- Correction de problèmes liés à la navigation.
- Amélioration de l'accessibilité de l'application.
