## Changelog : conseillers-entreprises (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité du code, la correction de bugs et l'ajout de nouvelles statistiques pour le suivi de l'activité. Des améliorations ont également été apportées à l'interface d'administration pour faciliter la gestion des données et des utilisateurs. Enfin, le nom du service a été mis à jour pour refléter son évolution.

### Évolutions fonctionnelles
- Possibilité de filtrer les experts en excluant certains codes INSEE [#4452](https://github.com/betagouv/conseillers-entreprises/pull/4452).
- Ajout de nouvelles statistiques :
  - Nombre d'entreprises aidées en moins de 5 jours [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446).
  - Acquisitions par nouvelles entreprises [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446).
- Possibilité de visualiser et modifier les flags `app_info` des utilisateurs dans l'interface d'administration [#4443](https://github.com/betagouv/conseillers-entreprises/pull/4443).
- Amélioration de l'export CSV des réponses aux besoins dans l'interface d'administration [#4459](https://github.com/betagouv/conseillers-entreprises/pull/4459).
- Correction d'un bug empêchant la recherche d'entreprises avec moins de 3 caractères [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481).
- Correction de l'affichage des besoins de diagnostic [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483).

### Évolutions techniques
- Mise à jour de Ruby en version 4.0.3 [#4449](https://github.com/betagouv/conseillers-entreprises/pull/4449).
- Suppression du code lié à l'ancienne API adresse [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489).
- Suppression des jobs qui échouent et de l'email associé [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488).
- Amélioration de la gestion des logs d'authentification : ajout de l'IP et des headers X-Forwarded-For [#4464](https://github.com/betagouv/conseillers-entreprises/pull/4464).
- Refactorisation du code pour supprimer des méthodes inutilisées [#4455](https://github.com/betagouv/conseillers-entreprises/pull/4455).
- Synchronisation du schéma de la base de données [#4468](https://github.com/betagouv/conseillers-entreprises/pull/4468).
- Mise à jour des dépendances npm et yarn (webpack-dev-server, babel/plugin-transform-modules-systemjs, fast-uri) [#4462](https://github.com/betagouv/conseillers-entreprises/pull/4462), [#4472](https://github.com/betagouv/conseillers-entreprises/pull/4472).
- Ajout d'une revue de dépendances GitHub Actions [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492).

### Autres changements
- Mise à jour de la documentation et des noms des institutions pour refléter l'évolution du service (CE -> SPCE) [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457).
- Suppression du sujet "support" [#4438](https://github.com/betagouv/conseillers-entreprises/pull/4438).
- Correction de références obsolètes (Baleen remplacé par Ubika) [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457).
- Amélioration de la lisibilité du code et correction de problèmes de style avec Rubocop.
- Lien direct vers Sidekiq depuis le menu Jobs dans l'interface d'administration [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487).
