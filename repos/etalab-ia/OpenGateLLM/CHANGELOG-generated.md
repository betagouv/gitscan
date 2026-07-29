## Changelog : OpenGateLLM (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes d'architecture interne, de sécurité et de gestion des modèles. Des refactorings importants ont été effectués pour adopter une architecture plus propre et plus maintenable, notamment pour les utilisateurs, les clés API et les embeddings. La sécurité a été renforcée en corrigeant une potentielle énumération d'utilisateurs et en gérant des vulnérabilités connues.

### Évolutions fonctionnelles
- Amélioration de la gestion des clés API : migration de l'endpoint GET /v1/admin/tokens vers une nouvelle architecture plus propre [#947](https://github.com/etalab-ia/OpenGateLLM/issues/947).
- Amélioration de la gestion des utilisateurs : refactoring de l'endpoint /v1/admin/users pour une architecture plus propre [#962](https://github.com/etalab-ia/OpenGateLLM/issues/962).
- Correction d'un problème dans le playground empêchant la propagation du bouton de rôle [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943).
- Amélioration de la construction du corps de la requête pour les modèles, avec la prise en compte des champs de fichiers de modèles [#977](https://github.com/etalab-ia/OpenGateLLM/issues/977).
- Remplacement du calcul de limite de documents par un tokenizer de tokens [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950).
- Correction de la validation des clés API legacy après refactoring [#941](https://github.com/etalab-ia/OpenGateLLM/issues/941).

### Évolutions techniques
- Refactoring de l'endpoint POST /v1/embeddings vers une architecture plus propre [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945).
- Suppression de la fonctionnalité RAG (Retrieval-Augmented Generation) [#956](https://github.com/etalab-ia/OpenGateLLM/issues/956).
- Améliorations du workflow de CI/CD : correction de problèmes liés à l'installation de packages pour les tests E2E et la documentation [#964](https://github.com/etalab-ia/OpenGateLLM/issues/964), [#968](https://github.com/etalab-ia/OpenGateLLM/issues/968), [#957](https://github.com/etalab-ia/OpenGateLLM/issues/957).
- Correction d'un problème de conflit de version avec le package `rich` [#973](https://github.com/etalab-ia/OpenGateLLM/issues/973).
- Correction pour ignorer des CVEs bloquant les scans Trivy critiques [#969](https://github.com/etalab-ia/OpenGateLLM/issues/969).
- Amélioration de la gestion des erreurs d'authentification pour éviter l'énumération d'utilisateurs [#963](https://github.com/etalab-ia/OpenGateLLM/issues/963).

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) concernant la séparation de la fonctionnalité RAG [#971](https://github.com/etalab-ia/OpenGateLLM/issues/971).
- Mise à jour de la documentation générée [#975](https://github.com/etalab-ia/OpenGateLLM/issues/975), [#958](https://github.com/etalab-ia/OpenGateLLM/issues/958).
- Modification des variables d'environnement par défaut dans le fichier de configuration d'exemple [#974](https://github.com/etalab-ia/OpenGateLLM/issues/974).
- Ignorance de certaines CVEs pour des librairies spécifiques [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951), [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944).
