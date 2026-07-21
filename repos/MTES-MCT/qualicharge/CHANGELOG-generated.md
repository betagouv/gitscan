## Changelog : qualicharge (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'API et aux tâches de supervision (Prefect) pour une meilleure gestion des données de recharge des véhicules électriques. Des indicateurs de performance supplémentaires ont été ajoutés et des corrections ont été apportées pour une analyse plus précise des données, notamment concernant les points de recharge hors service. Des mises à jour de sécurité des dépendances ont également été effectuées.

### Évolutions fonctionnelles
- L'API requiert maintenant au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout d'indicateurs E1-DMR et E5 pour une meilleure analyse des données de session. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431) et [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)
- Correction de la plage de temps utilisée pour les requêtes dans Prefect, améliorant la précision des données. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des points de recharge hors service dans les calculs Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Ajout d'un offset de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)

### Évolutions techniques
- Mise à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform) pour bénéficier des dernières corrections et améliorations de sécurité.
- Mise à jour des actions GitHub (checkout, setup-python, setup-uv, zizmor-action) pour bénéficier des dernières fonctionnalités et corrections.
- Mise à jour des dépendances Python pour corriger des vulnérabilités de sécurité et améliorer la stabilité.
- Bump de la release API à la version 0.34.1 [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)

### Autres changements
- Aucune documentation ou configuration n'a été modifiée.
