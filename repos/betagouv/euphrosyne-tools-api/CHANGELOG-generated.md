## Changelog : euphrosyne-tools-api (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur la maintenance technique du projet, notamment la mise à jour des dépendances et la migration vers une nouvelle version de Python (3.14). Ces mises à jour visent à améliorer la sécurité, la performance et la stabilité de l'API.

### Évolutions techniques
- Migration vers Python 3.14 : Le projet a été mis à jour pour utiliser Python 3.14, ce qui permet de bénéficier des dernières améliorations et corrections de sécurité du langage. [#695](https://github.com/betagouv/euphrosyne-tools-api/pull/695)
- Refactor du code avec Black : Le code a été formaté avec Black pour améliorer la lisibilité et la cohérence. [#673](https://github.com/betagouv/euphrosyne-tools-api/pull/673)
- Mise à jour des dépendances : Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, incluant :
    - `azure-mgmt-resource` vers 25.0.0
    - `azure-mgmt-compute` vers 37.2.0
    - `fastapi` vers 0.129.0
    - `uvicorn[standard]` vers 0.41.0
    - `sentry-sdk[fastapi]` vers 2.53.0
    - `pydantic-settings` vers 2.13.1
    - `ruff` vers 0.15.2
    - `mypy` vers 1.19.1
    - `stream-zip` vers 0.0.84
    - `azure-identity` vers 1.25.2
    - `isort` vers 8.0.0

### Autres changements
- Remplacement de `azure-mgmt-resource` par `azure-mgmt-resource-deployments`. [#689](https://github.com/betagouv/euphrosyne-tools-api/pull/689)
- Ajout du fichier `.python-version` et suppression de `runtime.txt` pour une meilleure gestion de la version de Python. [#7bc21da](https://github.com/betagouv/euphrosyne-tools-api/commit/7bc21da)
- Mise à jour des workflows CI/CD pour utiliser Python 3.14. [#97ee37d](https://github.com/betagouv/euphrosyne-tools-api/commit/97ee37d)
