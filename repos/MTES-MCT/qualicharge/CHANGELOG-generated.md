## Changelog : qualicharge (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Qualicharge se concentrent sur l'amélioration de la granularité des indicateurs de performance des bornes de recharge, la suppression de fonctionnalités obsolètes et la mise à jour de nombreuses dépendances pour garantir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Extension des indicateurs de volume aux niveaux d'OperationalUnit, permettant une analyse plus précise des données de recharge. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)
- Suppression des requêtes API qui utilisaient un utilisateur mis en cache, améliorant la sécurité et la cohérence des données.

### Évolutions techniques
- Mises à jour de plusieurs dépendances majeures, incluant Terraform, Metabase, Keycloak, Python et ses librairies associées (Pygments, pytest, requests, python-dotenv, python-multipart). Ces mises à jour visent à corriger des failles de sécurité et à bénéficier des dernières améliorations de performance.
- Mise à jour des images Docker utilisées pour les différents composants de la plateforme (uv, curl, locust, terraform, keycloak, metabase).
- Mise à jour des actions GitHub utilisées pour le CI/CD (setup-uv, gh-action-pypi-publish, upload-artifact).

### Autres changements
- Aucune documentation ou configuration n'a été modifiée durant cette période.
