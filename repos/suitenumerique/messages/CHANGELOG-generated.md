## Changelog : messages (30 derniers jours, au 4 mai 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la sécurité, de la gestion des invitations, de l'indexation de la recherche et de l'expérience utilisateur globale. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant la gestion des erreurs et l'affichage de l'interface.

### Évolutions fonctionnelles
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés [#644](https://github.com/suitenumerique/messages/issues/644).
- Ajout de notifications de mention via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Possibilité d'assigner des threads [#622](https://github.com/suitenumerique/messages/issues/622).
- Amélioration de l'assignation des labels avec l'archivage et le widget de sélection multiple [#632](https://github.com/suitenumerique/messages/issues/632).
- Ajout de la possibilité pour les spectateurs de thread de poster des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).
- Ajout de la possibilité de reindexer à partir d'une date spécifique.
- Ajout de la possibilité de configurer des backends d'authentification inbound.
- Ajout de la vérification SPF récursive et de la validation optionnelle au moment de l'envoi [#625](https://github.com/suitenumerique/messages/issues/625).
- Ajout de la gestion de l'encryption, des scopes personnalisés et des niveaux d'audit pour les canaux [#599](https://github.com/suitenumerique/messages/issues/599).

### Évolutions techniques
- Amélioration de la gestion des erreurs de transport OpenSearch avec des tentatives de réexécution.
- Optimisation du chargement des données pour l'indexation de la recherche.
- Refactorisation du code pour éviter les erreurs de sérialisation des tâches Celery.
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Correction des noms de processus dans le Procfile pour le déploiement PaaS.
- Placement des imports et des files d'attente de worker reindex dans des conteneurs dédiés.
- Amélioration de la logique du widget frontend pour supporter les attributs legacy et nouveaux [#650](https://github.com/suitenumerique/messages/issues/650).
- Correction d'un problème de condition de concurrence dans la suppression du dernier éditeur.
- Amélioration de la gestion des erreurs non sérialisables dans les tâches Celery et arrêt du polling infini [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'un bug empêchant l'affichage correct des popups de labels avec le modal de création de label [#635](https://github.com/suitenumerique/messages/issues/635).
- Correction d'un problème de formatage de la date des événements de thread.
- Mise à jour des dépendances cunningham et ui-kit.
- Correction d'un problème empêchant l'application des droits d'édition complets sur les mutations de thread.
- Correction d'un problème de stacking des labels.
- Amélioration de la gestion des erreurs de quota dans les livraisons MDA [#626](https://github.com/suitenumerique/messages/issues/626).

### Autres changements
- Correction d'un bug qui signalait incorrectement les emails "De=À" comme étant l'expéditeur [#652](https://github.com/suitenumerique/messages/issues/652).
- Application forcée de la langue par défaut [#647](https://github.com/suitenumerique/messages/issues/647).
- Ajout d'une protection contre les attaques SSRF et autorisation des redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Ajout d'un flag de fonctionnalité pour la fonctionnalité de division de thread [#624](https://github.com/suitenumerique/messages/issues/624).
- Suppression de la réversion de la fonctionnalité d'assignation de thread.
- Amélioration de la robustesse des vérifications DNS.
- Correction d'un problème d'initialisation de l'entrée d'événement de thread lors de l'ouverture.
- Suppression de l'utilisation de `mailbox.id` dans les métriques.
- Correction de l'utilisation de `boto3` dans les tests.
