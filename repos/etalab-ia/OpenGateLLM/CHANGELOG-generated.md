## Changelog : OpenGateLLM (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes d'architecture interne, de sécurité et de gestion des documents. Des refactorings importants ont été effectués pour adopter une architecture plus propre et plus maintenable, notamment pour les utilisateurs, les clés API et les embeddings. La sécurité a été renforcée en corrigeant une potentielle énumération d'utilisateurs et en gérant des vulnérabilités connues. La gestion des documents a également été optimisée avec l'introduction d'un tokenizer pour le comptage de tokens.

### Évolutions fonctionnelles
- **Authentification:** Correction d'une faille de sécurité permettant d'éviter l'énumération des utilisateurs via les erreurs d'authentification. [#963](https://github.com/etalab-ia/OpenGateLLM/issues/963)
- **Gestion des documents:**  Amélioration du comptage de tokens pour la gestion des documents, remplaçant le calcul par taille par un tokenizer. [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950)
- **Playground:** Correction d'un problème de propagation de bouton dans l'interface Playground. [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943)
- **RAG:** Suppression de la fonctionnalité RAG (Retrieval Augmented Generation). [#956](https://github.com/etalab-ia/OpenGateLLM/issues/956)

### Évolutions techniques
- **Architecture:** Refactoring majeur de l'endpoint `/v1/admin/users` pour adopter une architecture plus propre. [#962](https://github.com/etalab-ia/OpenGateLLM/issues/962)
- **Architecture:** Migration de l'endpoint `/v1/admin/tokens` vers une architecture plus propre. [#947](https://github.com/etalab-ia/OpenGateLLM/issues/947)
- **Architecture:** Refactoring de l'endpoint `/v1/embeddings` pour adopter une architecture plus propre. [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945)
- **CI/CD:** Améliorations du workflow de release et de l'intégration continue (Semgrep, Trivy). [#957](https://github.com/etalab-ia/OpenGateLLM/issues/957)
- **CI/CD:** Correction de problèmes bloquant les scans de sécurité Trivy. [#969](https://github.com/etalab-ia/OpenGateLLM/issues/969)
- **Dépendances:** Mise à jour de la version de `rich` pour éviter un conflit de versions. [#973](https://github.com/etalab-ia/OpenGateLLM/issues/973)

### Autres changements
- **Documentation:** Mise à jour de la documentation générée et des versions de release. [#958](https://github.com/etalab-ia/OpenGateLLM/issues/958) et [#975](https://github.com/etalab-ia/OpenGateLLM/issues/975)
- **Configuration:** Modification des variables d'environnement par défaut dans le fichier `config.example`. [#974](https://github.com/etalab-ia/OpenGateLLM/issues/974)
- **Sécurité:** Ignorance temporaire de certaines CVE (Common Vulnerabilities and Exposures) pour permettre la progression des builds. [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951) et [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944)
- **Architecture Decision Record (ADR):** Ajout d'un ADR concernant la séparation de la fonctionnalité RAG. [#971](https://github.com/etalab-ia/OpenGateLLM/issues/971)
- **Corrections post-release:** Corrections mineures après la release 0.4.9. [#953](https://github.com/etalab-ia/OpenGateLLM/issues/953)
