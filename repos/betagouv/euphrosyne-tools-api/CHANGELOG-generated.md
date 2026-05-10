## Changelog : euphrosyne-tools-api (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une gestion de cycle de vie des données "Hot" et "Cool", permettant de déplacer des données entre différents niveaux de stockage Azure.  Des améliorations ont également été apportées à la robustesse et à la gestion des erreurs, notamment lors des opérations de suppression et de gestion des jobs AzCopy. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la gestion du cycle de vie des données "Hot" et "Cool" : implémentation des workflows de restauration et de passage au stockage "Cool" [#678](https://github.com/betagouv/euphrosyne-tools-api/pull/678).
- Implémentation d'un endpoint de suppression de projet.
- Ajout d'endpoints pour obtenir le statut des opérations de cycle de vie (COOL et RESTORE).
- Amélioration de la gestion des erreurs lors de la suppression de fichiers : une vérification du nombre de fichiers est effectuée avant la suppression.
- L'API refuse désormais les opérations d'écriture sur le stockage "Cool".
- Ajout d'un endpoint pour récupérer le rôle de stockage (storage role).

### Évolutions techniques
- Refactorisation de la gestion des chemins de données pour une résolution déterministe des chemins pour les données "Hot" et "Cool".
- Amélioration de la gestion des erreurs et de la robustesse des opérations AzCopy, notamment la gestion des erreurs "job not found".
- Intégration d'un script d'installation d'AzCopy.
- Amélioration des tests AzCopy avec une meilleure gestion des messages JSON et des mocks.
- Centralisation de la logique de parsing des chemins de données.
- Refactorisation de l'initialisation des clients Azure avec support du rôle de stockage.
- Déploiement automatique sur Scalingo lors de la création d'une release.
- Amélioration de la gestion des états "canceled" et "unknown" pour éviter les messages d'erreur.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des dépendances : `azure-mgmt-compute`, `types-requests`, `ruff`, `mypy`, `pydantic-settings`, `uvicorn`, `fastapi`, `azure-keyvault-secrets`, `sentry-sdk`, `pytest`, `anyio`, `types-python-jose`.
