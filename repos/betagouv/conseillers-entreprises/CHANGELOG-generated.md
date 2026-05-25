## Changelog : conseillers-entreprises (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la robustesse de l'application, avec des corrections de bugs et des optimisations des logs. Des améliorations ont également été apportées à l'interface d'administration, notamment pour les statistiques et la gestion des utilisateurs, ainsi qu'une nouvelle fonctionnalité pour l'enquête auprès des conseillers. Enfin, des mises à jour de dépendances ont été effectuées pour assurer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant d'afficher un questionnaire aux utilisateurs via une modale et un nouvel élément de navigation. [#4434](https://github.com/betagouv/conseillers-entreprises/pull/4434)
- Amélioration de la gestion des statistiques avec l'ajout de nouvelles statistiques sur les acquisitions et les temps de réponse. [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446)
- Possibilité de visualiser et modifier les flags `app_info` des utilisateurs dans l'interface d'administration. [#4443](https://github.com/betagouv/conseillers-entreprises/pull/4443)
- Amélioration de l'export CSV des satisfactions des entreprises dans l'interface d'administration. [#4459](https://github.com/betagouv/conseillers-entreprises/pull/4459)
- Correction d'un bug empêchant la progression des étapes de diagnostic. [#4445](https://github.com/betagouv/conseillers-entreprises/pull/4445)

### Évolutions techniques
- Mise à jour de Ruby en version 4.0.3. [#4449](https://github.com/betagouv/conseillers-entreprises/pull/4449)
- Amélioration de la gestion des logs d'authentification, incluant l'IP, le port et les en-têtes `X-Forwarded-For`. [#4464](https://github.com/betagouv/conseillers-entreprises/pull/4464)
- Correction de la gestion des emails dans les logs d'authentification. [#4479](https://github.com/betagouv/conseillers-entreprises/pull/4479)
- Refactorisation du code pour supprimer des méthodes inutilisées dans `MatchFilter`. [#4455](https://github.com/betagouv/conseillers-entreprises/pull/4455)
- Suppression de code obsolète lié au support utilisateur et à la gestion des bandeaux d'information. [#4438](https://github.com/betagouv/conseillers-entreprises/pull/4438) et [#4440](https://github.com/betagouv/conseillers-entreprises/pull/4440)
- Synchronisation du schéma de la base de données. [#4468](https://github.com/betagouv/conseillers-entreprises/pull/4468)
- Limitation de la longueur des requêtes de recherche d'entreprises à 3 caractères pour améliorer la performance. [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481)
- Amélioration de la gestion des erreurs liées à la recherche d'entreprises. [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481)

### Autres changements
- Mise à jour de plusieurs dépendances (webpack-dev-server, babel, fast-uri, devise, mjml, erb).
- Correction de noms d'institutions et d'articles dans la documentation. [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457)
- Ajout de tests unitaires et de specs pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la configuration et du code pour une meilleure lisibilité et maintenabilité.
- Correction de problèmes mineurs d'interface utilisateur et de traduction.
