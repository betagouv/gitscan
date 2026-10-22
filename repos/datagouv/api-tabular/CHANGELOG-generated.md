## Changelog : api-tabular (30 derniers jours, au 20 octobre 2026)

### Résumé
Les récentes mises à jour se concentrent sur l'amélioration de l'infrastructure de déploiement (CI/CD) et l'optimisation de la suite de tests automatisés pour garantir une meilleure stabilité du service.

### Évolutions techniques
- CI/CD : Migration du déploiement des images Docker vers un nouveau registre de conteneurs ([#123](https://github.com/datagouv/api-tabular/pull/123)) et mise en conformité de la gestion des jetons de publication via `UV_PUBLISH_TOKEN` ([#117](https://github.com/datagouv/api-tabular/pull/117)).
- Tests : Refactorisation des tests de l'endpoint de santé (*health check*) pour supprimer la dépendance à la bibliothèque `aioresponses` ([#124](https://github.com/datagouv/api-tabular/pull/124)).
