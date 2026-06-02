## Changelog : find (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, le projet find a connu une importante phase de nettoyage et de simplification. Des fonctionnalités expérimentales comme la recherche par embedding ont été supprimées pour se concentrer sur la recherche BM25.  De plus, la qualité du code a été améliorée grâce à l'ajout de hooks de pré-commit et la suppression de code mort. Plusieurs dépendances ont également été mises à jour, notamment Django, Redis et Pydantic.

### Évolutions fonctionnelles
- Suppression de la recherche par embedding/hybride, maintenant uniquement la recherche BM25 est disponible.
- Suppression de l'application d'évaluation.

### Évolutions techniques
- Unification des indices de recherche avec une portée de service. [#104](https://github.com/suitenumerique/find/issues/104)
- Mise à jour de Pydantic vers la version 2.13.4.
- Mise à jour de Redis vers la version 6.
- Suppression du code mort identifié par Vulture.
- Suppression du service Dockerize non utilisé.
- Ajout de hooks de pré-commit pour améliorer la qualité du code.
- Suppression des dépendances inutilisées `url-normalize` et déplacement de `factory_boy` vers les dépendances de développement.
- Amélioration des assertions des tests pour plus de clarté.
- Correction de typos dans la documentation.

### Autres changements
- Simplification du changelog pour la version initiale.
- Autorisation des constantes en majuscules dans les paramètres Django pour Pylint.
- Mises à jour de nombreuses dépendances (Django, drf-spectacular-sidecar, psycopg, opensearch-py, faker, dockerflow, ruff, pyjwt, pyfakefs, responses, sentry-sdk, pylint, whitenoise, ipython, djangorestframework, gunicorn, requests, pytest-cov, celery) via Dependabot/Renovate. Ces mises à jour incluent des correctifs de sécurité pour Django [#112](https://github.com/suitenumerique/find/issues/112) et d'autres améliorations.
