## Changelog : conversations (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la gestion des projets et l'expérience utilisateur. Des correctifs ont été apportés pour améliorer la fiabilité du système, notamment en surveillant la santé des modèles d'IA et en ajustant le comportement des pods. L'interface utilisateur a été enrichie avec un nouveau menu déroulant pour l'aide, un mode maintenance configurable et des améliorations pour la gestion des projets et des documents.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance configurable permettant de mettre le système hors service temporairement [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed).
- Amélioration du filtrage et de l'affichage des chats dans l'administration [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d).
- Possibilité de taper pendant que le LLM génère une réponse [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b).
- Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation) [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2).
- Nouveau menu déroulant pour accéder à l'aide, remplaçant l'ancien bouton [#aa24e0f](https://github.com/suitenumerique/conversations/commit/aa24e0f).
- Nouvelle modale de configuration des paramètres [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9).
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408).

### Évolutions techniques
- Surveillance de la santé du modèle Albert via une tâche CronJob et une intégration Helm [#757d75e](https://github.com/suitenumerique/conversations/commit/757d75e), [#41a591e](https://github.com/suitenumerique/conversations/commit/41a591e).
- Refonte de la logique de polling de la santé du modèle [#2536ffa](https://github.com/suitenumerique/conversations/commit/2536ffa).
- Correction d'un problème empêchant les pods de respecter le budget de perturbation du backend [#b1f62d6](https://github.com/suitenumerique/conversations/commit/b1f62d6).
- Suppression du point de terminaison de la liste des utilisateurs [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878).
- Amélioration de l'instruction pour éviter les hallucinations d'URL [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef).
- Restriction de l'outil d'auto-documentation aux questions méta [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5).

### Autres changements
- Mise à jour des dépendances du backend et du frontend [#3ba131e](https://github.com/suitenumerique/conversations/commit/3ba131e).
- Désactivation des scripts d'installation Yarn dans le build Docker pour renforcer la sécurité [#119b814](https://github.com/suitenumerique/conversations/commit/119b814).
- Mise à jour des chaînes de caractères traduites [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101).
- Bump de la version à 0.0.17 [#2b9551d](https://github.com/suitenumerique/conversations/commit/2b9551d).
- Bump de la version à 0.0.16 [#293efff](https://github.com/suitenumerique/conversations/commit/293efff).
