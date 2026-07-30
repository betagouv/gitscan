## Changelog : qualicharge (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout d'indicateurs de performance dans Prefect pour le suivi des sessions de recharge, ainsi que sur des corrections concernant le calcul des plages horaires et l'inclusion des points de recharge hors service. Des améliorations ont également été apportées à l'API pour la gestion des tarifs.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout d'indicateurs E1-DMR, E2, E3 et E5 dans Prefect pour un meilleur suivi des sessions de recharge. [#c47a775](https://github.com/MTES-MCT/qualicharge/commit/c47a775), [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431), [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)
- Correction du calcul de la plage horaire pour les requêtes Prefect utilisant la table `lateststatus`. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des points de recharge hors service dans les calculs Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- L'API stocke désormais uniquement les champs de tarif non nuls en brut. [#7a5c26d](https://github.com/MTES-MCT/qualicharge/commit/7a5c26d)

### Évolutions techniques
- Mise à jour de la version de l'API à 0.34.1. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)
- Mises à jour de plusieurs dépendances Docker (Keycloak, Metabase, Locust, Curl, Terraform, UV) et actions GitHub (checkout, setup-python, setup-uv, zizmor-action). Ces mises à jour sont principalement des corrections de sécurité et des améliorations de performance.
- Mise à jour des dépendances Python pour corriger des vulnérabilités de sécurité. [#1832d50](https://github.com/MTES-MCT/qualicharge/commit/1832d50)

### Autres changements
- Ajout d'un offset de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
