## Changelog : idp-status-monitoring (30 derniers jours, au 4 juillet 2026)

### Résumé
Ce mois-ci, les mises à jour se sont principalement concentrées sur la maintenance et la correction de bugs. Une correction importante a été apportée au producteur pour éviter des problèmes de concurrence lors de l'envoi de réponses. De nombreuses dépendances ont également été mises à jour vers leurs dernières versions pour améliorer la sécurité et la stabilité.

### Évolutions fonctionnelles
- Correction d'un bug dans le producteur qui causait un "stealing" de réponses entre différentes instances concurrentes [#123](https://github.com/proconnect-gouv/idp-status-monitoring/issues/123).

### Évolutions techniques
- Mise à jour de plusieurs dépendances :
    - `docker/build-push-action` (7.2.0 -> 7.3.0)
    - `docker/login-action` (4.2.0 -> 4.4.0)
    - `docker/setup-compose-action` (2.2.0 -> 2.3.0)
    - `docker/setup-buildx-action` (4.1.0 -> 4.2.0)
    - `docker/metadata-action` (6.1.0 -> 6.2.0)
    - `prettier` (3.8.4 -> 3.9.4)
    - `uuid` (14.0.0 -> 14.0.1)
    - `hono` (4.12.23 -> 4.12.27)
    - `actions/checkout` (6.0.2 -> 6.0.3)

### Autres changements
- Aucune information disponible.
