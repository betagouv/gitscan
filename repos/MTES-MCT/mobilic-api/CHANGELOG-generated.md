## Changelog : mobilic-api (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration des performances de l'API, notamment au niveau de la page d'accueil et de la gestion des requêtes. Des corrections ont été apportées pour assurer la fiabilité des données et des fonctionnalités existantes, ainsi que l'ajout de la possibilité de lier un contact et une entreprise à une transaction.

### Évolutions fonctionnelles
- Possibilité d'ajouter un contact à une transaction (deal) [#715](https://github.com/MTES-MCT/mobilic-api/pull/715).
- Amélioration de la vue des activités pour les administrateurs [#719](https://github.com/MTES-MCT/mobilic-api/pull/719).
- Ajout de la possibilité de supprimer un contexte (context) [#4995470](https://github.com/MTES-MCT/mobilic-api/commit/4995470).
- Amélioration du traitement des pauses longues dans le calcul des alertes réglementaires [#701](https://github.com/MTES-MCT/mobilic-api/pull/701).

### Évolutions techniques
- Optimisation des requêtes pour la page d'accueil de l'administration, améliorant significativement les performances [#713](https://github.com/MTES-MCT/mobilic-api/pull/713).
- Instrumentation des requêtes SQL pour le suivi des performances via Sentry [#706](https://github.com/MTES-MCT/mobilic-api/pull/706).
- Augmentation du nombre de workers Gunicorn et ajustement des timeouts pour améliorer la capacité de l'API à gérer les requêtes [#711](https://github.com/MTES-MCT/mobilic-api/pull/711).
- Correction d'un effet de bord qui réinitialisait les modifications d'administration via le "freeze" des missions [#706](https://github.com/MTES-MCT/mobilic-api/pull/706).
- Correction de la registration de la mutation `snooze_nb_worker_info` [#716](https://github.com/MTES-MCT/mobilic-api/pull/716).
- Simplification du code lié aux réglementations en supprimant des variables inutilisées [#701](https://github.com/MTES-MCT/mobilic-api/pull/701).

### Autres changements
- Corrections et améliorations diverses du code Brevo (synchronisation des transactions, gestion des erreurs, idempotence) [#715](https://github.com/MTES-MCT/mobilic-api/pull/715).
- Amélioration de la description du champ `dismiss_context` pour inclure un exemple de payload [#5cb296c](https://github.com/MTES-MCT/mobilic-api/commit/5cb296c).
- Corrections de tests unitaires et d'intégration pour assurer la stabilité du code.
- Corrections de petites inconsistances et erreurs mineures dans divers modules.
