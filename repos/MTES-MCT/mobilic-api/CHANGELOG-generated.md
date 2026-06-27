## Changelog : mobilic-api (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances de l'API, notamment au niveau du tableau de bord administrateur et de la gestion des requêtes simultanées. Des corrections de bugs ont également été apportées pour améliorer la précision des données et la gestion des alertes. Enfin, de nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des contextes et des invitations.

### Évolutions fonctionnelles
- Amélioration de la vue d'activité pour les administrateurs, permettant un suivi plus précis des actions. [#719](https://github.com/MTES-MCT/mobilic-api/pull/719)
- Possibilité de supprimer un contexte via l'API.
- Correction de l'affichage du nombre d'invitations sur le tableau de bord administrateur. [#705](https://github.com/MTES-MCT/mobilic-api/pull/705)
- Correction d'un bug lié à la gestion des pauses longues et des dépassements de temps de travail. [#701](https://github.com/MTES-MCT/mobilic-api/pull/701)
- Ajout de la distinction entre les alertes jour et nuit dans le résumé mensuel des réglementations. [#701](https://github.com/MTES-MCT/mobilic-api/pull/701)

### Évolutions techniques
- Optimisation des requêtes SQL pour le tableau de bord administrateur afin d'améliorer les performances. [#713](https://github.com/MTES-MCT/mobilic-api/pull/713)
- Instrumentation des temps d'exécution des requêtes SQL pour une meilleure surveillance avec Sentry. [#706](https://github.com/MTES-MCT/mobilic-api/pull/706)
- Augmentation du nombre de workers Gunicorn et ajustement des timeouts pour améliorer la capacité de l'API à gérer les requêtes simultanées. [#711](https://github.com/MTES-MCT/mobilic-api/pull/711), [#709](https://github.com/MTES-MCT/mobilic-api/pull/709)
- Refactoring pour piloter le nombre de workers Gunicorn via la variable d'environnement `WEB_CONCURRENCY`. [#712](https://github.com/MTES-MCT/mobilic-api/pull/712)
- Correction d'un effet de bord qui réinitialisait les modifications d'administration via le "freeze". [#718](https://github.com/MTES-MCT/mobilic-api/pull/718)
- Correction de l'enregistrement de l'information sur le nombre de workers pour le snooze. [#716](https://github.com/MTES-MCT/mobilic-api/pull/716)

### Autres changements
- Ajout d'un exemple de payload dans la description du champ `dismiss_context`.
- Suppression de variables inutilisées dans le code de gestion des réglementations.
- Amélioration de la documentation et du code pour une meilleure maintenabilité.
