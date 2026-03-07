## Changelog : euphrosyne-tools-api (30 derniers jours)

### Résumé
Ce changelog résume les mises à jour récentes de l'API Euphrosyne Tools. Les changements principaux concernent la mise à jour des dépendances du projet, notamment les librairies Python utilisées pour le développement et l'infrastructure Azure. Une migration vers Python 3.14 a également été effectuée pour bénéficier des dernières améliorations et corrections de sécurité.

### Évolutions techniques
- Migration vers Python 3.14 : Le projet a été mis à jour pour utiliser Python 3.14, améliorant ainsi la compatibilité et la sécurité. [#695](https://github.com/betagouv/euphrosyne-tools-api/pull/695)
- Mise à jour des workflows CI/CD : Les workflows de tests et de mise à jour des caches ont été adaptés pour utiliser Python 3.14. [#693](https://github.com/betagouv/euphrosyne-tools-api/pull/693)
- Remplacement de `azure-mgmt-resource` par `azure-mgmt-resource-deployments` :  Simplification de la gestion des ressources Azure. [#689](https://github.com/betagouv/euphrosyne-tools-api/pull/689)

### Autres changements
- Mises à jour de dépendances : De nombreuses dépendances ont été mises à jour vers leurs dernières versions, incluant :
    - `fastapi` (0.128.0 -> 0.135.1)
    - `uvicorn[standard]` (0.38.0 -> 0.41.0)
    - `azure-mgmt-compute` (37.1.0 -> 37.2.0)
    - `azure-identity` (1.25.1 -> 1.25.2)
    - `sentry-sdk[fastapi]` (2.51.0 -> 2.53.0)
    - `pydantic-settings` (2.12.0 -> 2.13.1)
    - `ruff` (0.14.14 -> 0.15.4)
    - `isort` (7.0.0 -> 8.0.1)
    - `python-dotenv` (1.2.1 -> 1.2.2)
    - `stream-zip` (0.0.83 -> 0.0.84)
