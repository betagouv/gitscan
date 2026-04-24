## Changelog : messages (30 derniers jours, au 20 avril 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la stabilité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour la gestion des threads et des notifications. Des améliorations de sécurité ont également été apportées, notamment en matière de prévention des attaques SSRF et de validation DNS.

### Évolutions fonctionnelles
- Possibilité d'envoyer des messages internes via un ThreadEvent [#566](https://github.com/suitenumerique/messages/issues/566).
- Ajout de notifications de mentions via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Les utilisateurs peuvent désormais affecter des labels aux threads, avec des options d'archivage et d'actions en masse [#632](https://github.com/suitenumerique/messages/issues/632).
- Les utilisateurs ayant uniquement le droit de visualiser un thread peuvent désormais poster des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).
- Amélioration du format de la date des événements de thread [#635](https://github.com/suitenumerique/messages/issues/635).
- Ajout de la possibilité de configurer des backends d'authentification entrants [#636](https://github.com/suitenumerique/messages/issues/636).
- Ajout de la validation du temps d'envoi et de la vérification SPF récursive pour une meilleure sécurité DNS [#625](https://github.com/suitenumerique/messages/issues/625).
- Ajout de vérifications de l'état de santé de lprobe et de la vérification du checksum pour lprobe et caddy [#600](https://github.com/suitenumerique/messages/issues/600).

### Évolutions techniques
- Correction d'une condition de concurrence dans la suppression du dernier éditeur [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'une erreur de course dans la suppression du dernier éditeur [#633](https://github.com/suitenumerique/messages/issues/633).
- Factorisation du code SSRF et autorisation des redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Mise à jour des dépendances cunningham et ui-kit [#635](https://github.com/suitenumerique/messages/issues/635).
- La fonctionnalité de division de thread est désormais contrôlée par un indicateur de fonctionnalité [#624](https://github.com/suitenumerique/messages/issues/624).
- Ajout de l'encryption, de scopes personnalisés, de niveaux et d'audits pour les canaux [#599](https://github.com/suitenumerique/messages/issues/599).
- Correction de l'ordre des threads [#617](https://github.com/suitenumerique/messages/issues/617).
- Correction de la gestion des erreurs de tâches Celery non sérialisables [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'une erreur de citation dans la livraison sortante MDA [#626](https://github.com/suitenumerique/messages/issues/626).
- Correction de l'initialisation de l'entrée d'événement de thread lors de l'ouverture [#635](https://github.com/suitenumerique/messages/issues/635).

### Autres changements
- Correction des tests qui dépendaient de boto3 [#633](https://github.com/suitenumerique/messages/issues/633).
- Suppression de npm des moteurs dans package.json [#616](https://github.com/suitenumerique/messages/issues/616).
- Amélioration de l'affichage/masquage de ThreadEventInput en fonction de la pertinence [#635](https://github.com/suitenumerique/messages/issues/635).
- Focus sur le champ `to` lors du transfert [#635](https://github.com/suitenumerique/messages/issues/635).
- Application du droit d'édition complet sur les mutations de thread [#635](https://github.com/suitenumerique/messages/issues/635).
- Alignement du bouton d'envoi à gauche [#635](https://github.com/suitenumerique/messages/issues/635).
- Désactivation du menu d'application lorsqu'aucune option n'est disponible [#635](https://github.com/suitenumerique/messages/issues/635).
