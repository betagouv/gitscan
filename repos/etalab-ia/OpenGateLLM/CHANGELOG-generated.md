## Changelog : OpenGateLLM (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de santé des modèles, de gestion des fichiers audio, et de robustesse générale. Des corrections ont été apportées à la documentation et au processus de déploiement, et des optimisations ont été réalisées pour améliorer la performance et la sécurité. L'intégration avec Langfuse a également été améliorée.

### Évolutions fonctionnelles
- Ajout d'un support de vérification de l'état de santé des modèles, permettant de s'assurer de leur disponibilité et de leur bon fonctionnement. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Amélioration du support des fichiers audio : ajout des formats SRT et VTT, et support de la transcription audio diarizée. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855), [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- Intégration améliorée avec Langfuse pour le suivi de l'utilisation. [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812)
- Correction de la base URL pour Langfuse. [#868](https://github.com/etalab-ia/OpenGateLLM/issues/868)
- Correction de la fermeture des fichiers PDF après lecture pour éviter les fuites de ressources. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)

### Évolutions techniques
- Refactorisation du code lié à la gestion des modèles, notamment la séparation de la logique de récupération des modèles en deux cas d'utilisation distincts. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Refactorisation du code lié à la gestion des utilisateurs (renommage de `UserInfoRepo`). [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865)
- Optimisation du nombre de shards Elasticsearch par défaut (réduction de 24 à 12). [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829)
- Amélioration de la configuration des modèles pour un code plus propre. [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823)
- Corrections et améliorations du workflow de documentation et de déploiement. [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836), [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838), [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862)
- Correction de problèmes liés à l'analyse de vulnérabilités avec Trivy et ajout d'exceptions pour certaines CVE. [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857)
- Correction d'une erreur WebSocket dans le playground. [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828)
- Suppression de préfixes inutiles dans les messages d'erreur. [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826)
- Suppression d'imports inutiles dans le domaine des modèles. [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822)
- Correction de la gestion des routes Prometheus pour une meilleure granularité. [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824)

### Autres changements
- Correction mineure de l'interface utilisateur du playground. [#860](https://github.com/etalab-ia/OpenGateLLM/issues/860)
- Ajout d'un nouveau document à la documentation déployée du playground. [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854)
- Renommage du fichier `bootstrapadmin`. [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)
- Création d'une image de playground privée pour une sécurité accrue. [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835)
- Mise à jour des versions des paquets.
