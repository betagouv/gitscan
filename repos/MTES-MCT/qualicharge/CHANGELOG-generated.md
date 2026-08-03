## Changelog : qualicharge (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des tarifs de recharge et des indicateurs de performance dans Prefect, ainsi que sur des mises à jour de sécurité et de dépendances pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif de recharge. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Amélioration du stockage des champs de tarif dans l'API : seuls les champs non nuls sont désormais stockés en brut. [#7a5c26d](https://github.com/MTES-MCT/qualicharge/commit/7a5c26d)
- Ajout d'indicateurs E2 et E3 dans Prefect pour un suivi plus précis des performances. [#c47a775](https://github.com/MTES-MCT/qualicharge/commit/c47a775)
- Ajout d'indicateurs E1-DMR dans Prefect. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)

### Évolutions techniques
- Correction d'une erreur dans Prefect concernant la définition de la plage de temps pour les requêtes utilisant la table `lateststatus`, incluant désormais les points de recharge hors service. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c) [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Mise à jour de la version de l'API (patch) à 0.34.1. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)

### Autres changements
- Mises à jour des dépendances et des images Docker (Metabase, Keycloak, Locust, Curl, Terraform, UV, pydantic-settings, python-multipart, pyjwt) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Mise à jour des actions GitHub (checkout, setup-python, setup-uv, zizmor-action) pour bénéficier des dernières fonctionnalités et corrections.
- Correction de vulnérabilités dans les dépendances Python. [#1832d50](https://github.com/MTES-MCT/qualicharge/commit/1832d50)
