## Changelog : qualicharge (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la granularité des indicateurs de performance dans l'interface Prefect, ainsi que sur la suppression d'une fonctionnalité d'API obsolète. De nombreuses mises à jour de dépendances ont également été appliquées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles

- Extension des indicateurs de volume aux niveaux d'OperationalUnit dans Prefect. [#1527322](https://github.com/MTES-MCT/qualicharge/pull/1527322)
- Suppression des requêtes API pour les utilisateurs mis en cache. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)

### Évolutions techniques

- Mises à jour régulières des images Docker pour Metabase, Terraform, Curl, Locust et Keycloak afin de bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Mises à jour des actions GitHub (setup-uv, gh-action-pypi-publish, upload-artifact) pour bénéficier des dernières fonctionnalités et corrections.
- Mises à jour de plusieurs dépendances Python (pytest, pygments, python-dotenv, python-multipart, requests) pour corriger des vulnérabilités de sécurité et améliorer la stabilité.
- Mise à jour de l'outil de gestion d'environnement UV.

### Autres changements

- Aucune modification significative de la documentation ou de la configuration n'a été apportée durant cette période.
