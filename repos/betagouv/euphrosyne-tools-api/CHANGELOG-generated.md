## Changelog : euphrosyne-tools-api (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une gestion de données "chaude" vers "froide" (Hot to Cool) pour les projets, permettant une transition des données actives vers un stockage moins coûteux.  Des améliorations ont également été apportées à la gestion des opérations de suppression de projets et à la robustesse générale de l'API, notamment en cas d'erreurs.  Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Implémentation du workflow de transition des données "chaudes" vers "froides" pour les projets, incluant des endpoints pour démarrer, surveiller et gérer ces opérations. [#678](https://github.com/betagouv/euphrosyne-tools-api/issues/678)
- Ajout d'un endpoint de suppression de projet, permettant de supprimer les données associées à un projet.
- Amélioration de la gestion des erreurs lors de l'initialisation des projets et de l'exécution des endpoints.
- Ajout d'un endpoint pour récupérer le rôle de stockage (storage role).
- Possibilité de spécifier le `project_slug` dans les endpoints liés aux données.

### Évolutions techniques
- Refactorisation de l'implémentation de la gestion des chemins de données pour une meilleure cohérence et une plus grande flexibilité.
- Amélioration de la gestion des erreurs et des exceptions, notamment pour les opérations de stockage.
- Ajout d'une abstraction pour l'exécution d'AzCopy, facilitant les tests et la maintenance.
- Mise en place d'un script d'installation d'AzCopy.
- Amélioration des tests unitaires avec une meilleure gestion des messages JSON et des mocks.
- Implémentation de la persistance et de l'idempotence des opérations de cycle de vie des données.
- Renforcement de la sécurité en appliquant des permissions en lecture seule (readonly) sur le stockage "froid".
- Amélioration de la gestion des états "annulé" et "inconnu" pour les opérations asynchrones.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et améliorations.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des dépendances suivantes : `ruff`, `mypy`, `pydantic-settings`, `uvicorn`, `fastapi`, `azure-keyvault-secrets`, `sentry-sdk`, `pytest`, `aiohttp`, `requests`, `types-requests`, `types-python-jose`, `anyio`.
