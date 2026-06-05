## Changelog : euphrosyne-tools-api (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la correction d'un bug affectant la récupération des informations sur les machines virtuelles et sur la mise à jour des dépendances du projet pour bénéficier des dernières corrections de sécurité et améliorations de performance. Plusieurs dépendances ont été mises à jour vers leurs versions les plus récentes.

### Évolutions fonctionnelles
- Correction d'un problème de signature lors de la récupération de la liste des ressources par groupe de ressources. [#781](https://github.com/betagouv/euphrosyne-tools-api/pull/781)

### Évolutions techniques
- Mise à jour de `azure-mgmt-web` vers la version 11.0.0.
- Mise à jour de `azure-mgmt-compute` vers la version 38.0.0.
- Mise à jour de `mypy` vers la version 2.1.0.
- Mises à jour de plusieurs dépendances incluant `fastapi`, `azure-storage-blob`, `azure-storage-file-share`, `uvicorn`, `requests`, `pydantic-settings`, `sentry-sdk`, `pytest-asyncio`, `black`, `ruff` et `types-requests` vers leurs dernières versions mineures et correctives.

### Autres changements
- Aucune modification de documentation ou de configuration n'a été apportée durant cette période.
