## Changelog : OpenGateLLM (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une refonte architecturale importante, visant à améliorer la maintenabilité et l'extensibilité du code. Plusieurs endpoints ont été migrés vers une architecture plus propre, notamment ceux liés à l'authentification, aux clés API, aux embeddings et aux utilisateurs. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau du playground et de la gestion des documents.

### Évolutions fonctionnelles
- Amélioration du playground : ajout d'un bouton de copie pour les clés API nouvellement créées [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896).
- Correction d'un bug empêchant la propagation du bouton de rôle dans le playground [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943).
- Possibilité de rechercher des utilisateurs par adresse e-mail [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909).
- Augmentation de la taille maximale des documents uploadés à 20MB [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902).
- Amélioration de la santé des modèles via l'appel à l'endpoint `/metrics` [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911).
- Correction d'un bug lié à la validation des clés API héritées [#941](https://github.com/etalab-ia/OpenGateLLM/issues/941).
- Correction d'un problème de fermeture de session PostgreSQL lors de l'appel aux LLMs en mode chat completion [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940).

### Évolutions techniques
- Refactorisation de l'endpoint `/login` vers une architecture plus propre [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937).
- Refactorisation de l'endpoint `/v1/embeddings` vers une architecture plus propre [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945).
- Refactorisation de l'endpoint `/v1/admin/keys` vers une architecture plus propre [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933).
- Refactorisation de l'endpoint `/v1/rerank` vers une architecture plus propre [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905).
- Refactorisation de l'endpoint `DELETE /v1/admin/users/{user_id}` vers une architecture plus propre [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898).
- Simplification de la logique de décodage des clés API [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930).
- Déplacement des schémas d'administration dans un dossier dédié [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928).
- Correction d'un import circulaire [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929).
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation dans l'endpoint de création d'utilisateur [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934).
- Modification de la variable `refresh_interval` d'Elasticsearch pour une meilleure performance [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904).
- Mise à jour de la documentation générée [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915).

### Autres changements
- Ignorer une vulnérabilité CVE-2026-55200 dans libssh2 [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944).
- Optimisation du build CI/CD et ignore des CVEs [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900).
- Ajout d'un fichier `.dockerignore` [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901).
- Ajout d'une durée minimale de publication pour les releases npm [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907).
- Suppression de champs inutiles de l'objet `authenticated_user` [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932).
- Renommage de `user_with_role` en `authenticated_user` [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931).
- Mise à jour de la dépendance `tmp` dans les documents [#895](https://github.com/etalab-ia/OpenGateLLM/issues/895).
