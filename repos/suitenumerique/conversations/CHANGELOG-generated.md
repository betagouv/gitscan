## Changelog : conversations (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du système, la gestion de la santé des modèles d'IA, l'expérience utilisateur et la sécurité. Des indicateurs de santé des modèles sont désormais disponibles, des corrections ont été apportées pour améliorer la stabilité et l'interface utilisateur a été affinée, notamment avec une nouvelle gestion des paramètres et des bannières d'état.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance planifiées. [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed)
- Amélioration de l'interface utilisateur pour la création de projets : passage automatique à une nouvelle conversation. [#d243b55](https://github.com/suitenumerique/conversations/commit/d243b55)
- Possibilité de taper pendant que le modèle d'IA génère une réponse, améliorant la réactivité de l'interface. [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b)
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Nouvelle interface pour les paramètres avec une taille adaptée. [#a5e0894](https://github.com/suitenumerique/conversations/commit/a5e0894)
- Ajout de bannières d'état dynamiques pour indiquer la santé des assistants IA. [#1d1279a](https://github.com/suitenumerique/conversations/commit/1d1279a)
- Amélioration du filtrage et de l'affichage des chats dans l'interface d'administration. [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d)
- Remplacement du bouton d'aide par un menu déroulant plus complet. [#aa24e0f](https://github.com/suitenumerique/conversations/commit/aa24e0f)

### Évolutions techniques
- Implémentation d'un système de surveillance de la santé des modèles Albert, avec polling régulier et affichage d'indicateurs. [#41a591e](https://github.com/suitenumerique/conversations/commit/41a591e), [#757d75e](https://github.com/suitenumerique/conversations/commit/757d75e), [#6beeaea](https://github.com/suitenumerique/conversations/commit/6beeaea)
- Ajout d'un processeur d'historique à fenêtre glissante pour optimiser la gestion des conversations. [#1241a1e](https://github.com/suitenumerique/conversations/commit/1241a1e)
- Refonte de la gestion des rôles et des accès, avec une liste de contournement pour une flexibilité accrue. [#6211fb5](https://github.com/suitenumerique/conversations/commit/6211fb5)
- Mise en place d'un refroidissement (cooldown) du taux de requêtes basé sur l'état de santé du modèle. [#42a5c43](https://github.com/suitenumerique/conversations/commit/42a5c43)
- Correction d'un problème de redirection OIDC qui exposait le port interne. [#3dc1628](https://github.com/suitenumerique/conversations/commit/3dc1628)
- Suppression de l'endpoint listant les utilisateurs. [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878)
- Amélioration de l'instruction pour éviter les hallucinations d'URL. [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef)
- Optimisation de l'indexation des collections pour améliorer les performances de recherche. [#f9a5c37](https://github.com/suitenumerique/conversations/commit/f9a5c37)

### Autres changements
- Mise à jour des traductions. [#6f0ef43](https://github.com/suitenumerique/conversations/commit/6f0ef43), [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101)
- Mise à jour des dépendances du backend et du frontend. [#3ba131e](https://github.com/suitenumerique/conversations/commit/3ba131e)
- Correction de problèmes liés à la gestion des pods Helm. [#b1f62d6](https://github.com/suitenumerique/conversations/commit/b1f62d6)
- Mise à jour de la version du chart Helm. [#5ae3f6e](https://github.com/suitenumerique/conversations/commit/5ae3f6e)
- Désactivation des scripts d'installation Yarn pour renforcer la sécurité. [#119b814](https://github.com/suitenumerique/conversations/commit/119b814)
- Amélioration de la documentation et de la configuration.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
