## Changelog : qualicharge (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de qualicharge se concentrent sur l'amélioration de la granularité des données affichées (indicateurs de volume étendus aux unités opérationnelles) et la maintenance de la sécurité et des dépendances du projet. Des mises à jour régulières des outils et librairies utilisés ont également été effectuées pour garantir la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Extension des indicateurs de volume aux niveaux des unités opérationnelles, permettant une analyse plus précise des données de recharge. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)

### Évolutions techniques
- Suppression des requêtes API utilisant un utilisateur mis en cache, améliorant la sécurité et la cohérence des données.
- Mises à jour de plusieurs dépendances majeures :
    - Terraform (v1.14.9)
    - Metabase (v0.60.2)
    - Django (v6.0.4)
    - Keycloak (v26.6)
    - Locust (v2.43.4)
    - uv (v0.11.8)
- Mises à jour des actions CI/CD :
    - `astral-sh/setup-uv` (v8.1.0 puis v8)
    - `pypa/gh-action-pypi-publish` (v1.14.0)
    - `actions/upload-artifact` (v7.0.1)

### Autres changements
- Mise à jour de la documentation et des dépendances de sécurité :
    - `python-dotenv` (v1.2.2)
    - `pygments` (v2.20.0)
    - `pytest` (v9.0.3)
    - `python-multipart` (v0.0.26)
    - `requests` (v2.33.0)
- Diverses mises à jour mineures de dépendances et d'images Docker.
