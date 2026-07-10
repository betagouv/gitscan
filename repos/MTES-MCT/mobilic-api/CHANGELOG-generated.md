## Changelog : mobilic-api (30 derniers jours, au 09 juillet 2026)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la gestion des webinaires, l'intégration avec Brevo (outil de marketing), l'expérience administrateur et l'observabilité de l'application. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de lier un contact et une entreprise à un deal. [#715](https://github.com/MTES-MCT/mobilic-api/pull/715)
- Amélioration de la vue des activités pour les administrateurs, avec la possibilité de supprimer un contexte. [#719](https://github.com/MTES-MCT/mobilic-api/pull/719)
- Ajout de la gestion des jours travaillés modifiés (ajout/édition). [#707](https://github.com/MTES-MCT/mobilic-api/pull/707)
- Intégration de la synchronisation des deals existants avec Brevo, avec une option de test (dry-run). [#725](https://github.com/MTES-MCT/mobilic-api/pull/725)
- Possibilité de supprimer un contexte via l'API. [#720](https://github.com/MTES-MCT/mobilic-api/pull/720)

### Évolutions techniques
- Optimisation de la récupération des webinaires en utilisant un cache Redis et en gérant les limites de débit. [#725](https://github.com/MTES-MCT/mobilic-api/pull/725)
- Ajout d'indicateurs SQL pour l'observabilité et le suivi des performances des requêtes dans Sentry. [#706](https://github.com/MTES-MCT/mobilic-api/pull/706)
- Correction d'un effet secondaire involontaire qui réinitialisait les modifications administratives des missions. [#716](https://github.com/MTES-MCT/mobilic-api/pull/716) et [#718](https://github.com/MTES-MCT/mobilic-api/pull/718)
- Correction de bugs et améliorations de la robustesse de l'intégration Brevo, notamment la gestion des erreurs et l'idempotence. [#727](https://github.com/MTES-MCT/mobilic-api/pull/727)
- Correction de tests et suppression de code mort dans divers modules.

### Autres changements
- Ajout d'exemples de payload dans la description d'un champ pour améliorer la documentation.
- Amélioration de la description du champ `dismiss_context`.
- Correction de la mutation `register_snooze_nb_worker_info`.
- Correction de tests pour assurer la non-régression des données d'activités.
- Amélioration de la complexité du code (Sonarcloud) pour l'intégration Brevo et le module `control`.
