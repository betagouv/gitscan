## Changelog : datagouv-mcp (30 derniers jours, au 18 mai 2026)

### Résumé
Les dernières mises à jour de datagouv-mcp se concentrent sur l'ajout de nouveaux outils pour interagir avec les données de data.gouv.fr, l'amélioration de la sécurité en corrigeant une vulnérabilité, et l'amélioration de la gestion des dépendances et de la documentation. Des améliorations de la journalisation et du suivi des événements ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un nouvel outil `search_organizations` permettant de rechercher des organisations sur la plateforme data.gouv.fr ([#103](https://github.com/datagouv/datagouv-mcp/pull/103)).
- Amélioration de l'alignement de la formulation des API tierces avec les identifiants des services de données ([#110](https://github.com/datagouv/datagouv-mcp/pull/110)).
- Ajout d'un script de développement `call_tool` et d'un contrôle de santé approfondi pour faciliter le débogage et la surveillance de l'application ([#100](https://github.com/datagouv/datagouv-mcp/pull/100)).

### Évolutions techniques
- Correction d'une vulnérabilité de sécurité (CVE-2026-44432) en contraignant la version de la librairie `urllib3` ([#112](https://github.com/datagouv/datagouv-mcp/pull/112)).
- Mise à jour des dépendances du projet.
- Suppression d'une contrainte temporaire sur `urllib3`.
- Ajout de modèles de politique IA pour les issues et pull requests sur GitHub ([#107](https://github.com/datagouv/datagouv-mcp/pull/107)).
- Correction de problèmes de typage.

### Autres changements
- Ajout de titres d'outils et d'annotations MCP.
- Amélioration de la documentation et des directives de contribution.
- Ajout de la journalisation structurée pour les appels aux outils MCP.
- Suivi des appels aux outils MCP via Matomo, avec configuration de l'URL de base et possibilité de désactiver le suivi.
- Amélioration de la gestion des erreurs 4xx/5xx de l'API Tabular avec des indications pour le LLM.
- Simplification de la gestion des tags pour correspondre au schéma Swagger de l'API.
- Suppression du paramètre `question` de la fonction `query_resource_data`.
