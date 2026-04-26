## Changelog : parcours-rag (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec la création et le développement du module 3 de l'atelier RAG. Ce module se concentre sur l'implémentation pratique de techniques RAG, incluant la création de skills, l'intégration de données (ANSSI Essentiels), et la mise en place d'un flux de travail structuré avec des étapes de validation (checkpoints). L'accent a été mis sur la documentation détaillée et l'amélioration de l'expérience utilisateur pour les participants de l'atelier.

### Évolutions fonctionnelles
- Ajout du module 3 à l'atelier RAG, comprenant un squelette de skill, des étapes de validation (CP1 à CP6) et des guides pour les facilitateurs et les participants. [#3](https://github.com/etalab-ia/parcours-rag/pull/3)
- Intégration du corpus ANSSI Essentiels (17 PDFs) pour servir de base aux exercices du module 3. [#2](https://github.com/etalab-ia/parcours-rag/pull/2)
- Ajout d'une skill Google Slides pour la création de présentations et de supports de formation. [#23](https://github.com/etalab-ia/parcours-rag/pull/23)
- Implémentation d'un flux de travail pour la création de slides statiques avec Slidev. [#17](https://github.com/etalab-ia/parcours-rag/pull/17)
- Création d'un guide pour les facilitateurs détaillant le déroulement de l'atelier. [#16](https://github.com/etalab-ia/parcours-rag/pull/16)
- Mise en place d'une structure de "hint ladders" pour guider les participants à travers les étapes du module 3. [#15](https://github.com/etalab-ia/parcours-rag/pull/15)

### Évolutions techniques
- Refactorisation du code pour adopter une convention de skills de premier niveau pour le module 3. [#9](https://github.com/etalab-ia/parcours-rag/pull/9)
- Amélioration de la portabilité des scripts de test en durcissant leur configuration. [#11](https://github.com/etalab-ia/parcours-rag/pull/11)
- Adoption de npm comme gestionnaire de paquets pour le module 3, permettant une installation autonome. [#10](https://github.com/etalab-ia/parcours-rag/pull/10)
- Mise à jour des dépendances du projet (TypeScript, @ai-sdk, etc.).
- Ajout de tooling CI/CD (Biome, GitHub Actions, release-please) pour l'automatisation des tests, du linting et des releases. [#4](https://github.com/etalab-ia/parcours-rag/pull/4)
- Configuration de l'exclusion de certains fichiers et dossiers dans les outils de linting et de test. [#12](https://github.com/etalab-ia/parcours-rag/pull/12)

### Autres changements
- Amélioration de la documentation du module 3, notamment en clarifiant les instructions d'installation des skills et en ajoutant des références aux différents checkpoints.
- Simplification des instructions d'installation des skills.
- Suppression des références obsolètes et des fichiers inutiles.
- Ajout d'un fichier `.aiexclude` pour ignorer les métadonnées des agents et la documentation des skills.
- Ajout d'un fichier `manifest.json` avec une nouvelle ligne de fin.
