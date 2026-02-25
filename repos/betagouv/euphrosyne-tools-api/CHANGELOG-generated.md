## Changelog : euphrosyne-tools-api (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de l'API euphrosyne-tools-api. Les principales améliorations concernent la migration vers une nouvelle version de Python (3.14), l'ajout du support du stockage Azure Blob et des mises à jour régulières des dépendances pour assurer la sécurité et la stabilité du service.

### Évolutions fonctionnelles
- Ajout du support du stockage Azure Blob pour la gestion des données projets. (#675)

### Évolutions techniques
- Migration vers Python 3.14 (#695, #693, #7bc21da, #97ee37d)
- Refactor du code avec Black pour améliorer la lisibilité et la cohérence. (#673, #ae6466b)
- Mise à jour de la librairie `azure-mgmt-resource` vers `azure-mgmt-resource-deployments`. (#689, #e3c8604)
- Mises à jour de plusieurs dépendances : `fastapi`, `uvicorn`, `azure-mgmt-compute`, `pytest`, `pytest-asyncio`, `sentry-sdk`, `pydantic-settings`, `ruff`, `mypy`, `stream-zip`, `azure-identity`.

### Autres changements
- Mises à jour de la configuration des workflows de CI/CD pour supporter Python 3.14. (#693)
