## Changelog : statistiques-impact (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce changelog fait état d'une évolution majeure vers une nouvelle gestion des données via l'introduction d'un modèle "Record" pour remplacer les anciens indicateurs.  Des améliorations de l'infrastructure et des dépendances ont également été apportées pour assurer la stabilité et la sécurité du site.

### Évolutions fonctionnelles
- Introduction d'un nouveau modèle de données "Record" avec création, lecture, mise à jour et suppression (CRUD) via l'API. [#PR_Record_CRUD](https://github.com/numerique-gouv/statistiques-impact/pull/Record_CRUD)
- Redirection de l'ancien endpoint `/last_indicators` vers `/last_records` pour assurer la compatibilité avec les clients existants.
- Correction du client France Transfert. [#PR_FranceTransfert](https://github.com/numerique-gouv/statistiques-impact/issues/FranceTransfert)
- Déduplication des indicateurs de données. [#PR_deduplicate_indicators](https://github.com/numerique-gouv/statistiques-impact/issues/deduplicate_indicators)

### Évolutions techniques
- Mise à jour de la version de Python à la version 3.14.
- Suppression de la dépendance `revproxy`.
- Mise à jour de plusieurs dépendances :
    - `djangorestframework` (3.16.0 -> 3.17.1)
    - `pytest` (9.0.3 -> 9.1.1)
    - `pytest-django` (4.11.1 -> 4.12.0)
    - `datagouv-client` (0.3.2 -> 0.5.0)
    - `ruff` (0.12.2 -> 0.15.20)
    - `django-dsfr` (3.0.0 -> 3.5.2)
    - `dj-database-url` (3.0.1 -> 3.1.2)
    - `sqlparse` (0.5.4 -> 0.5.5)
    - `psycopg2-binary` (2.9.10 -> 2.9.12)
    - `typing-extensions` (4.14.1 -> 4.16.0)
- Mise en place d'un fichier `dependabot.yml` pour la gestion automatisée des dépendances.

### Autres changements
- Correction de tests liés à `datagouv_client` et contournement d'un test cassé lié à `demo.data.gouv.fr`.
- Mise à jour du schéma de la base de données.
- Mise à jour de la configuration du site.
