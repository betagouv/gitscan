## Changelog : territoires-en-transitions (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'import de plans d'action, notamment avec l'ajout d'une nouvelle fonctionnalité d'importation via différents formats de fichiers (Excel, CSV, PDF). Des améliorations ont également été apportées à la duplication de plans, à la gestion des preuves et des documents, ainsi qu'à l'interface utilisateur pour une meilleure expérience globale. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité d'import de plans d'action à partir de fichiers Excel, CSV et PDF. [#26f13d9](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/26f13d9)
- Possibilité de dupliquer un plan d'action existant, avec copie des notes, budgets détaillés et documents associés. [#a428150](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/a428150), [#8a86ba6](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/8a86ba6), [#2bb4132](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/2bb4132)
- Amélioration de l'affichage des valeurs cibles et limites des indicateurs. [#e927165](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/e927165)
- Ajout d'une modale pour demander un audit. [#cd04de5](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/cd04de5)
- Amélioration de la page "Plateforme" du site avec une nouvelle mise en page et une section FAQ. [#a2de354](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/a2de354)
- Ajout d'une option pour filtrer les mesures désactivées par la personnalisation. [#e5a5b51](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/e5a5b51)

### Évolutions techniques
- Refactorisation importante du code lié à l'import de plans d'action, incluant la validation des données, la gestion des erreurs et l'utilisation de services dédiés. [#82d877d](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/82d877d), [#6a2fdb2](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/6a2fdb2)
- Migration de nombreux labels JSX statiques vers un système de labels centralisé pour une meilleure maintenabilité. [#83095b9](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/83095b9)
- Mise à jour des dépendances et correction de vulnérabilités de sécurité. [#0591a18](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/0591a18), [#6b4b226](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/6b4b226)
- Amélioration de la performance et de la robustesse des tests. [#f9fbef9](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/f9fbef9)
- Utilisation de nouveaux composants du Design System (DS) pour améliorer la cohérence visuelle. [#d7eac84](https://github.com/incubateur-ademe/territoires-en-transitions/pulls/d7eac84)

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements d'API.
- Corrections de typos et améliorations de la lisibilité du code.
- Nettoyage du code et suppression de fichiers inutilisés.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour de la configuration des CI/CD.
