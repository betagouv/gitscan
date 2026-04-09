## Changelog : datagouv-mcp (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la documentation, la correction de bugs et l'optimisation des performances. Des ajustements ont été apportés pour améliorer la compatibilité avec différents clients (Claude sur Windows, IBM Bob) et pour gérer plus robustement les erreurs et les limites d'API. L'ajout de la surveillance via Sentry permet une meilleure détection et résolution des problèmes.

### Évolutions fonctionnelles
- Amélioration de la documentation pour la configuration avec OpenCode MCP [#99](https://github.com/datagouv/datagouv-mcp/pull/99).
- Note ajoutée dans la documentation concernant l'utilisation de Claude Desktop sur Windows et son intégration avec Node.js [#90](https://github.com/datagouv/datagouv-mcp/pull/90).
- Utilisation de l'API v2 pour la recherche, améliorant potentiellement la pertinence et la performance [#70](https://github.com/datagouv/datagouv-mcp/pull/70).
- Gestion améliorée des valeurs `None` dans les métriques pour éviter les erreurs de type [#78](https://github.com/datagouv/datagouv-mcp/pull/78).
- Correction d'une erreur concernant la variable d'environnement Matomo [#99](https://github.com/datagouv/datagouv-mcp/pull/99).
- Correction d'une limite atteinte avec l'API lors de la récupération des métriques [#75](https://github.com/datagouv/datagouv-mcp/pull/75).

### Évolutions techniques
- Ajout de tests de stress pour la gestion des déconnexions client [#83](https://github.com/datagouv/datagouv-mcp/pull/83).
- Mise à jour des dépendances pour corriger des alertes de sécurité [#79](https://github.com/datagouv/datagouv-mcp/pull/79).
- Amélioration de la gestion des clients HTTP dans Matomo en utilisant un client partagé [#88](https://github.com/datagouv/datagouv-mcp/pull/88).
- Lecture de l'URL de base de Matomo à partir d'une variable d'environnement, avec désactivation du suivi si non définie [#89](https://github.com/datagouv/datagouv-mcp/pull/89).
- Ajout de la surveillance des erreurs et des performances avec Sentry.
- Ajout de logs structurés pour les appels d'outils MCP.
- Refactoring pour utiliser un client `httpx` partagé.
- Exécution des workflows CI sur toutes les branches.
- Alignement des imports Ruff avec la configuration CI.

### Autres changements
- Amélioration des directives de contribution dans la documentation [#82](https://github.com/datagouv/datagouv-mcp/pull/82).
- Correction de fautes de frappe et améliorations de la documentation générale.
- Ajout d'un décorateur pour les tests de logging.
- Mise à jour de la documentation pour inclure le type de serveur IBM Bob.
- Suppression d'imports inutilisés.
- Suppression de compétences non utilisées.
- Amélioration de la documentation README avec une image de couverture et une meilleure organisation.
