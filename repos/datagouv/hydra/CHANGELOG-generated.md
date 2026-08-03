## Changelog : hydra (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations à la robustesse du traitement des fichiers compressés (gzip), des corrections pour la gestion des requêtes HTTP et des ajustements pour l'alignement entre l'API et l'interface en ligne de commande. Une mise à jour de la librairie `csv-detective` est également incluse.

### Évolutions fonctionnelles
- Amélioration de la résilience lors de la décompression de fichiers gzip corrompus [#467](https://github.com/datagouv/hydra/pull/467).
- L'outil en ligne de commande `check resource` est maintenant aligné avec l'API [#459](https://github.com/datagouv/hydra/pull/459).

### Évolutions techniques
- Mise à jour de la librairie `csv-detective` vers la version 0.12.0 [#463](https://github.com/datagouv/hydra/pull/463).
- Correction d'un problème lié au fallback des requêtes HEAD [#460](https://github.com/datagouv/hydra/pull/460).
- Refactorisation des utilitaires de base de données (partiellement revertée) [#452](https://github.com/datagouv/hydra/pull/452).
- Ajout d'une migration pour la table `resources_exceptions` [#457](https://github.com/datagouv/hydra/pull/457).

### Autres changements
- Mise à jour du fichier `.gitignore` [#458](https://github.com/datagouv/hydra/pull/458).
- Publication de la version 2.13.1 [#461](https://github.com/datagouv/hydra/pull/461).
