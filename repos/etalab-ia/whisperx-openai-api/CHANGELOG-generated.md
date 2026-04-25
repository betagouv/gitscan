## Changelog : whisperx-openai-api (30 derniers jours, au 23 avril 2026)

### Résumé
Ce projet a connu une phase initiale de développement rapide. L'API est maintenant fonctionnelle et propose la transcription ainsi que la diarisation des locuteurs, tout en respectant le format d'entrée/sortie de l'API OpenAI.  Un système d'intégration continue et de déploiement continu (CI/CD) a été mis en place pour automatiser les tests et le déploiement.

### Évolutions fonctionnelles
- L'API permet désormais de réaliser de la transcription et de la diarisation des locuteurs.
- La diarisation est optionnelle, offrant plus de flexibilité aux utilisateurs.
- L'API est compatible avec le format d'entrée/sortie de l'API OpenAI, facilitant son intégration dans des systèmes existants. [#1](https://github.com/etalab-ia/whisperx-openai-api/issues/1)

### Évolutions techniques
- Mise en place d'un pipeline CI/CD pour automatiser les tests et le déploiement.
- Utilisation de `uv.lock` pour verrouiller les dépendances et assurer la reproductibilité de l'environnement.
- Mise à jour du Dockerfile pour inclure les dépendances nécessaires.
- Initialisation du dépôt avec un premier commit fonctionnel.

### Autres changements
- Ajout d'une documentation initiale (non détaillée dans les commits).
