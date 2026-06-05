## Changelog : transport-validator (30 derniers jours, au 4 juin 2026)

### Résumé
Cette mise à jour améliore la performance et la stabilité du validateur de données GTFS en production. Plus précisément, elle introduit un allocateur mémoire plus efficace par défaut, ce qui permet de réduire la consommation de mémoire et d'optimiser les performances globales.

### Évolutions techniques
- Passage à l'allocateur mémoire `jemalloc` par défaut pour améliorer la consommation mémoire en production. [#241](https://github.com/etalab/transport-validator/issues/241)
