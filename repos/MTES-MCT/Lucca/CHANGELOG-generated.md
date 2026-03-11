## Changelog : Lucca (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à la gestion des départements, notamment l'importation de données et la validation. L'interface utilisateur a été enrichie avec l'ajout de fonctionnalités de gestion des adhérents et des utilisateurs, incluant des tableaux de données paginés et des options de clonage. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la gestion des adhérents avec intégration de DataTable : ajout, modification, listage paginé et accès aux départements associés [#22bc77e](https://github.com/MTES-MCT/Lucca/commit/22bc77e).
- Possibilité de cloner un adhérent vers un autre département [#cd1e966](https://github.com/MTES-MCT/Lucca/commit/cd1e966).
- Amélioration du formulaire de département : ajout d'une option d'importation automatique et validation conditionnelle des champs code et fichier des communes [#211b2b1](https://github.com/MTES-MCT/Lucca/commit/211b2b1).
- Ajout d'un panneau "Adhérents" dans la page de détails d'un utilisateur [#14ee7d3](https://github.com/MTES-MCT/Lucca/commit/14ee7d3).
- Implémentation d'un tableau de données paginé pour la gestion des utilisateurs, incluant une colonne pour les départements [#ca3e6c8](https://github.com/MTES-MCT/Lucca/commit/ca3e6c8).
- Amélioration de la gestion des logos : changement du type de paramètre pour utiliser un média, mise à jour des filtres Twig et amélioration de la génération de l'URL du média [#5b5046e](https://github.com/MTES-MCT/Lucca/commit/5b5046e).
- Ajout de la possibilité d'activer un bloc d'activation des administrateurs dans le template index des adhérents [#6878311](https://github.com/MTES-MCT/Lucca/commit/6878311).
- Amélioration de la gestion des paramètres du site web avec l'ajout d'un pied de page configurable [#b47d807](https://github.com/MTES-MCT/Lucca/commit/b47d807).

### Évolutions techniques
- Refactorisation du `AdherentController` et du `DataTableTrait` pour une meilleure gestion des données et une sélection d'entités distincte [#d06052e](https://github.com/MTES-MCT/Lucca/commit/d06052e).
- Simplification de la méthode `indexAction` dans `AdherentController` en supprimant la récupération de données inutiles [#e913311](https://github.com/MTES-MCT/Lucca/commit/e913311).
- Mise à jour des préfixes de routage pour utiliser `/api` pour les API [#2749967](https://github.com/MTES-MCT/Lucca/commit/2749967).
- Amélioration de la gestion des services GeoApiService pour importer les services de l'État et mettre à jour la logique de mappage des tribunaux [#dc3f30a](https://github.com/MTES-MCT/Lucca/commit/dc3f30a).
- Mise à jour du modèle Department pour autoriser le nom nullable et améliorer la logique d'importation des données [#d225bbe](https://github.com/MTES-MCT/Lucca/commit/d225bbe).
- Suppression de code de débogage et nettoyage du code dans `ChecklistController`, `TagService` et `UserController` [#62ce766](https://github.com/MTES-MCT/Lucca/commit/62ce766).
- Correction d'un bug dans l'édition des procès-verbaux [#b001310](https://github.com/MTES-MCT/Lucca/commit/b001310).
- Refactorisation des dépôts `Control` et `Minute` pour supprimer le champ de dossier inutile des requêtes [#ba175f7](https://github.com/MTES-MCT/Lucca/commit/ba175f7).

### Autres changements
- Mise à jour de la documentation README pour améliorer la clarté et l'organisation des instructions d'installation [#4068408](https://github.com/MTES-MCT/Lucca/commit/4068408).
- Mise à jour de la version de l'application à v4.4.0, v4.4.1 et v4.4.2 [#b9cbb86](https://github.com/MTES-MCT/Lucca/commit/b9cbb86), [#dc02495](https://github.com/MTES-MCT/Lucca/commit/dc02495), [#6ec1463](https://github.com/MTES-MCT/Lucca/commit/6ec1463).
- Ajout d'un contrôle de configuration de l'API Aigle et affichage d'un message flash si elle n'est pas configurée [#e61fcfb](https://github.com/MTES-MCT/Lucca/commit/e61fcfb).
- Mise à jour de la valeur par défaut de `showInHomePage` pour le département et ajustement de l'exigence du champ communes [#85b7326](https://github.com/MTES-MCT/Lucca/commit/85b7326).
- Mise à jour du type de paramètre du logo et de la valeur dans DataGenerator, amélioration de LogoFinder pour récupérer les médias [#b07b41b](https://github.com/MTES-MCT/Lucca/commit/b07b41b).
- Implémentation d'une méthode clone pour réinitialiser les propriétés et éviter les problèmes de clonage [#6360790](https://github.com/MTES-MCT/Lucca/commit/6360790).
- Validation du format de l'adresse e-mail de l'expéditeur et du nom avant l'envoi [#654c909](https://github.com/MTES-MCT/Lucca/commit/654c909).
- Correction de la gestion des images de logo sur la page d'accueil [#ee2b7f7](https://github.com/MTES-MCT/Lucca/commit/ee2b7f7).
- Ajout de ProposalService et intégration de la création de proposition dans l'initialisation du département et ajout d'un lien vers les tags natinfs [#a86b144](https://github.com/MTES-MCT/Lucca/commit/a86b144).
- Suppression d'un asset inutile [#f55d202](https://github.com/MTES-MCT/Lucca/commit/f55d202).
