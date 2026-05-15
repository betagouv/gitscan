## Changelog : find (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la qualité du code, la simplification de l'architecture et la mise à jour des dépendances pour assurer la sécurité et la stabilité du projet. Plusieurs fonctionnalités expérimentales ont été supprimées pour se concentrer sur le cœur de la recherche documentaire.

### Évolutions fonctionnelles
- Suppression de l'évaluation de la recherche et de la recherche hybride, maintenant uniquement la recherche BM25.
- Correction de fautes de frappe dans la documentation.

### Évolutions techniques
- Unification des index de recherche avec une portée de service.
- Suppression du code mort identifié par l'outil Vulture.
- Suppression d'un service Docker inutilisé.
- Mise à jour de Redis vers la version 6.
- Mise à jour de Pydantic vers la version 2.13.4.
- Renforcement des assertions de tests pour une meilleure clarté.
- Ajout de hooks pre-commit pour améliorer la qualité du code.
- Suppression des dépendances inutilisées `url-normalize` et déplacement de `factory_boy` vers les dépendances de développement.
- Simplification du changelog pour la release initiale.
- Autorisation des constantes en majuscules dans les paramètres Django (pour Pylint).

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `opensearch-py` vers la version 3.2.0
    - `drf-spectacular-sidecar` vers la version 2026.5.1
    - `types-requests` vers la version 2.33.0.20260503
    - `psycopg` vers la version 3.3.4
    - `django` vers la version 6.0.5 (incluant des correctifs de sécurité)
    - `faker` vers la version 40.15.0
    - `dockerflow` vers la version 2026
    - `ruff` vers la version 0.15.12
    - `url-normalize` vers la version 3
    - `pyjwt` vers la version 2.12.1
    - `pyfakefs` vers la version 6.2.0
    - `responses` vers la version 0.26.0
    - `sentry-sdk` vers la version 2.58.0
    - `pylint` vers la version 4.0.5
    - `drf-spectacular-sidecar` vers la version 2026.4.14
    - `whitenoise` vers la version 6.12.0
    - `types-requests` vers la version 2.33.0.20260408
    - `ipython` vers la version 9.13.0
    - `djangorestframework` vers la version 3.17.1
    - `psycopg` vers la version 3.3.3
    - `gunicorn` vers la version 25
    - `requests` vers la version 2.33.1
    - `pytest-cov` vers la version 7.1.0
    - `celery` vers la version 5.6.3
    - `pytest-django` vers la version 4.12.0
    - `django-lasuite` vers la version 0.0.26
    - `django` vers la version 5.2.13 et 6.0.5 (correctifs de sécurité)
    - `requests` vers la version 2.33.0 (correctif de sécurité)
    - `pytest` vers la version 9.0.3 (correctif de sécurité)
    - `pyjwt` vers la version 2.12.0 (correctif de sécurité)
    - `langchain-text-splitters` vers la version 1.1.2 (correctif de sécurité)
- Séparation des PR de dépendances Python pour une meilleure gestion.
- Épinglage des dépendances pour une meilleure reproductibilité.
