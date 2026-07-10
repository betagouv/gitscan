## Changelog : OpenGateLLM (30 derniers jours, au 7 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une refonte architecturale significative de plusieurs de ses composants clés, notamment l'authentification, la gestion des clés API et les embeddings. Ces améliorations visent à rendre le code plus maintenable, plus testable et à préparer le projet pour de futures évolutions. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles

- Amélioration du calcul de la limite des documents en utilisant un tokenizer pour une gestion plus précise des tokens [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950).
- Correction d'un bug empêchant la propagation du bouton de rôle dans l'interface de Playground [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943).
- Correction de la validation des clés API héritées après la refactorisation [#941](https://github.com/etalab-ia/OpenGateLLM/issues/941).
- Correction d'un problème de fermeture de session dans PostgreSQL lors de l'appel aux LLMs pour la complétion de chat [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940).
- Ajout de la possibilité de rechercher des utilisateurs par adresse e-mail [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909).
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation lors de la création d'un utilisateur [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934).
- Amélioration de l'état de santé des modèles en appelant l'endpoint `/metrics` [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911).

### Évolutions techniques

- Refactorisation de l'endpoint `/v1/embeddings` pour adopter une architecture plus propre [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945).
- Refactorisation de l'authentification (endpoint `/login`) vers une architecture plus propre [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937).
- Refactorisation de l'endpoint `/v1/admin/keys` vers une architecture plus propre [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933).
- Refactorisation de l'endpoint `/rerank` pour une architecture plus propre [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905).
- Simplification de la logique de décodage des clés API [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930).
- Déplacement des schémas d'administration dans un dossier dédié [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928).
- Correction d'un import circulaire [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929).
- Mise à jour de la documentation générée et des versions de publication [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916) et [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915).
- Suppression des champs inutiles de `authenticated_user` [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932).
- Renommage de `user_with_role` en `authenticated_user` [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931).

### Autres changements

- Correction de la release après la publication de la version 0.4.9 [#953](https://github.com/etalab-ia/OpenGateLLM/issues/953).
- Mise à jour du workflow de release [#954](https://github.com/etalab-ia/OpenGateLLM/issues/954).
- Ignorance de certaines vulnérabilités (CVE-2026-11940 et CVE-2026-55200) [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951) et [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944).
- Ajout d'une durée minimale de publication pour npm [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907).
