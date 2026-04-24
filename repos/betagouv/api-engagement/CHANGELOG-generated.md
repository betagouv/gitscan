## Changelog : api-engagement (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de performance, de sécurité et de fonctionnalités. Des optimisations ont été apportées à la recherche d'organisations, à la gestion des missions SDIS, et à la limitation du taux de requêtes. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant les sauvegardes de la base de données et la gestion des erreurs. L'accessibilité de l'application a été améliorée, ainsi que la sécurité globale du projet.

### Évolutions fonctionnelles
- Ajout du support des missions "opération de réserve" ([#901](https://github.com/betagouv/api-engagement/issues/901)).
- Amélioration du formulaire d'édition du widget.
- Amélioration de la recherche d'organisations grâce à l'utilisation de `tsvector` pour une recherche plus rapide et pertinente ([#950](https://github.com/betagouv/api-engagement/issues/950)).
- Ajout de limiteurs de débit (rate limiting) pour les requêtes des éditeurs et par adresse IP ([#932](https://github.com/betagouv/api-engagement/issues/932)).
- Scripts pour la gestion des missions SDIS ont été ajoutés ([#942](https://github.com/betagouv/api-engagement/issues/942)).
- Amélioration de la liste des utilisateurs et des formulaires utilisateurs dans l'application.
- Amélioration du sélecteur de date pour une meilleure accessibilité.

### Évolutions techniques
- Mise en place de sauvegardes régulières de la base de données RDB ([#955](https://github.com/betagouv/api-engagement/issues/955), [#957](https://github.com/betagouv/api-engagement/issues/957)).
- Refactorisation de la suppression des champs dénormalisés de `stat_event` pour optimiser la base de données ([#866](https://github.com/betagouv/api-engagement/issues/866), [#921](https://github.com/betagouv/api-engagement/issues/921)).
- Suppression des champs d'organisation hérités dans l'API pour simplifier le schéma et améliorer la maintenance ([#917](https://github.com/betagouv/api-engagement/issues/917), [#918](https://github.com/betagouv/api-engagement/issues/918)).
- Amélioration de la gestion des erreurs et des exceptions, notamment en cas de payload trop volumineux.
- Mise à jour de plusieurs dépendances (ESLint, Vite, etc.).
- Amélioration des règles CLAUDE pour une meilleure analyse du code.
- Ajout d'une politique de sécurité.
- Amélioration de la documentation OpenAPI.

### Autres changements
- Amélioration de l'accessibilité de l'application (RGAA 10.11).
- Corrections de scripts CI/CD pour le déploiement en sandbox.
- Suppression de la colonne `organization_client_id` dans les statistiques.
- Correction de problèmes liés au proxy Metabase.
- Correction d'un bug empêchant la déconnexion des utilisateurs en cas d'erreur réseau.
- Suppression de la relation `mission.organization_client_id` dans l'API.
- Amélioration des tests et de la couverture de code.
