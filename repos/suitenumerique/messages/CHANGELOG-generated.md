## Changelog : messages (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'ajout de fonctionnalités pour la gestion des canaux et des messages internes, ainsi que sur la correction de bugs et l'amélioration de l'expérience utilisateur. Des améliorations significatives ont été apportées à la gestion des notifications et à la flexibilité de l'authentification.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer des backends d'authentification pour les messages entrants [#636](https://github.com/suitenumerique/messages/issues/636).
- Possibilité d'envoyer des messages internes via un ThreadEvent [#566](https://github.com/suitenumerique/messages/issues/566).
- Ajout de notifications de mention via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Les utilisateurs peuvent désormais affecter des labels aux threads, avec des widgets pour l'archivage et l'application en masse [#632](https://github.com/suitenumerique/messages/issues/632).
- Les utilisateurs ayant uniquement un accès de visualisation de thread peuvent désormais publier des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).
- Amélioration du format de la date des événements de thread.
- Ajout de vérifications SPF récursives et validation optionnelle au moment de l'envoi [#625](https://github.com/suitenumerique/messages/issues/625).
- Ajout de vérifications de l'intégrité (checksum) et de healthchecks pour lprobe [#600](https://github.com/suitenumerique/messages/issues/600).
- Ajout de la possibilité de diviser un thread depuis un message (fonctionnalité masquée derrière un flag de fonctionnalité) [#624](https://github.com/suitenumerique/messages/issues/624).

### Évolutions techniques
- Factorisation du code SSRF et autorisation des redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Ajout de la gestion de l'encryption, de scopes personnalisés et de l'audit pour les canaux [#599](https://github.com/suitenumerique/messages/issues/599).
- Correction d'une condition de concurrence dans la suppression du dernier éditeur.
- Mise à jour de Cunningham et de ui-kit.
- Application de droits d'édition complets sur les mutations de thread.
- Amélioration de l'ordonnancement des threads [#617](https://github.com/suitenumerique/messages/issues/617).
- Correction de la gestion des erreurs de tâches Celery non sérialisables.
- Correction d'une erreur de citation dans MDA et ajout de la journalisation du proxy SOCKS dans la livraison sortante [#626](https://github.com/suitenumerique/messages/issues/626).

### Autres changements
- Correction de l'empilement des popups de labels avec la modale de création de label [#635](https://github.com/suitenumerique/messages/issues/635).
- Suppression de `npm` des moteurs dans `package.json` [#616](https://github.com/suitenumerique/messages/issues/616).
- Correction d'un double appel et d'un scintillement lors de la recherche [#596](https://github.com/suitenumerique/messages/issues/596).
- Affichage/masquage de l'entrée ThreadEvent lorsque pertinent.
- Focus sur le champ `to` lors du transfert.
- Désactivation du menu d'application lorsque aucune option n'est disponible.
- Alignement du bouton d'envoi à gauche.
- Suppression de l'utilisation de `mailbox.id` dans les métriques.
