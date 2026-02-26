## Changelog : meet-whisperx (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'API meet-whisperx au cours des 30 derniers jours. Les changements incluent des améliorations de la configuration, des tests automatisés, une meilleure gestion des modèles audio et une réduction de la taille des dépendances. Une nouvelle version (v1.2.0) a également été publiée.

### Évolutions fonctionnelles
- Préchargement des modèles d'alignement audio pour une meilleure performance. (#95d31fe)
- Clarification des paramètres de configuration des modèles audio. (#95d31fe)
- Publication de la version 1.2.0. (#d84ab5b)

### Évolutions techniques
- Ajout de tests HTTP avec simulation de la couche d'inférence pour garantir la robustesse de l'API. (#03fa382)
- Intégration de l'exécution des tests dans le pipeline CI/CD. (#c051279)
- Passage de `pip` à `uv` pour le verrouillage des dépendances, améliorant la reproductibilité et la gestion des dépendances. (#f7d0c4c)
- Refactorisation des dépendances dans `pyproject.toml` pour une meilleure organisation. (#3f11ad7)
- Déplacement de la dépendance `matplotlib` vers les dépendances de développement, réduisant la taille de l'installation de base. (#35860b5, #0d875be)
- Définition explicite de la dépendance à `transformers` version 4.x. (#10e9366)
- Suppression du fichier `compose.yaml` non utilisé. (#f9ebe45)
- Suppression des guillemets autour des chemins absolus dans le fichier docker-compose. (#f88762a)

### Autres changements
- Ajout d'un fichier `.env.example` pour faciliter la configuration de l'application. (#d9d99ef)
- Passage de la configuration par arguments en ligne de commande à des variables d'environnement. (#94d1b8a)
- Mise à jour du fichier `.gitignore` pour ignorer les fichiers créés par les agents et éditeurs d'IA. (#9444bc4)
