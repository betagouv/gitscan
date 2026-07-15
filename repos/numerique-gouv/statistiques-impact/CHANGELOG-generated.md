## Changelog : statistiques-impact (30 derniers jours, au 26 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte de la gestion des indicateurs, désormais appelés "records", avec la création d'une API complète pour leur gestion.  De nombreuses dépendances ont été mises à jour pour améliorer la sécurité et la stabilité de l'application. La version de Python a également été mise à niveau.

### Évolutions fonctionnelles
- Ajout d'une API CRUD (Créer, Lire, Mettre à jour, Supprimer) pour la gestion des "records" (anciennement "indicateurs").
- Redirection automatique de l'ancienne URL `/last_indicators` vers `/last_records`.
- Correction du client France Transfert.

### Évolutions techniques
- Mise à niveau de la version de Python à 3.14.
- Mise à jour de nombreuses dépendances :
    - `pandas` (2.3.1 -> 3.0.3)
    - `djangorestframework` (3.16.0 -> 3.17.1)
    - `psycopg2-binary` (2.9.10 -> 2.9.12)
    - `pytest` (9.0.3 -> 9.1.1)
    - `pytest-django` (4.11.1 -> 4.12.0)
    - `datagouv-client` (0.3.2 -> 0.5.0)
    - `ruff` (0.12.2 -> 0.15.20 puis 0.15.21)
    - `drf-spectacular` (0.28.0 -> 0.30.0)
    - `whitenoise` (6.9.0 -> 6.12.0)
    - `typing-extensions` (4.14.1 -> 4.16.0)
    - `dj-database-url` (3.0.1 -> 3.1.2)
    - `sqlparse` (0.5.4 -> 0.5.5)
    - `django-dsfr` (3.0.0 -> 3.5.2)
    - `responses` (0.25.7 -> 0.26.2)
- Suppression de la dépendance `revproxy`.
- Création du fichier de configuration Dependabot (`.dependabot/dependabot.yml`).

### Autres changements
- Déduplication des indicateurs (records) [#b385455](https://github.com/numerique-gouv/statistiques-impact/commit/b385455).
- Mise à jour du schéma de l'API.
- Correction des tests liés à `datagouv_client`.
- Suppression d'un test cassé dépendant de `demo.data.gouv.fr`.
- Mise à jour de la documentation du schéma.
