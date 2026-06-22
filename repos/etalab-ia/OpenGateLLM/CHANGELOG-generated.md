## Changelog : OpenGateLLM (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'importantes améliorations en termes d'architecture et de sécurité, notamment au niveau de l'authentification et de la gestion des utilisateurs. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'ajout d'une limite de stockage pour les documents et la gestion des vulnérabilités dans le CI/CD sont également des points notables.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie pour les clés API dans l'interface de playground. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Possibilité de rechercher des utilisateurs par adresse email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Gestion des réponses non-string de l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)
- Limitation du stockage des documents à 20MB par document. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation lors de la création d'un utilisateur. [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934)
- La santé des modèles est maintenant vérifiée via l'endpoint `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)

### Évolutions techniques
- Refactorisation importante de l'authentification vers une architecture plus propre. [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937)
- Refactorisation de l'endpoint POST `/v1/admin/keys` vers une architecture plus propre. [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933)
- Refactorisation de l'endpoint `/rerank` vers une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Refactorisation de l'endpoint DELETE `/v1/admin/users/{user_id}` vers une architecture plus propre. [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898)
- Refactorisation de l'endpoint GET `/v1/admin/users` vers une architecture plus propre. [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893)
- Simplification de la logique de décodage des clés API. [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)
- Correction d'une importation circulaire. [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929)
- Optimisation du CI/CD : Ignorer les CVE et optimiser le build. [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Variable de l'intervalle de rafraîchissement Elasticsearch. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)

### Autres changements
- Mise à jour de la documentation générée. [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915), [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
- Ajout d'un fichier `.dockerignore`. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901)
- Renommage de `user_with_role` en `authenticated_user`. [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931)
- Suppression des champs inutiles de `authenticated_user`. [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932)
- Ajout d'une durée minimale de publication npm. [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907)
