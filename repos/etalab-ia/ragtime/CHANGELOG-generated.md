## Changelog : ragtime (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec un changement de nom de "rag-facile" à "ragtime".  Des améliorations significatives ont été apportées à la gestion des collections via une nouvelle interface en ligne de commande (CLI).  Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été implémentées, notamment concernant l'authentification et la configuration initiale.

### Évolutions fonctionnelles
- Ajout d'une interface en ligne de commande (CLI) complète pour la gestion des collections (création, activation, désactivation). [#214](https://github.com/etalab-ia/ragtime/pull/214)
- Amélioration de l'authentification dans Chainlit, qui est désormais conditionnelle à la configuration de Supabase. [#216](https://github.com/etalab-ia/ragtime/pull/216)
- Lors de la configuration initiale, le script affiche désormais les prochaines étapes au lieu de démarrer automatiquement le serveur de développement. [#215](https://github.com/etalab-ia/ragtime/pull/215)
- Demande du mot de passe lors de la saisie de la clé API pour une meilleure sécurité. [#216](https://github.com/etalab-ia/ragtime/pull/216)

### Évolutions techniques
- Suppression de l'agentic harness et de la commande `ragtime learn`. [#217](https://github.com/etalab-ia/ragtime/pull/217)
- Renommage du projet de "rag-facile" à "ragtime", impactant les workflows et le script d'installation. [#211](https://github.com/etalab-ia/ragtime/pull/211)
- Mise à jour de la configuration `wt.toml` pour utiliser `pre-start` au lieu de `post-create` (déprécié). [#225](https://github.com/etalab-ia/ragtime/pull/225)
- Ajout de `supabase` et `asyncpg` comme dépendances pour Chainlit lors de la configuration. [#216](https://github.com/etalab-ia/ragtime/pull/216)
- Correction de tests pour supporter les codes ANSI et confirmer correctement les actions. [#214](https://github.com/etalab-ia/ragtime/pull/214)

### Autres changements
- Mise à jour de la documentation README avec les nouvelles informations sur le projet et l'ajout d'un badge d'état alpha. [#213](https://github.com/etalab-ia/ragtime/pull/213)
- Ajout de `.ragtime/` à `.gitignore`. [#225](https://github.com/etalab-ia/ragtime/pull/225)
- Mises à jour des dépendances : `pydf` (6.8.0 -> 6.9.1), `ruff-pre-commit` (0.15.7).
