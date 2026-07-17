## Changelog : mobilic-api (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la performance, la correction de bugs et l'ajout de fonctionnalités liées à la gestion des webinaires et des activités. Des optimisations ont été apportées pour réduire la charge sur l'infrastructure et améliorer la réactivité de l'application, notamment en utilisant la mise en cache Redis.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter un contact aux deals. [#715](https://github.com/MTES-MCT/mobilic-api/pull/715)
- Amélioration de la vue des activités pour les administrateurs, avec une meilleure présentation des informations. [#719](https://github.com/MTES-MCT/mobilic-api/pull/719)
- Ajout de contrôles pour l'ajout et la modification des jours travaillés. [#707](https://github.com/MTES-MCT/mobilic-api/pull/707)
- Possibilité de supprimer un contexte. [#720](https://github.com/MTES-MCT/mobilic-api/pull/720)

### Évolutions techniques
- Optimisation de la récupération des webinaires avec mise en cache Redis et gestion des limites de débit de l'API Livestorm. [#725](https://github.com/MTES-MCT/mobilic-api/pull/725), [#726](https://github.com/MTES-MCT/mobilic-api/pull/726), [#728](https://github.com/MTES-MCT/mobilic-api/pull/728), [#730](https://github.com/MTES-MCT/mobilic-api/pull/730)
- Amélioration de la performance du dashboard en limitant les validations en attente aux missions récentes.
- Correction d'un problème de requêtes SQL complexes dans le dashboard.
- Ajout d'indicateurs SQL pour l'observabilité et le suivi des performances des requêtes dans Sentry. [#706](https://github.com/MTES-MCT/mobilic-api/pull/706)
- Refactorisation du code lié aux webinaires pour améliorer la maintenabilité et la performance.
- Correction de bugs liés à la validation des missions et à la gestion des informations des workers. [#716](https://github.com/MTES-MCT/mobilic-api/pull/716), [#718](https://github.com/MTES-MCT/mobilic-api/pull/718)
- Suppression de code mort et correction de problèmes de complexité dans le code Brevo.

### Autres changements
- Filtrage des erreurs répétitives dans Sentry pour réduire le bruit. [#724](https://github.com/MTES-MCT/mobilic-api/pull/724)
- Amélioration des tests unitaires et d'intégration pour assurer la qualité du code.
- Corrections de tests pour assurer la non-régression des fonctionnalités.
- Synchronisation des deals existants avec Brevo et ajout d'une option de test.
- Mise à jour de la documentation et correction de descriptions.
