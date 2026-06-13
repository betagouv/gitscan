## Changelog : b3desk (30 derniers jours, au 2026-06-12)

### Résumé
Les dernières mises à jour de b3desk se concentrent sur l'amélioration de la gestion des réunions et des utilisateurs, notamment en introduisant la possibilité de déléguer la gestion de réunions et en limitant les actions de l'owner sur ses propres réunions. Des améliorations techniques ont également été apportées pour automatiser la publication des releases et mapper les informations utilisateur provenant de l'authentification OIDC.

### Évolutions fonctionnelles
- Possibilité de déléguer la gestion de réunions via l'API. [#357](https://github.com/numerique-gouv/b3desk/issues/357)
- Limitation du nombre maximal de délégués à 15 par réunion. [#364](https://github.com/numerique-gouv/b3desk/issues/364)
- L'owner d'une réunion ne peut plus s'ajouter lui-même comme délégué. [#364](https://github.com/numerique-gouv/b3desk/issues/364)
- Amélioration de la configuration de l'environnement de développement : redirection automatique vers `b3desk.localhost`.

### Évolutions techniques
- Intégration du mapping des claims OIDC pour une meilleure gestion des informations utilisateur. [#360](https://github.com/numerique-gouv/b3desk/issues/360)
- Automatisation de la publication des releases GitHub lors de la création de tags.
- Mise à jour de la version de développement à 1.6.4dev.
- Amélioration des vérifications de linting.

### Autres changements
- Documentation : ajout d'un exemple de personnalisation du scope. [#355](https://github.com/numerique-gouv/b3desk/issues/355)
