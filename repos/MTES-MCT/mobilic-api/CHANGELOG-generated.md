## Changelog : mobilic-api (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de l'API, notamment au niveau du tableau de bord d'administration, et sur la correction de bugs liés à l'affichage des données réglementaires et des statistiques. Des améliorations ont également été apportées à l'observabilité de l'application avec l'ajout de métriques SQL.

### Évolutions fonctionnelles
- Correction de l'affichage des alertes réglementaires journalières/nocturnes dans le résumé mensuel [#701](https://github.com/MTES-MCT/mobilic-api/pull/701).
- Amélioration de la précision du calcul des dépassements de temps de travail avant une pause prolongée [#701](https://github.com/MTES-MCT/mobilic-api/pull/701).
- Correction de l'affichage des compteurs sur le tableau de bord d'administration pour qu'ils correspondent aux panneaux de détails correspondants [#705](https://github.com/MTES-MCT/mobilic-api/pull/705).
- Affichage d'un indicateur pour les jours avec plusieurs employeurs sur les alertes réglementaires [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Ajout d'une information indiquant si un utilisateur a des missions cette semaine sur le tableau de bord [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).
- Correction de la sémantique et du fuseau horaire des compteurs du tableau de bord d'administration suite aux retours de recette (Marie) [#703](https://github.com/MTES-MCT/mobilic-api/pull/703).

### Évolutions techniques
- Augmentation du nombre de workers Gunicorn et réduction des timeouts pour améliorer la performance de l'API [#709](https://github.com/MTES-MCT/mobilic-api/pull/709), [#711](https://github.com/MTES-MCT/mobilic-api/pull/711).
- Optimisation des requêtes du tableau de bord d'administration pour améliorer les performances [#713](https://github.com/MTES-MCT/mobilic-api/pull/713).
- Instrumentation du temps d'exécution des requêtes SQL pour une meilleure observabilité avec Sentry [#706](https://github.com/MTES-MCT/mobilic-api/pull/706).
- Configuration du nombre de workers Gunicorn via la variable d'environnement `WEB_CONCURRENCY` [#711](https://github.com/MTES-MCT/mobilic-api/pull/711).
- Suppression de code inutilisé lié à la gestion des pauses longues [#701](https://github.com/MTES-MCT/mobilic-api/pull/701).

### Autres changements
- Nettoyage et refactoring du code lié aux réglementations.
