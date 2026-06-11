## Changelog : monstagedeseconde (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des conventions, la correction de bugs liés aux applications et à la signature électronique, ainsi que des optimisations techniques pour la performance et la sécurité de la plateforme. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des rôles et permissions.

### Évolutions fonctionnelles
- Possibilité de modifier l'adresse email des représentants légaux. [#813](https://github.com/betagouv/monstagedeseconde/issues/813)
- Correction d'un bug empêchant la publication correcte des offres après des clics intempestifs. [#907](https://github.com/betagouv/monstagedeseconde/issues/907)
- Amélioration de la gestion des conventions : correction d'un problème de double publication et affichage correct des conventions signées par l'employeur. [#889](https://github.com/betagouv/monstagedeseconde/issues/889), [#905](https://github.com/betagouv/monstagedeseconde/issues/905)
- Ajout de la possibilité d'importer des étudiants depuis l'administration. [#883](https://github.com/betagouv/monstagedeseconde/issues/883)
- Correction d'un problème empêchant les étudiants de postuler plusieurs fois à la même offre.
- Amélioration de la gestion des semaines vides dans le calendrier. [#899](https://github.com/betagouv/monstagedeseconde/issues/899)
- Ajout de la possibilité de gérer le niveau d'étude des étudiants. [#883](https://github.com/betagouv/monstagedeseconde/issues/883)
- Amélioration du wording concernant la récupération des candidatures. [#876](https://github.com/betagouv/monstagedeseconde/issues/876)
- Limitation de la taille des images uploadées. [#904](https://github.com/betagouv/monstagedeseconde/issues/904)
- Ajout d'un chatbot Crisp pour l'assistance utilisateur. [#895](https://github.com/betagouv/monstagedeseconde/issues/895)
- Amélioration de la gestion des types d'utilisateurs lors de l'inscription. [#866](https://github.com/betagouv/monstagedeseconde/issues/866)
- Correction d'une vulnérabilité XSS dans le rejet des candidatures. [#869](https://github.com/betagouv/monstagedeseconde/issues/869)

### Évolutions techniques
- Refactorisation de l'architecture des autorisations (abilities) pour une meilleure maintenabilité. [#889](https://github.com/betagouv/monstagedeseconde/issues/889)
- Mise à jour de Ruby à la version 3.4.9. [#884](https://github.com/betagouv/monstagedeseconde/issues/884)
- Amélioration de la gestion des erreurs liées à l'API Sygne, avec ajout de classes d'erreur spécifiques et de mécanismes de retry.
- Optimisation des requêtes SQL pour la reconstruction des données de revue.
- Amélioration de la gestion des jobs asynchrones (Sidekiq) pour éviter les interruptions.
- Mise à jour de diverses dépendances (webpack-dev-server, babel/plugin-transform-modules-systemjs, view_component, devise, faraday, jwt).

### Autres changements
- Suppression de fichiers inutiles et nettoyage du code.
- Mise à jour de la documentation.
- Correction de typos et amélioration du wording dans divers endroits de l'application.
- Ajout de tests pour améliorer la couverture et la stabilité du code.
- Suppression d'un add-on tiers inutile.
- Configuration de l'environnement de production pour activer le mode maintenance.
- Ajout de compétences pour l'outil d'IA Claude.
- Correction de problèmes de tests.
- Suppression de fichiers de dump inutiles.
- Correction de problèmes de CSP.
- Ajout de préfixes téléphoniques pour la Guadeloupe.
