## Changelog : parcours-rag (30 derniers jours, au 21 avril 2026)

### Résumé
Le projet a connu une évolution majeure avec l'ajout du module 3, axé sur la mise en pratique du RAG (Retrieval-Augmented Generation). Ce module comprend un guide pour les animateurs, des exercices progressifs (hint ladders) et des exemples concrets d'implémentation. Des améliorations ont également été apportées à l'infrastructure CI/CD pour faciliter le développement et le déploiement.

### Évolutions fonctionnelles
- Ajout du module 3 au parcours RAG, comprenant un guide pour les animateurs d'atelier [#17](https://github.com/etalab-ia/parcours-rag/pull/17).
- Implémentation de "hint ladders" (échelles d'indices) pour les checkpoints 1 à 6 du module 3, facilitant l'apprentissage progressif [#16](https://github.com/etalab-ia/parcours-rag/pull/16), [#15](https://github.com/etalab-ia/parcours-rag/pull/15), [#14](https://github.com/etalab-ia/parcours-rag/pull/14).
- Ajout d'un index de référence RAG avec 5 questions d'évaluation [#13](https://github.com/etalab-ia/parcours-rag/pull/13).
- Intégration du corpus ANSSI Essentiels (17 PDFs) pour l'entraînement et l'évaluation des modèles RAG [#1](https://github.com/etalab-ia/parcours-rag/pull/1).
- Mise en place d'une structure de base pour les compétences (skills) Mastra [#3](https://github.com/etalab-ia/parcours-rag/pull/3), [#2](https://github.com/etalab-ia/parcours-rag/pull/2), [#1](https://github.com/etalab-ia/parcours-rag/pull/1).

### Évolutions techniques
- Mise à jour des actions GitHub pour les versions de release-please, checkout et setup-node [#6](https://github.com/etalab-ia/parcours-rag/pull/6), [#7](https://github.com/etalab-ia/parcours-rag/pull/7), [#8](https://github.com/etalab-ia/parcours-rag/pull/8).
- Configuration de l'outil de linting et de formattage de code Biome, avec intégration dans le pipeline CI/CD [#4](https://github.com/etalab-ia/parcours-rag/pull/4).
- Utilisation de `pnpm` pour la gestion des dépendances.
- Harmonisation des "hint ladders" pour une meilleure cohérence entre les checkpoints.

### Autres changements
- Amélioration de la documentation et des liens Markdown pour une meilleure lisibilité et une navigation plus intuitive [#14](https://github.com/etalab-ia/parcours-rag/pull/14), [#13](https://github.com/etalab-ia/parcours-rag/pull/13).
- Ajout d'un document de conception pour l'atelier du module 3, précisant les décisions prises.
- Correction de divers problèmes mineurs et amélioration de la structure du code.
