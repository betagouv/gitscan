## Changelog : qualicharge (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la maintenance et la sécurité du projet. Plusieurs dépendances ont été mises à jour pour corriger des vulnérabilités et bénéficier des dernières améliorations. Une amélioration a été apportée à l'API pour supprimer la mise en cache des utilisateurs, et une correction a été effectuée sur l'indicateur OCCT pour optimiser la gestion des sessions.

### Évolutions fonctionnelles
- Suppression de la récupération des utilisateurs mis en cache dans l'API. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)
- Correction de l'indicateur OCCT pour éviter les sessions trop longues. [#cfa75f0](https://github.com/MTES-MCT/qualicharge/commit/cfa75f0)
- Publication de la version 0.33.1 de l'API. [#1b32e4b](https://github.com/MTES-MCT/qualicharge/commit/1b32e4b)

### Évolutions techniques
- Mise à jour de plusieurs dépendances Python pour corriger des failles de sécurité et bénéficier des dernières améliorations (pytest, requests, pygments, python-multipart). [#f08bb14](https://github.com/MTES-MCT/qualicharge/commit/f08bb14), [#e95f12f](https://github.com/MTES-MCT/qualicharge/commit/e95f12f), [#f347604](https://github.com/MTES-MCT/qualicharge/commit/f347604), [#669b3fb](https://github.com/MTES-MCT/qualicharge/commit/669b3fb)
- Mise à jour des images Docker utilisées par le projet (Keycloak, Metabase, Terraform, Curl, Locust).
- Mise à jour des actions Github utilisées pour le CI/CD (setup-uv, gh-action-pypi-publish, upload-artifact).

### Autres changements
- Mise à jour de la version de Django à 6.0.4 dans le dashboard. [#75a3748](https://github.com/MTES-MCT/qualicharge/commit/75a3748)
