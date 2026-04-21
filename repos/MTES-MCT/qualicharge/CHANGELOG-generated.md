## Changelog : qualicharge (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les mises à jour de qualicharge se concentrent sur l'amélioration de la sécurité, la maintenance technique et la correction de bugs liés à la gestion des stations de recharge. Une attention particulière a été portée à la gestion du cycle de vie des stations (désactivation/réactivation) et à la gestion des erreurs dans l'API.

### Évolutions fonctionnelles

- Correction d'un bug permettant de réactiver les stations de recharge lorsque qu'un seul point de charge est de nouveau opérationnel. [#304cb88](https://github.com/MTES-MCT/qualicharge/commit/304cb88)
- Amélioration des messages d'erreur statiques pour les opérations de lecture et de liste dans l'API. [#9e1d972](https://github.com/MTES-MCT/qualicharge/commit/9e1d972)
- Suppression des requêtes API mettant en cache les informations utilisateur. [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d)
- Les stations de recharge orphelines sont désormais désactivées au lieu d'être supprimées. [#639294a](https://github.com/MTES-MCT/qualicharge/commit/639294a)

### Évolutions techniques

- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et bénéficier des dernières améliorations : `pygments`, `pytest`, `pyjwt`, `requests`, `python-multipart`.
- Mise à jour des images Docker de Keycloak, Metabase, Locust, Terraform, et d'autres outils.
- Mise à jour des actions GitHub utilisées pour le CI/CD (Renovate, Upload Artifact, etc.).
- Amélioration de la gestion des sessions longues dans l'indicateur OCCT. [#cfa75f0](https://github.com/MTES-MCT/qualicharge/commit/cfa75f0)
- Mise à jour de Django en version 6.0.4. [#75a3748](https://github.com/MTES-MCT/qualicharge/commit/75a3748)

### Autres changements

- Publication d'une nouvelle version de l'API (0.33.1). [#1b32e4b](https://github.com/MTES-MCT/qualicharge/commit/1b32e4b)
