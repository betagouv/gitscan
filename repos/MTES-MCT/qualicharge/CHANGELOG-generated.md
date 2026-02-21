## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à qualicharge au cours des 30 derniers jours. Les changements incluent des corrections de bugs dans les flux de données, des améliorations de la robustesse du système, des refactorisations pour une meilleure maintenabilité, et des mises à jour régulières des dépendances pour assurer la sécurité et la performance.

### Évolutions fonctionnelles
- Correction d'un bug dans l'indicateur de qualité PDCM dans les tâches Prefect. (#50bfa31)
- Amélioration de la gestion des points de recharge hors service dans les vérifications de refroidissement des données. (#aacb98a)
- Correction de l'unité de mesure de l'énergie envoyée par CARBURE. (#45bba03)
- Correction de la gestion des numéros SIREN incorrects dans le flux `tiruert_for_day`. (#20cff43)
- Amélioration du flux TIRUERT vers CARBURE. (#40547e6)
- Publication d'une nouvelle version de l'API (0.32.0) avec correction pour la gestion des fuseaux horaires des champs `Status` et `Session`. (#6f76b05, #af8d0f0)

### Évolutions techniques
- Refactorisation des flux de refroidissement pour une meilleure organisation et maintenabilité. (#2a9556e)
- Activation des linters pour tous les modules du projet, améliorant la qualité du code. (#c1a254c)
- Mise à jour de plusieurs dépendances, incluant FastAPI, Django, PostgreSQL, httpx, pydantic, sqlalchemy, Docker, Docker Compose, et d'autres outils de supervision et CI/CD. (Voir section "Autres changements" pour plus de détails)
- Amélioration de la robustesse des flux de refroidissement en permettant des échecs anticipés. (#08aa38b)

### Autres changements
- Mises à jour de dépendances (automatisées par Dependabot et Renovate) :
  - flask et werkzeug
  - ghcr.io/astral-sh/uv (plusieurs mises à jour)
  - metabase/metabase (plusieurs mises à jour)
  - sqlparse
  - locustio/locust
  - hashicorp/terraform
  - astral-sh/uv (plusieurs mises à jour)
  - cryptography
  - python-multipart
  - zizmorcore/zizmor-action
  - actions/checkout
  - actions/setup-python
  - astral-sh/setup-uv
  - orjson
