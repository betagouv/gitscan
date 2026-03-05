## Changelog : Lucca (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à la gestion des départements, des utilisateurs et des adhérents, notamment en termes d'import de données, de validation et d'interface utilisateur. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application. L'application a été mise à jour vers la version 4.4.0.

### Évolutions fonctionnelles
- Ajout de la possibilité de cloner un adhérent vers un autre département. [#cd1e966](https://github.com/MTES-MCT/Lucca/commit/cd1e966)
- Amélioration de la gestion des logos : type de paramètre modifié pour accepter des médias, filtres Twig mis à jour pour la récupération des logos. [#5b5046e](https://github.com/MTES-MCT/Lucca/commit/5b5046e)
- Ajout d'un bloc d'activation du menu administrateur dans le template des adhérents. [#6878311](https://github.com/MTES-MCT/Lucca/commit/6878311)
- Ajout d'un panneau "Adhérents" dans la page de détails de l'utilisateur. [#14ee7d3](https://github.com/MTES-MCT/Lucca/commit/14ee7d3)
- Implémentation d'une table de données avec chargement paresseux pour la gestion des utilisateurs, avec une colonne "Départements". [#ca3e6c8](https://github.com/MTES-MCT/Lucca/commit/ca3e6c8)
- Amélioration de la gestion des paramètres du site web avec l'ajout de paramètres pour le pied de page. [#b47d807](https://github.com/MTES-MCT/Lucca/commit/b47d807)
- Ajout de la possibilité d'importer automatiquement les départements. [#2dbddd9](https://github.com/MTES-MCT/Lucca/commit/2dbddd9)
- Amélioration du formulaire de création/modification de département avec validation conditionnelle pour le code et le fichier des communes. [#211b2b1](https://github.com/MTES-MCT/Lucca/commit/211b2b1)
- Ajout de la possibilité de vérifier la disponibilité de l'API avant l'import des départements. [#8116d0a](https://github.com/MTES-MCT/Lucca/commit/8116d0a)
- Amélioration de la gestion des images de logo sur la page d'accueil. [#ee2b7f7](https://github.com/MTES-MCT/Lucca/commit/ee2b7f7)

### Évolutions techniques
- Refactorisation du `AdherentController` et du `DataTableTrait` pour une meilleure gestion des données et une sélection d'entités distinctes. [#d06052e](https://github.com/MTES-MCT/Lucca/commit/d06052e)
- Simplification de la méthode `indexAction` dans `AdherentController` en supprimant la récupération de données inutiles. [#e913311](https://github.com/MTES-MCT/Lucca/commit/e913311)
- Mise à jour des préfixes de routage pour utiliser `/api` pour les routes API. [#2749967](https://github.com/MTES-MCT/Lucca/commit/2749967)
- Correction de la relation entre les entités `Control`, `Minute`, `Folder` et ajout de suppression en cascade pour éviter les erreurs de clé étrangère. [#f7bf245](https://github.com/MTES-MCT/Lucca/commit/f7bf245)
- Implémentation d'une méthode `clone` pour éviter les problèmes de clonage. [#6360790](https://github.com/MTES-MCT/Lucca/commit/6360790)
- Mise à jour de la version de l'application à v4.4.0. [#b9cbb86](https://github.com/MTES-MCT/Lucca/commit/b9cbb86)
- Mise à jour de la version de l'application à v4.3.9. [#60f3d8b](https://github.com/MTES-MCT/Lucca/commit/60f3d8b)
- Mise à jour de la version de l'application à v4.3.8. [#8b84707](https://github.com/MTES-MCT/Lucca/commit/8b84707)

### Autres changements
- Mise à jour de la documentation README pour améliorer la clarté et l'organisation des instructions d'installation. [#4068408](https://github.com/MTES-MCT/Lucca/commit/4068408)
- Suppression des instructions de débogage et nettoyage du code dans `ChecklistController`, `TagService` et `UserController`. [#62ce766](https://github.com/MTES-MCT/Lucca/commit/62ce766)
- Mise à jour de la valeur par défaut de `showInHomePage` pour le département et ajustement de l'exigence du champ `towns`. [#85b7326](https://github.com/MTES-MCT/Lucca/commit/85b7326)
- Mise à jour du type et de la valeur du paramètre de logo et amélioration de `LogoFinder` pour récupérer les médias. [#b07b41b](https://github.com/MTES-MCT/Lucca/commit/b07b41b)
- Ajout de services de proposition et intégration de la création de proposition lors de l'initialisation du département et ajout d'un lien de balise vers natinfs. [#a86b144](https://github.com/MTES-MCT/Lucca/commit/a86b144)
- Ajout du champ `parcelClean` à l'entité `Plot` pour le projet de script lucca. [#4e41ef5](https://github.com/MTES-MCT/Lucca/commit/4e41ef5)
- Validation du format de l'adresse e-mail et du nom de l'expéditeur avant l'envoi. [#654c909](https://github.com/MTES-MCT/Lucca/commit/654c909)
- Suppression d'un asset inutile. [#f55d202](https://github.com/MTES-MCT/Lucca/commit/f55d202)
- Correction de la source de l'image du logo. [#43d1dd3](https://github.com/MTES-MCT/Lucca/commit/43d1dd3)
- Correction de l'édition de procès-verbal. [#b001310](https://github.com/MTES-MCT/Lucca/commit/b001310)
