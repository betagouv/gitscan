## Changelog : parcours-rag (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec le développement du module 3 du parcours RAG. Ce module propose une expérience d'apprentissage complète, incluant des guides pour les formateurs, des diapositives de présentation, des exercices pratiques avec des paliers d'aide progressifs et un index de référence. L'objectif est de faciliter la compréhension et la mise en œuvre des techniques de RAG. Des améliorations de l'infrastructure CI/CD et de la qualité du code ont également été apportées.

### Évolutions fonctionnelles
- Ajout du module 3 au parcours RAG, comprenant :
    - Un guide pour les formateurs détaillant la mise en œuvre d'un atelier de 3 heures [#17](https://github.com/etalab-ia/parcours-rag/pull/17).
    - Des diapositives de présentation (Slidev) pour accompagner la formation [#18](https://github.com/etalab-ia/parcours-rag/pull/18).
    - Un système d'indices progressifs pour aider les apprenants à traverser les différents checkpoints [#16](https://github.com/etalab-ia/parcours-rag/pull/16).
    - Un index de référence avec 5 questions d'évaluation pour valider la compréhension des concepts [#13](https://github.com/etalab-ia/parcours-rag/pull/13).
    - Une structure de checkpoints (CP1 à CP6) avec des instructions claires et des exemples [#14](https://github.com/etalab-ia/parcours-rag/pull/14), [#15](https://github.com/etalab-ia/parcours-rag/pull/15).
- Intégration du corpus ANSSI Essentiels (17 PDFs) pour servir de base aux exercices pratiques [#2](https://github.com/etalab-ia/parcours-rag/pull/2).
- Mise en place d'un environnement Mastra de base avec la passerelle Albert pour le checkpoint 1 [#1](https://github.com/etalab-ia/parcours-rag/pull/1).

### Évolutions techniques
- Mise à jour des dépendances :
    - TypeScript (5.9.3 -> 6.0.3)
    - `@ai-sdk` packages
    - `pnpm/action-setup` (4 -> 6)
    - `actions/checkout` (4 -> 6)
    - `actions/setup-node` (4 -> 6)
    - `softprops/action-gh-release` (2 -> 3)
- Refactorisation du code pour améliorer la structure et la maintenabilité, notamment dans le module 3.
- Amélioration de la configuration CI/CD avec l'ajout d'outils comme Biome pour le linting et le formatage du code [#4](https://github.com/etalab-ia/parcours-rag/pull/4).
- Utilisation de markdown pour les liens dans l'index des checkpoints pour une meilleure lisibilité [#12](https://github.com/etalab-ia/parcours-rag/pull/12).

### Autres changements
- Documentation : Amélioration de la documentation du module 3, notamment concernant les types publics et les références aux checkpoints [#20](https://github.com/etalab-ia/parcours-rag/pull/20), [#21](https://github.com/etalab-ia/parcours-rag/pull/21), [#22](https://github.com/etalab-ia/parcours-rag/pull/22).
- Ajout d'un fichier `manifest.json` et correction d'une erreur de newline [#4](https://github.com/etalab-ia/parcours-rag/pull/4).
- Ajout d'une description du design du module 3 [#19](https://github.com/etalab-ia/parcours-rag/pull/19).
