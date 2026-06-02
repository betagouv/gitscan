## Changelog : OpenGateLLM (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de gestion des modèles, de sécurité et de stabilité. Des corrections ont été apportées pour une meilleure compatibilité avec différentes APIs de modèles de langage, notamment Mistral. L'administration des utilisateurs a été refactorisée pour une architecture plus propre. Des améliorations de l'interface utilisateur du playground et de la gestion des formats audio ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'un support pour la vérification de l'état de santé des modèles, permettant de s'assurer de leur disponibilité et de leur bon fonctionnement. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Prise en charge de nouveaux formats audio (srt/vtt) pour la transcription audio, offrant plus de flexibilité aux utilisateurs. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855)
- Correction de la gestion des réponses non-string de l'API Mistral, améliorant la compatibilité avec ce modèle. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)
- Correction de l'ID des segments audio pour la transcription, assurant un fonctionnement correct. [#859](https://github.com/etalab-ia/OpenGateLLM/issues/859)
- Correction de l'URL de base pour Langfuse, améliorant l'intégration avec cet outil de monitoring. [#868](https://github.com/etalab-ia/OpenGateLLM/issues/868)

### Évolutions techniques
- Refactorisation de l'endpoint `/v1/admin/users` pour adopter une architecture plus propre et maintenable. [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893) et [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Refactorisation du `getmodelsusecase` en deux use cases distincts pour une meilleure organisation du code. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Renommage de `userinforepo` pour une meilleure clarté du code. [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865)
- Renommage du fichier `bootstrapadmin` pour une meilleure cohérence. [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)
- Amélioration du pipeline CI/CD pour inclure des analyses de vulnérabilités avec Trivy et ignorer certaines exceptions connues. [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872), [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857)
- Injection du contexte dans Langfuse pour un meilleur suivi des performances. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891), [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862), [#858](https://github.com/etalab-ia/OpenGateLLM/issues/858)
- Correction mineure de l'interface utilisateur du playground. [#860](https://github.com/etalab-ia/OpenGateLLM/issues/860)
- Ajout d'une nouvelle documentation pour le playground déployé. [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854)
- Corrections liées à la release 0.4.3 du playground. [#856](https://github.com/etalab-ia/OpenGateLLM/issues/856)
