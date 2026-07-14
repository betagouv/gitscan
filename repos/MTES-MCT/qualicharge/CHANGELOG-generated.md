## Changelog : qualicharge (30 derniers jours, au 11 juillet 2026)

### Résumé
Ce mois-ci, les mises à jour de QualiCharge se concentrent sur l'amélioration de la précision des indicateurs de session et l'inclusion des points de recharge hors service dans les analyses Prefect. Une nouvelle version de l'API a également été publiée. Des mises à jour de sécurité et de dépendances ont été appliquées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un indicateur E1-DMR dans Prefect [#1234](https://github.com/MTES-MCT/qualicharge/issues/1234).
- Ajout d'un indicateur E5 dans Prefect.
- Inclusion des points de recharge hors service dans les analyses Prefect, améliorant ainsi la couverture des données [#1234](https://github.com/MTES-MCT/qualicharge/issues/1234).
- Publication d'une nouvelle version de l'API (0.34.1).
- Correction d'un bug dans Prefect concernant le décalage temporel des indicateurs de session.

### Évolutions techniques
- Mise à jour de Keycloak vers la version 26.7.
- Mise à jour de Metabase vers la version 0.62.4.
- Mise à jour de Locust vers la version 2.45.0.
- Mise à jour de Curl vers la version 8.21.0.
- Mise à jour de Terraform vers la version 1.15.8.
- Mise à jour de l'action GitHub `actions/checkout` vers la version 7.
- Mise à jour de l'action GitHub `setup-python` vers la version 6.3.0.
- Mise à jour de l'action GitHub `setup-uv` vers la version 8.3.2.
- Mise à jour de l'image Docker `ghcr.io/astral-sh/uv` vers la version 0.11.28.

### Autres changements
- Mises à jour de sécurité de plusieurs dépendances Python (pydantic-settings, python-multipart, pyjwt).
- Améliorations générales de la configuration et des dépendances du projet.
