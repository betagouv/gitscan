## Changelog : euphrosyne-tools-api (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'implémentation d'une gestion du cycle de vie des données de projet (passage du chaud au froid, restauration) avec une attention particulière à la robustesse et à l'idempotence des opérations. Des améliorations ont également été apportées à l'API pour supporter ces nouvelles fonctionnalités et à l'infrastructure avec des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour supprimer un projet.
- Implémentation du workflow de "refroidissement" (cool) des données de projet, permettant de les archiver sur un stockage moins coûteux.
- Implémentation du workflow de restauration des données de projet.
- Ajout d'endpoints pour obtenir le statut des opérations de "refroidissement" et de restauration.
- L'API accepte désormais uniquement `project_slug` comme variable dans les endpoints liés aux données.
- Ajout d'une gestion des erreurs pour les opérations de stockage en lecture seule.

### Évolutions techniques
- Refactorisation de la gestion des chemins de données pour une résolution déterministe entre les stockages "chaud" et "froid".
- Amélioration de la gestion des erreurs et de la robustesse lors de l'utilisation d'AzCopy pour le transfert de données.
- Ajout d'un script d'installation d'AzCopy.
- Implémentation d'une abstraction "AzCopy runner" pour faciliter les tests et la maintenance.
- Amélioration des tests avec une meilleure gestion des messages JSON et des mocks.
- Persistance et idempotence des opérations de cycle de vie des données grâce à l'ajout d'un suivi des opérations.
- Utilisation du rôle de stockage Euphrosyne pour initialiser les clients Azure.
- Refactorisation du code pour une meilleure cohérence et lisibilité.

### Autres changements
- Ajout d'un fichier `EPIC.md` pour documenter les grandes étapes du projet.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités.
- Mises à jour de plusieurs dépendances (requests, ruff, sentry-sdk, aiohttp, fastapi, uvicorn, types-requests, types-python-jose, azure-mgmt-storage, pytest, anyio).
