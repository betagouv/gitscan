## Changelog : mobilic-api (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la gestion des détachements des employés, de la gestion des litiges et de la robustesse de l'application. Des corrections ont également été apportées pour optimiser les performances et la stabilité, notamment concernant l'intégration avec Livestorm et la gestion des webinars. Des améliorations de l'observabilité ont été ajoutées pour faciliter le diagnostic des problèmes.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de demande de détachement d'employé avec envoi d'emails associés. [#743](https://github.com/MTES-MCT/mobilic-api/issues/743)
- Implémentation de la gestion des contestations initiées par les employés, incluant l'historique des actions. [#722](https://github.com/MTES-MCT/mobilic-api/issues/722)
- Possibilité de créer des missions en mode impersonation et de suivre les actions associées dans les exports. [#732](https://github.com/MTES-MCT/mobilic-api/issues/732)
- Amélioration de la vue d'activité pour les administrateurs. [#719](https://github.com/MTES-MCT/mobilic-api/issues/719)
- Ajout de la possibilité d'ajouter un contact aux deals. [#715](https://github.com/MTES-MCT/mobilic-api/issues/715)
- Contrôle amélioré de l'ajout et de la modification des jours de travail. [#707](https://github.com/MTES-MCT/mobilic-api/issues/707)
- Ajout de la colonne et des totaux de temps de pause dans l'export des jours de travail des employés. [#736](https://github.com/MTES-MCT/mobilic-api/issues/736)

### Évolutions techniques
- Optimisation de la récupération des webinars pour éviter les limitations de débit de l'API Livestorm, avec mise en cache Redis. [#725](https://github.com/MTES-MCT/mobilic-api/issues/725)
- Correction d'un effet secondaire lors de la validation des missions qui empêchait le gel. [#718](https://github.com/MTES-MCT/mobilic-api/issues/718)
- Amélioration de la gestion des erreurs Sentry pour réduire le bruit et faciliter le diagnostic. [#724](https://github.com/MTES-MCT/mobilic-api/issues/724)
- Instrumentation SQL pour mesurer le temps d'exécution des requêtes et améliorer l'observabilité. [#706](https://github.com/MTES-MCT/mobilic-api/issues/706)
- Refactoring du code lié à l'historique des litiges et aux exports pour corriger des problèmes de qualité identifiés par SonarCloud. [#715](https://github.com/MTES-MCT/mobilic-api/issues/715)
- Correction de problèmes d'idempotence, de migration, de typage et de gestion des erreurs dans l'intégration Brevo.
- Correction de bugs et amélioration de la robustesse de l'intégration Livestorm (gestion des timeouts, etc.). [#728](https://github.com/MTES-MCT/mobilic-api/issues/728), [#730](https://github.com/MTES-MCT/mobilic-api/issues/730)

### Autres changements
- Mise à jour des migrations de la base de données pour les fonctionnalités de détachement, de litige et d'impersonation.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections.
- Amélioration de la documentation et des exemples de payloads GraphQL.
- Correction de divers problèmes de code identifiés par SonarCloud.
