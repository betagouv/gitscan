## Changelog : ragtime (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec un changement de nom, passant de "rag-facile" à "ragtime".  Des améliorations significatives ont été apportées à la gestion des collections via une nouvelle interface en ligne de commande (CLI).  Des corrections de bugs et des améliorations de la configuration ont également été implémentées, notamment pour l'authentification et l'installation.

### Évolutions fonctionnelles
- Ajout d'une interface en ligne de commande (CLI) complète pour la gestion des collections, permettant d'activer, désactiver et gérer les collections de documents. [#214](https://github.com/etalab-ia/ragtime/pull/214)
- Amélioration de l'authentification dans Chainlit pour qu'elle soit conditionnelle à la configuration de Supabase. [#216](https://github.com/etalab-ia/ragtime/pull/216)
- Modification du script d'installation pour afficher les prochaines étapes au lieu de démarrer automatiquement le serveur de développement. [#215](https://github.com/etalab-ia/ragtime/pull/215)
- Mise à jour de la documentation pour refléter le nouveau nom du projet et son statut "alpha". [#213](https://github.com/etalab-ia/ragtime/pull/213) et [#208](https://github.com/etalab-ia/ragtime/pull/208)

### Évolutions techniques
- Renommage du projet de "rag-facile" à "ragtime", impactant les workflows, les scripts d'installation et la documentation. [#211](https://github.com/etalab-ia/ragtime/pull/211)
- Suppression de la fonctionnalité "agentic harness" et de la commande `ragtime learn`. [#217](https://github.com/etalab-ia/ragtime/pull/217) et [#219](https://github.com/etalab-ia/ragtime/pull/219)
- Mise à jour des dépendances : pydpdf (6.8.0 -> 6.9.1) et ruff-pre-commit. [#210](https://github.com/etalab-ia/ragtime/pull/210) et [#209](https://github.com/etalab-ia/ragtime/pull/209)
- Amélioration de la gestion des erreurs et des tests pour la CLI de gestion des collections.

### Autres changements
- Mise à jour de la documentation README avec des liens corrects et l'ajout d'un badge indiquant le statut "alpha" du projet.
- Ajout d'un message d'avertissement concernant le statut "tech preview" du projet.
- Corrections mineures de la mise en forme du README.
- Mise à jour de la configuration `wt.toml` pour utiliser `pre-start` au lieu de `post-create`.
- Ajout de `.ragtime/` à `.gitignore`.
- Bump des packages workspace à la version 0.25.0 et activation de l'auto-installation dans `.prototools`.
