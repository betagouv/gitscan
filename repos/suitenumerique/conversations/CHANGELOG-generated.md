## Changelog : conversations (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la gestion des projets, notamment la prise en charge des fichiers et la recherche RAG (Retrieval-Augmented Generation). Des améliorations ont également été apportées à la santé du modèle Albert, avec une surveillance proactive, et à l'expérience utilisateur, avec la possibilité de continuer à taper pendant la génération de réponses par l'IA et un mode de maintenance configurable.

### Évolutions fonctionnelles
- Ajout d'un mode de maintenance configurable pour l'application. [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed)
- Amélioration de la gestion des projets : prise en charge des fichiers pour la recherche RAG. [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Possibilité de taper pendant que le LLM génère une réponse. [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b)
- Amélioration du filtrage et de l'affichage des chats dans l'administration. [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d)
- Nouvelle interface pour les paramètres. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps. [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408)

### Évolutions techniques
- Ajout d'une surveillance de la santé du modèle Albert avec un job Cron et une intégration dans le chart Helm. [#41a591e](https://github.com/suitenumerique/conversations/commit/41a591e), [#757d75e](https://github.com/suitenumerique/conversations/commit/757d75e), [#6beeaea](https://github.com/suitenumerique/conversations/commit/6beeaea)
- Amélioration de l'instruction pour éviter les hallucinations d'URL. [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef)
- Suppression de l'endpoint listant les utilisateurs. [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878)
- Mise à jour des dépendances back et front. [#3ba131e](https://github.com/suitenumerique/conversations/commit/3ba131e)
- Désactivation des scripts d'installation yarn dans le build Docker pour plus de sécurité. [#119b814](https://github.com/suitenumerique/conversations/commit/119b814)

### Autres changements
- Mise à jour des traductions. [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101)
- Correction de bugs et améliorations diverses de l'interface utilisateur et du code.
- Bump de la version à 0.0.17. [#2b9551d](https://github.com/suitenumerique/conversations/commit/2b9551d)
- Bump de la version à 0.0.16. [#293efff](https://github.com/suitenumerique/conversations/commit/293efff)
