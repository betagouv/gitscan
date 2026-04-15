## Changelog : messages (30 derniers jours, au 15 avril 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de l'expérience utilisateur, notamment en permettant aux utilisateurs de commenter les threads en interne, d'assigner des labels en masse et d'améliorer la gestion des notifications. Des améliorations significatives ont également été apportées à la sécurité et à la validation des emails, ainsi qu'à l'infrastructure sous-jacente.

### Évolutions fonctionnelles
- Les utilisateurs peuvent désormais poster des commentaires internes sur les threads, facilitant la collaboration interne sur les messages. [#632](https://github.com/suitenumerique/messages/issues/632)
- Ajout de la possibilité d'assigner des labels aux threads, y compris en masse, pour une meilleure organisation.
- Amélioration du format d'affichage de la date des événements dans les threads.
- Les utilisateurs reçoivent désormais des notifications lorsqu'ils sont mentionnés dans un message. [#621](https://github.com/suitenumerique/messages/issues/621)
- Possibilité d'envoyer des messages internes via les événements de thread. [#566](https://github.com/suitenumerique/messages/issues/566)
- Ajout de la prise en charge de la connexion silencieuse. [#1767e17](https://github.com/suitenumerique/messages/commit/1767e17)
- Ajout de vérifications de l'intégrité (checksum) et de healthchecks pour lprobe et Caddy. [#600](https://github.com/suitenumerique/messages/issues/600)

### Évolutions techniques
- Amélioration de la validation DNS avec ajout d'une vérification SPF récursive et d'une validation du temps d'envoi. [#625](https://github.com/suitenumerique/messages/issues/625)
- Ajout de fonctionnalités d'encryption, de scopes personnalisés et de niveaux d'audit pour les canaux. [#599](https://github.com/suitenumerique/messages/issues/599)
- La fonctionnalité de division de thread est désormais contrôlée par un *feature flag*, permettant une activation progressive et contrôlée. [#624](https://github.com/suitenumerique/messages/issues/624)
- Correction de l'ordre des threads. [#617](https://github.com/suitenumerique/messages/issues/617)
- Optimisation de la recherche en utilisant l'API en masse et le préchargement pour la réindexation complète. [#595](https://github.com/suitenumerique/messages/issues/595)
- Correction d'un problème de double requête et de scintillement lors de la recherche. [#596](https://github.com/suitenumerique/messages/issues/596)
- Suppression de `npm` des moteurs de dépendances. [#616](https://github.com/suitenumerique/messages/issues/616)
- Mise à jour de `cunningham` et `ui-kit`. [#a7dc4b4](https://github.com/suitenumerique/messages/commit/a7dc4b4)

### Autres changements
- Correction d'un bug empêchant la définition complète des droits d'édition sur les mutations de thread. [#01b45a6](https://github.com/suitenumerique/messages/commit/01b45a6)
- Alignement du bouton d'envoi sur la gauche. [#13d34c2](https://github.com/suitenumerique/messages/commit/13d34c2)
- Typage des erreurs d'API Orval. [#1c83a51](https://github.com/suitenumerique/messages/commit/1c83a51)
- Suppression du marquage du thread comme lu lors de l'envoi d'une réponse automatique. [#594](https://github.com/suitenumerique/messages/issues/594)
- Désactivation du menu d'application lorsque aucune option n'est disponible. [#efbae5f](https://github.com/suitenumerique/messages/commit/efbae5f)
