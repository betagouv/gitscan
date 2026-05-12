## Changelog : OpenGateLLM (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, de fonctionnalités audio et de refactoring interne pour une meilleure maintenabilité et performance. L'interface du playground a également été peaufinée et la gestion des documents a été optimisée.

### Évolutions fonctionnelles
- **Audio :** Ajout du support des formats SRT et VTT pour la transcription audio [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855).
- **Audio :** Intégration de la transcription diarizée, permettant d'identifier les différents locuteurs dans un fichier audio [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832).
- **Gestion documentaire :** Correction d'un bug où les fichiers PDF n'étaient pas correctement fermés après lecture, ce qui pouvait entraîner des problèmes de performance [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833).
- **Monitoring :** Amélioration du monitoring Prometheus en utilisant des motifs de routes au lieu d'URL complètes, pour une meilleure lisibilité et maintenabilité [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824).
- **Intégrations :** Ajout du support de Langfuse pour le suivi de l'utilisation des modèles [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812).
- **Sécurité :** Création d'une image Docker privée pour le playground, renforçant la sécurité des environnements de test [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835).
- **Playground :** Correction d'erreurs liées à la mise à niveau de Reflex dans le playground [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828) et correction d'une erreur de validation de la longueur du mot de passe [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809).
- **Playground :** Ajout d'un nouveau document à la démo du playground [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854) et correction de petits problèmes d'interface [#860](https://github.com/etalab-ia/OpenGateLLM/issues/860).

### Évolutions techniques
- **Refactoring :** Refactorisation importante des modèles et de la gestion des providers de modèles pour une architecture plus propre et maintenable [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796), [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823).
- **Refactoring :** Refactorisation des endpoints liés aux rôles d'administration pour une meilleure cohérence avec l'architecture du projet [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808).
- **CI/CD :** Mise en place d'un scan de vulnérabilités avec Trivy et déploiement automatisé des releases [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857).
- **Elasticsearch :** Réduction du nombre de shards Elasticsearch par défaut de 24 à 12 pour optimiser les performances [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829).
- **Documentation :** Mise à jour de la documentation générée automatiquement et des versions des releases [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838), [#862](https://github.com/etalab-ia/OpenGateLLM/issues/862).
- **Nommage :** Renommage de certains répertoires et fichiers pour une meilleure cohérence et lisibilité [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864), [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865).

### Autres changements
- Correction de la configuration du workflow de documentation [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836), [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837).
- Suppression de préfixes inutiles dans les messages d'erreur [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826).
- Suppression d'imports inutiles dans le domaine des modèles [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822).
- Correction d'un problème où le modèle Whisper recevait une langue par défaut incorrecte [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819).
- Mise à jour des versions des packages et dépendances [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830).
