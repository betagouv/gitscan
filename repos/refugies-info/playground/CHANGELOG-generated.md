## Changelog : playground (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des documents, notamment en ajoutant des fonctionnalités de filtrage, de tri et de journalisation des activités. Des améliorations ont également été apportées à l'interface utilisateur pour faciliter la traduction et l'archivage des fiches, ainsi qu'à la gestion des logs et des agents Lletta.

### Évolutions fonctionnelles
- Ajout d'un filtre sur la barre de recherche pour spécifier le champ à interroger. [#300](https://github.com/refugies-info/playground/issues/300)
- Possibilité de trier la liste des fichiers importés par date d'importation. [#299](https://github.com/refugies-info/playground/issues/299)
- Affichage des dates de publication et d'archivage sur les fiches. [#296](https://github.com/refugies-info/playground/issues/296)
- Intégration d'un système de notes pour les fiches. [#292](https://github.com/refugies-info/playground/issues/292)
- Possibilité de mettre à jour le statut de travail directement depuis l'en-tête de la fiche et la liste. [#293](https://github.com/refugies-info/playground/issues/293)
- Amélioration de l'interface utilisateur pour la page de traduction et la liste des traductions. [#282](https://github.com/refugies-info/playground/issues/282), [#283](https://github.com/refugies-info/playground/issues/283)
- Ajout d'un message d'avertissement pour indiquer à l'utilisateur qu'une autre personne est en train d'éditer la fiche. [#256](https://github.com/refugies-info/playground/issues/256)
- Ajout d'un filtre pour spécifier le champ à rechercher. [#291](https://github.com/refugies-info/playground/issues/291)
- Possibilité de trier par numéro de version sur la liste des documents. [#278](https://github.com/refugies-info/playground/issues/278)
- Affichage des versions d'ingestion sous forme de fractions. [#277](https://github.com/refugies-info/playground/issues/277)

### Évolutions techniques
- Enregistrement des tokens consommés pour chaque opération avec Lletta. [#295](https://github.com/refugies-info/playground/issues/295)
- Ajout de logs pour l'ensemble des opérations, incluant l'archivage, la modification du statut et les actions sur les documents. [#297](https://github.com/refugies-info/playground/issues/297)
- Amélioration de la gestion des états de traitement. [#294](https://github.com/refugies-info/playground/issues/294)
- Mise en place d'un environnement local de développement pour éviter la consommation de ressources de production. [#275](https://github.com/refugies-info/playground/issues/275)
- Correction d'un problème de création d'agent sur Lletta. [#298](https://github.com/refugies-info/playground/issues/298)
- Refactoring du code pour améliorer la cohérence et la maintenabilité.
- Mise à jour des dépendances et correction de bugs mineurs.

### Autres changements
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Nettoyage du code et suppression de fichiers inutiles.
- Amélioration des tests unitaires.
- Correction de problèmes de typage et de gestion des erreurs.
- Centralisation des données utilisateurs dans le Bomo. [#289](https://github.com/refugies-info/playground/issues/289)
- Suppression de l'action d'archivage sur la page de traduction.
- Amélioration de la gestion des permissions pour les traductions.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de bugs et amélioration de la stabilité de l'application.
