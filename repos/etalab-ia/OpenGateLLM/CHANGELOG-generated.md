## Changelog : OpenGateLLM (30 derniers jours, au 23 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de gestion des utilisateurs, de santé des modèles, de support audio et d'intégration avec Langfuse pour le suivi de l'utilisation. Des corrections de bugs et des améliorations de la documentation et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout du support de vérification de l'état de santé des modèles, permettant de s'assurer de leur disponibilité et de leur bon fonctionnement. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Prise en charge des formats SRT et VTT pour la transcription audio. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855)
- Ajout du support de la transcription audio diarizée. [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- Intégration avec Langfuse pour le suivi de l'utilisation des modèles. [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812)
- Correction d'un bug empêchant la fermeture correcte des fichiers PDF après lecture. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)
- Correction de l'URL de base pour Langfuse. [#868](https://github.com/etalab-ia/OpenGateLLM/issues/868)
- Correction d'un bug concernant l'ID des segments audio pour la transcription. [#859](https://github.com/etalab-ia/OpenGateLLM/issues/859)

### Évolutions techniques
- Refactorisation de l'endpoint `/v1/admin/users` pour une meilleure architecture. [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Séparation du `getmodelsusecase` en deux use cases distincts pour une meilleure modularité. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Renommage de `userinforepo` pour une meilleure clarté. [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865)
- Création d'une image Docker privée pour le playground, améliorant la sécurité. [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835)
- Optimisation du nombre de shards Elasticsearch par défaut. [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829)
- Correction des versions des paquets pour assurer la cohérence. [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830)
- Amélioration du workflow de déploiement de la documentation. [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836) [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#858](https://github.com/etalab-ia/OpenGateLLM/issues/858) [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862) [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891) [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838)
- Corrections mineures de l'interface utilisateur du playground. [#860](https://github.com/etalab-ia/OpenGateLLM/issues/860)
- Ajout d'une nouvelle documentation au playground déployé. [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854)
- Ignorer certaines vulnérabilités (CVE) dans les scans de sécurité Trivy. [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872) [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873) [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874)
- Correction du workflow de scan et de déploiement avec Trivy. [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857)
- Corrections suite au déploiement de la version 0.4.3 du playground. [#856](https://github.com/etalab-ia/OpenGateLLM/issues/856)
- Renommage du fichier `bootstrapadmin`. [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)
