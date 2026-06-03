## Changelog : parcours-rag (30 derniers jours, au 5 mai 2026)

### Résumé
Ce changelog fait état d'améliorations significatives du module 3, notamment en termes de robustesse et d'outils d'évaluation. Des corrections ont été apportées pour améliorer la précision de l'extraction de citations et l'efficacité du pipeline RAG, notamment en optimisant l'utilisation de la base de données vectorielle LibSQL. Des mises à jour de dépendances ont également été intégrées pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Amélioration du module 3 avec l'ajout d'outils d'évaluation CP6 et une meilleure robustesse générale. [#34](https://github.com/etalab-ia/parcours-rag/pull/34)
- Amélioration de la précision de l'extraction des numéros de page dans les citations. [#36bf614](https://github.com/etalab-ia/parcours-rag/commit/36bf614)
- Amélioration de l'analyse des citations pour imposer un format explicite. [#36bf614](https://github.com/etalab-ia/parcours-rag/commit/36bf614)

### Évolutions techniques
- Optimisation de l'utilisation de l'instance LibSQLVector pour améliorer les performances du pipeline de récupération. [#659f563](https://github.com/etalab-ia/parcours-rag/commit/659f563)
- Préservation des métadonnées de page dans le pipeline de création d'index et de chunking RAG. [#139a7de](https://github.com/etalab-ia/parcours-rag/commit/139a7de)
- Mise à jour de l'action `release-please` pour bénéficier des dernières améliorations. [#4053ae6](https://github.com/etalab-ia/parcours-rag/commit/4053ae6)

### Autres changements
- Mise à jour des dépendances : `unpdf` (1.6.0 -> 1.6.2), `zod` (4.3.6 -> 4.4.3), `@slidev/cli` (52.14.2 -> 52.15.1), `@ai-sdk/*` et `mastra/*`. Ces mises à jour sont gérées par Dependabot et visent à maintenir la sécurité et la compatibilité du projet.
