## Changelog : data_pass (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de fonctionnalités pour la gestion des autorisations et des utilisateurs, ainsi que des corrections de performance et de bugs. Des améliorations significatives ont également été apportées à la documentation et à l'infrastructure du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de bannir un utilisateur ([#1508](https://github.com/etalab/data_pass/pull/1508)).
- Amélioration de l'interface pour la gestion des rôles et des autorisations, notamment avec l'ajout de scopes pour le formulaire Solis ([#1502](https://github.com/etalab/data_pass/pull/1502), [#1507](https://github.com/etalab/data_pass/pull/1507)).
- Ajout de la possibilité de retirer entièrement des droits à un utilisateur ([#1494](https://github.com/etalab/data_pass/pull/1494)).
- Amélioration de l'affichage du statut des demandes (revendiqué/non revendiqué) ([#1539](https://github.com/etalab/data_pass/pull/1539)).
- Ajout d'une bannière de maintenance ProConnect visible sur toutes les pages.
- Amélioration de l'affichage des erreurs de vérification d'email lors de la soumission.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API v1 ([#1523](https://github.com/etalab/data_pass/pull/1523)).
- Mise à jour des libellés concernant la tarification Eaje ([#1497](https://github.com/etalab/data_pass/pull/1497)).
- Ajout d'une page de documentation pour les webhooks ([#1500](https://github.com/etalab/data_pass/pull/1500)).
- Ajout d'informations sur les services CISIRH ([#1546](https://github.com/etalab/data_pass/pull/1546), [#1545](https://github.com/etalab/data_pass/pull/1545)).

### Évolutions techniques
- Refactorisation de la gestion des diffs des changelogs.
- Optimisation des requêtes N+1 sur le dashboard demandeur ([#1499](https://github.com/etalab/data_pass/pull/1499)).
- Amélioration de la configuration des tests CI/CD pour une exécution plus rapide et plus fiable ([#1503](https://github.com/etalab/data_pass/pull/1503)).
- Mise à jour des dépendances (Rails Pulse, Rubocop, Zlib, etc.).
- Ajout d'un service MarkdownRenderer.
- Amélioration de la gestion des erreurs lors de la soumission de demandes avec Turbo Streams.
- Introduction d'un système de gestion des rôles plus centralisé.
- Ajout d'événements pour le suivi des actions des administrateurs.
- Utilisation d'ID numériques pour les routes d'habilitation.
- Migration des tables Rails Pulse et LazyLoad Faker.
- Simplification de l'affichage des erreurs de connexion.

### Autres changements
- Réorganisation de la documentation en sous-dossiers (technique, métier, API particulier) ([#1549](https://github.com/etalab/data_pass/pull/1549)).
- Ajout de la documentation pour le système HabilitationType dynamique ([#1548](https://github.com/etalab/data_pass/pull/1548)).
- Amélioration de la documentation des webhooks.
- Ajout de guidelines pour l'utilisation de CLAUDE pour la rédaction des commits.
- Corrections de typos et améliorations de la qualité du code.
- Mise à jour des scopes OAuth2.
- Ajout de commentaires et de documentation pour améliorer la maintenabilité du code.
