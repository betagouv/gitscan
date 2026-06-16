## Changelog : sill-deploy (30 derniers jours, au 12 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à sill-deploy au cours du dernier mois. Les principales évolutions concernent l'ajout de fonctionnalités pour la gestion des organisations et des sources de données, des améliorations de l'interface utilisateur pour la sélection des logiciels, et des corrections de bugs pour stabiliser les tests et l'importation automatique. Des workflows de déploiement SILL ont également été ajoutés.

### Évolutions fonctionnelles
- Ajout de la récupération et de la recherche d'organisations sur Wikidata. [#505](https://github.com/codegouvfr/sill-deploy/issues/505)
- Ajout de la possibilité de récupérer l'organisation pour ROR et RNS. [#523](https://github.com/codegouvfr/sill-deploy/issues/523)
- Ajout de la possibilité de configurer les cartes de sélection de logiciels sur la page d'accueil via l'interface utilisateur.
- Ajout de protections pour les logiciels.
- Amélioration de l'importation automatique des données, empêchant la création d'entrées utilisateur. [#528](https://github.com/codegouvfr/sill-deploy/issues/528)
- Ajout de la récupération de tous les identifiants sur HAL. [#515](https://github.com/codegouvfr/sill-deploy/issues/515)
- Ajout d'un rôle administrateur et d'une page d'administration pour gérer les attributs personnalisés.
- Restriction des attributs personnalisés à l'administration uniquement.
- Contrainte de la largeur de la page et troncature des étiquettes d'attributs longs dans l'interface d'administration.

### Évolutions techniques
- Ajout de workflows de déploiement SILL et synchronisation avec l'upstream.
- Refactoring pour effectuer le filtrage au niveau SQL plutôt qu'au niveau des résultats. [#516](https://github.com/codegouvfr/sill-deploy/issues/516)
- Utilisation de la configuration de la source pour résoudre l'identifiant du dépôt.
- Correction de l'ordre des tests pour assurer une exécution déterministe.
- Amélioration de la stabilité des assertions pour les logiciels similaires.
- Correction de l'installation des navigateurs Playwright en CI.
- Correction de l'exécution des tests Playwright en CI.
- Mise à jour des dépendances Renovate.

### Autres changements
- Clarification de la documentation concernant le routage de l'API Helm.
- Ajout d'un script pour initialiser la base de données racine.
- Correction du réordonnancement des références de migration. [#523](https://github.com/codegouvfr/sill-deploy/issues/523)
- Correction de l'espacement entre le héros de la page d'accueil et la sélection des logiciels.
- Modification de l'entrée d'objet et renommage de la variable. [#528](https://github.com/codegouvfr/sill-deploy/issues/528)
- Blocage de la création de logiciels via l'API lorsque l'utilisation de la fonctionnalité d'ajout de logiciel ou de service est désactivée.
- Plusieurs augmentations de version (build bumps).
