## Changelog : messages (30 derniers jours, au 20 avril 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la stabilité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour la gestion des messages et des threads. Des améliorations de sécurité ont également été apportées, notamment en matière de prévention des attaques SSRF et de gestion des autorisations. L'intégration avec Keycloak a été mise à jour et de nouvelles options de configuration ont été ajoutées pour une plus grande flexibilité.

### Évolutions fonctionnelles
- Possibilité d'envoyer des messages internes via un ThreadEvent [#566](https://github.com/suitenumerique/messages/issues/566).
- Ajout de notifications de mention via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Les utilisateurs peuvent désormais affecter des labels aux threads, avec des widgets pour l'archivage et l'application en masse [#632](https://github.com/suitenumerique/messages/issues/632).
- Amélioration du format de la date des événements de thread.
- Les utilisateurs ayant uniquement le droit de visualiser un thread peuvent désormais publier des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).
- Ajout de vérifications SPF récursives et de validation facultative au moment de l'envoi [#625](https://github.com/suitenumerique/messages/issues/625).
- Ajout de contrôles de santé lprobe et de vérification de checksum pour lprobe + caddy [#600](https://github.com/suitenumerique/messages/issues/600).

### Évolutions techniques
- Factorisation du code SSRF et autorisation des redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Ajout de backends d'authentification inbound configurables [#636](https://github.com/suitenumerique/messages/issues/636).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Ajout de niveaux d'encryption, de scopes personnalisés et d'audits pour les channels [#599](https://github.com/suitenumerique/messages/issues/599).
- Correction d'une condition de concurrence dans la suppression du dernier éditeur.
- Correction d'une erreur de gestion des tâches Celery non sérialisables, évitant ainsi les boucles infinies de polling [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'une erreur de citation dans la livraison sortante MDA [#626](https://github.com/suitenumerique/messages/issues/626).
- Mise en place d'un feature flag pour la fonctionnalité de division de thread [#624](https://github.com/suitenumerique/messages/issues/624).
- Correction de l'ordre des threads [#617](https://github.com/suitenumerique/messages/issues/617).
- Correction de bugs liés à l'affichage des popups de labels et à la superposition avec le modal de création de label [#635](https://github.com/suitenumerique/messages/issues/635).
- Amélioration de l'initialisation de l'entrée d'événement de thread lors de l'ouverture.
- Affichage/masquage de l'entrée ThreadEvent lorsque pertinent.
- Focus sur le champ `to` lors du transfert.
- Correction des droits d'édition complets sur les mutations de thread.

### Autres changements
- Mise à jour des dépendances cunningham et ui-kit.
- Suppression de npm des moteurs dans package.json [#616](https://github.com/suitenumerique/messages/issues/616).
- Alignement du bouton d'envoi à gauche.
- Désactivation du menu d'application lorsque aucune option n'est disponible.
- Correction des tests qui dépendaient de boto3 [#7a0f6fb](https://github.com/suitenumerique/messages/commit/7a0f6fb).
