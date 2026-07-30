## Changelog : mobilic-api (30 derniers jours, au 27 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la gestion des signalements (contestation) et des détachements d'employés, avec l'ajout de nouvelles fonctionnalités pour initier des demandes de détachement et contester des éléments. Des corrections ont également été apportées pour améliorer la robustesse et la performance de l'API, notamment en lien avec les webinaires Livestorm et l'export de données.

### Évolutions fonctionnelles
- Ajout de la possibilité pour un employé de formuler une contestation. [#722](https://github.com/MTES-MCT/mobilic-api/pulls/722)
- Implémentation de la demande de détachement d'un employé avec envoi d'emails associés. [#731](https://github.com/MTES-MCT/mobilic-api/pulls/731)
- Amélioration de l'affichage des motifs d'activité dans l'historique des missions et dans les exports PDF. [#742](https://github.com/MTES-MCT/mobilic-api/pulls/742), [#738](https://github.com/MTES-MCT/mobilic-api/pulls/738)
- Ajout de la possibilité de tracer les actions de validation lors de la création de missions en mode impersonation. [#732](https://github.com/MTES-MCT/mobilic-api/pulls/732)
- Amélioration du contenu des emails liés aux détachements d'employés. [#743](https://github.com/MTES-MCT/mobilic-api/pulls/743), [#744](https://github.com/MTES-MCT/mobilic-api/pulls/744)
- Ajout d'une colonne et de totaux pour le temps de pause dans l'export des journées de travail des employés. [#736](https://github.com/MTES-MCT/mobilic-api/pulls/736)

### Évolutions techniques
- Optimisation de la récupération des webinaires Livestorm avec mise en cache Redis et gestion des limites de débit. [#725](https://github.com/MTES-MCT/mobilic-api/pulls/725)
- Correction d'un problème de performance lié aux requêtes sur les validations en attente sur le dashboard.
- Amélioration de la gestion des erreurs Sentry pour réduire le bruit et faciliter le diagnostic. [#724](https://github.com/MTES-MCT/mobilic-api/pulls/724)
- Refactorisation du code lié aux activités pour corriger des anomalies détectées par SonarCloud. [#715](https://github.com/MTES-MCT/mobilic-api/pulls/715)
- Fusion des branches de migration de la base de données pour les fonctionnalités de détachement, de contestation et d'impersonation.
- Correction d'un problème de synchronisation de l'adresse email lors de la rédemption d'une invitation d'emploi. [#739](https://github.com/MTES-MCT/mobilic-api/pulls/739)

### Autres changements
- Correction de plusieurs bugs mineurs et améliorations de la qualité du code.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Mise à jour de la documentation.
- Correction de problèmes de timeout pour les appels à l'API Livestorm. [#728](https://github.com/MTES-MCT/mobilic-api/pulls/728), [#730](https://github.com/MTES-MCT/mobilic-api/pulls/730)
