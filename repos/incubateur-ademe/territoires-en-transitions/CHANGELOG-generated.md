## Changelog : territoires-en-transitions (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la performance et l'expérience utilisateur. Des correctifs de sécurité ont été implémentés pour prévenir les injections SQL. L'interface utilisateur a été améliorée avec de nouveaux composants et des corrections de bugs, notamment au niveau des tableaux et des formulaires. Des optimisations ont été apportées à la gestion des données et des imports, et des fonctionnalités ont été ajoutées pour faciliter l'audit et le suivi des actions.

### Évolutions fonctionnelles
- Correction d'une vulnérabilité d'injection SQL sur la recherche de collectivités. [#6499ceb](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6499ceb)
- Amélioration de l'édition des actions : ajout d'une vue tabulaire éditable et d'un menu d'actions. [#d1da417](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d1da417)
- Possibilité de filtrer les actions par statut et priorité dans la vue "Toutes les actions". [#4e842bc](https://github.com/incubateur-ademe/territoires-en-transitions/commit/4e842bc)
- Ajout d'une page dédiée aux mesures désactivées par la personnalisation. [#0c5b3a9](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0c5b3a9)
- Amélioration de la gestion des fichiers et des annexes : ajout de points d'accès TRPC pour l'ajout et la synchronisation. [#35a2c95](https://github.com/incubateur-ademe/territoires-en-transitions/commit/35a2c95)
- Ajout d'une fonctionnalité de génération d'archives ZIP des preuves d'audit (côté backend). [#73ca87f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/73ca87f)
- Ajout d'une modale pour demander un audit. [#cd04de5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/cd04de5)
- Mise à jour de la page publique matrice d'impact. [#8218ef9](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8218ef9)
- Amélioration de la page programme du site. [#fed9bfa](https://github.com/incubateur-ademe/territoires-en-transitions/commit/fed9bfa)

### Évolutions techniques
- Refactoring de l'architecture pour utiliser TRPC pour la récupération des données des collectivités, des ressources et de l'historique. [#c056905](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c056905)
- Migration de composants UI vers `@tet/ui` pour une meilleure cohérence et réutilisabilité. [#7a37cb0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7a37cb0)
- Suppression de code obsolète et de dépendances inutilisées. [#d539e3d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d539e3d)
- Optimisation des performances des imports de plans et de la gestion des RichTextEditor. [#d084f6b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d084f6b)
- Amélioration de la configuration et des tests CI/CD. [#a464ae6](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a464ae6)
- Ajout d'index sur les tables d'historique pour améliorer les performances des requêtes. [#b9d106d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9d106d)

### Autres changements
- Mise à jour de la documentation et des tests.
- Correction de typos et amélioration de la lisibilité du code.
- Amélioration des messages d'erreur et du feedback utilisateur.
- Mise à jour des dépendances. [#bf29f54](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bf29f54)
- Suppression de fichiers inutilisés. [#3f3106b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/3f3106b)
- Amélioration du typage et de la structure du code.
