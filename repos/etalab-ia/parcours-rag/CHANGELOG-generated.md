## Changelog : parcours-rag (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le module 3 du parcours RAG, avec des optimisations de performance et des outils d'évaluation plus robustes. Des corrections ont été apportées pour améliorer la précision de l'extraction de citations et la gestion des métadonnées des documents.  Plusieurs dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration du module 3 RAG avec un runtime plus robuste et l'ajout d'outils d'évaluation CP6. [#34](https://github.com/etalab-ia/parcours-rag/pull/34)
- Correction du formatage des citations dans le prompt d'évaluation pour une meilleure précision. [#36bf614](https://github.com/etalab-ia/parcours-rag/commit/36bf614)
- Amélioration de l'analyse des numéros de page dans les citations. [#556b623](https://github.com/etalab-ia/parcours-rag/commit/556b623)

### Évolutions techniques
- Réutilisation de l'instance LibSQLVector pour les appels de récupération afin d'optimiser les performances. [#659f563](https://github.com/etalab-ia/parcours-rag/commit/659f563)
- Préservation des métadonnées par page dans le pipeline de chunking et d'indexation RAG. [#139a7de](https://github.com/etalab-ia/parcours-rag/commit/139a7de)

### Autres changements
- Mise à jour des dépendances suivantes :
    - unpdf (1.6.0 -> 1.6.2)
    - zod (4.3.6 -> 4.4.3)
    - @ai-sdk/*
    - @slidev/cli (52.14.2 -> 52.15.1)
    - mastra/*
    - @biomejs/biome
    - googleapis/release-please-action (4 -> 5)
