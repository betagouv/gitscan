## Changelog : messages (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la gestion des threads, notamment en permettant leur assignation et en améliorant la gestion des notifications. Des améliorations de sécurité ont également été implémentées, ainsi que des optimisations de performance et des corrections de bugs pour une meilleure expérience utilisateur. De nouvelles fonctionnalités ont été ajoutées pour la configuration des backends d'authentification et la validation DNS.

### Évolutions fonctionnelles
- Possibilité d'assigner un thread à un utilisateur. [#2673725](https://github.com/suitenumerique/messages/pull/2673725)
- Ajout de notifications pour les mentions d'utilisateurs. [#621](https://github.com/suitenumerique/messages/issues/621)
- Possibilité d'envoyer des messages internes via un ThreadEvent. [#566](https://github.com/suitenumerique/messages/issues/566)
- Ajout de la possibilité de visualiser et de poster des commentaires internes sur les threads pour les utilisateurs ayant uniquement un accès de visualisation. [#632](https://github.com/suitenumerique/messages/issues/632)
- Amélioration de l'assignation des labels avec une interface de sélection groupée et une option d'archivage.
- Ajout d'une option pour configurer des backends d'authentification entrants. [#636](https://github.com/suitenumerique/messages/issues/636)
- Ajout de vérifications SPF récursives et de validation du temps d'envoi pour la sécurité DNS. [#625](https://github.com/suitenumerique/messages/issues/625)
- Ajout de vérifications de l'intégrité des données avec lprobe et Caddy. [#600](https://github.com/suitenumerique/messages/issues/600)

### Évolutions techniques
- Amélioration de la performance de la réindexation de la recherche en optimisant la taille des payloads.
- Décalage des tâches d'indexation pour éviter les blocages.
- Correction d'une condition de concurrence dans la suppression du dernier éditeur.
- Correction de tests qui dépendaient de `boto3`.
- Mise à jour de Keycloak vers la version 26.6.1. [#637](https://github.com/suitenumerique/messages/issues/637)
- Refactorisation du code SSRF pour permettre les redirections dans le proxy d'images. [#631](https://github.com/suitenumerique/messages/issues/631)
- Mise en place d'un flag de fonctionnalité pour la division des threads. [#624](https://github.com/suitenumerique/messages/issues/624)
- Amélioration de la gestion des erreurs des tâches Celery avec arrêt du polling infini. [#633](https://github.com/suitenumerique/messages/issues/633)
- Mise à jour de Cunningham et de l'UI Kit. [#647](https://github.com/suitenumerique/messages/issues/647)

### Autres changements
- Correction d'un bug d'affichage des popups de labels. [#635](https://github.com/suitenumerique/messages/issues/635)
- Correction d'un bug d'initialisation de l'entrée d'événement de thread. [#634](https://github.com/suitenumerique/messages/issues/634)
- Correction d'une erreur de citation dans la livraison sortante MDA. [#626](https://github.com/suitenumerique/messages/issues/626)
- Désactivation du menu d'application lorsque aucune option n'est disponible.
- Amélioration du format de date des événements de thread.
- Suppression de `npm` des moteurs du projet. [#616](https://github.com/suitenumerique/messages/issues/616)
- Correction de l'ordre des threads. [#617](https://github.com/suitenumerique/messages/issues/617)
- Alignement du bouton d'envoi sur la gauche.
- Amélioration de la gestion des erreurs non sérialisables dans les tâches Celery.
