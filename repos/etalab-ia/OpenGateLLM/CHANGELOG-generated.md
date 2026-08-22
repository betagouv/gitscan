## Changelog : OpenGateLLM (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, OpenGateLLM a franchi une étape importante de sa maturité technique avec une refonte majeure de son architecture interne vers un modèle de "Clean Architecture", visant à améliorer la maintenabilité du projet. Côté utilisateur, l'expérience a été enrichie par l'intégration du support SSO et l'amélioration de l'interface de test (Playground).

### Évolutions fonctionnelles
- **Authentification** : Support de la connexion et déconnexion via SSO avec `oauth2-proxy` [#986](https://github.com/etalab-ia/OpenGateLLM/pull/986).
- **Playground** : Correction du formulaire d'authentification pour une meilleure expérience utilisateur [#981](https://github.com/etalab-ia/OpenGateLLM/pull/981).
- **Monitoring** : Amélioration de la visibilité dans Langfuse en enregistrant désormais les requêtes non-streaming [#987](https://github.com/etalab-ia/OpenGateLLM/pull/987).
- **Corrections** : Ajustement de l'affichage de l'impact environnemental pour éviter les erreurs de valeurs nulles [#990](https://github.com/etalab-ia/OpenGateLLM/pull/990).

### Évolutions techniques
- **Refonte architecturale** : Migration massive de plusieurs endpoints vers une "Clean Architecture" pour stabiliser et structurer le code (gestion des clés API, informations utilisateur, transcription audio et OCR) [#1023](https://github.com/etalab-ia/OpenGateLLM/pull/1023), [#1021](https://github.com/etalab-ia/OpenGateLLM/pull/1021), [#1008](https://github.com/etalab-ia/OpenGateLLM/pull/1008), [#984](https://github.com/etalab-ia/OpenGateLLM/pull/984).
- **Optimisation des performances** : Amélioration de la gestion du pool de connexions PostgreSQL lors des appels aux fournisseurs d'IA pour libérer les ressources plus rapidement [#1005](https://github.com/etalab-ia/OpenGateLLM/pull/1005).
- **Gestion de la base de données** : Simplification du schéma de données par la suppression des tables PostgreSQL liées au RAG [#1007](https://github.com/etalab-ia/OpenGateLLM/pull/1007).
- **CI/CD** : Optimisation des pipelines de tests pour n'exécuter la couverture de code et les tests de bout en bout (E2E) que sur les Pull Requests prêtes à être fusionnées [#1025](https://github.com/etalab-ia/OpenGateLLM/pull/1025).

### Autres changements
- **Documentation** : Ajout d'un guide sur les agents (`AGENTS.md`) [#1017](https://github.com/etalab-ia/OpenGateLLM/pull/1017) et de documents de décision architecturale (ADR) concernant la séparation du RAG [#971](https://github.com/etalab-ia/OpenGateLLM/pull/971).
- **Configuration** : Mise à jour des variables d'environnement par défaut dans l'exemple de configuration [#974](https://github.com/etalab-ia/OpenGateLLM/pull/974) et actualisation de la documentation générée [#1009](https://github.com/etalab-ia/OpenGateLLM/pull/1009).
