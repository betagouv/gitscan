## Changelog : qualicharge (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données et de l'expérience utilisateur, notamment au niveau des indicateurs de performance des bornes de recharge. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles

- Suppression des requêtes API pour l'utilisateur mis en cache, améliorant la sécurité et la cohérence des données. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)
- Extension des indicateurs de volume aux niveaux d'Unités Opérationnelles dans Prefect, offrant une granularité accrue dans l'analyse des données. [#1527322](https://github.com/MTES-MCT/qualicharge/commit/1527322)
- Suppression des sessions longues de l'indicateur OCCT, améliorant la pertinence des données affichées. [#cfa75f0](https://github.com/MTES-MCT/qualicharge/commit/cfa75f0)

### Évolutions techniques

- Mises à jour de plusieurs dépendances pour bénéficier des dernières corrections de bugs et améliorations de sécurité (Pygments, pytest, requests, python-multipart, python-dotenv).
- Mises à jour des images Docker pour Keycloak, Metabase, Terraform, Curl, Locust et UV.
- Mise à jour de Django en version 6.0.4 pour bénéficier des dernières améliorations et correctifs de sécurité. [#75a3748](https://github.com/MTES-MCT/qualicharge/commit/75a3748)
- Mise à jour des actions GitHub (setup-uv, gh-action-pypi-publish, upload-artifact) pour bénéficier des dernières fonctionnalités et corrections.

### Autres changements

- Aucune documentation ou configuration n'a été modifiée durant cette période.
