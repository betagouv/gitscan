## Changelog : OpenGateLLM (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement sur OpenGateLLM se sont concentrés sur l'amélioration de l'architecture interne du projet, notamment en adoptant une approche "clean architecture" pour plusieurs endpoints de l'API. Des corrections de bugs et des optimisations ont également été apportées, ainsi que des améliorations de l'expérience utilisateur, comme l'ajout d'un bouton de copie pour les clés API et la gestion de la taille des documents.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie pour les clés API dans l'interface de création, facilitant leur utilisation. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Possibilité de rechercher des utilisateurs par adresse email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Limitation du stockage des documents pour une meilleure gestion des ressources. [#899](https://github.com/etalab-ia/OpenGateLLM/issues/899)
- Augmentation de la taille maximale des documents pouvant être uploadés à 20MB. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Amélioration de la santé des modèles en utilisant l'endpoint `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)

### Évolutions techniques
- Refactoring important de plusieurs endpoints de l'API (login, gestion des clés API, suppression d'utilisateurs, récupération d'utilisateurs) vers une architecture plus propre et maintenable ("clean architecture"). [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937), [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933), [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893)
- Refactoring de l'endpoint de rerank pour adopter une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Correction d'un problème de session PostgreSQL qui pouvait survenir lors d'appels aux LLMs en mode chat. [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940)
- Simplification de la logique de décodage des clés API. [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930)
- Correction d'une importation circulaire. [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)
- Ajout d'un suffixe "id" aux attributs d'utilisateur et d'organisation lors de la création d'un utilisateur. [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915)
- Amélioration du CI/CD : ajout d'un fichier `.dockerignore` et optimisation du build en ignorant les CVE. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901), [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Modification du nom de la variable `user_with_role` en `authenticated_user`. [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931)
- Suppression de champs inutiles de l'utilisateur authentifié. [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932)
- Variabilisation du `refresh_interval` pour Elasticsearch. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Ajout d'un minimum d'âge pour les releases npm. [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907)
