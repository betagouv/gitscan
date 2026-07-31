## Changelog : OpenGateLLM (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, de refactoring architectural et de correction de bugs. Des efforts ont été déployés pour améliorer la robustesse du pipeline CI/CD et la gestion des utilisateurs. La fonctionnalité RAG (Retrieval-Augmented Generation) a été temporairement supprimée pour permettre des refontes futures.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs d'authentification : Retour d'une erreur générique "invalid-credentials" pour éviter l'énumération des utilisateurs [#963](https://github.com/etalab-ia/OpenGateLLM/issues/963).
- Intégration de la tokenisation pour le comptage des tokens dans les documents [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950).
- Construction du corps de la requête pour les modèles avec les champs de modèle définis [#977](https://github.com/etalab-ia/OpenGateLLM/issues/977).
- Enregistrement des requêtes non-streaming dans Langfuse pour une meilleure traçabilité [#987](https://github.com/etalab-ia/OpenGateLLM/issues/987).

### Évolutions techniques
- Refactoring de l'architecture pour plusieurs endpoints :
    - `/v1/admin/users` vers une architecture plus propre [#962](https://github.com/etalab-ia/OpenGateLLM/issues/962).
    - `/v1/admin/tokens` vers une architecture plus propre [#947](https://github.com/etalab-ia/OpenGateLLM/issues/947).
    - `/v1/embeddings` vers une architecture plus propre [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945).
- Suppression du `ModelProviderGateway` dans le cadre d'une refactorisation [#972](https://github.com/etalab-ia/OpenGateLLM/issues/972).
- Suppression temporaire de la fonctionnalité RAG pour permettre une refonte ultérieure [#956](https://github.com/etalab-ia/OpenGateLLM/issues/956).
- Mise à jour de la configuration par défaut des variables d'environnement [#974](https://github.com/etalab-ia/OpenGateLLM/issues/974).
- Amélioration du workflow de release et de l'intégration continue (CI/CD) [#957](https://github.com/etalab-ia/OpenGateLLM/issues/957) et [#968](https://github.com/etalab-ia/OpenGateLLM/issues/968).
- Correction des problèmes liés aux CVEs bloquant les scans Trivy critiques [#969](https://github.com/etalab-ia/OpenGateLLM/issues/969).

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) concernant la séparation de la fonctionnalité RAG [#971](https://github.com/etalab-ia/OpenGateLLM/issues/971).
- Mise à jour de la documentation générée et des versions de release [#958](https://github.com/etalab-ia/OpenGateLLM/issues/958) et [#975](https://github.com/etalab-ia/OpenGateLLM/issues/975).
- Correction de conflits de versions de paquets (rich) [#973](https://github.com/etalab-ia/OpenGateLLM/issues/973).
- Ignorer une CVE spécifique pour éviter des faux positifs [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951).
