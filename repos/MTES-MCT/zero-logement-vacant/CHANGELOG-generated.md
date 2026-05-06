## Changelog : zero-logement-vacant (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance, la suppression de code obsolète et la préparation du projet pour de futures évolutions. Des corrections ont été apportées pour améliorer la gestion des statuts de logement et l'affichage des informations, notamment concernant les périmètres. L'infrastructure et les outils de développement ont également été mis à jour.

### Évolutions fonctionnelles
- Correction de l'affichage du nom du périmètre dans l'interface utilisateur.
- Amélioration de l'affichage des pourcentages et des taux de retour dans les tableaux de bord.
- Correction d'un bug empêchant l'affichage correct des images téléchargées.
- Ajout de notifications lors de la création de campagnes et de la suppression de groupes.
- Amélioration de la gestion des statuts de logement, notamment pour les logements "jamais contactés".
- Correction de l'alignement des boutons d'action dans la barre d'actions de groupe.
- Ajout d'un lien vers la CNIL sur les avertissements concernant les données sensibles.
- Possibilité de naviguer vers la liste des logements filtrée par campagne.

### Évolutions techniques
- Optimisation significative du temps de calcul du nombre de logements, réduisant le temps d'exécution de 4 à 36% selon les filtres.
- Refactorisation importante du code, avec suppression de code mort, de tables de bases de données inutilisées et de fonctionnalités obsolètes (ancien flux de campagne).
- Migration de l'OpenAPI spec vers un format YAML et remplacement de Swagger UI par Scalar.
- Remplacement de `convict` par `Zod` pour la gestion de la configuration du serveur.
- Mise à jour des dépendances, notamment `axios` et les plugins Vite.
- Amélioration de la couverture des tests, en particulier pour les modèles de données.
- Mise en place d'un système de triggers pour précalculer les nombres de logements et de propriétaires par groupe, améliorant ainsi les performances.
- Utilisation de `worktrunk` pour la gestion des branches et des environnements de développement.
- Amélioration de la gestion des droits d'accès et de l'authentification, notamment avec l'intégration du Portail DF.
- Passage à Node.js v24 pour les tests frontend.

### Autres changements
- Documentation technique mise à jour et complétée, incluant des diagrammes et des schémas.
- Ajout de badges Codecov et amélioration de la configuration du CI/CD.
- Ajout de documentation pour les nouvelles fonctionnalités et les changements d'architecture.
- Correction de problèmes de compatibilité avec certains environnements de CI.
- Amélioration de la configuration et des scripts de déploiement.
- Ajout de documentation pour l'utilisation de `worktrunk`.
- Ajout de plans et de spécifications pour les futures évolutions du projet.
- Suppression de certaines variables d'environnement sensibles et remplacement par la configuration CleverCloud.
