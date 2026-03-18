## Changelog : jeveuxaider-back (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des exports de données, la gestion des territoires et des missions, ainsi que la mise à jour de certaines dépendances et l'optimisation de la plateforme. Des corrections ont également été apportées pour améliorer la stabilité et la précision des données.

### Évolutions fonctionnelles
- **Exports :** Amélioration significative des exports de données, avec une sélection plus précise des champs et des relations pour optimiser la performance et la pertinence des données exportées. Les rôles administrateur sont exclus des exports de profils. [#145](https://github.com/betagouv/jeveuxaider-back/issues/145) [#142](https://github.com/betagouv/jeveuxaider-back/issues/142) [#141](https://github.com/betagouv/jeveuxaider-back/issues/141) [#139](https://github.com/betagouv/jeveuxaider-back/issues/139)
- **Territoires :** Ajout des départements d'outre-mer (DOM-TOM) manquants. [#138](https://github.com/betagouv/jeveuxaider-back/issues/138)
- **Missions :** Ajout d'un champ `is_open_to_minors` et de la logique associée pour gérer l'ouverture des missions aux mineurs. [#123](https://github.com/betagouv/jeveuxaider-back/issues/123)
- **Notifications :** Mise à jour du sujet et du contenu des notifications concernant la validation des territoires. [#129](https://github.com/betagouv/jeveuxaider-back/issues/129)
- **Témoignages :** Ajout d'une fonctionnalité permettant de revoir les témoignages. [#130](https://github.com/betagouv/jeveuxaider-back/issues/130)
- **Filtres :** Amélioration des filtres pour supporter les valeurs de tableaux pour les départements et régions. [#129](https://github.com/betagouv/jeveuxaider-back/issues/129)

### Évolutions techniques
- **Laravel Passport :** Mise à jour de Laravel Passport vers la version 13 et des dépendances associées. [#133](https://github.com/betagouv/jeveuxaider-back/issues/133)
- **Laravel :** Mise à jour des versions de Laravel. [#129](https://github.com/betagouv/jeveuxaider-back/issues/129)
- **Refactoring :** Refactorisation de la logique de filtrage des départements dans `NumbersController` pour améliorer la clarté et la performance.
- **Refactoring :** Refactorisation de la logique `searchable` pour les missions et structures. [#135](https://github.com/betagouv/jeveuxaider-back/issues/135)
- **API Engagement :** Ajout d'une méthode pour mettre à jour le statut de participation dans le service `ApiEngagement`. [#134](https://github.com/betagouv/jeveuxaider-back/issues/134)
- **Slack Notifications :** Mise à jour des notifications Slack avec des composants Block Kit. [#126](https://github.com/betagouv/jeveuxaider-back/issues/126)
- **Queue de tâches :** Redémarrage du scheduler de l'application front via une fonctionnalité dédiée. [#128](https://github.com/betagouv/jeveuxaider-back/issues/128)

### Autres changements
- Correction d'un bug concernant le code mort dans le gestionnaire pour la compatibilité avec Passport 13.
- Ajout du code manquant pour la région Grand Est dans les taxonomies.
- Ajout d'une commande pour supprimer un témoignage par son ID. [#132](https://github.com/betagouv/jeveuxaider-back/issues/132)
- Mise à jour des statistiques des bénévoles dans le modèle d'email de deuxième rappel. [#131](https://github.com/betagouv/jeveuxaider-back/issues/131)
- Correction d'un bug dans le type d'export pour les structures dans `ExportController`.
- Ajout d'une contrainte d'unicité à la table `settings` et définition d'une valeur par défaut pour la colonne `locked`. [#144](https://github.com/betagouv/jeveuxaider-back/issues/144)
- Mise à jour des canaux Slack pour les événements `UserHasExportedDatas` et `UserHasImportedDatas`. [#127](https://github.com/betagouv/jeveuxaider-back/issues/127)
- Refactorisation des méthodes `registerMediaConversions` pour permettre un paramètre `Media` nullable.
- Correction d'un bug dans l'écouteur de messages mail.
