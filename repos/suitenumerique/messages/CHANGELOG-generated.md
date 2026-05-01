## Changelog : messages (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, la sécurité et la robustesse de la plateforme. Les utilisateurs peuvent désormais inviter des personnes n'ayant pas encore de compte, assigner des threads, et bénéficier d'une meilleure gestion des mots de passe. Des optimisations ont été apportées à la recherche et à l'indexation, ainsi qu'à la gestion des erreurs et des tâches asynchrones.

### Évolutions fonctionnelles
- Possibilité d'inviter des utilisateurs qui n'ont pas encore accédé à la plateforme. [#644](https://github.com/suitenumerique/messages/issues/644)
- Renforcement de la sécurité des mots de passe en forçant l'inclusion de caractères spéciaux. [#640](https://github.com/suitenumerique/messages/issues/640)
- Ajout de la possibilité d'assigner des threads à des utilisateurs. [#621](https://github.com/suitenumerique/messages/issues/621)
- Ajout de notifications pour les mentions d'utilisateurs. [#621](https://github.com/suitenumerique/messages/issues/621)
- Amélioration de l'assignation des labels avec la possibilité d'archiver et d'utiliser un widget en masse.
- Possibilité d'envoyer des messages internes via ThreadEvent. [#566](https://github.com/suitenumerique/messages/issues/566)
- Ajout d'une vérification SPF récursive et d'une validation optionnelle au moment de l'envoi pour une meilleure sécurité des emails. [#625](https://github.com/suitenumerique/messages/issues/625)
- Ajout de la gestion de l'encryption, de scopes personnalisés et de l'audit pour les canaux. [#599](https://github.com/suitenumerique/messages/issues/599)

### Évolutions techniques
- Optimisation de la recherche et de l'indexation : remplacement de `delete_by_query` par une suppression en masse par `_id`, gestion des erreurs de transport OpenSearch, et report des tâches d'indexation.
- Amélioration de la gestion des erreurs Celery : gestion des erreurs de tâches non sérialisables et arrêt du polling infini. [#633](https://github.com/suitenumerique/messages/issues/633)
- Refonte de l'architecture des workers pour séparer les imports et le reindex dans des conteneurs dédiés. [#643](https://github.com/suitenumerique/messages/issues/643)
- Mise à jour de Keycloak vers la version 26.6.1. [#637](https://github.com/suitenumerique/messages/issues/637)
- Amélioration de la gestion des erreurs SSRF et ajout de la possibilité de rediriger dans le proxy d'images. [#631](https://github.com/suitenumerique/messages/issues/631)
- Mise à jour des dépendances frontend (Cunningham & ui-kit).
- Correction de problèmes de noms de processus dans le Procfile (PAAS). [#648](https://github.com/suitenumerique/messages/issues/648)

### Autres changements
- Support des widgets legacy et nouveaux. [#650](https://github.com/suitenumerique/messages/issues/650)
- Correction de bugs mineurs dans l'interface utilisateur (popup des labels, focus sur le champ "à", format de date des événements de thread).
- Mise à jour de la documentation et des tests.
- Correction de problèmes liés aux droits d'édition sur les threads.
- Ajout d'un flag de fonctionnalité pour la fonctionnalité de division de thread. [#624](https://github.com/suitenumerique/messages/issues/624)
- Suppression de `npm` des moteurs. [#616](https://github.com/suitenumerique/messages/issues/616)
