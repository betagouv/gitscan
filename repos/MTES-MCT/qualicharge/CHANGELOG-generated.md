## Changelog : qualicharge (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la granularité des indicateurs Prefect, la suppression de fonctionnalités obsolètes liées à la gestion de la cache utilisateur dans l'API, et la mise à jour de nombreuses dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Extension des indicateurs Prefect au niveau des Operational Units, permettant un suivi plus précis des opérations. [#1527322](https://github.com/MTES-MCT/qualicharge/issues/1527322)
- Suppression des requêtes API concernant la cache utilisateur, simplifiant ainsi l'API et améliorant potentiellement la sécurité.

### Évolutions techniques
- Mises à jour de plusieurs dépendances majeures, incluant Django (v6.0.4), Metabase (v0.60.2, v0.59.6), Terraform (v1.14.9, v1.14.8), et Pygments (v2.20.0) pour bénéficier des dernières corrections et améliorations.
- Mise à jour des images Docker utilisées pour les différents composants du projet (uv, terraform, metabase, curl, locust, keycloak).
- Mises à jour des actions GitHub utilisées dans les workflows CI/CD (setup-uv, gh-action-pypi-publish, upload-artifact).
- Correction d'une vulnérabilité de sécurité dans la librairie `python-multipart` (v0.0.26).
- Mise à jour de la librairie `requests` (v2.33.0) pour corriger des vulnérabilités de sécurité.

### Autres changements
- Mise à jour de la documentation et des configurations pour refléter les changements apportés.
- Amélioration continue des workflows CI/CD pour une meilleure automatisation et fiabilité.
