## Changelog : qualicharge (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la granularité des indicateurs de performance dans Prefect, la suppression de données utilisateur mises en cache dans l'API, et la mise à jour de nombreuses dépendances pour bénéficier des dernières corrections de sécurité et améliorations.

### Évolutions fonctionnelles
- Amélioration des indicateurs Prefect : Extension des indicateurs de volume au niveau des Operational Units. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)
- Suppression des requêtes API utilisateur mises en cache : Suppression des requêtes API pour les utilisateurs mis en cache afin d'assurer la cohérence des données. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)

### Évolutions techniques
- Mises à jour de dépendances : De nombreuses dépendances ont été mises à jour vers leurs dernières versions stables, incluant :
    - `python-dotenv` vers 1.2.2
    - `pytest` vers 9.0.3
    - `pygments` vers 2.20.0
    - `python-multipart` vers 0.0.26 (correction de sécurité)
    - `requests` vers 2.33.0 (correction de sécurité)
    - `Django` vers 6.0.4 (dashboard)
- Mises à jour d'images Docker : Plusieurs images Docker ont été mises à jour, notamment `astral-sh/uv`, `hashicorp/terraform`, `metabase/metabase`, `quay.io/keycloak/keycloak`, `curlimages/curl`, `locustio/locust`.
- Mises à jour d'actions GitHub : Les actions GitHub `astral-sh/setup-uv`, `pypa/gh-action-pypi-publish`, `actions/upload-artifact` ont été mises à jour.

### Autres changements
- Suppression des sessions longues de l'indicateur OCCT dans Prefect. [#cfa75f0](https://github.com/MTES-MCT/qualicharge/commit/cfa75f0)
