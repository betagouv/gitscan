## Changelog : ragtime (30 derniers jours, au 31 mars 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec un changement de nom de "rag-facile" à "ragtime".  De plus, des améliorations significatives ont été apportées à la gestion des collections via une nouvelle interface en ligne de commande (CLI), ainsi qu'à l'intégration avec Chainlit, notamment en matière d'authentification et de persistance des données. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une interface en ligne de commande (CLI) complète pour la gestion des collections : création, activation, désactivation. [#198](https://github.com/etalab-ia/ragtime/pull/198) [#809140d](https://github.com/etalab-ia/ragtime/commit/809140d80bb383c6827e39fb42d4a9dc2e1fbeec)
- Amélioration de l'intégration avec Chainlit :
    - L'authentification est désormais conditionnelle à la configuration de Supabase. [#217](https://github.com/etalab-ia/ragtime/pull/217)
    - Affichage du nom d'utilisateur (display name) correct dans le menu utilisateur Chainlit.
    - Lecture du nom d'affichage (display_name) à partir des métadonnées utilisateur Supabase.
- Modification du script d'installation pour afficher les prochaines étapes au lieu de démarrer automatiquement le serveur de développement. [#215](https://github.com/etalab-ia/ragtime/pull/215)
- Amélioration de la gestion des erreurs lors de l'initialisation du projet (git). [#200](https://github.com/etalab-ia/ragtime/pull/200)
- Ajout de commandes CLI pour l'accès aux traces. [#203](https://github.com/etalab-ia/ragtime/pull/203)

### Évolutions techniques
- Renommage du projet de "rag-facile" à "ragtime" : modification des workflows, du script d'installation et de la documentation. [#211](https://github.com/etalab-ia/ragtime/pull/211)
- Suppression du "agentic harness" et de la commande `ragtime learn`. [#219](https://github.com/etalab-ia/ragtime/pull/219)
- Mise à jour des dépendances :
    - `pypdf` vers la version 6.9.1 [#210](https://github.com/etalab-ia/ragtime/pull/210)
    - `ruff-pre-commit` vers la version 0.15.7 et 0.15.5 [#202](https://github.com/etalab-ia/ragtime/pull/202) [#209](https://github.com/etalab-ia/ragtime/pull/209)
    - `pyjwt` vers la version 2.12.0 [#204](https://github.com/etalab-ia/ragtime/pull/204)
- Amélioration de la configuration de la persistance. [#206](https://github.com/etalab-ia/ragtime/pull/206)
- Corrections et améliorations des migrations de la base de données.

### Autres changements
- Mise à jour de la documentation :
    - Correction des URL du dépôt.
    - Ajout d'un badge indiquant le statut "alpha".
    - Clarification de la nécessité d'utiliser l'URL API de Supabase.
    - Ajout d'une notification concernant le statut de "tech preview" archivé.
- Ajout d'un fichier `.ragtime/` à `.gitignore`.
- Mise à jour de la configuration `wt.toml` pour utiliser `pre-start` au lieu de `post-create`.
- Correction de l'art ASCII de RAGTIME dans le README.
