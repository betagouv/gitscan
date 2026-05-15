## Changelog : coolify-logs-proxy (30 derniers jours, au 30 avril 2026)

### Résumé
Ce proxy pour les logs Coolify a connu une première phase de développement rapide avec l'ajout de fonctionnalités clés pour la récupération des logs et l'intégration avec GitHub.  Les améliorations se concentrent sur la robustesse, la gestion des erreurs et l'authentification, permettant une meilleure intégration avec les applications Coolify et une gestion plus fiable des événements GitHub.

### Évolutions fonctionnelles
- Ajout d'un endpoint `/runtime-logs` pour récupérer les logs d'exécution.
- Implémentation de l'authentification via l'appartenance à une organisation GitHub.
- Ajout d'un webhook GitHub pour nettoyer Coolify lors de la suppression d'un dépôt [#3905fbd](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/3905fbd).
- Amélioration de la gestion des erreurs lorsque le conteneur d'exécution n'est pas actif [#6c945f6](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/6c945f6).
- Prise en charge de l'analyse des logs structurés de Coolify [#f935206](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/f935206).
- Utilisation de l'UUID de déploiement pour une identification plus précise.

### Évolutions techniques
- Initialisation du projet coolify-logs-proxy [#6feab91](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/6feab91).
- Correction de l'utilisation d'URL absolues pour `deployment_url` [#3492139](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/3492139).
- Tolérance aux réponses enveloppées (wrapped) de l'API Coolify [#064cadd](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/064cadd).
- Enrichissement des endpoints `/_debug` avec des résumés complets [#f1d1eb4](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/f1d1eb4).
- Suppression des endpoints `/_debug` en production [#3492139](https://github.com/betagouv-experimentations/coolify-logs-proxy/commit/3492139).
