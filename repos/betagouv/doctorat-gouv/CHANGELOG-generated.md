## Changelog : doctorat-gouv (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment en matière de filtres de recherche, d'affichage des informations et d'internationalisation. Des améliorations ont également été apportées à l'import des données et à la gestion des champs de texte.

### Évolutions fonctionnelles
- **Filtres de recherche :**
    - Ajout d'un bouton pour réinitialiser tous les filtres [#d9282af](https://github.com/betagouv/doctorat-gouv/commit/d9282af).
    - Amélioration de l'affichage des filtres sélectionnés et de leur nombre [#a2a0a2c](https://github.com/betagouv/doctorat-gouv/commit/a2a0a2c), [#55c6ef1](https://github.com/betagouv/doctorat-gouv/commit/55c6ef1), [#9c15c29](https://github.com/betagouv/doctorat-gouv/commit/9c15c29).
    - Implémentation de filtres multi-sélection [#70aa23a](https://github.com/betagouv/doctorat-gouv/commit/70aa23a).
    - Ajout de filtres par année de thèse [#18564ee](https://github.com/betagouv/doctorat-gouv/commit/18564ee), [#0aa9377](https://github.com/betagouv/doctorat-gouv/commit/0aa9377), [#0f93b02](https://github.com/betagouv/doctorat-gouv/commit/0f93b02).
- **Affichage des informations :**
    - Modification de l'affichage de l'année de thèse au format académique (n/n+1) [#774bda7](https://github.com/betagouv/doctorat-gouv/commit/774bda7).
    - Amélioration de l'affichage sur mobile [#ee73efd](https://github.com/betagouv/doctorat-gouv/commit/ee73efd).
    - Affichage d'un message informatif lorsque certains champs sont vides [#60dc2f9](https://github.com/betagouv/doctorat-gouv/commit/60dc2f9).
    - Affichage d'un message lorsqu'un sujet est attribué [#28e7ef7](https://github.com/betagouv/doctorat-gouv/commit/28e7ef7).
    - Affichage des versions anglaises du titre, des mots-clés et du résumé dans la page de recherche et les détails [#1308ff2](https://github.com/betagouv/doctorat-gouv/commit/1308ff2), [#0bd97ed](https://github.com/betagouv/doctorat-gouv/commit/0bd97ed).
- **Autres améliorations :**
    - Ajout d'un compteur de caractères pour le champ motivation avec des contrôles de longueur [#a6dbf8d](https://github.com/betagouv/doctorat-gouv/commit/a6dbf8d), [#621ca5e](https://github.com/betagouv/doctorat-gouv/commit/621ca5e), [#1b68798](https://github.com/betagouv/doctorat-gouv/commit/1b68798).
    - Ajout d'un mode de rattrapage pour l'import des propositions de thèse ADUM [#67671cc](https://github.com/betagouv/doctorat-gouv/commit/67671cc).
    - Sauvegarde de la page active dans le filtre de recherche [#63f3b2e](https://github.com/betagouv/doctorat-gouv/commit/63f3b2e).
    - Sauvegarde des choix de tri lors du changement de page [#357ac12](https://github.com/betagouv/doctorat-gouv/commit/357ac12).
    - Ajout d'une fonctionnalité de tri dans la page de recherche [#ef9fa79](https://github.com/betagouv/doctorat-gouv/commit/ef9fa79).

### Évolutions techniques
- **Internationalisation (i18n) :**
    - Intégration de l'internationalisation dans la page détails et la page de recherche [#0335516](https://github.com/betagouv/doctorat-gouv/commit/0335516), [#cb866ff](https://github.com/betagouv/doctorat-gouv/commit/cb866ff), [#aa34085](https://github.com/betagouv/doctorat-gouv/commit/aa34085).
    - Internationalisation de plusieurs filtres et menus [#cdfebe7](https://github.com/betagouv/doctorat-gouv/commit/cdfebe7), [#cb872d7](https://github.com/betagouv/doctorat-gouv/commit/cb872d7), [#c7043bd](https://github.com/betagouv/doctorat-gouv/commit/c7043bd), [#834a68c](https://github.com/betagouv/doctorat-gouv/commit/834a68c).
- **Refactoring et corrections :**
    - Correction d'un problème lié au contrôle du sujet de thèse [#7c69ffc](https://github.com/betagouv/doctorat-gouv/commit/7c69ffc).
    - Correction d'un problème lié aux champs objectif et contexte non renseignés [#8c9656c](https://github.com/betagouv/doctorat-gouv/commit/8c9656c).
    - Suppression du contrôle sur le sujet de thèse pour permettre les offres d'encadrement sans sujet [#f1a8a7b](https://github.com/betagouv/doctorat-gouv/commit/f1a8a7b).

### Autres changements
- Préparation et finalisation des versions 0.2.7, 0.2.6 et 0.2.5 [#4e6da8b](https://github.com/betagouv/doctorat-gouv/commit/4e6da8b), [#0b7971a](https://github.com/betagouv/doctorat-gouv/commit/0b7971a), [#165f227](https://github.com/betagouv/doctorat-gouv/commit/165f227).
- Amélioration des espaces et de la traduction de certains champs [#4933381](https://github.com/betagouv/doctorat-gouv/commit/4933381), [#ae770b1](https://github.com/betagouv/doctorat-gouv/commit/ae770b1).
- Modification de la taille maximale du champ motivation [#6fae4e1](https://github.com/betagouv/doctorat-gouv/commit/6fae4e1).
- Correction de la taille des fichiers scss [#1a41069](https://github.com/betagouv/doctorat-gouv/commit/1a41069).
