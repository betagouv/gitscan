## Changelog : OpenGateLLM (30 derniers jours, au 5 juillet 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'une refonte architecturale significative, notamment au niveau de l'authentification, de la gestion des clés API et des embeddings. Des améliorations ont été apportées à la gestion des utilisateurs et à la santé des modèles, ainsi que des corrections de bugs et des optimisations de sécurité.

### Évolutions fonctionnelles
- Amélioration de la gestion des documents : remplacement du limiteur de caractères par un tokenizer pour une meilleure gestion des entrées. [#950](https://github.com/etalab-ia/OpenGateLLM/issues/950)
- Correction d'un bug empêchant la propagation du bouton de rôle dans l'interface de playground. [#943](https://github.com/etalab-ia/OpenGateLLM/issues/943)
- Correction de la validation des clés API héritées après refactorisation. [#941](https://github.com/etalab-ia/OpenGateLLM/issues/941)
- Amélioration de la recherche d'utilisateurs par email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Ajout d'un endpoint de santé pour vérifier l'état des modèles via l'appel `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)
- Correction d'un problème de schéma pour l'annotation de documents Mistral. [#946](https://github.com/etalab-ia/OpenGateLLM/issues/946)
- Correction d'un problème de fermeture de session PostgreSQL lors de l'appel aux LLMs pour la complétion de chat. [#940](https://github.com/etalab-ia/OpenGateLLM/issues/940)

### Évolutions techniques
- Refactorisation de l'endpoint `/v1/embeddings` pour une architecture plus propre. [#945](https://github.com/etalab-ia/OpenGateLLM/issues/945)
- Refactorisation de l'authentification (endpoint `/login`) vers une architecture plus propre. [#937](https://github.com/etalab-ia/OpenGateLLM/issues/937)
- Refactorisation de l'endpoint `/v1/admin/keys` vers une architecture plus propre. [#933](https://github.com/etalab-ia/OpenGateLLM/issues/933)
- Refactorisation de l'endpoint `/rerank` vers une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Simplification de la logique de décodage des clés API. [#930](https://github.com/etalab-ia/OpenGateLLM/issues/930)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)
- Correction d'une importation circulaire. [#929](https://github.com/etalab-ia/OpenGateLLM/issues/929)
- Ajout de suffixes "id" aux attributs utilisateur et organisation dans l'endpoint de création d'utilisateur. [#934](https://github.com/etalab-ia/OpenGateLLM/issues/934)
- Renommage de `user_with_role` en `authenticated_user`. [#931](https://github.com/etalab-ia/OpenGateLLM/issues/931)
- Suppression de champs inutiles de `authenticated_user`. [#932](https://github.com/etalab-ia/OpenGateLLM/issues/932)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#916](https://github.com/etalab-ia/OpenGateLLM/issues/916), [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915)
- Ajout d'une durée minimale de publication pour les paquets npm. [#907](https://github.com/etalab-ia/OpenGateLLM/issues/907)
- Ignorance de certaines vulnérabilités (CVE-2026-11940, CVE-2026-55200) après analyse. [#951](https://github.com/etalab-ia/OpenGateLLM/issues/951), [#944](https://github.com/etalab-ia/OpenGateLLM/issues/944)
