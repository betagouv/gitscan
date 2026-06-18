## Changelog : catalogi (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions de catalogi se concentrent sur l'amélioration de la gestion des organisations (ROR, RNS, Wikidata), l'ajout de protections pour les logiciels, la configuration de la page d'accueil et des améliorations de l'interface d'administration. Des corrections et optimisations ont également été apportées pour stabiliser les tests et améliorer la performance.

### Évolutions fonctionnelles
- Ajout de la récupération et de la recherche d'organisations sur Wikidata. [#505](https://github.com/codegouvfr/catalogi/issues/505)
- Possibilité de configurer les cartes de sélection de logiciels sur la page d'accueil via l'interface utilisateur.
- Ajout de protections pour les logiciels.
- Blocage de la création de logiciels via l'API lorsque la fonctionnalité d'ajout via l'interface utilisateur est désactivée.
- Amélioration de l'affichage des noms de logiciels en permettant un retour aux sources si le nom principal est absent.
- Ajout d'une page d'administration (accessible avec un nouveau rôle) pour gérer les attributs personnalisés, avec restriction de l'accès et amélioration de l'affichage. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Ajout de la récupération de tous les identifiants sur HAL. [#515](https://github.com/codegouvfr/catalogi/issues/515)
- Amélioration de l'importation automatique pour ne plus créer d'entrée utilisateur. [#528](https://github.com/codegouvfr/catalogi/issues/528)

### Évolutions techniques
- Optimisation de la requête SQL pour la mise à jour parallèle des sources. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Refactorisation du code pour utiliser des objets en entrée et renommer des variables. [#528](https://github.com/codegouvfr/catalogi/issues/528)
- Amélioration de la stabilité des tests Playwright, notamment en stabilisant les assertions sur les logiciels similaires et en corrigeant l'installation des navigateurs en CI.
- Correction de l'ordre des tests live.
- Correction de l'ordre des références de migration. [#523](https://github.com/codegouvfr/catalogi/issues/523)
- Amélioration de la documentation sur le routage de l'API Helm.
- Ajout d'un script pour monter la base de données root.

### Autres changements
- Amélioration de l'espacement entre le héros de la page d'accueil et la sélection des logiciels.
- Correction de l'ordre des tests.
- Mises à jour de dépendances via Renovate.
- Augmentation du numéro de version.
