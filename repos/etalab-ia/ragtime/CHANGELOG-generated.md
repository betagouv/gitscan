## Changelog : ragtime (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet ragtime a connu des changements importants, notamment la suppression de la fonctionnalité "agentic harness" et de la commande `ragtime learn`. Ces modifications visent à simplifier le projet et à se concentrer sur ses fonctionnalités principales. Des améliorations ont également été apportées à la gestion des collections et à la configuration initiale.

### Évolutions fonctionnelles
- Suppression de la fonctionnalité "agentic harness" et de la commande `ragtime learn` ([#217](https://github.com/etalab-ia/ragtime/pull/217)).
- Ajout d'une gestion complète des collections via l'interface en ligne de commande (CLI) ([#219](https://github.com/etalab-ia/ragtime/pull/219)).
- Lors de la configuration initiale, le serveur de développement ne démarre plus automatiquement, mais affiche les prochaines étapes à suivre ([#217](https://github.com/etalab-ia/ragtime/pull/217)).

### Évolutions techniques
- Refactorisation du code pour supprimer la fonctionnalité "agentic harness" et la commande `ragtime learn` ([609e987](https://github.com/etalab-ia/ragtime/commit/609e987a767687ccf687d5f881787b0ef9761440)).
- Mise à jour de la configuration `wt.toml` pour utiliser `pre-start` au lieu de `post-create` (déprécié) ([fe0ddbd](https://github.com/etalab-ia/ragtime/commit/fe0ddbd)).
- Mise à jour des packages du workspace vers la version 0.25.0 et activation de l'installation automatique avec `prototools` ([b88e69b](https://github.com/etalab-ia/ragtime/commit/b88e69b)).

### Autres changements
- Ajout de `.ragtime/` au fichier `.gitignore` ([59cbe0b](https://github.com/etalab-ia/ragtime/commit/59cbe0b)).
- Renommage du projet de "rag-facile" à "ragtime" ([15a1969](https://github.com/etalab-ia/ragtime/commit/15a1969d67e8f79a79c99d3138381c888287d386)).
- Correction de l'art ASCII du logo RAGTIME dans le README et dans l'application ([78913bc](https://github.com/etalab-ia/ragtime/commit/78913bcc4c9437513a17cacf27ff979046890a85), [c8376d2](https://github.com/etalab-ia/ragtime/commit/c8376d2f7c5b0356bdd5470869ff1206692e73b3)).
