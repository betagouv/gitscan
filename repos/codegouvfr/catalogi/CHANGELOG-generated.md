## Changelog : catalogi (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de la recherche et de l'importation de logiciels, ainsi que sur l'ajout de nouvelles fonctionnalités d'administration pour la gestion des attributs personnalisés. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la récupération et de la recherche d'organisations sur Wikidata [#505](https://github.com/codegouvfr/catalogi/issues/505).
- Amélioration de la recherche de logiciels par source [#516](https://github.com/codegouvfr/catalogi/issues/516).
- Ajout de protections pour les logiciels.
- Configuration des cartes de sélection de logiciels sur la page d'accueil via l'interface utilisateur.
- Possibilité de bloquer la création de logiciels via l'API lorsque l'utilisation de la fonctionnalité "ajouter un logiciel ou un service" est désactivée.
- Ajout de la récupération de tous les identifiants sur HAL [#515](https://github.com/codegouvfr/catalogi/issues/515).
- Amélioration de l'affichage de la page d'accueil avec un espacement plus compact entre le héros et la sélection des logiciels.
- Ajout d'une page d'administration (accessible avec le rôle admin) pour gérer les attributs personnalisés, incluant la restriction de leur accès et la gestion de leur affichage [#528](https://github.com/codegouvfr/catalogi/issues/528).
- Le nom du logiciel peut maintenant retomber sur les sources si nécessaire.

### Évolutions techniques
- Refactorisation de la logique de filtrage des logiciels pour effectuer le filtrage directement au niveau SQL, améliorant ainsi les performances [#516](https://github.com/codegouvfr/catalogi/issues/516).
- Amélioration de la gestion des références de migration.
- Stabilisation des tests similaires pour les logiciels.
- Mise à jour de la configuration de l'importation automatique pour ne pas créer d'entrée utilisateur [#528](https://github.com/codegouvfr/catalogi/issues/528).
- Amélioration de la configuration du cache des navigateurs Playwright pour les tests CI.
- Correction de l'installation des navigateurs Playwright en CI.
- Correction des tests Playwright qui échouaient en CI.
- Clarification de la documentation concernant le routage de l'API Helm.

### Autres changements
- Mise à jour des dépendances Renovate.
- Ajout d'un script pour initialiser la base de données racine.
- Bump de version.
