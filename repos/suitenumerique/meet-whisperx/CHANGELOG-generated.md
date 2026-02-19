## Changelog : meet-whisperx (30 derniers jours)

### Résumé
Les dernières mises à jour de meet-whisperx améliorent la configuration et la flexibilité de l'API, notamment en passant à une configuration basée sur des variables d'environnement. Des optimisations ont également été apportées pour réduire la taille des dépendances et simplifier l'installation. Une nouvelle version (v1.2.0) a été publiée.

### Évolutions fonctionnelles
- Préchargement des modèles d'alignement audio pour une meilleure performance. (#95d31fe)
- Clarification des paramètres de configuration des modèles. (#95d31fe)

### Évolutions techniques
- Passage de la configuration par arguments en ligne de commande à des variables d'environnement pour une plus grande flexibilité et une meilleure gestion des secrets. (#94d1b8a)
- Réorganisation des dépendances dans `pyproject.toml` pour une meilleure clarté. (#3f11ad7)
- Matplotlib est maintenant une dépendance de développement optionnelle, réduisant la taille de l'installation de base. (#35860b5, #0d875be)
- Suppression du fichier `compose.yaml` inutilisé. (#f9ebe45)
- Suppression des guillemets autour des chemins absolus dans le fichier docker-compose. (#f88762a)
- Dépendance explicite sur `transformers` version 4.x. (#10e9366)

### Autres changements
- Ajout d'un fichier `.env.example` pour faciliter la configuration de l'API. (#d9d99ef)
- Mise à jour du fichier `.gitignore` pour ignorer les fichiers liés à un agent IA et à un éditeur. (#9444bc4)
- Publication de la version v1.2.0. (#d84ab5b)
