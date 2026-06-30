## Changelog : repo-falcon (30 derniers jours, au 28 juin 2026)

### Résumé
Ce mois-ci, repo-falcon a connu une avancée significative dans ses capacités d'analyse de code et de génération de graphes de connaissances. Les améliorations se concentrent sur la précision de l'analyse, la détection de connexions inattendues dans le code, et l'ajout de fonctionnalités pour une meilleure compréhension et exploration du code, notamment via une intégration optionnelle d'un modèle de langage local.

### Évolutions fonctionnelles
- **Insights améliorés :** Détection de connexions surprenantes dans le code et suggestions de questions pour aider à l'exploration du code.
- **Nouvelles commandes CLI :** Ajout de commandes déterministes pour interroger le code par symbole, chemin, hubs et communautés.
- **Amélioration du graphe d'appels :**
    - Typage des récepteurs pour les langages JavaScript/TypeScript, Python et Java, améliorant la précision du graphe d'appels.
    - Ajout d'arêtes "REFERENCES" pour suivre l'utilisation des types.
    - Rubrique de confiance pour les arêtes du graphe d'appels, avec signalement des arêtes ambiguës.
- **Intégration LLM locale optionnelle :** Possibilité d'enrichir l'analyse avec un modèle de langage local pour le labeling communautaire.
- **Communautés déterministes :** Remplacement de l'algorithme de propagation d'étiquettes par un algorithme de modularité de Louvain déterministe pour la détection de communautés.

### Évolutions techniques
- **Validation centralisée :** Ajout d'une validation centralisée pour les références Git, les labels et le confinement des chemins.
- **Benchmark :** Implémentation d'un benchmark pour évaluer la réduction du nombre de tokens par rapport au corpus brut.
- **Mémoire de travail déterministe :** Implémentation d'une boucle de réflexion de la mémoire de travail déterministe pour mémoriser et refléter l'état.
- **Index amélioré :** Amélioration de l'indexation pour inclure le graphe d'appels au niveau du symbole, avec prise en compte du `.gitignore` et une meilleure résilience lors du scan.

### Autres changements
- **Documentation :**
    - Ajout d'une étude de cas sur l'auto-hébergement reproductible.
    - Index des exemples de travail.
    - Documentation sur l'évaluation et graphify, ainsi que des observations sur la couche LLM.
- **Mise à jour des dépendances :** Mise à jour de `devbox.lock`.
