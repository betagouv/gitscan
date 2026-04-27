## Changelog : datagouv-mcp (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de l'interaction avec l'API Tabular, le suivi des appels aux outils via Matomo pour une meilleure analyse, et l'ajout de vérifications de santé plus approfondies. Des corrections de bugs et des simplifications de code ont également été apportées pour améliorer la stabilité et la maintenance du projet.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors de l'utilisation de l'API Tabular : le système gère désormais mieux les réponses d'erreur (4xx/5xx) de l'API et fournit des indications à l'IA pour une meilleure résolution. [#94](https://github.com/datagouv/datagouv-mcp/pull/94)
- Suivi des appels aux outils MCP : les appels aux outils sont désormais enregistrés en tant qu'événements Matomo, permettant un suivi et une analyse plus précis de leur utilisation. [#101](https://github.com/datagouv/datagouv-mcp/pull/101)
- Ajout de titres aux outils et annotations MCP : améliore la clarté et l'identification des outils disponibles. [#102](https://github.com/datagouv/datagouv-mcp/pull/102)
- Ajout d'un script de développement pour effectuer des vérifications de santé approfondies et tester l'appel aux outils. [#100](https://github.com/datagouv/datagouv-mcp/pull/100)

### Évolutions techniques
- Simplification de la gestion des tags pour correspondre à la définition de l'API Swagger. [#98](https://github.com/datagouv/datagouv-mcp/pull/98)
- Suppression du paramètre `question` de la fonction `query_resource_data` pour simplifier le code. [#95](https://github.com/datagouv/datagouv-mcp/pull/95)
- Utilisation d'un client `httpx` partagé pour Matomo afin d'optimiser les performances. [#88](https://github.com/datagouv/datagouv-mcp/pull/88)
- Correction d'une erreur de variable d'environnement Matomo.
- Correction d'un problème de limite de requêtes à l'API `get_metrics`. [#75](https://github.com/datagouv/datagouv-mcp/pull/75)

### Autres changements
- Ajout de modèles de politique IA pour les issues et pull requests sur GitHub. [#107](https://github.com/datagouv/datagouv-mcp/pull/107)
- Mise à jour de la documentation README avec des informations sur la configuration OpenCode MCP et l'utilisation de Claude Desktop sur Windows. [#99](https://github.com/datagouv/datagouv-mcp/pull/90)
- Mise à jour du fichier `.gitignore`.
- Publication des versions 0.2.24, 0.2.23 et 0.2.22.
