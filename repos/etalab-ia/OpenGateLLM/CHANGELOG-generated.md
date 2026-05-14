## Changelog : OpenGateLLM (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, de gestion audio, de documentation et de refactoring interne. L'ajout de la prise en charge de Langfuse pour le suivi de l'utilisation, ainsi que des corrections de bugs et des optimisations de performance, contribuent à une expérience utilisateur plus stable et enrichie. Des efforts importants ont également été déployés pour améliorer l'architecture interne du projet et la qualité du code.

### Évolutions fonctionnelles
- **Audio :** Ajout de la prise en charge des formats SRT et VTT pour la transcription audio. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855)
- **Audio :** Prise en charge de la transcription audio diarizée. [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- **Intégrations :** Ajout de la prise en charge de Langfuse pour le suivi de l'utilisation des modèles. [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812)
- **Playground :** Corrections diverses de l'interface utilisateur et du comportement du playground. [#856](https://github.com/etalab-ia/OpenGateLLM/issues/856), [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828), [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809)
- **Sécurité :** Création d'une image Docker privée pour le playground afin d'améliorer la sécurité. [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835)
- **Documents :** Correction d'un bug qui empêchait la fermeture correcte des fichiers PDF après lecture. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)

### Évolutions techniques
- **Architecture :** Refactoring important de l'architecture interne, notamment des modèles et des gestionnaires de modèles, pour un code plus propre et plus maintenable. [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796), [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823)
- **API :** Suppression de l'endpoint `/v1/admin/roles` et refactoring des endpoints liés aux rôles pour une meilleure cohérence architecturale. [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808)
- **Monitoring :** Modification des URLs utilisées pour les métriques Prometheus afin d'utiliser des motifs de route plus génériques. [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824)
- **Elasticsearch :** Réduction du nombre de shards Elasticsearch par défaut de 24 à 12 pour optimiser les performances. [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829)
- **CI/CD :** Amélioration du workflow de déploiement avec l'ajout d'un scan Trivy. [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857)

### Autres changements
- **Documentation :** Mise à jour de la documentation générée et des versions publiées. [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862), [#858](https://github.com/etalab-ia/OpenGateLLM/issues/858), [#840](https://github.com/etalab-ia/OpenGateLLM/issues/840), [#839](https://github.com/etalab-ia/OpenGateLLM/issues/839), [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838), [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836)
- **Code :** Renommage de certains fichiers et variables pour une meilleure lisibilité et cohérence. [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865), [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)
- **Corrections :** Correction d'un bug lié à l'envoi du langage par défaut au modèle Whisper. [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819)
- **Divers :** Suppression de préfixes inutiles dans les messages d'erreur et suppression d'imports inutiles. [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826), [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822)
