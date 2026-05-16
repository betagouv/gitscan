## Changelog : qualicharge (30 derniers jours, au 11 mai 2026)

### Résumé
Les dernières mises à jour de Qualicharge concernent principalement la maintenance et la sécurité des dépendances du projet. Une amélioration fonctionnelle a été apportée pour étendre les indicateurs de volume au niveau des unités opérationnelles, permettant une analyse plus granulaire des données de recharge.

### Évolutions fonctionnelles
- Extension des indicateurs de volume aux unités opérationnelles. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)

### Évolutions techniques
- Mise à jour de Django en version 6.0.5 incluant des correctifs de sécurité.
- Mises à jour des images Docker pour Metabase, Terraform, et uv.
- Mises à jour de plusieurs actions utilisées dans les workflows CI/CD (setup-uv, zizmor-action).
- Suppression des requêtes API en cache pour l'utilisateur.

### Autres changements
- Mises à jour de diverses dépendances Python (urllib3, python-dotenv, python-multipart, mako) pour bénéficier des dernières corrections et améliorations de sécurité.
- Mises à jour de la librairie astral-sh/uv et de ses images Docker.
