## Changelog : datagouv-mcp (30 derniers jours, au 20 avril 2026)

### Résumé
Les dernières mises à jour de datagouv-mcp se concentrent sur l'amélioration de la robustesse, de la surveillance et de l'intégration avec des outils de suivi comme Matomo. Des améliorations ont également été apportées à la gestion des erreurs et à la configuration, notamment pour faciliter l'utilisation avec différents clients et environnements.

### Évolutions fonctionnelles
- Ajout de titres d'outils et d'annotations MCP pour une meilleure identification et compréhension des outils disponibles. [#102](https://github.com/datagouv/datagouv-mcp/pull/102)
- Amélioration de la gestion des erreurs de l'API Tabular (codes 4xx/5xx) en fournissant des indications au LLM pour une meilleure résolution. [#94](https://github.com/datagouv/datagouv-mcp/pull/94)
- Suivi des appels aux outils MCP en tant qu'événements Matomo, permettant une analyse de l'utilisation des outils. [#101](https://github.com/datagouv/datagouv-mcp/pull/101)
- Ajout d'un "deep health check" et d'un script de développement `call_tool` pour faciliter le diagnostic et le test. [#100](https://github.com/datagouv/datagouv-mcp/pull/100)
- Configuration OpenCode MCP ajoutée à la documentation README. [#99](https://github.com/datagouv/datagouv-mcp/pull/99)
- Note dans la documentation README concernant l'utilisation de Claude Desktop sur Windows et son intégration avec Node. [#90](https://github.com/datagouv/datagouv-mcp/pull/90)

### Évolutions techniques
- Simplification de la gestion des tags pour correspondre à la définition Swagger de l'API. [#98](https://github.com/datagouv/datagouv-mcp/pull/98)
- Suppression du paramètre `question` de la fonction `query_resource_data`, simplifiant ainsi l'appel de cette fonction. [#95](https://github.com/datagouv/datagouv-mcp/pull/95)
- Utilisation d'un client `httpx` partagé pour Matomo au lieu d'un client par requête, améliorant ainsi les performances. [#88](https://github.com/datagouv/datagouv-mcp/pull/88)
- Lecture de l'URL de base de Matomo à partir d'une variable d'environnement et désactivation du suivi si la variable n'est pas définie. [#89](https://github.com/datagouv/datagouv-mcp/pull/89)
- Ajout d'un test de stress pour la gestion des déconnexions client. [#83](https://github.com/datagouv/datagouv-mcp/pull/83)
- Mise à jour des dépendances pour corriger les alertes de dépendabot. [#79](https://github.com/datagouv/datagouv-mcp/pull/79)
- Amélioration de la configuration du workflow CircleCI pour exécuter les tests sur toutes les branches et aligner les imports de Ruff avec la configuration CI. [#81](https://github.com/datagouv/datagouv-mcp/pull/81)
- Correction d'une erreur dans la limite du nombre de métriques récupérées, qui dépassait la limite maximale de l'API. [#75](https://github.com/datagouv/datagouv-mcp/pull/75)
- Gestion des valeurs `None` dans les métriques pour éviter une erreur de type. [#78](https://github.com/datagouv/datagouv-mcp/pull/78)

### Autres changements
- Mise à jour du fichier `.gitignore`. [#1bc7f3b](https://github.com/datagouv/datagouv-mcp/commit/1bc7f3b)
- Publication des versions 0.2.23 et 0.2.22.
- Amélioration des directives de contribution dans la documentation. [#82](https://github.com/datagouv/datagouv-mcp/pull/82)
- Correction d'une variable d'environnement Matomo incorrecte.
- Ajout de logging structuré pour les appels aux outils MCP.
- Ajout d'un test unitaire pour le logging.
- Correction d'une faute de frappe.
- Importation de la variable de nom du logger.
