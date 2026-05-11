## Changelog : datagouv-mcp (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouveaux outils pour faciliter l'accès aux données de data.gouv.fr via les chatbots d'IA, l'amélioration de la robustesse du système face aux erreurs des APIs, et le suivi de l'utilisation des outils pour une meilleure compréhension des besoins des utilisateurs. Des corrections et des refactorisations ont également été apportées pour optimiser le code et simplifier la maintenance.

### Évolutions fonctionnelles
- Ajout d'un nouvel outil permettant de rechercher des organisations sur data.gouv.fr [#103](https://github.com/datagouv/datagouv-mcp/pull/103).
- Amélioration de la gestion des erreurs de l'API Tabular (erreurs 4xx/5xx) en fournissant des indications aux modèles de langage pour une meilleure gestion des problèmes [#94](https://github.com/datagouv/datagouv-mcp/pull/94).
- Ajout de titres aux outils MCP et d'annotations pour une meilleure identification et utilisation [#102](https://github.com/datagouv/datagouv-mcp/pull/102).
- Implémentation du suivi des appels aux outils MCP via Matomo, permettant d'analyser l'utilisation et d'identifier les points d'amélioration [#101](https://github.com/datagouv/datagouv-mcp/pull/101).

### Évolutions techniques
- Refactorisation de la gestion des tags pour correspondre à la définition de l'API Swagger [#98](https://github.com/datagouv/datagouv-mcp/pull/98).
- Suppression du paramètre `question` de la fonction `query_resource_data` pour simplifier le code [#95](https://github.com/datagouv/datagouv-mcp/pull/95).
- Ajout d'un script de développement `call_tool` et d'un health check plus approfondi [#100](https://github.com/datagouv/datagouv-mcp/pull/100).
- Alignement de la formulation des APIs tierces avec les identifiants du service de données [#110](https://github.com/datagouv/datagouv-mcp/pull/110).

### Autres changements
- Ajout de modèles de politiques d'utilisation de l'IA pour les issues et les pull requests sur GitHub [#107](https://github.com/datagouv/datagouv-mcp/pull/107).
- Mise à jour des dépendances du projet [#105](https://github.com/datagouv/datagouv-mcp/pull/105).
