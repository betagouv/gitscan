## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de l'importation et de la gestion des données, notamment via l'intégration de nouvelles sources (Wikidata, HAL) et l'optimisation des performances. Des améliorations de l'interface utilisateur ont également été apportées, avec notamment la configuration des cartes de sélection de logiciels sur la page d'accueil et l'ajout d'informations sur les protections logicielles.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer les cartes de sélection de logiciels sur la page d'accueil via l'interface utilisateur. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Affichage des protections logicielles dans une modale avec un message d'administration.
- Amélioration de la recherche et de la récupération des organisations sur Wikidata. [#505](https://github.com/codegouvfr/catalogi/issues/505)
- Ajout de la récupération de tous les identifiants sur HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Possibilité de configurer l'identifiant du dépôt à partir de la source.
- Blocage de l'API de création de logiciel lorsque l'utilisation de la fonctionnalité "ajouter un logiciel ou un service" est désactivée.
- Amélioration de l'ordre des migrations. [#523](https://github.com/codegouvfr/catalogi/issues/523)

### Évolutions techniques
- Optimisation de la requête SQL pour la mise à jour parallèle des sources. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Correction de l'ordre de tri déterministe pour les données externes des logiciels lors des tests.
- Refactorisation du code pour utiliser des objets en entrée et renommer les variables. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Amélioration de la stabilité des tests Playwright en CI.
- Mise en cache des navigateurs Playwright pour accélérer les tests.
- Clarification de la documentation concernant le routage de l'API Helm.
- Ajout d'un script pour initialiser la base de données racine.

### Autres changements
- Correction d'un bug empêchant la fermeture des requêtes de fusion GitHub.
- Ajout de l'affichage des métadonnées du dépôt sur GitHub pour les références de données externes. [#547](https://github.com/codegouvfr/catalogi/issues/547)
- Amélioration de l'espacement entre le héros de la page d'accueil et la sélection des logiciels.
- Correction du nom du logiciel pour qu'il puisse revenir aux sources si nécessaire.
- Corrections diverses et améliorations suite aux revues de code.
- Mises à jour des dépendances Renovate.
