## Changelog : parcours-rag (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec le développement du module 3, axé sur l'implémentation et l'évaluation de techniques de RAG (Retrieval-Augmented Generation).  Ce module comprend la création d'un squelette de skill, l'ajout de corpus de données (ANSSI Essentiels), et la mise en place d'un environnement de test et d'évaluation. Des améliorations ont également été apportées à l'infrastructure CI/CD et aux dépendances du projet.

### Évolutions fonctionnelles
- Ajout du module 3, incluant un squelette de skill, des checkpoints et une documentation préliminaire. [#3](https://github.com/etalab-ia/parcours-rag/pull/3)
- Intégration du corpus ANSSI Essentiels (17 PDFs) pour l'entraînement et l'évaluation des modèles RAG. [#2](https://github.com/etalab-ia/parcours-rag/pull/2)
- Mise en place d'un environnement de test avec un pipeline RAG de référence et 5 questions d'évaluation. [#13](https://github.com/etalab-ia/parcours-rag/pull/13)
- Amélioration de la gestion des compétences (skills) avec une simplification des instructions d'installation et une meilleure organisation des fichiers. [#24](https://github.com/etalab-ia/parcours-rag/pull/24), [#25](https://github.com/etalab-ia/parcours-rag/pull/25)
- Ajout de documentation pour les compétences Google Slides et GWS. [#23](https://github.com/etalab-ia/parcours-rag/pull/23)
- Implémentation d'une structure de "hint ladder" pour guider les utilisateurs à travers les étapes d'évaluation. [#16](https://github.com/etalab-ia/parcours-rag/pull/16)
- Ajout d'un guide pour les facilitateurs pour animer un atelier de 3 heures sur le module 3. [#17](https://github.com/etalab-ia/parcours-rag/pull/17)

### Évolutions techniques
- Mise à jour des dépendances du projet (zod, unpdf, @ai-sdk, @mastra, slidev, etc.).
- Refactorisation du code pour adopter une convention de nommage plus cohérente pour les compétences (skills).
- Amélioration de la robustesse du runtime RAG du module 3 et ajout d'outils d'évaluation CP6. [#34](https://github.com/etalab-ia/parcours-rag/pull/34)
- Mise en place d'une infrastructure CI/CD avec Biome pour le linting et le formatage, GitHub Actions pour l'automatisation des tests et la publication des releases. [#4](https://github.com/etalab-ia/parcours-rag/pull/4)
- Optimisation de la réutilisation de l'instance LibSQLVector pour améliorer les performances. [#659f563](https://github.com/etalab-ia/parcours-rag/commit/659f563)
- Correction de bugs liés à la gestion des métadonnées des pages et à l'analyse des numéros de page dans les citations. [#36bf614](https://github.com/etalab-ia/parcours-rag/commit/36bf614), [#556b623](https://github.com/etalab-ia/parcours-rag/commit/556b623)

### Autres changements
- Clarification de la documentation pour le module 3, notamment concernant les commandes slash et les types publics. [#20](https://github.com/etalab-ia/parcours-rag/pull/20), [#22](https://github.com/etalab-ia/parcours-rag/pull/22)
- Ajout d'un fichier `.aiexclude` pour ignorer les métadonnées des agents et la documentation des compétences. [#b9dd99c](https://github.com/etalab-ia/parcours-rag/commit/b9dd99c)
- Amélioration de la gestion des scripts de test pour assurer leur portabilité. [#5e86725](https://github.com/etalab-ia/parcours-rag/commit/5e86725)
- Correction de problèmes mineurs liés aux liens Markdown et aux références de chemin dans la documentation.
