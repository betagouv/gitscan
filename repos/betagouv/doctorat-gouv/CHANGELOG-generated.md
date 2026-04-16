## Changelog : doctorat-gouv (30 derniers jours, au 13 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en ce qui concerne la recherche et le filtrage des sujets de thèse. Des améliorations ont été apportées à l'affichage des filtres, à la gestion des données importées depuis Amethis et ADUM, et à la présentation des informations sur les propositions de thèse. Plusieurs corrections et optimisations ont également été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité d'utiliser `innerHTML` pour interpréter les balises HTML provenant d'ADUM et Amethis, assurant une mise en forme correcte des champs longs. [#31](https://github.com/betagouv/doctorat-gouv/pull/31)
- Implémentation d'un pipe pour convertir les sauts de ligne (`/r/n`) en balises `<br>`, améliorant l'affichage du texte multiligne. [#32](https://github.com/betagouv/doctorat-gouv/pull/32)
- Intégration de l'appel à l'API Amethis pour récupérer des données. [#29](https://github.com/betagouv/doctorat-gouv/pull/29)
- Ajout d'un bouton pour réinitialiser tous les filtres appliqués.
- Amélioration de l'affichage des filtres sélectionnés, notamment en version mobile.
- Ajout de la fonctionnalité de multi-filtres, permettant de sélectionner plusieurs options dans un même filtre.
- Ajout d'un filtre par année pour les sujets de thèse.
- Ajout d'une nouvelle colonne "année" dans les informations de la proposition de thèse.
- Amélioration de l'affichage de la version mobile de la plateforme, notamment des boutons de type de proposition.
- Ajout d'un message informatif indiquant qu'un sujet a été attribué.
- Ajout d'un nouveau champ "sujetAttribue" pour indiquer si un sujet est attribué.
- Ajout d'un menu filtre pour filtrer les propositions par type.
- Affichage d'un message générique lorsqu'aucun financement n'est renseigné.
- Adaptation de la traduction de certains champs pour une meilleure clarté.
- Ne plus afficher les champs non renseignés dans la page de détails d'une proposition.
- Augmentation de la taille maximale du champ "motivation" à 3500 caractères et ajout d'un compteur de caractères.

### Évolutions techniques
- Changement de la méthode d'affichage du nombre de filtres actifs.
- Modification de l'affichage horizontal des filtres actifs.
- Sauvegarde de la page active dans le filtre de recherche et modification du SCSS associé.
- Sauvegarde des choix de tri lors du changement de page.
- Ajout d'une nouvelle fonctionnalité de tri dans la page de recherche.
- Modification du style de la barre de tri pour utiliser un composant DSFR (Design System Fr).
- Amélioration de la gestion de la taille des fichiers SCSS.

### Autres changements
- Préparation et finalisation des versions 0.2.6, 0.2.7 et 0.2.8.
- Correction d'un problème avec le bouton multi-filtres.
- Désactivation temporaire du scheduler Amethis.
- Améliorations mineures des espaces dans le code.
- Internationalisation des badges "impactList".
- Adaptation de la traduction de certains champs en anglais.
- Ajout d'une clé i18n pour le champ RGPD obligatoire.
- Ajout d'un mode de rattrapage pour l'import des propositions de thèse ADUM.
