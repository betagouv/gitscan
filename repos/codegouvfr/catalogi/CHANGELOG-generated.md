## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de la gestion des sources de données externes (notamment GitHub, ROR et RNS), l'ajout de fonctionnalités de protection des logiciels et l'amélioration de l'interface utilisateur pour la configuration et la sélection des logiciels affichés sur la page d'accueil. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer l'affichage des logiciels sur la page d'accueil via l'interface utilisateur ([#523](https://github.com/codegouvfr/catalogi/issues/523)).
- Implémentation de protections pour les logiciels, avec un affichage dans une modale et un message d'administration.
- Réintégration des métadonnées de dépôt GitHub pour les références de données externes ([#547](https://github.com/codegouvfr/catalogi/issues/547)).
- Ajout de la récupération et de la recherche d'organisations sur Wikidata ([#505](https://github.com/codegouvfr/catalogi/issues/505)).
- Possibilité de bloquer la création de logiciels via l'API lorsque l'utilisation de la fonctionnalité "ajouter un logiciel ou service" est désactivée.
- Amélioration de la gestion des sources de données et mise à jour parallèle des données ([#516](https://github.com/codegouvfr/catalogi/issues/516)).

### Évolutions techniques
- Optimisation de la requête SQL pour filtrer les données au niveau de la base de données plutôt qu'en JavaScript ([#516](https://github.com/codegouvfr/catalogi/issues/516)).
- Amélioration de la stabilité des tests, notamment en rendant les assertions plus déterministes.
- Correction d'un problème d'ordre dans les tests.
- Utilisation de la configuration de la source pour résoudre l'identifiant du dépôt.
- Correction de l'ordre des migrations.

### Autres changements
- Clarification de la documentation concernant le routage de l'API Helm.
- Amélioration de l'espacement entre les éléments de la page d'accueil.
- Mises à jour de la configuration de l'en-tête SILL et de l'accessibilité.
- Correction d'un bug lié à la fermeture des requêtes de fusion GitHub.
- Plusieurs corrections et améliorations suite aux revues de code.
