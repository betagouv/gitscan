## Changelog : OpenGateLLM (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une série d'améliorations axées sur la robustesse, la sécurité et l'architecture interne. Des refactorings importants ont été effectués pour adopter une architecture plus propre et plus maintenable, notamment au niveau de la gestion des utilisateurs, des clés API et des modèles. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, comme l'ajout d'un bouton de copie pour les clés API et la gestion des documents.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie pour faciliter la duplication des clés API dans l'interface de Playground. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Amélioration de la recherche d'utilisateurs par email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Possibilité de définir des limites de stockage pour les documents. [#899](https://github.com/etalab-ia/OpenGateLLM/issues/899)
- Prise en charge de la vérification de l'état de santé des modèles via l'endpoint `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)
- Correction de la gestion des réponses non-string de l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)
- Augmentation du temps de rafraîchissement d'Elasticsearch à 2 secondes pour améliorer la performance. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Correction d'un bug empêchant le téléchargement de documents de plus de 20MB. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)

### Évolutions techniques
- Refactorisation de l'endpoint `/v1/admin/keys` pour adopter une architecture plus propre. [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933)
- Refactorisation de l'endpoint `/v1/admin/users` et `/v1/admin/users/{user_id}` pour adopter une architecture plus propre. [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898) et [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Refactorisation de l'endpoint `/v1/rerank` pour adopter une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Simplification de la logique de décodage des clés API. [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)
- Séparation de la logique de récupération des modèles en deux use cases distincts. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Correction d'une importation circulaire. [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929)
- Amélioration de la configuration du CI/CD : ajout d'un fichier `.dockerignore` et optimisation de la construction. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901) et [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Injection du contexte dans Langfuse pour le monitoring. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)

### Autres changements
- Mise à jour de la documentation générée. [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916) et [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915) et [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
- Renommage de `user_with_role` en `authenticated_user` pour plus de clarté. [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931)
- Suppression de champs inutiles de `authenticated_user`. [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932)
- Ajout d'un suffixe "id" aux attributs utilisateur et organisation dans l'endpoint de création d'utilisateur. [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934)
- Ajout d'une limite minimale d'âge pour les releases npm. [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907)
