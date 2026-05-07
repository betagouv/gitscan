## Changelog : qualicharge (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de qualicharge se concentrent sur l'amélioration de la granularité des indicateurs de performance pour les unités opérationnelles, la suppression d'une fonctionnalité de cache utilisateur obsolète dans l'API, et la mise à jour de nombreuses dépendances pour bénéficier des dernières corrections de sécurité et améliorations.

### Évolutions fonctionnelles
- Amélioration des indicateurs de performance : Extension des indicateurs de volume au niveau des unités opérationnelles. [#1527322](https://github.com/MTES-MCT/qualicharge/pull/1527322)
- Suppression du cache utilisateur : Suppression des requêtes API mettant en cache les informations utilisateur. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)

### Évolutions techniques
- Mises à jour de dépendances : De nombreuses dépendances ont été mises à jour vers leurs dernières versions, incluant des correctifs de sécurité pour `python-multipart`, `pygments`, `pytest`, `requests` et d'autres.
- Mises à jour d'images Docker : Les images Docker de Keycloak, Metabase, Terraform, Curl et Locust ont été mises à jour.
- Amélioration des actions CI/CD : Plusieurs actions utilisées dans les workflows CI/CD ont été mises à jour.

### Autres changements
- Documentation : Aucune modification de la documentation n'a été apportée durant cette période.
- Configuration : Aucune modification de la configuration n'a été apportée durant cette période.
