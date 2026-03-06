## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a déployé une refonte majeure de l'interface utilisateur, améliorant significativement l'expérience utilisateur. Des corrections de bugs ont été apportées, notamment concernant la gestion des erreurs et l'authentification. Des améliorations techniques ont également été réalisées pour optimiser la performance et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur avec une mise en page à une colonne, améliorant la réactivité et l'accessibilité. [#802](https://github.com/proconnect-gouv/federation/pull/802)
- Ajout d'un bouton de contact pour signaler les problèmes lors d'erreurs internes (500). [#829](https://github.com/proconnect-gouv/federation/pull/829)
- Amélioration de la gestion des erreurs et des messages d'information liés à l'authentification OIDC. [#853](https://github.com/proconnect-gouv/federation/pull/853)
- Possibilité d'utiliser la touche "autocomplete" sur les formulaires d'administration. [#865](https://github.com/proconnect-gouv/federation/pull/865)
- Correction d'un bug empêchant la connexion des administrateurs. [#898](https://github.com/proconnect-gouv/federation/pull/898)
- Suppression du support email par défaut pour l'IDP par défaut. [#886](https://github.com/proconnect-gouv/federation/pull/886)

### Évolutions techniques
- Mise à jour de plusieurs dépendances, notamment Cypress (14.5.4 -> 15.1.0), Prettier (3.6.2 -> 3.8.1), Docker Compose, et diverses bibliothèques JavaScript et Node.js.
- Passage à l'utilisation de modules ESNext. [#855](https://github.com/proconnect-gouv/federation/pull/855)
- Amélioration de la gestion des variables booléennes dans Ansible. [#849](https://github.com/proconnect-gouv/federation/pull/849)
- Ajout d'une alerte en cas d'utilisation de l'environnement de test. [#848](https://github.com/proconnect-gouv/federation/pull/848)
- Suppression d'un index TTL obsolète sur MongoDB. [#850](https://github.com/proconnect-gouv/federation/pull/850)
- Ajout de tests Cypress pour Kubernetes. [#903](https://github.com/proconnect-gouv/federation/pull/903) et [#899](https://github.com/proconnect-gouv/federation/pull/899)
- Augmentation du timeout de Mongoose watcher. [#904](https://github.com/proconnect-gouv/federation/pull/904)

### Autres changements
- Suppression de code inutilisé (FSA5, SP3).
- Suppression du fichier manifest.webmanifest.
- Mise à jour de la politique de sécurité et ajout d'un rapport de vulnérabilités. [#867](https://github.com/proconnect-gouv/federation/pull/867) et [#868](https://github.com/proconnect-gouv/federation/pull/868)
- Amélioration des tests unitaires et d'intégration.
- Nettoyage du code et refactoring.
