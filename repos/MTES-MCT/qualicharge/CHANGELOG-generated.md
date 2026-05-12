## Changelog : qualicharge (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions de qualicharge se concentrent sur l'amélioration de la granularité des données affichées, notamment au niveau des unités opérationnelles, et sur la maintenance de la sécurité et des dépendances du projet. Plusieurs mises à jour de bibliothèques et d'images Docker ont été appliquées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Extension des indicateurs de volume au niveau des unités opérationnelles. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)

### Évolutions techniques
- Suppression des requêtes API pour les utilisateurs mis en cache, améliorant potentiellement la sécurité et la cohérence des données. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)
- Mises à jour de plusieurs dépendances et images Docker (Django, Metabase, Terraform, curl, Keycloak, Locust, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Mise à jour de l'action `setup-uv` et de l'image Docker `uv` pour la gestion de l'environnement Python.
- Mise à jour des actions GitHub (upload-artifact, gh-action-pypi-publish) pour bénéficier des dernières fonctionnalités et corrections.

### Autres changements
- Mise à jour de la documentation et des dépendances de développement (pytest, pygments, python-dotenv, python-multipart).
- Corrections de sécurité mineures via des mises à jour de dépendances (python-multipart, requests).
