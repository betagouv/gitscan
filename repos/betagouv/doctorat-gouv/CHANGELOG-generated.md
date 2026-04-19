## Changelog : doctorat-gouv (30 derniers jours, au 13 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en ce qui concerne la recherche et le filtrage des sujets de doctorat. Des améliorations significatives ont été apportées à l'affichage des filtres, avec l'introduction de filtres multiples et une meilleure gestion de l'affichage sur mobile. L'intégration de l'API Amethis a également débuté.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les sujets par année (n, n+1, n-1) [#7850883](https://github.com/betagouv/doctorat-gouv/commit/7850883).
- Amélioration de l'affichage des filtres actifs, notamment en version mobile [#a2a0a2c](https://github.com/betagouv/doctorat-gouv/commit/a2a0a2c).
- Introduction de filtres multiples, permettant de combiner plusieurs critères de recherche [#70aa23a](https://github.com/betagouv/doctorat-gouv/commit/70aa23a).
- Ajout d'un bouton de réinitialisation de tous les filtres [#d9282af](https://github.com/betagouv/doctorat-gouv/commit/d9282af).
- Ajout d'une nouvelle fonctionnalité de tri dans la page de recherche, avec sauvegarde des choix de tri lors de la navigation [#ef9fa79](https://github.com/betagouv/doctorat-gouv/commit/ef9fa79).
- Ajout d'un message informatif indiquant si un sujet a été attribué [#af184fd](https://github.com/betagouv/doctorat-gouv/commit/af184fd).
- Ajout d'un menu filtre pour filtrer par type de proposition [#102cb2c](https://github.com/betagouv/doctorat-gouv/commit/102cb2c).
- Amélioration de l'affichage en version mobile des boutons de type de proposition [#c14aeb8](https://github.com/betagouv/doctorat-gouv/commit/c14aeb8).
- Amélioration de la version mobile générale [#ee73efd](https://github.com/betagouv/doctorat-gouv/commit/ee73efd).
- Ajout d'un pipe pour convertir les sauts de ligne en balises `<br>` pour une meilleure interprétation du HTML provenant d'ADUM et Amethis [#a8f3335](https://github.com/betagouv/doctorat-gouv/commit/a8f3335).

### Évolutions techniques
- Début d'intégration de l'API Amethis [#2684dab](https://github.com/betagouv/doctorat-gouv/commit/2684dab).
- Utilisation de `innerHTML` pour interpréter les balises HTML d'ADUM et Amethis [#a8f3335](https://github.com/betagouv/doctorat-gouv/commit/a8f3335).
- Modification de la méthode d'affichage du nombre de filtres actifs.
- Sauvegarde de la page active dans le filtre de recherche [#63f3b2e](https://github.com/betagouv/doctorat-gouv/commit/63f3b2e).
- Ajout d'un scroll automatique pour revenir à la page de recherche après une action [#7850883](https://github.com/betagouv/doctorat-gouv/commit/7850883).

### Autres changements
- Désactivation temporaire d'AmethisScheduler [#0d66eae](https://github.com/betagouv/doctorat-gouv/commit/0d66eae).
- Correction de problèmes liés à la taille des fichiers SCSS [#1a41069](https://github.com/betagouv/doctorat-gouv/commit/1a41069).
- Renforcement du contrôle sur les champs vides pour ne plus les afficher [#60dc2f9](https://github.com/betagouv/doctorat-gouv/commit/60dc2f9).
- Modification du message de l'info-bulle pour s'adapter au type de proposition [#759736d](https://github.com/betagouv/doctorat-gouv/commit/759736d).
- Ajout d'une nouvelle colonne "année" dans la proposition de thèse [#98687ba](https://github.com/betagouv/doctorat-gouv/commit/98687ba).
- Améliorations mineures des espaces [#4933381](https://github.com/betagouv/doctorat-gouv/commit/4933381).
- Préparation des versions 0.2.8, 0.2.7 et 0.2.6.
- Finalisation des versions 0.2.7, 0.2.6 et 0.2.5.
