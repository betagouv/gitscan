## Changelog : conseillers-entreprises (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la maintenance de l'application, avec des corrections de bugs, la suppression de code obsolète et des optimisations techniques. Des améliorations ont également été apportées à l'administration, notamment pour les statistiques et la gestion des utilisateurs, ainsi qu'une refonte de l'affichage des besoins de diagnostic.

### Évolutions fonctionnelles
- Amélioration de l'affichage des éléments de besoin de diagnostic en utilisant une mise en page en grille. [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483)
- Ajout d'une nouvelle statistique pour suivre les acquisitions par nouvelles entreprises. [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446)
- Ajout d'une statistique pour suivre les besoins traités en moins de cinq jours. [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446)
- Possibilité de visualiser et modifier les flags `app_info` des utilisateurs dans l'administration. [#4443](https://github.com/betagouv/conseillers-entreprises/pull/4443)
- Ajout d'un modal pour l'enquête auprès des conseillers. [#4434](https://github.com/betagouv/conseillers-entreprises/pull/4434)
- Correction : Suppression du code lié à l'ancienne API adresse. [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489)
- Correction : Suppression des jobs ayant échoué et suppression du mail associé. [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488) [#4472](https://github.com/betagouv/conseillers-entreprises/pull/4472)
- Correction : Empêcher les recherches d'entreprises avec moins de 3 caractères. [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481)
- Correction : Correction d'un bug empêchant la mise à jour du statut de diagnostic. [#4435](https://github.com/betagouv/conseillers-entreprises/pull/4435)

### Évolutions techniques
- Mise à jour de Ruby en version 4.0.3. [#4449](https://github.com/betagouv/conseillers-entreprises/pull/4449)
- Mise à jour de dépendances npm : `webpack-dev-server` (5.2.3 -> 5.2.4), `babel/plugin-transform-modules-systemjs` (7.29.0 -> 7.29.4), `fast-uri` (3.1.0 -> 3.1.2).
- Suppression de code obsolète et nettoyage général du code. [#4455](https://github.com/betagouv/conseillers-entreprises/pull/4455) [#4440](https://github.com/betagouv/conseillers-entreprises/pull/4440) [#4438](https://github.com/betagouv/conseillers-entreprises/pull/4438)
- Refactorisation de la gestion des erreurs et des logs d'authentification pour inclure l'IP et les en-têtes `X-Forwarded-For`. [#4468](https://github.com/betagouv/conseillers-entreprises/pull/4468)
- Synchronisation du schéma de la base de données. [#4468](https://github.com/betagouv/conseillers-entreprises/pull/4468)
- Amélioration de la gestion des liens vers les jobs Sidekiq dans l'interface d'administration. [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487)
- Suppression de l'utilisation de `WithSupportUser` et factorisation des appels à `support_user`. [#4437](https://github.com/betagouv/conseillers-entreprises/pull/4437)

### Autres changements
- Mise à jour de la documentation et des noms d'institutions. [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457)
- Ajout d'un workflow pour la revue des dépendances GitHub. [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492)
- Amélioration des tests et correction de problèmes de linting.
