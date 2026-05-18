## Changelog : datagouv-mcp (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouveaux outils pour interagir avec les données de data.gouv.fr, notamment la recherche d'organisations. Des corrections de sécurité et des améliorations de la robustesse ont également été apportées, ainsi que des optimisations pour le suivi et l'analyse de l'utilisation des outils.

### Évolutions fonctionnelles
- Ajout d'un nouvel outil `search_organizations` permettant de rechercher des organisations sur data.gouv.fr [#103](https://github.com/datagouv/datagouv-mcp/pull/103).
- Amélioration de la correspondance entre la terminologie des API tierces et les identifiants des services de données [#110](https://github.com/datagouv/datagouv-mcp/pull/110).
- Ajout de titres aux outils et d'annotations MCP pour une meilleure identification et utilisation [#102](https://github.com/datagouv/datagouv-mcp/pull/102).
- Suivi des appels aux outils MCP en tant qu'événements Matomo [#101](https://github.com/datagouv/datagouv-mcp/pull/101).
- Ajout d'un script de développement `call_tool` et d'une vérification de santé approfondie [#100](https://github.com/datagouv/datagouv-mcp/pull/100).

### Évolutions techniques
- Correction d'une vulnérabilité de sécurité dans la bibliothèque `urllib3` (CVE-2026-44432) [#112](https://github.com/datagouv/datagouv-mcp/pull/112).
- Mise à jour des dépendances pour corriger les alertes de sécurité et améliorer la stabilité [#105](https://github.com/datagouv/datagouv-mcp/pull/105).
- Simplification de la gestion des tags pour correspondre au schéma Swagger de l'API [#98](https://github.com/datagouv/datagouv-mcp/pull/98).
- Suppression du paramètre `question` de la fonction `query_resource_data` [#95](https://github.com/datagouv/datagouv-mcp/pull/95).
- Amélioration de la gestion des erreurs 4xx/5xx de l'API Tabular avec des indications pour le LLM [#94](https://github.com/datagouv/datagouv-mcp/pull/94).

### Autres changements
- Ajout de modèles de politique IA pour les issues et les PR sur GitHub [#107](https://github.com/datagouv/datagouv-mcp/pull/107).
- Ajout de documentation pour la configuration d'OpenCode MCP [#99](https://github.com/datagouv/datagouv-mcp/pull/99).
- Note concernant l'utilisation de Claude Desktop sur Windows [#90](https://github.com/datagouv/datagouv-mcp/pull/90).
- Amélioration des guidelines de contribution [#82](https://github.com/datagouv/datagouv-mcp/pull/82).
