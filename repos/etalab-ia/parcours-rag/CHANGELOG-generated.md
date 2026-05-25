## Changelog : parcours-rag (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le module 3 du parcours RAG, avec des optimisations de performance et des outils d'évaluation. Des corrections ont également été apportées pour améliorer la précision de l'indexation et de la récupération d'informations, notamment en ce qui concerne la gestion des citations et des métadonnées des pages. Enfin, les dépendances du projet ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration du module 3 avec un renforcement de l'exécution RAG et l'ajout d'outils d'évaluation CP6. [#34](https://github.com/etalab-ia/parcours-rag/pull/34)
- Amélioration du formatage des citations dans les prompts d'évaluation pour une plus grande précision. [#36bf614](https://github.com/etalab-ia/parcours-rag/commit/36bf614)
- Correction de l'analyse des numéros de page dans les citations, permettant la gestion des numéros avec ou sans point. [#556b623](https://github.com/etalab-ia/parcours-rag/commit/556b623)

### Évolutions techniques
- Optimisation de la réutilisation de l'instance LibSQLVector pour les appels de récupération, améliorant ainsi les performances. [#659f563](https://github.com/etalab-ia/parcours-rag/commit/659f563)
- Préservation des métadonnées de page lors du pipeline d'indexation et de chunking RAG pour une meilleure granularité des informations. [#139a7de](https://github.com/etalab-ia/parcours-rag/commit/139a7de)

### Autres changements
- Mise à jour des dépendances :
    - unpdf (1.6.0 -> 1.6.2)
    - zod (4.3.6 -> 4.4.3)
    - @ai-sdk/*
    - @slidev/cli (52.14.2 -> 52.15.1)
    - mastra/*
    - @biomejs/biome
    - googleapis/release-please-action (4 -> 5)
