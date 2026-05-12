## Changelog : find (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé un important travail de maintenance et d'optimisation du projet. Des améliorations de la qualité du code ont été apportées, du code mort a été supprimé et des dépendances mises à jour pour renforcer la sécurité et la stabilité. La recherche a été simplifiée en se concentrant sur l'algorithme BM25.

### Évolutions fonctionnelles
- Simplification de la recherche : Seul l'algorithme BM25 est désormais utilisé pour la recherche, les fonctionnalités d'embedding et de recherche hybride ayant été supprimées.

### Évolutions techniques
- Mise à jour de Redis vers la version 6.
- Unification des indices de recherche avec une portée de service.
- Suppression du code mort identifié par l'outil Vulture.
- Suppression de l'application d'évaluation.
- Suppression d'un service Docker inutilisé.
- Renforcement des assertions des tests pour plus de clarté.
- Ajout de hooks pre-commit pour améliorer la qualité du code.
- Mise à jour de plusieurs dépendances :
    - `pydantic` vers la version 2.13.4
    - `opensearch-py` vers la version 3.2.0
    - `drf-spectacular-sidecar` vers la version 2026.5.1
    - `psycopg` vers la version 3.3.4
    - `django` vers la version 6.0.5 (incluant des correctifs de sécurité)
    - `django` vers la version 5.2.13 (incluant des correctifs de sécurité)
    - `requests` vers la version 2.33.1 (incluant des correctifs de sécurité)
    - `pytest` vers la version 9.0.3 (incluant des correctifs de sécurité)
    - `pyjwt` vers la version 2.12.0 et 2.12.1 (incluant des correctifs de sécurité)
    - `langchain-text-splitters` vers la version 1.1.2 (incluant des correctifs de sécurité)
- Modification de la configuration Pylint pour autoriser l'utilisation de constantes en majuscules pour les paramètres Django.
- Suppression de `url-normalize` et déplacement de `factory_boy` vers les dépendances de développement.

### Autres changements
- Correction de fautes de frappe dans la documentation.
- Séparation des pull requests de mise à jour des dépendances Python pour une meilleure gestion.
- Épuration des dépendances et fixation des versions.
- Simplification du changelog pour la publication initiale.
