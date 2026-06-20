## Changelog : OpenGateLLM (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, d'architecture et de fonctionnalités. Les efforts se sont concentrés sur la refactorisation du code pour une meilleure maintenabilité et l'implémentation de nouvelles fonctionnalités comme la gestion des limites de stockage des documents et l'amélioration de la santé des modèles. Des corrections de bugs et des optimisations de performance ont également été apportées pour une expérience utilisateur plus fluide.

### Évolutions fonctionnelles
- Amélioration de la recherche d'utilisateurs par email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Ajout d'un bouton de copie pour les clés API dans l'interface de jeu (playground). [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Limitation du stockage des documents à 20MB par document. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Gestion améliorée du contenu non-string renvoyé par l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)
- La santé des modèles est maintenant vérifiée en appelant l'endpoint `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)
- Ajout d'un suffixe "id" aux attributs d'utilisateur et d'organisation lors de la création d'un utilisateur. [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934)

### Évolutions techniques
- Refactorisation importante de l'architecture de plusieurs endpoints : `/login`, `/v1/admin/keys`, `/v1/admin/users/{user_id}`, `/v1/admin/users`, `/rerank` vers une architecture plus propre. [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937), [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933), [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867), [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Simplification de la logique de décodage des clés API. [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930)
- Correction d'une importation circulaire. [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)
- Variable de l'intervalle de rafraîchissement d'Elasticsearch. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Injection du contexte dans Langfuse pour le monitoring. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)
- Optimisation du build CI/CD et gestion des vulnérabilités (CVE). [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Ajout d'un fichier `.dockerignore`. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901)
- Renommage de `user_with_role` en `authenticated_user`. [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931)
- Suppression de champs inutiles de `authenticated_user`. [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915), [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
- Ajout d'une durée minimale de publication npm. [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907)
- Correction de la revue post-commit. [#938](https://github.com/etalab-ia/OpenGateLLM/issues/938)
