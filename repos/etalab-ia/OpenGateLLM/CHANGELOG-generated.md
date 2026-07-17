## Changelog : OpenGateLLM (30 derniers jours, au 11 juillet 2026)

### Résumé
Les dernières mises à jour d'OpenGateLLM se concentrent sur l'amélioration de l'architecture interne, la sécurité et la correction de bugs. Des refactorings importants ont été réalisés sur les endpoints d'authentification et de gestion des clés API, et des vulnérabilités de sécurité ont été corrigées. La fonctionnalité RAG (Retrieval-Augmented Generation) a été supprimée.

### Évolutions fonctionnelles
- Correction d'un bug dans le playground empêchant la propagation du bouton de rôle [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943).
- Amélioration de la gestion des documents : le calcul de la limite est désormais basé sur un tokenizer de tokens, offrant une meilleure précision [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950).
- Correction de la validation des clés API héritées après refactoring [#941](https://github.com/etalab-ia/OpenGateLLM/issues/941).
- Suppression de la fonctionnalité RAG [#956](https://github.com/etalab-ia/OpenGateLLM/issues/956).

### Évolutions techniques
- Refactoring de l'endpoint `/v1/embeddings` pour adopter une architecture plus propre [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945).
- Refactoring des endpoints `/login` et `/v1/admin/keys` pour adopter une architecture plus propre [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937) et [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933).
- Correction d'un problème de fermeture de session dans PostgreSQL lors d'appels aux LLMs pour la complétion de chat [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940).
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation lors de la création d'un utilisateur [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934).
- Améliorations du workflow de release et de l'intégration continue (CI/CD) [#954](https://github.com/etalab-ia/OpenGateLLM/issues/954) et [#957](https://github.com/etalab-ia/OpenGateLLM/issues/957).
- Correction de la publication post-0.4.9 [#953](https://github.com/etalab-ia/OpenGateLLM/issues/953).

### Autres changements
- Ignoré de certaines vulnérabilités (CVE-2026-11940 et CVE-2026-55200) [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951) et [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944).
- Mise à jour de la documentation générée [#958](https://github.com/etalab-ia/OpenGateLLM/issues/958) et [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916).
- Suppression de champs inutiles de l'utilisateur authentifié [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932).
- Renommage de `user_with_role` en `authenticated_user` [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931).
- Ajout d'une durée minimale de publication npm [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907).
