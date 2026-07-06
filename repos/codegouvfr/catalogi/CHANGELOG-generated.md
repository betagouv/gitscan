## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des organisations (ROR, RNSR, Wikidata) et des données externes, notamment pour l'intégration avec GitHub. L'interface utilisateur a également été améliorée avec l'ajout de protections logicielles et la configuration des cartes de sélection des logiciels sur la page d'accueil. Des corrections et optimisations ont été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de récupérer et de rechercher des organisations sur Wikidata. [#505](https://github.com/codegouvfr/catalogi/issues/505)
- Réintégration des métadonnées de dépôt sur les références de données externes GitHub. [#547](https://github.com/codegouvfr/catalogi/issues/547)
- Affichage des protections logicielles dans une modale avec un message d'administration.
- Configuration des cartes de sélection des logiciels sur la page d'accueil via l'interface utilisateur.
- Blocage de l'API de création de logiciel lorsque l'utilisation de la fonctionnalité "ajouter un logiciel ou service" est désactivée.
- Amélioration de l'ordre des tests pour les données externes de logiciels.
- Ajout de la récupération d'organisation pour ROR et RNSR. [#523](https://github.com/codegouvfr/catalogi/issues/523)

### Évolutions techniques
- Refactorisation du filtre SQL pour améliorer la performance de la recherche. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Mise à jour de l'ordre des migrations. [#523](https://github.com/codegouvfr/catalogi/issues/523)
- Optimisation de la mise à jour des données par source et en parallèle. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Correction d'un problème d'ordre non déterministe dans les tests.
- Amélioration de l'espacement entre le héros de la page d'accueil et la sélection des logiciels.

### Autres changements
- Ajout d'un test et correction de la fermeture des pull requests GitHub.
- Corrections diverses et améliorations suite aux revues de code.
- Mises à jour des dépendances via Renovate.
- Augmentation du numéro de version.
