## Changelog : conversations (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la robustesse et à la surveillance de la plateforme, notamment en ajoutant une gestion de la santé des modèles d'IA et des mécanismes de fallback. Des améliorations ont également été apportées à l'expérience utilisateur, avec des messages d'erreur plus clairs et une meilleure gestion des langues. Enfin, des améliorations de sécurité et de gestion des accès ont été implémentées.

### Évolutions fonctionnelles
- Affichage de messages d'erreur plus spécifiques en cas de problèmes de parsing de documents [#2ffffae](https://github.com/suitenumerique/conversations/issues/2ffffae).
- Affichage d'une bannière d'alerte dynamique indiquant l'état de santé de l'assistant IA.
- Amélioration de la gestion des erreurs lors de la suppression d'index [#4263e9a](https://github.com/suitenumerique/conversations/issues/4263e9a).
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Amélioration du filtrage et de l'affichage dans l'administration des chats [#db7bf6d](https://github.com/suitenumerique/conversations/issues/db7bf6d).
- Le bouton d'aide a été remplacé par un menu déroulant pour une meilleure organisation [#aa24e0f](https://github.com/suitenumerique/conversations/issues/aa24e0f).
- La taille maximale des pièces jointes est maintenant affichée en cas d'échec de l'upload [#78c3190](https://github.com/suitenumerique/conversations/issues/78c3190).
- Le nom par défaut du produit est maintenant "L'Assistant" [#9199cfc](https://github.com/suitenumerique/conversations/issues/9199cfc).

### Évolutions techniques
- Implémentation de Celery pour l'exécution de tâches asynchrones [#9abe4b9](https://github.com/suitenumerique/conversations/issues/9abe4b9).
- Ajout d'un mécanisme de fallback pour les modèles d'IA [#b57d758](https://github.com/suitenumerique/conversations/issues/b57d758).
- Mise en place d'un système de surveillance de la santé des modèles Albert avec un CronJob et une intégration Helm [#41a591e](https://github.com/suitenumerique/conversations/issues/41a591e), [#757d75e](https://github.com/suitenumerique/conversations/issues/757d75e), [#6beeaea](https://github.com/suitenumerique/conversations/issues/6beeaea).
- Ajout d'un processeur d'historique à fenêtre glissante pour la gestion des conversations [#1241a1e](https://github.com/suitenumerique/conversations/issues/1241a1e).
- Refactorisation du module de vues de chat et utilisation de constantes partagées [#0c06446](https://github.com/suitenumerique/conversations/issues/0c06446).
- Mise à jour de la version de Python et des dépendances [#df4c0ae](https://github.com/suitenumerique/conversations/issues/df4c0ae).
- Implémentation d'un contrôle d'accès basé sur les rôles avec une liste de contournement [#6211fb5](https://github.com/suitenumerique/conversations/issues/6211fb5).
- Ajout d'un système de limitation du débit (rate limiting) basé sur l'état de santé du modèle [#42a5c43](https://github.com/suitenumerique/conversations/issues/42a5c43).

### Autres changements
- Mise à jour des chaînes de traduction [#bd8c532](https://github.com/suitenumerique/conversations/issues/bd8c532), [#6f0ef43](https://github.com/suitenumerique/conversations/issues/6f0ef43).
- Correction d'un problème de redirection OIDC qui exposait le port interne [#3dc1628](https://github.com/suitenumerique/conversations/issues/3dc1628).
- Modification du statut "orange" de la santé du modèle en "jaune" [#dc6cfe3](https://github.com/suitenumerique/conversations/issues/dc6cfe3).
- Mise à jour des logos et des favicons [#ea17208](https://github.com/suitenumerique/conversations/issues/ea17208).
- Correction de liens et de cibles [#9dd4cb7](https://github.com/suitenumerique/conversations/issues/9dd4cb7).
- Mise à jour des dépendances frontend et mail [#68dd00b](https://github.com/suitenumerique/conversations/issues/68dd00b).
- Mise à jour de la version de la release à 0.0.19 [#77c41c4](https://github.com/suitenumerique/conversations/issues/77c41c4) et 0.0.18 [#94400b7](https://github.com/suitenumerique/conversations/issues/94400b7).
