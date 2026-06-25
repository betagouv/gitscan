## Changelog : conversations (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la gestion de la santé des modèles d'IA, et l'expérience utilisateur. Des correctifs ont été apportés pour améliorer la robustesse du système, notamment en cas de problèmes avec les fournisseurs de LLM ou lors de l'indexation de documents. L'interface utilisateur a été affinée avec des améliorations visuelles et des messages d'erreur plus clairs. De nouvelles fonctionnalités comme le mode maintenance et des indicateurs de santé du modèle ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance planifiées. [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed)
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Amélioration de l'affichage des erreurs lors du téléchargement de pièces jointes (limite de taille). [#78c3190](https://github.com/suitenumerique/conversations/commit/78c3190)
- Affichage d'un message d'erreur spécifique en cas d'échec de l'analyse d'un document. [#2ffffae](https://github.com/suitenumerique/conversations/commit/2ffffae)
- Amélioration du filtrage et de l'affichage des chats dans l'administration. [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d)
- Ajout de bannières dynamiques indiquant l'état de santé des modèles d'IA. [#1d1279a](https://github.com/suitenumerique/conversations/commit/1d1279a)
- Remplacement du bouton d'aide par un menu déroulant dans l'onboarding. [#aa24e0f](https://github.com/suitenumerique/conversations/commit/aa24e0f)
- Utilisation du nom "L'Assistant" par défaut pour le produit. [#9199cfc](https://github.com/suitenumerique/conversations/commit/9199cfc)

### Évolutions techniques
- Mise à jour de la version de Python à 3.14 et des dépendances associées.
- Ajout d'un système de refroidissement (cooldown) basé sur l'état de santé du modèle pour limiter le taux de requêtes. [#42a5c43](https://github.com/suitenumerique/conversations/commit/42a5c43)
- Implémentation d'un processeur d'historique à fenêtre glissante (sliding window). [#1241a1e](https://github.com/suitenumerique/conversations/commit/1241a1e)
- Ajout d'un job Cron pour interroger l'état de santé du modèle Albert. [#41a591e](https://github.com/suitenumerique/conversations/commit/41a591e)
- Refactorisation du code pour améliorer la gestion des rôles et des accès. [#6211fb5](https://github.com/suitenumerique/conversations/commit/6211fb5)
- Correction d'un problème de redirection OIDC qui exposait le port interne. [#3dc1628](https://github.com/suitenumerique/conversations/commit/3dc1628)
- Mise à jour du chart Helm vers la version 0.0.6. [#5ae3f6e](https://github.com/suitenumerique/conversations/commit/5ae3f6e)
- Amélioration de la gestion des pods lors des déploiements Helm. [#b1f62d6](https://github.com/suitenumerique/conversations/commit/b1f62d6)
- Suppression du point de terminaison de la liste des utilisateurs. [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878)

### Autres changements
- Mise à jour des chaînes de traduction. [#6f0ef43](https://github.com/suitenumerique/conversations/commit/6f0ef43), [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532)
- Modification de la couleur d'avertissement pour l'icône de la bannière. [#b33481a](https://github.com/suitenumerique/conversations/commit/b33481a)
- Mise à jour des logos et des favicons. [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208)
- Correction du lien de contact et du lien vers la documentation. [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7)
- Mise à jour des dépendances frontend et mail. [#68dd00b](https://github.com/suitenumerique/conversations/commit/68dd00b)
- Modification du statut "orange" de la santé du modèle en "jaune". [#dc6cfe3](https://github.com/suitenumerique/conversations/commit/dc6cfe3)
- Mise à jour de la taille du modal des paramètres. [#a5e0894](https://github.com/suitenumerique/conversations/commit/a5e0894)
- Ajout de la possibilité de modifier le statut de santé du modèle dans l'administration. [#64085d4](https://github.com/suitenumerique/conversations/commit/64085d4)
- Désactivation des scripts d'installation yarn dans le build Docker. [#119b814](https://github.com/suitenumerique/conversations/commit/119b814)
