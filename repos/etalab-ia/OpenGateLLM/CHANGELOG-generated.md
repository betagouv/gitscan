## Changelog : OpenGateLLM (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de fonctionnalités audio, de gestion documentaire et de sécurité. Des corrections de bugs et des refactorings ont également été réalisés pour améliorer la stabilité et la maintenabilité du projet. L'interface du playground a été peaufinée et l'intégration avec Langfuse a été ajoutée pour le suivi de l'utilisation.

### Évolutions fonctionnelles
- **Audio :** Ajout de la prise en charge des formats SRT et VTT pour les transcriptions audio [#855](https://github.com/etalab-ia/OpenGateLLM/issues/855).
- **Audio :** Support de la transcription audio diarizée [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832).
- **Gestion documentaire :** Correction d'un bug où les fichiers PDF n'étaient pas correctement fermés après lecture [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833).
- **Intégrations :** Ajout de la prise en charge de Langfuse pour le suivi de l'utilisation des modèles [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812).
- **Sécurité :** Création d'une image Docker privée pour le playground, améliorant la sécurité des déploiements [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835).
- **Playground :** Corrections diverses de l'interface utilisateur [#856](https://github.com/etalab-ia/OpenGateLLM/issues/856) et correction d'une erreur liée à la mise à niveau de Reflex [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828).

### Évolutions techniques
- **Refactoring :** Refactorisation des modèles de configuration pour une architecture plus propre [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823) et des providers de modèles [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796).
- **Architecture :** Refactorisation des endpoints liés aux rôles d'administration vers une architecture plus propre [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808).
- **Elasticsearch :** Réduction du nombre de shards Elasticsearch par défaut de 24 à 12 pour optimiser les performances [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829).
- **Monitoring :** Correction des URLs dans les métriques Prometheus, en utilisant des patterns de routes pour une meilleure identification [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824).
- **CI/CD :** Mise en place d'un workflow de déploiement incluant un scan Trivy pour la sécurité [#857](https://github.com/etalab-ia/OpenGateLLM/issues/857).
- **Documentation :** Mise à jour du workflow de documentation et des documents déployés sur le playground [#854](https://github.com/etalab-ia/OpenGateLLM/issues/854), [#840](https://github.com/etalab-ia/OpenGateLLM/issues/840), [#839](https://github.com/etalab-ia/OpenGateLLM/issues/839), [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836).

### Autres changements
- Correction du code de langue par défaut pour Whisper de "english" à "en" [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807).
- Correction d'une erreur dans le playground concernant la longueur maximale du mot de passe [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809).
- Suppression de préfixes inutiles dans les messages d'erreur [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826).
- Suppression d'imports inutiles dans les modèles [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822).
- Mise à jour des versions des paquets [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830).
