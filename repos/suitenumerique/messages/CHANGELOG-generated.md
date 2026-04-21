## Changelog : messages (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la gestion des threads et des notifications, ainsi que sur l'ajout de nouvelles fonctionnalités pour les canaux de communication. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Possibilité d'envoyer des messages internes via un ThreadEvent [#566](https://github.com/suitenumerique/messages/issues/566).
- Ajout de notifications de mention via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Les utilisateurs peuvent maintenant affecter des labels aux threads, avec des options d'archivage et d'actions en masse [#632](https://github.com/suitenumerique/messages/issues/632).
- Amélioration du format de la date des événements de thread [#635](https://github.com/suitenumerique/messages/issues/635).
- Les utilisateurs ayant uniquement le droit de visualiser un thread peuvent désormais poster des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).
- Ajout de la possibilité de configurer des backends d'authentification entrants [#636](https://github.com/suitenumerique/messages/issues/636).
- Ajout d'une vérification SPF récursive et d'une validation optionnelle au moment de l'envoi [#625](https://github.com/suitenumerique/messages/issues/625).
- Ajout de vérifications de l'état de santé et de la somme de contrôle pour lprobe et Caddy [#600](https://github.com/suitenumerique/messages/issues/600).

### Évolutions techniques
- Refactorisation du code SSRF pour autoriser les redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Correction d'une condition de concurrence dans la suppression du dernier éditeur [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'une erreur de traitement des erreurs de tâches Celery non sérialisables [#633](https://github.com/suitenumerique/messages/issues/633).
- Correction d'une erreur de citation dans la livraison sortante MDA [#626](https://github.com/suitenumerique/messages/issues/626).
- Ajout de fonctionnalités d'encryption, de scopes personnalisés, de niveaux et d'audit pour les canaux [#599](https://github.com/suitenumerique/messages/issues/599).
- Mise en place d'un feature flag pour la fonctionnalité de division de thread [#624](https://github.com/suitenumerique/messages/issues/624).
- Amélioration de l'ordre des threads [#617](https://github.com/suitenumerique/messages/issues/617).
- Mise à jour de cunningham et ui-kit [#635](https://github.com/suitenumerique/messages/issues/635).
- Correction pour forcer les droits d'édition complets sur les mutations de thread [#635](https://github.com/suitenumerique/messages/issues/635).

### Autres changements
- Correction des tests qui dépendaient de boto3 [#635](https://github.com/suitenumerique/messages/issues/635).
- Initialisation de l'entrée d'événement de thread lors de l'ouverture [#635](https://github.com/suitenumerique/messages/issues/635).
- Suppression de `npm` des moteurs du projet [#616](https://github.com/suitenumerique/messages/issues/616).
- Amélioration de l'affichage du popup de label [#635](https://github.com/suitenumerique/messages/issues/635).
- Désactivation du menu d'application lorsqu'aucune option n'est disponible [#635](https://github.com/suitenumerique/messages/issues/635).
- Focus sur le champ "à" lors d'un transfert [#635](https://github.com/suitenumerique/messages/issues/635).
- Alignement du bouton d'envoi à gauche [#635](https://github.com/suitenumerique/messages/issues/635).
