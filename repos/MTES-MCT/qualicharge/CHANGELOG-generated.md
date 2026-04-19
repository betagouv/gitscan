## Changelog : qualicharge (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les mises à jour de Qualicharge se sont concentrées sur l'amélioration de la sécurité, la correction de bugs liés à la gestion des stations de recharge et l'optimisation de la gestion des données. Des améliorations continues de l'infrastructure et des dépendances ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait la remise en service correcte des stations lorsque seulement un point de charge était opérationnel. [#936](https://github.com/MTES-MCT/qualicharge/issues/936)
- Amélioration des messages d'erreur lors de la lecture ou de la liste des stations via l'API.
- Suppression des requêtes API mettant en cache les informations utilisateur, améliorant potentiellement la sécurité et la performance.
- Décommissionnement des stations orphelines au lieu de les supprimer définitivement, permettant une meilleure gestion des données.
- Suppression des sessions longues de l'indicateur OCCT pour améliorer la clarté des données.

### Évolutions techniques
- Mise à jour de plusieurs dépendances Python pour corriger des failles de sécurité et bénéficier des dernières améliorations : `python-multipart`, `pyjwt`, `requests`, `dynaconf`, `pytest`, `pygments`.
- Mise à jour des images Docker pour Keycloak, Curl, Locust, Terraform et Metabase vers leurs dernières versions stables.
- Mise à jour des actions GitHub utilisées pour le CI/CD (upload-artifact, gh-action-pypi-publish, setup-uv).
- Mise à jour de la version de Django à la version 6.0.4.

### Autres changements
- Bump de la version de l'API à 0.33.1.
- Amélioration de la documentation et de la configuration.
