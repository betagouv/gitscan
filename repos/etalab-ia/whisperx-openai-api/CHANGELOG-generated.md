## Changelog : whisperx-openai-api (30 derniers jours, au 7 mai 2026)

### Résumé
Ce projet a connu un développement initial rapide, passant d'un commit initial à une API fonctionnelle avec support de plusieurs formats de sortie et une configuration optimisée pour la production. L'accent a été mis sur la compatibilité avec l'API OpenAI, la performance et la flexibilité.

### Évolutions fonctionnelles
- Ajout de la possibilité de générer des transcriptions et des informations de diarisation au format JSON, SRT et VTT. [#3](https://github.com/etalab-ia/whisperx-openai-api/issues/3)
- La diarisation est désormais optionnelle, offrant plus de flexibilité aux utilisateurs. [#1](https://github.com/etalab-ia/whisperx-openai-api/issues/1)
- Ajout du support pour le format texte en sortie. [#2](https://github.com/etalab-ia/whisperx-openai-api/issues/2)
- Adaptation de l'API pour correspondre au schéma d'entrée/sortie OpenAI, facilitant l'intégration avec d'autres outils. [#1](https://github.com/etalab-ia/whisperx-openai-api/issues/1)
- Mise à jour de la taille par défaut du batch à 32 pour améliorer le débit. [#2](https://github.com/etalab-ia/whisperx-openai-api/issues/2)

### Évolutions techniques
- Optimisation des performances et préparation pour un déploiement en production. [#2](https://github.com/etalab-ia/whisperx-openai-api/issues/2)
- Mise à jour de la configuration CUDA pour supporter les GPU H200. [#3](https://github.com/etalab-ia/whisperx-openai-api/issues/3)
- Implémentation d'une intégration CI/CD pour automatiser les tests et le déploiement.
- Modification du type de l'ID des segments de `str` à `int`.
- Mise à jour du Dockerfile pour une meilleure gestion des dépendances.
- Ajout d'un fichier `uv.lock` pour verrouiller les versions des dépendances uvicorn.

### Autres changements
- Mise à jour de la documentation README.md pour refléter les nouvelles fonctionnalités et la configuration.
- Initialisation du projet et premiers commits.
