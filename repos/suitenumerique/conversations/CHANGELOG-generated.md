## Changelog : conversations (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la gestion des erreurs et l'expérience utilisateur. Des correctifs ont été apportés pour gérer les pannes des fournisseurs de LLM, améliorer la gestion des projets et des documents, et affiner l'interface utilisateur. Des améliorations techniques ont également été apportées pour la surveillance de la santé des modèles et la gestion des accès basée sur les rôles.

### Évolutions fonctionnelles
- Correction : Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est hors service [#716a0c3](https://github.com/suitenumerique/conversations/commit/716a0c3).
- Amélioration : Possibilité de continuer à taper pendant que le LLM génère une réponse [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b).
- Amélioration : Amélioration du filtrage et de l'affichage des conversations dans l'interface d'administration [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d).
- Nouvelle fonctionnalité : Mode maintenance pour l'application [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed).
- Nouvelle fonctionnalité : Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation) [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2).
- Nouvelle fonctionnalité : Bannière d'état configurable avec une visibilité limitée dans le temps [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408).
- Amélioration : Le modal de projet respecte désormais l'indicateur de fonctionnalité d'upload de documents [#e4f1d94](https://github.com/suitenumerique/conversations/commit/e4f1d94).
- Amélioration : Passage automatique à une nouvelle conversation lors de la création d'un projet [#d243b55](https://github.com/suitenumerique/conversations/commit/d243b55).
- Amélioration : Le bouton d'aide a été remplacé par un menu déroulant [#aa24e0f](https://github.com/suitenumerique/conversations/commit/aa24e0f).
- Amélioration : Utilisation de la langue du navigateur pour l'interface utilisateur par défaut au premier chargement [#cf06b5b](https://github.com/suitenumerique/conversations/commit/cf06b5b).

### Évolutions techniques
- Sécurité : Ajout d'un filtrage d'accès basé sur les rôles avec une liste de contournement [#6211fb5](https://github.com/suitenumerique/conversations/commit/6211fb5).
- Infrastructure : Ajout d'une tâche Cron pour surveiller l'état de santé du modèle Albert [#757d75e](https://github.com/suitenumerique/conversations/commit/757d75e, #41a591e](https://github.com/suitenumerique/conversations/commit/41a591e).
- Infrastructure : Mise à jour du chart Helm vers la version v0.0.6 [#5ae3f6e](https://github.com/suitenumerique/conversations/commit/5ae3f6e).
- Infrastructure : Amélioration de la configuration du CronJob model-health [#6beeaea](https://github.com/suitenumerique/conversations/commit/6beeaea).
- Performance : Désindexation des collections inactives et réindexation lors d'une conversation [#f9a5c37](https://github.com/suitenumerique/conversations/commit/f9a5c37).
- Sécurité : Désactivation des scripts d'installation yarn dans le build Docker [#119b814](https://github.com/suitenumerique/conversations/commit/119b814).
- Correction : Empêcher les pods de tâches Helm de correspondre au budget de perturbation du backend [#b1f62d6](https://github.com/suitenumerique/conversations/commit/b1f62d6).

### Autres changements
- Documentation : Mise à jour des chaînes de traduction [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101).
- Maintenance : L'outil d'auto-documentation est désormais limité aux questions méta [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5).
- Suppression : Suppression du point de terminaison de la liste des utilisateurs [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878).
