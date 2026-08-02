## Changelog : OpenGateLLM (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une refonte architecturale significative, notamment au niveau des endpoints OCR, de la gestion des utilisateurs et des clés API, pour une meilleure maintenabilité et une plus grande cohérence. Des améliorations ont également été apportées à la sécurité, notamment en empêchant l'énumération des utilisateurs. L'interface utilisateur du playground a été améliorée et la gestion des RAG (Retrieval-Augmented Generation) a été revue.

### Évolutions fonctionnelles
- **Playground:** L'authentification dans le playground utilise désormais un formulaire Reflex pour une meilleure expérience utilisateur. [#981](https://github.com/etalab-ia/OpenGateLLM/issues/981)
- **RAG:** Suppression de la fonctionnalité RAG. [#956](https://github.com/etalab-ia/OpenGateLLM/issues/956)
- **OCR:** Refonte de l'endpoint `/v1/ocr` vers une architecture plus propre et plus maintenable. [#984](https://github.com/etalab-ia/OpenGateLLM/issues/984)
- **Gestion des utilisateurs:** Refonte de l'endpoint `/v1/admin/users` vers une architecture plus propre. [#962](https://github.com/etalab-ia/OpenGateLLM/issues/962)
- **Gestion des clés API:** Migration de l'endpoint `GET /v1/admin/tokens` vers une architecture plus propre. [#947](https://github.com/etalab-ia/OpenGateLLM/issues/947)
- **Sécurité:** Amélioration de la sécurité en retournant une erreur générique en cas d'identifiants invalides pour empêcher l'énumération des utilisateurs. [#963](https://github.com/etalab-ia/OpenGateLLM/issues/963)

### Évolutions techniques
- **Architecture:** Suppression de `ModelProviderGateway` dans l'administration. [#972](https://github.com/etalab-ia/OpenGateLLM/issues/972)
- **Monitoring:**  Les requêtes non-streaming sont maintenant loguées dans Langfuse. [#987](https://github.com/etalab-ia/OpenGateLLM/issues/987)
- **CI/CD:** Corrections pour ignorer les CVE perl-base bloquant les scans Trivy CRITICAL et pour l'installation des packages nécessaires aux tests E2E. [#969](https://github.com/etalab-ia/OpenGateLLM/issues/969), [#964](https://github.com/etalab-ia/OpenGateLLM/issues/964)
- **Configuration:** Modification de la valeur par défaut des variables d'environnement dans le fichier de configuration d'exemple. [#974](https://github.com/etalab-ia/OpenGateLLM/issues/974)
- **Gestion des dépendances:** Mise à jour de plusieurs dépendances (sharp, svgo, tar, undici, postcss).
- **Documentation:** Mise à jour de la documentation générée et des versions de publication. [#975](https://github.com/etalab-ia/OpenGateLLM/issues/975), [#958](https://github.com/etalab-ia/OpenGateLLM/issues/958)

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) concernant la séparation de la fonctionnalité RAG. [#971](https://github.com/etalab-ia/OpenGateLLM/issues/971)
- Correction pour préférer `0.0` à `None` pour les impacts environnementaux. [#990](https://github.com/etalab-ia/OpenGateLLM/issues/990)
- Correction d'un test d'intégration de la configuration legacy. [#991](https://github.com/etalab-ia/OpenGateLLM/issues/991)
- Ignorer un CVE spécifique pour éviter des problèmes de sécurité bloquants. [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951)
- Améliorations des workflows de release et de semgrep. [#957](https://github.com/etalab-ia/OpenGateLLM/issues/957)
- Publication de la version 0.4.9. [#953](https://github.com/etalab-ia/OpenGateLLM/issues/953)
