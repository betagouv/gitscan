## Changelog : OpenGateLLM (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, de gestion des documents audio et de refactoring interne pour une meilleure architecture et maintenabilité. Des corrections de bugs et des optimisations ont également été apportées, notamment au niveau du playground et de l'intégration avec Langfuse.

### Évolutions fonctionnelles
- Ajout de la prise en charge des formats SRT et VTT pour l'audio. [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855)
- Prise en charge de la transcription audio diarizée. [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- Intégration de Langfuse pour le suivi de l'utilisation des modèles. [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812)
- Possibilité de créer une image de playground privée pour une sécurité accrue. [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835)
- Correction d'un bug qui fermait incorrectement les fichiers PDF après lecture. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)
- Correction d'une erreur dans le playground liée à une mise à niveau de Reflex. [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828)
- Correction d'une erreur empêchant la définition d'un mot de passe trop long dans le playground. [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809)
- Correction du code de langue par défaut pour Whisper, passant de "english" à "en". [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807)

### Évolutions techniques
- Refactoring important des modèles pour une architecture plus propre et plus maintenable. [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823), [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796), [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822)
- Refactoring des endpoints liés à la gestion des rôles pour une meilleure architecture. [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808)
- Optimisation du nombre de shards Elasticsearch par défaut, réduit de 24 à 12. [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829)
- Amélioration de la gestion des URLs dans les métriques Prometheus, en utilisant des patterns de routes. [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824)
- Correction de la configuration des versions des packages. [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830)
- Mise à jour du workflow de documentation. [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836)

### Autres changements
- Mise à jour de la documentation et des versions générées. [#858](https://github.com/etalab-ia/OpenGateLLM/issues/858), [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838)
- Ajout d'un nouveau document au playground déployé. [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854)
- Mise à jour de Node et Astro dans la documentation. [#840](https://github.com/etalab-ia/OpenGateLLM/issues/840), [#839](https://github.com/etalab-ia/OpenGateLLM/issues/839)
- Corrections liées au bootstrap de l'administration. [#827](https://github.com/etalab-ia/OpenGateLLM/issues/827)
- Suppression de préfixes inutiles dans les messages d'erreur. [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826)
- Ajout d'un scan Trivy et déploiement de release via GitHub Actions. [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857)
- Corrections du playground (version 0.4.3). [#856](https://github.com/etalab-ia/OpenGateLLM/issues/856)
