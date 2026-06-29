## Changelog : hydra (30 derniers jours, au 22 juin 2026)

### Résumé
Les dernières mises à jour de Hydra apportent des améliorations à la robustesse du système, notamment des corrections de bugs et des ajustements de configuration. Une nouvelle fonctionnalité permet d'inclure la version de Python dans l'endpoint de santé, facilitant le monitoring. Des optimisations de performance ont été réalisées avec le passage à Python 3.14. Des modifications importantes ont été apportées à la gestion des formats de données, avec une introduction puis une réversion temporaire de nouvelles fonctionnalités.

### Évolutions fonctionnelles
- L'endpoint de santé inclut désormais la version de Python utilisée, facilitant le diagnostic des problèmes liés à l'environnement d'exécution. [#433](https://github.com/datagouv/hydra/pull/433)
- Ajout d'un champ `header` lors de l'analyse des fichiers Parquet. [#431](https://github.com/datagouv/hydra/pull/431)
- Amélioration du silence des logs avec l'option `--quiet` dans l'interface en ligne de commande (CLI), qui s'applique désormais à tous les loggers. [#432](https://github.com/datagouv/hydra/pull/432)
- Introduction puis suppression temporaire de la gestion des formats de données. [#430](https://github.com/datagouv/hydra/pull/430)

### Évolutions techniques
- Passage à Python 3.14 pour des gains de performance. [#378](https://github.com/datagouv/hydra/pull/378)
- Refactorisation de l'interface en ligne de commande (CLI). [#437](https://github.com/datagouv/hydra/pull/437)
- Mise à jour de la dépendance `urllib3` pour corriger une vulnérabilité de sécurité (GHSA-mf9v-mfxr-j63j). [#420](https://github.com/datagouv/hydra/pull/420)
- Amélioration de la couverture des tests avec l'ajout de nouveaux tests unitaires. [#434](https://github.com/datagouv/hydra/pull/434)
- Refactorisation des tests existants. [#435](https://github.com/datagouv/hydra/pull/435)
- Utilisation du jeton UV recommandé pour la publication sur PyPI. [#451](https://github.com/datagouv/hydra/pull/451)

### Autres changements
- Mise à jour de la documentation README pour refléter le comportement actuel de l'API, de la CLI et des workers. [#439](https://github.com/datagouv/hydra/pull/439)
- Suppression des cibles `storage_path` obsolètes. [#450](https://github.com/datagouv/hydra/pull/450)
- Correction d'une erreur dans la documentation des queues RQ.
- Correction d'une erreur dans la gestion des couches OGC. [#440](https://github.com/datagouv/hydra/pull/440)
