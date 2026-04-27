## Changelog : qualicharge (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données disponibles dans Prefect, notamment au niveau des unités opérationnelles, et sur la suppression de données obsolètes pour optimiser les performances. Des mises à jour de sécurité et des corrections de dépendances ont également été appliquées pour assurer la stabilité et la sécurité de la plateforme. Enfin, l'API a été simplifiée en supprimant la gestion des utilisateurs mis en cache.

### Évolutions fonctionnelles

*   Suppression de la gestion des utilisateurs mis en cache dans l'API, simplifiant ainsi les requêtes et améliorant potentiellement les performances. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)
*   Extension des indicateurs de volume Prefect au niveau des unités opérationnelles, offrant une granularité plus fine pour l'analyse des données. [#1527322](https://github.com/MTES-MCT/qualicharge/commit/1527322)

### Évolutions techniques

*   Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et bénéficier des dernières améliorations :
    *   `python-dotenv` vers la version 1.2.2 [#3aff939](https://github.com/MTES-MCT/qualicharge/commit/3aff939)
    *   `python-multipart` vers la version 0.0.26 (correction de sécurité) [#f347604](https://github.com/MTES-MCT/qualicharge/commit/f347604)
    *   `pygments` vers la version 2.20.0 [#f08bb14](https://github.com/MTES-MCT/qualicharge/commit/f08bb14)
    *   `pytest` vers la version 9.0.3 [#e95f12f](https://github.com/MTES-MCT/qualicharge/commit/e95f12f)
    *   `requests` vers la version 2.33.0 [#669b3fb](https://github.com/MTES-MCT/qualicharge/commit/669b3fb)
*   Mise à jour des images Docker :
    *   `hashicorp/terraform` vers v1.14.9 [#d6abc19](https://github.com/MTES-MCT/qualicharge/commit/d6abc19) et v1.14.8 [#d7f883b](https://github.com/MTES-MCT/qualicharge/commit/d7f883b)
    *   `metabase/metabase` vers v0.60.2 [#43b9daa](https://github.com/MTES-MCT/qualicharge/commit/43b9daa) et v0.59.6 [#62e2a04](https://github.com/MTES-MCT/qualicharge/commit/62e2a04)
    *   `quay.io/keycloak/keycloak` vers v26.6 [#64c2a95](https://github.com/MTES-MCT/qualicharge/commit/64c2a95)
    *   `curlimages/curl` vers v8.19.0 [#4b12ee0](https://github.com/MTES-MCT/qualicharge/commit/4b12ee0)
    *   `locustio/locust` vers v2.43.4 [#f01229d](https://github.com/MTES-MCT/qualicharge/commit/f01229d)
    *   `ghcr.io/astral-sh/uv` vers v0.11.7 [#4163a07](https://github.com/MTES-MCT/qualicharge/commit/4163a07) et v0.11.6 [#9ba1358](https://github.com/MTES-MCT/qualicharge/commit/9ba1358)
*   Mise à jour des actions GitHub :
    *   `astral-sh/setup-uv` vers v8.1.0 [#496d24a](https://github.com/MTES-MCT/qualicharge/commit/496d24a) et v8 [#2ea055e](https://github.com/MTES-MCT/qualicharge/commit/2ea055e)
    *   `zizmorcore/zizmor-action` vers v0.5.3 [#0439d7e](https://github.com/MTES-MCT/qualicharge/commit/0439d7e)
    *   `pypa/gh-action-pypi-publish` vers v1.14.0 [#826e359](https://github.com/MTES-MCT/qualicharge/commit/826e359)
    *   `actions/upload-artifact` vers v7.0.1 [#d96b787](https://github.com/MTES-MCT/qualicharge/commit/d96b787)
*   Mise à jour de Django vers la version 6.0.4 [#75a3748](https://github.com/MTES-MCT/qualicharge/commit/75a3748)

### Autres changements

*   Suppression des sessions longues de l'indicateur OCCT Prefect pour améliorer les performances. [#cfa75f0](https://github.com/MTES-MCT/qualicharge/commit/cfa75f0)
