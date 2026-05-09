## Changelog : find (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, le projet find a subi une phase de nettoyage et de simplification importante. Des fonctionnalités expérimentales comme la recherche par embedding ont été supprimées pour se concentrer sur la recherche BM25. De nombreuses dépendances ont été mises à jour, notamment Django et Redis, et des outils de qualité de code ont été ajoutés pour améliorer la maintenabilité du projet.

### Évolutions fonctionnelles
- Correction du type de valeur dans la recherche [#68](https://github.com/suitenumerique/find/issues/68).

### Évolutions techniques
- Suppression du code mort identifié par l'outil Vulture.
- Suppression de la fonctionnalité de recherche par embedding et de la recherche hybride, recentrant le projet sur l'algorithme BM25.
- Suppression de l'application d'évaluation.
- Mise à jour de Redis vers la version 6.
- Mise à jour de Django vers la version 6 [#112](https://github.com/suitenumerique/find/issues/112).
- Suppression de `url-normalize` et déplacement de `factory_boy` vers les dépendances de développement.
- Suppression du service Dockerize inutilisé.
- Ajout de hooks pre-commit pour améliorer la qualité du code.
- Autorisation des constantes en majuscules dans les paramètres Django pour Pylint.

### Autres changements
- Correction de fautes de frappe dans la documentation.
- Plusieurs mises à jour de dépendances (Faker, Dockerflow, Ruff, url-normalize, pyjwt, pyfakefs, responses, sentry-sdk, pylint, drf-spectacular-sidecar, whitenoise, types-requests, ipython, djangorestframework, psycopg, gunicorn, requests, pytest-cov, celery, pytest-django, django-lasuite) ont été effectuées par Renovate Bot. Ces mises à jour incluent des correctifs de sécurité pour Django, Requests, PyJWT, Langchain et Pytest.
- Séparation des Pull Requests de dépendances Python pour une meilleure gestion.
- Épinglage des dépendances pour une meilleure stabilité [#75](https://github.com/suitenumerique/find/issues/75).
