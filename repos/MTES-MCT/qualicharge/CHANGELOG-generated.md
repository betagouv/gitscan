## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à qualicharge au cours des 30 derniers jours. Les changements incluent des validations plus strictes des données des bornes de recharge, des corrections de bugs concernant les indicateurs de qualité et des mises à jour de sécurité des dépendances. Une nouvelle version de l'API (0.33.0) a également été publiée.

### Évolutions fonctionnelles
- Amélioration de la validation des données d'itinérance (ID) [#900](https://github.com/MTES-MCT/qualicharge/issues/900)
- Correction des indicateurs de qualité PDCM dans Prefect.
- Mise à jour des indicateurs pour les attentes de qualité.

### Évolutions techniques
- Autorisation de l'allocation de pseudo-TTY pour `psql` afin d'améliorer la gestion des bases de données.
- Suppression de la tâche `bench-api` pour simplifier le pipeline CI.
- Restriction de la durée maximale d'une session à une semaine.
- Restriction des limites de puissance nominale et d'énergie des sessions.
- Validation de la validité du numéro SIREN (checksum) avant l'ingestion des données.
- Vérification que la localisation des bornes de recharge se trouve sur le territoire français.
- Exigence d'un `num_pdl` pour les connexions directes.
- Déplacement des valeurs nulles du champ `_Station.raccordement` vers Direct.
- Déclenchement du CI même lorsque la branche cible n'est pas `main`.
- Exigence du champ `raccordement` pour les données statiques.
- Mises à jour de plusieurs dépendances : Django (v6.0.3 - sécurité), Flask, Werkzeug, black (v26.3.1 - sécurité), orjson (v3.11.6), sqlparse (v0.5.4).
- Mises à jour des images Docker : metabase (v0.59.2, v0.59.1, v0.58.8, v0.58.7), terraform (v1.14.7, v1.14.6), ghcr.io/astral-sh/uv (v0.10.9, v0.10.8, v0.10.7, v0.10.4).
- Mises à jour des actions GitHub : actions/download-artifact (v8.0.1), astral-sh/setup-uv (v7.5.0, v7.3.1), GitHub Artifact Actions.

### Autres changements
- Publication de la version 0.33.0 de l'API.
