## Changelog : OpenGateLLM (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes d'architecture logicielle, de gestion des documents et de robustesse des modèles. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme. L'interface utilisateur a été légèrement améliorée avec l'ajout d'un bouton de copie pour les clés API.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie pour faciliter la duplication des clés API dans l'interface utilisateur. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Amélioration de la gestion des documents : la taille maximale des chunks de documents est désormais limitée à 20MB. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Ajout de la limitation du stockage des documents. [#899](https://github.com/etalab-ia/OpenGateLLM/issues/899)
- Prise en charge de la vérification de l'état de santé des modèles. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Gestion améliorée des réponses non-string de l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)

### Évolutions techniques
- Refactorisation importante de l'endpoint `rerank` pour une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Refactorisation des endpoints `/v1/admin/users/{user_id}`, `/v1/admin/users` et `POST /v1/admin/users` vers une architecture plus propre. [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893), [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Séparation du use case `getmodelsusecase` en deux use cases distincts pour une meilleure organisation. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Augmentation du `refresh_interval` d'Elasticsearch à 2 secondes pour une meilleure performance. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Injection du contexte dans Langfuse pour un meilleur suivi. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)

### Autres changements
- Amélioration du pipeline CI/CD : ajout d'un fichier `.dockerignore` et optimisation de la construction des images Docker. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901), [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Ignorer certaines vulnérabilités (CVE) dans les analyses de sécurité Trivy. [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872)
- Mise à jour de la documentation générée et des versions de publication. [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
