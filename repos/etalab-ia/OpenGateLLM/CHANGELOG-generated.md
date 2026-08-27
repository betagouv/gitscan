## Changelog : OpenGateLLM (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois a été marqué par un travail de fond sur la robustesse et la maintenabilité du système. Les principales évolutions concernent l'intégration du support SSO pour une authentification simplifiée, l'amélioration de la visibilité via de nouveaux tableaux de bord Grafana, et une refonte majeure de l'architecture interne pour garantir une meilleure stabilité à long terme.

### Évolutions fonctionnelles
- **Authentification** : Support du login/logout SSO via `oauth2-proxy` [#986](https://github.com/etalab-ia/OpenGateLLM/pull/986).
- **Observabilité** : Ajout de templates Grafana pour le monitoring du trafic et de l'inférence [#903](https://github.com/etalab-ia/OpenGateLLM/pull/903).
- **API** : Simplification et renommage des endpoints utilisateur (ex: `/v1/me/info` devient `/v1/me`) [#1033](https://github.com/etalab-ia/OpenGateLLM/pull/1033).
- **Monitoring** : Amélioration du suivi dans Langfuse avec la prise en compte des requêtes non-streamées [#987](https://github.com/etalab-ia/OpenGateLLM/pull/987).
- **Interface** : Amélioration du formulaire d'authentification dans le Playground via Reflex [#981](https://github.com/etalab-ia/OpenGateLLM/pull/981).

### Évolutions techniques
- **Architecture** : Migration massive de nombreux endpoints (organisations, usage, clés, audio, OCR) vers une "Clean Architecture" pour améliorer la modularité et la testabilité [#1050, #1045, #1039, #1038, #1024, #1023, #1021, #1020, #1022, #1008, #984].
- **Performance & Base de données** : 
    - Optimisation de la gestion des connexions PostgreSQL en libérant les connexions du pool lors des appels aux fournisseurs [#1005](https://github.com/etalab-ia/OpenGateLLM/pull/1005).
    - Nettoyage de la base de données avec la suppression des tables PostgreSQL liées au RAG [#1007](https://github.com/etalab-ia/OpenGateLLM/pull/1007).
- **Infrastructure & Cache** : Implémentation d'une fonctionnalité de réinitialisation des clés Redis [#952](https://github.com/etalab-ia/OpenGateLLM/pull/952).
- **CI/CD** : Optimisation des pipelines de tests (la couverture et les tests E2E ne s'exécutent désormais que sur les PR prêtes) [#1025](https://github.com/etalab-ia/OpenGateLLM/pull/1025).
- **Sécurité** : Migration des secrets client SSO vers les secrets GitHub Actions pour une meilleure gestion des environnements [#1006](https://github.com/etalab-ia/OpenGateLLM/pull/1006).

### Autres changements
- **Documentation** : Mises à jour de la documentation générée et gestion des versions de release [#1055, #1054, #1009].
- **Documentation** : Ajout du fichier `AGENTS.md` [#1017](https://github.com/etalab-ia/OpenGateLLM/pull/1017).
