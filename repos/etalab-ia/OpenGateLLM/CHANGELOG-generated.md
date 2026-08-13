## Changelog : OpenGateLLM (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a franchi une étape importante de sa structuration interne en migrant plusieurs composants clés vers une architecture plus robuste et maintenable (Clean Architecture). Les évolutions se sont également concentrées sur le renforcement de la sécurité des accès, l'amélioration de la fiabilité des tests automatisés et la précision du monitoring.

### Évolutions fonctionnelles
- **Sécurité** : Protection contre l'énumération d'utilisateurs via l'utilisation de messages d'erreur d'authentification génériques [#963](https://github.com/etalab-ia/OpenGateLLM/issues/963).
- **Interface utilisateur** : Correction des formulaires d'authentification dans l'interface Playground [#981](https://github.com/etalab-ia/OpenGateLLM/issues/981).
- **Données** : Amélioration de la précision des indicateurs d'impact environnemental (utilisation de 0.0 au lieu de None) [#990](https://github.com/etalab-ia/OpenGateLLM/issues/990).

### Évolutions techniques
- **Refactorisation majeure** : Migration vers une "Clean Architecture" pour plusieurs points d'entrée critiques de l'API : endpoint OCR [#984](https://github.com/etalab-ia/OpenGateLLM/issues/984), gestion des utilisateurs [#962](https://github.com/etalab-ia/OpenGateLLM/issues/962) et gestion des tokens [#947](https://github.com/etalab-ia/OpenGateLLM/issues/947).
- **Optimisation de la CI/CD** : Résolution des problèmes de dépendances pour l'exécution des tests E2E [#964](https://github.com/etalab-ia/OpenGateLLM/issues/964), [#968](https://github.com/etalab-ia/OpenGateLLM/issues/968) et gestion des scans de sécurité Trivy [#969](https://github.com/etalab-ia/OpenGateLLM/issues/969).
- **Observabilité** : Amélioration du monitoring avec l'enregistrement des requêtes non-streaming dans Langfuse [#987](https://github.com/etalab-ia/OpenGateLLM/issues/987).
- **Maintenance du code** : Suppression de `ModelProviderGateway` [#972](https://github.com/etalab-ia/OpenGateLLM/issues/972), ajustement des corps de requêtes pour les modèles [#977](https://github.com/etalab-ia/OpenGateLLM/issues/977) et résolution de conflits de versions de packages.

### Autres changements
- **Documentation** : Ajout d'une décision d'architecture (ADR) concernant la séparation du RAG [#971](https://github.com/etalab-ia/OpenGateLLM/issues/971) et mise à jour de la documentation générée [#975](https://github.com/etalab-ia/OpenGateLLM/issues/975).
- **Configuration** : Mise à jour des variables d'environnement par défaut dans les exemples de configuration [#974](https://github.com/etalab-ia/OpenGateLLM/issues/974).
- **Tests** : Intégration de tests pour la gestion de la configuration héritée [#991](https://github.com/etalab-ia/OpenGateLLM/issues/991).
