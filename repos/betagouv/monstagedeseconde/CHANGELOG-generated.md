## Changelog : monstagedeseconde (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des stages et des offres, avec des corrections de bugs et des optimisations des tests pour assurer une meilleure stabilité de la plateforme. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour les pages partenaires et l'affichage des logos.

### Évolutions fonctionnelles
- Amélioration du formulaire des offres de stage [#1666](https://github.com/betagouv/monstagedeseconde/issues/1666).
- Mise à jour des pages partenaires, incluant l'ajout d'un carrousel de logos [#1778](https://github.com/betagouv/monstagedeseconde/issues/1778) et [#1780](https://github.com/betagouv/monstagedeseconde/issues/1780).
- Mise à jour de la page étudiant [#1775](https://github.com/betagouv/monstagedeseconde/issues/1775).
- Amélioration de la gestion de la signature groupée des conventions, rendant l'appariement signature/convention indépendant de l'ordre de traitement.
- Adaptation de la plateforme aux vacances d'été 2026 [#1747](https://github.com/betagouv/monstagedeseconde/issues/1747).
- Correction d'un bug empêchant l'accès administrateur pendant la maintenance.

### Évolutions techniques
- Refactorisation du code pour mutualiser des éléments communs [#MGF-1768](https://github.com/betagouv/monstagedeseconde/issues/MGF-1768).
- Mise à jour de la gestion du déploiement en staging pour éviter les blocages.
- Amélioration de la robustesse des tests système, avec correction de nombreux tests défaillants et suppression de code obsolète.
- Normalisation de la recherche d'emails dans le guard de connexion pour la maintenance.
- Mise à jour de plusieurs dépendances : `msgpack`, `mcp`, `oauth2`, `rails-html-sanitizer`, `websocket-driver`, `js-yaml`, `view_component`, `webpack-dev-server`, `fast-uri`.

### Autres changements
- Correction de violations d'accessibilité (a11y) sur plusieurs pages, notamment après la remise en service des captures W3C.
- Mise en quarantaine des pages présentant des violations d'accessibilité préexistantes.
- Mise à jour des tâches d'archivage des entreprises et des étudiants.
- Correction de bugs et améliorations diverses pour stabiliser la plateforme.
- Amélioration des tests d'inscription.
- Correction du callback Sygne.
- Correction d'une vérification des heures dans l'offre.
