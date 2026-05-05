## Changelog : whisperx-openai-api (30 derniers jours, au 29 avril 2026)

### Résumé
Ce projet a connu un démarrage rapide avec la mise en place d'une API compatible OpenAI pour la transcription et la diarisation audio basée sur WhisperX. Les récentes améliorations se concentrent sur l'optimisation des performances, la flexibilité de la configuration et la préparation pour un déploiement en production, notamment grâce à l'ajout d'un pipeline CI/CD.

### Évolutions fonctionnelles
- Ajout du support pour le format texte en entrée.
- La diarisation est désormais optionnelle.
- L'API est maintenant compatible avec le schéma d'entrée/sortie OpenAI standard. [#1](https://github.com/etalab-ia/whisperx-openai-api/issues/1)
- Amélioration des performances et préparation pour la production. [#2](https://github.com/etalab-ia/whisperx-openai-api/issues/2)
- Augmentation de la taille du batch par défaut à 32 pour de meilleures performances.

### Évolutions techniques
- Mise en place d'un pipeline CI/CD pour l'automatisation des tests et du déploiement.
- Mise à jour du Dockerfile pour une meilleure gestion des dépendances.
- Ajout d'un fichier `uv.lock` pour verrouiller les versions des dépendances Uvicorn.
- Initialisation du dépôt et configuration de base.

### Autres changements
- Mise à jour de la documentation README.md pour refléter les dernières évolutions.
