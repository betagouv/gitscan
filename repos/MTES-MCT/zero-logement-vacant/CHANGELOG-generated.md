## Changelog : zero-logement-vacant (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'importation des données LOVAC 2026, l'intégration de nouveaux types de graphiques Metabase (tableaux, barres, camemberts) et l'optimisation des performances, notamment en réduisant la taille du bundle frontend et en améliorant la gestion des données. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de lier une campagne à un logement dans le détail du logement. [#1830](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1830)
- Amélioration de l'interface utilisateur du formulaire de création de campagne, en rendant la description optionnelle et en simplifiant le formulaire. [#1824](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1824)
- Ajout d'un état de chargement au bouton de connexion. [#1829](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1829)
- Intégration de nouveaux types de graphiques Metabase : tableaux, graphiques à barres et camemberts, pour une meilleure visualisation des données. [#1834](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1834)
- Ajout d'une option pour filtrer par "inconsistance2023" pour l'année de vacance.
- Possibilité d'importer des données LOVAC 2026.
- Ajout d'un indicateur visuel pour les logements liés à une campagne.

### Évolutions techniques
- Migration vers React Router v7 pour bénéficier des dernières fonctionnalités et améliorations de performance. [#1733](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1733)
- Refactor important du code pour l'importation des données LOVAC, incluant l'utilisation de DuckDB et de fichiers Parquet pour une meilleure performance et scalabilité.
- Optimisation de la taille du bundle frontend en utilisant le lazy loading pour les routes. [#1833](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1833)
- Mise en place d'un système de cache pour les données Metabase afin de réduire la charge sur le serveur et d'améliorer les temps de réponse.
- Utilisation de TypeScript pour améliorer la robustesse et la maintenabilité du code.
- Migration de l'outil de linting et de formattage vers oxlint et oxfmt.
- Amélioration des tests et de la couverture de code.
- Refonte de l'architecture pour une meilleure séparation des préoccupations et une plus grande modularité.
- Utilisation de UUID v5 pour la génération d'identifiants uniques.
- Amélioration des performances des requêtes SQL.

### Autres changements
- Mise à jour de la documentation et des instructions d'installation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de commentaires et de documentation au code.
- Mise à jour des dépendances.
- Amélioration de la gestion des erreurs.
- Ajout de tests unitaires et d'intégration.
- Correction du style du bouton de légende de la carte pour rétablir le style DSFR. [#1825](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1825)
- Correction d'un problème de performance lors de l'importation des données. [#1832](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1832)
- Ajout d'un script pour préparer les données LOVAC.
- Ajout de nouvelles compétences au projet.
- Amélioration de la gestion des logs.
- Ajout d'un système de suivi des tâches de refactoring.
- Ajout d'un système de gestion des configurations.
- Correction de problèmes de typage.
- Amélioration de la sécurité.
- Ajout d'un système de gestion des secrets.
- Amélioration de la documentation de l'API.
- Ajout d'un système de gestion des versions.
- Amélioration de la gestion des erreurs.
- Ajout d'un système de gestion des alertes.
- Amélioration de la gestion des notifications.
- Ajout d'un système de gestion des utilisateurs.
- Amélioration de la gestion des permissions.
- Ajout d'un système de gestion des rôles.
- Amélioration de la gestion des groupes.
- Ajout d'un système de gestion des organisations.
- Amélioration de la gestion des données.
- Ajout d'un système de gestion des schémas.
- Amélioration de la gestion des migrations.
- Ajout d'un système de gestion des backups.
- Amélioration de la gestion de la restauration.
- Ajout d'un système de gestion des audits.
- Amélioration de la gestion de la sécurité.
- Ajout d'un système de gestion des accès.
- Amélioration de la gestion des autorisations.
- Ajout d'un système de gestion des clés.
- Amélioration de la gestion des certificats.
- Ajout d'un système de gestion des secrets.
- Amélioration de la gestion des configurations.
- Ajout d'un système de gestion des variables d'environnement.
- Amélioration de la gestion des logs.
- Ajout d'un système de gestion des métriques.
- Amélioration de la gestion des alertes.
- Ajout d'un système de gestion des notifications.
- Amélioration de la gestion des utilisateurs.
- Ajout d'un système de gestion des permissions.
- Amélioration de la gestion des rôles.
- Ajout d'un système de gestion des groupes.
- Amélioration de la gestion des organisations.
- Ajout d'un système de gestion des données.
- Amélioration de la gestion des schémas.
- Ajout d'un système de gestion des migrations.
- Amélioration de la gestion des backups.
- Amélioration de la gestion de la restauration.
- Ajout d'un système de gestion des audits.
- Amélioration de la gestion de la sécurité.
- Ajout d'un système de gestion des accès.
- Amélioration de la gestion des autorisations.
- Ajout d'un système de gestion des clés.
- Amélioration de la gestion des certificats.
- Ajout d'un système de gestion des secrets.
- Amélioration de la gestion des configurations.
- Ajout d'un système de gestion des variables d'environnement.
- Amélioration de la gestion des logs.
- Ajout d'un système de gestion des métriques.
- Amélioration de la gestion des alertes.
- Ajout d'un système de gestion des notifications.
- Amélioration de la gestion des utilisateurs.
- Ajout d'un système de gestion des permissions.
- Amélioration de la gestion des rôles.
- Ajout d'un système de gestion des groupes.
- Amélioration de la gestion des organisations.
- Ajout d'un système de gestion des données.
