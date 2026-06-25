## Changelog : OpenGateLLM (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une série d'améliorations axées sur la sécurité, l'architecture et la robustesse. Les efforts se sont concentrés sur la refactorisation du code pour une meilleure maintenabilité, l'amélioration de la gestion des utilisateurs et des clés API, ainsi que la correction de bugs pour une expérience plus stable. Des améliorations ont également été apportées à la gestion des documents et à la surveillance de l'état des modèles.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie lors de la création d'une clé API dans le playground [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896).
- Possibilité de rechercher des utilisateurs par adresse email [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909).
- Limitation du stockage des documents à 20MB par document [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902).
- Amélioration de la gestion des modèles Mistral pour supporter les réponses non-string [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892).
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation lors de la création d'un utilisateur [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934).
- L'état de santé des modèles est maintenant vérifié via l'endpoint `/metrics` [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911).

### Évolutions techniques
- Refactorisation importante de l'architecture pour plusieurs endpoints : `/login` [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937), `/v1/admin/keys` [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933), `/v1/admin/users/{user_id}` [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), `/rerank` [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905) vers une architecture plus propre.
- Correction d'une importation circulaire [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929).
- Déplacement des schémas d'administration dans un dossier dédié [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928).
- Simplification de la logique de décodage des clés API [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930).
- Amélioration de la gestion de la session PostgreSQL pour éviter les problèmes lors de l'appel aux LLMs [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940).
- Modification du nom de `user_with_role` en `authenticated_user` pour plus de clarté [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931).
- Suppression de champs inutiles de `authenticated_user` [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932).
- Variable de rafraîchissement d'Elasticsearch pour une meilleure performance [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904).

### Autres changements
- Mise à jour de la documentation générée [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915).
- Ajout d'un fichier `.dockerignore` [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901).
- Optimisation du processus CI/CD et gestion des vulnérabilités [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900).
- Ajout d'une durée minimale de publication des releases npm [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907).
- Mise à jour de la dépendance `tmp` dans les documents [#895](https://github.com/etalab-ia/OpenGateLLM/issues/895).
- Correction de bugs liés à l'authentification [#938](https://github.com/etalab-ia/OpenGateLLM/issues/938).
