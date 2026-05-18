## Changelog : messages (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la performance de l'application. Les utilisateurs bénéficient d'une meilleure gestion des threads (assignation, lecture/non-lu), d'une interface plus flexible avec des panneaux redimensionnables, et d'une résolution de problèmes liés à l'affichage et au parsing des emails. Des optimisations techniques ont été apportées à l'indexation et à la recherche pour améliorer la réactivité.

### Évolutions fonctionnelles
- Possibilité d'assigner des threads à des utilisateurs [#2673725](https://github.com/suitenumerique/messages/issues/2673725).
- Ajout d'actions "Lu/Non lu" sur la barre d'actions des threads [#659](https://github.com/suitenumerique/messages/issues/659).
- Les panneaux de l'interface utilisateur sont désormais redimensionnables [#8a7cb8e](https://github.com/suitenumerique/messages/commit/8a7cb8e).
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés [#644](https://github.com/suitenumerique/messages/issues/644).
- Un tooltip confirme le rafraîchissement de la boîte de réception [#858e995](https://github.com/suitenumerique/messages/commit/858e995).
- Amélioration de l'affichage des en-têtes de panneau de thread avec des labels imbriqués [#658](https://github.com/suitenumerique/messages/issues/658).
- Possibilité d'utiliser un ID de canal spécifique pour le widget de feedback de la page d'accueil [#655](https://github.com/suitenumerique/messages/issues/655).
- Ajout d'informations sur le délai de propagation DNS [#654](https://github.com/suitenumerique/messages/issues/654).

### Évolutions techniques
- Refactorisation de la gestion du cache des requêtes de threads [#6be3b9e](https://github.com/suitenumerique/messages/issues/642).
- Optimisation de l'indexation et de la recherche : remplacement de `delete_by_query` par une suppression en masse par ID, gestion des erreurs de transport OpenSearch, amélioration du payload en masse pour la recherche, report des tâches d'indexation [#2603b2b](https://github.com/suitenumerique/messages/commit/2603b2b), [#81da914](https://github.com/suitenumerique/messages/commit/81da914), [#6d0eb0d](https://github.com/suitenumerique/messages/commit/6d0eb0d).
- Correction de la gestion des caractères spéciaux dans les mots de passe générés [#640](https://github.com/suitenumerique/messages/issues/640).
- Amélioration de la résilience de la vérification DNS.
- Correction de la gestion des erreurs d'analyse des emails avec encodage UTF8 [#656](https://github.com/suitenumerique/messages/issues/656).
- Correction des tests unitaires qui dépendaient de `boto3` [#7a0f6fb](https://github.com/suitenumerique/messages/commit/7a0f6fb).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Correction des noms de processus dans le Procfile pour le déploiement PaaS [#648](https://github.com/suitenumerique/messages/issues/648).
- Placement des imports et des files d'attente worker dans des conteneurs dédiés pour le déploiement PaaS [#643](https://github.com/suitenumerique/messages/issues/643).

### Autres changements
- Localisation du séparateur de pièces jointes [#1b03e1d](https://github.com/suitenumerique/messages/commit/1b03e1d).
- Suppression du marquage des emails "De=À" comme étant l'expéditeur [#652](https://github.com/suitenumerique/messages/issues/652).
- Support des attributs de widget legacy et nouveaux [#650](https://github.com/suitenumerique/messages/issues/650).
- Force l'utilisation de la langue par défaut [#647](https://github.com/suitenumerique/messages/issues/647).
- Initialisation de l'entrée d'événement de thread lors de l'ouverture [#9a44d2c](https://github.com/suitenumerique/messages/commit/9a44d2c).
