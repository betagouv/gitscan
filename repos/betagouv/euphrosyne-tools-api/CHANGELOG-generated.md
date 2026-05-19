## Changelog : euphrosyne-tools-api (30 derniers jours, au 2026-05-18)

### Résumé
Ce mois-ci, les évolutions de l'API Euphrosyne se concentrent sur l'amélioration de la robustesse et de la fiabilité du service, notamment en cas de problèmes d'accès aux données. Des améliorations ont également été apportées au processus de déploiement et des mises à jour de dépendances ont été effectuées pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Amélioration de la gestion des fichiers : Ajout d'une protection pour empêcher la suppression de fichiers si le nombre de fichiers actifs est insuffisant [#761](https://github.com/betagouv/euphrosyne-tools-api/pull/761).
- Robustesse accrue : L'API échoue maintenant de manière plus prévisible en cas d'absence de données actives, améliorant ainsi la fiabilité du service [#761](https://github.com/betagouv/euphrosyne-tools-api/pull/761).

### Évolutions techniques
- Déploiement automatisé : Mise en place d'un pipeline de déploiement automatique vers Scalingo lors de la création d'une nouvelle release [#762](https://github.com/betagouv/euphrosyne-tools-api/pull/762).
- Mises à jour de dépendances : Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, notamment `azure-mgmt-compute`, `azure-mgmt-web`, `fastapi`, `pydantic-settings`, `sentry-sdk`, `mypy`, `ruff` et `uvicorn`.

### Autres changements
- Documentation : Aucune modification de la documentation n'a été apportée durant cette période.
- Configuration : Aucune modification de la configuration n'a été apportée durant cette période.
