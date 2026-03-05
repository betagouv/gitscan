## Changelog : meet-whisperx (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à l'API meet-whisperx, qui permet de transcrire de l'audio en utilisant le modèle Whisper d'OpenAI. Les changements incluent des améliorations de la configuration, de la gestion des dépendances, de l'ajout de tests et de l'optimisation de l'environnement de développement. Une nouvelle version (v1.2.0) a également été publiée.

### Évolutions fonctionnelles
- Amélioration du chargement des modèles d'alignement audio et clarification des paramètres de modèle.
- Publication de la version 1.2.0 [#d84ab5b](https://github.com/suitenumerique/meet-whisperx/commit/d84ab5b).

### Évolutions techniques
- Passage de `pip` à `uv` pour la gestion des dépendances, améliorant la reproductibilité et la performance. [#f7d0c4c](https://github.com/suitenumerique/meet-whisperx/commit/f7d0c4c)
- Ajout de tests HTTP en simulant la couche d'inférence pour valider l'API. [#03fa382](https://github.com/suitenumerique/meet-whisperx/commit/03fa382)
- Ajout de l'exécution des tests à la pipeline CI. [#c051279](https://github.com/suitenumerique/meet-whisperx/commit/c051279)
- Déplacement de la dépendance `matplotlib` vers les dépendances de développement optionnelles, réduisant la taille de l'installation de base. [#35860b5](https://github.com/suitenumerique/meet-whisperx/commit/35860b5)
- Spécification explicite de la dépendance à `transformers` version 4.x. [#10e9366](https://github.com/suitenumerique/meet-whisperx/commit/10e9366)
- Suppression du fichier `compose.yaml` inutilisé. [#f9ebe45](https://github.com/suitenumerique/meet-whisperx/commit/f9ebe45)
- Suppression des guillemets autour des chemins absolus dans le fichier docker-compose. [#f88762a](https://github.com/suitenumerique/meet-whisperx/commit/f88762a)

### Autres changements
- Reconfiguration de l'application pour utiliser des variables d'environnement au lieu d'arguments en ligne de commande. [#94d1b8a](https://github.com/suitenumerique/meet-whisperx/commit/94d1b8a)
- Ajout d'un fichier `.env.example` pour faciliter la configuration. [#d9d99ef](https://github.com/suitenumerique/meet-whisperx/commit/d9d99ef)
- Réorganisation des dépendances dans le fichier `pyproject.toml`. [#3f11ad7](https://github.com/suitenumerique/meet-whisperx/commit/3f11ad7)
- Mise à jour du fichier `.gitignore` pour ignorer les fichiers liés à un agent IA et à un éditeur. [#9444bc4](https://github.com/suitenumerique/meet-whisperx/commit/9444bc4)
- Ajout de contraintes sur les dépendances. [#9643c28](https://github.com/suitenumerique/meet-whisperx/commit/9643c28)
