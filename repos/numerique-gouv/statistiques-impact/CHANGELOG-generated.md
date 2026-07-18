## Changelog : statistiques-impact (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte significative de la gestion des indicateurs, avec l'introduction d'un nouveau modèle de données "Record" pour remplacer l'ancien "last_indicators".  Plusieurs dépendances ont été mises à jour pour améliorer la sécurité et la performance. Une migration vers Python 3.14 a également été effectuée.

### Évolutions fonctionnelles
- Introduction d'un nouveau modèle de données "Record" pour une gestion plus flexible des données d'impact. L'ancien système "last_indicators" est désormais redirigé vers ce nouveau modèle. [#c00d4922](https://github.com/numerique-gouv/statistiques-impact/commit/00d4922)
- Création d'une API CRUD (Create, Read, Update, Delete) pour la gestion des "Record". [#c0a1042](https://github.com/numerique-gouv/statistiques-impact/commit/c0a1042)
- Déduplication des indicateurs de données. [#b385455](https://github.com/numerique-gouv/statistiques-impact/commit/b385455)

### Évolutions techniques
- Mise à jour de la version de Python à 3.14. [#bb70486](https://github.com/numerique-gouv/statistiques-impact/commit/bb70486)
- Mises à jour de plusieurs dépendances :
    - Django (3.16.0 -> 3.17.1)
    - drf-spectacular (0.28.0 -> 0.30.0)
    - psycopg2-binary (2.9.10 -> 2.9.12)
    - pytest (9.0.3 -> 9.1.1)
    - pytest-django (4.11.1 -> 4.12.0)
    - datagouv-client (0.3.2 -> 0.5.0)
    - ruff (0.12.2 -> 0.15.20 et 0.15.20 -> 0.15.21)
    - whitenoise (6.9.0 -> 6.12.0)
    - typing-extensions (4.14.1 -> 4.16.0)
    - django-dsfr (3.0.0 -> 3.5.2)
    - dj-database-url (3.0.1 -> 3.1.2)
    - sqlparse (0.5.4 -> 0.5.5)
    - responses (0.25.7 -> 0.26.2)
- Suppression de la dépendance `revproxy`. [#c9ecb8d](https://github.com/numerique-gouv/statistiques-impact/commit/c9ecb8d)
- Renommage du champ `nom_service_public_numerique` dans les modèles. [#098492a](https://github.com/numerique-gouv/statistiques-impact/commit/098492a)

### Autres changements
- Configuration initiale de Dependabot pour la gestion des dépendances. [#bf66319](https://github.com/numerique-gouv/statistiques-impact/commit/bf66319)
- Ajout d'une bannière d'erreur temporaire pour Proconnect. [#fb0f047](https://github.com/numerique-gouv/statistiques-impact/commit/fb0f047)
- Mise à jour du schéma de la base de données. [#0f10151](https://github.com/numerique-gouv/statistiques-impact/commit/0f10151)
