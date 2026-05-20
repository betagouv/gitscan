## Changelog : messages (30 derniers jours, au 19 mai 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de l'expérience utilisateur, notamment en permettant l'assignation de threads, en améliorant la gestion des index de recherche et en corrigeant des bugs liés à l'affichage et au traitement des emails. Des améliorations techniques ont également été apportées pour optimiser les performances et la fiabilité du système.

### Évolutions fonctionnelles
- Possibilité d'assigner des threads à des utilisateurs. [#2673725](https://github.com/suitenumerique/messages/pull/2673725)
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés. [#644](https://github.com/suitenumerique/messages/pull/644)
- Ajout d'une action pour marquer les threads comme lus/non lus directement depuis la barre d'actions. [#659](https://github.com/suitenumerique/messages/pull/659)
- Les sections du panneau sont désormais redimensionnables. [#8a7cb8e](https://github.com/suitenumerique/messages/commit/8a7cb8e)
- Une info-bulle confirme désormais l'actualisation de la boîte de réception. [#858e995](https://github.com/suitenumerique/messages/commit/858e995)
- Amélioration de l'affichage de l'en-tête du panneau de thread en cas de libellés imbriqués. [#658](https://github.com/suitenumerique/messages/pull/658)
- Ajout d'informations sur le délai de propagation DNS. [#654](https://github.com/suitenumerique/messages/pull/654)
- Possibilité de spécifier un ID de canal pour le widget de feedback de la page d'accueil. [#655](https://github.com/suitenumerique/messages/pull/655)
- Séparateur d'attachments localisé. [#1b03e1d](https://github.com/suitenumerique/messages/commit/1b03e1d)

### Évolutions techniques
- Refactorisation de la gestion du cache des requêtes de threads. [#642](https://github.com/suitenumerique/messages/pull/642)
- Amélioration des performances de la recherche en utilisant la suppression en masse par ID au lieu de `delete_by_query`. [#bff7464](https://github.com/suitenumerique/messages/commit/bff7464)
- Gestion améliorée des erreurs de transport OpenSearch avec des tentatives. [#2603b2b](https://github.com/suitenumerique/messages/commit/2603b2b)
- Décalage des tâches d'indexation pour améliorer les performances. [#6d0eb0d](https://github.com/suitenumerique/messages/commit/6d0eb0d)
- Amélioration du payload en masse pour la recherche. [#81da914](https://github.com/suitenumerique/messages/commit/81da914)
- Correction de la gestion des caractères spéciaux dans les mots de passe générés. [#640](https://github.com/suitenumerique/messages/pull/640)
- Mise à jour de la logique du widget pour utiliser la dernière version. [#649](https://github.com/suitenumerique/messages/pull/649)
- Correction des noms de processus dans le Procfile pour le déploiement. [#648](https://github.com/suitenumerique/messages/pull/648)
- Placement des imports et des files d'attente de worker de réindexation dans des conteneurs dédiés. [#643](https://github.com/suitenumerique/messages/pull/643)
- Correction de la logique pour ne plus signaler les emails "De=À" comme étant l'expéditeur. [#652](https://github.com/suitenumerique/messages/pull/652)
- Correction de bugs liés au parsing d'emails avec des caractères UTF-8. [#656](https://github.com/suitenumerique/messages/pull/656)
- Correction de tests dépendant de boto3. [#7a0f6fb](https://github.com/suitenumerique/messages/commit/7a0f6fb)

### Autres changements
- Suppression de la possibilité de marquer les messages individuellement comme lus/importants au profit de la gestion au niveau du thread. (Nécessite une réindexation de la recherche après la mise à jour).
- Force l'utilisation de la langue par défaut. [#647](https://github.com/suitenumerique/messages/pull/647)
- Correction de l'initialisation de l'entrée d'événement de thread lors de l'ouverture. [#9a44d2c](https://github.com/suitenumerique/messages/commit/9a44d2c)
