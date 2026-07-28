## Changelog : qualicharge (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout d'indicateurs de performance (E1-DMR, E2, E3, E5) dans Prefect pour un suivi plus précis de l'état des bornes de recharge, ainsi que sur des corrections concernant le calcul des plages de temps et la prise en compte des bornes hors service. Des améliorations ont également été apportées à l'API pour la gestion des tarifs.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- L'API stocke uniquement les champs de tarif non nuls en tant que données brutes. [#7a5c26d](https://github.com/MTES-MCT/qualicharge/commit/7a5c26d)

### Évolutions techniques
- Ajout des indicateurs E2 et E3 dans Prefect. [#c47a775](https://github.com/MTES-MCT/qualicharge/commit/c47a775)
- Ajout de l'indicateur E1-DMR dans Prefect. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)
- Ajout de l'indicateur E5 dans Prefect. [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)
- Correction d'une erreur dans Prefect concernant la définition de la plage de temps pour les requêtes utilisant la table `lateststatus`. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Correction dans Prefect pour inclure les points de recharge hors service. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Ajout d'un offset de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
- Bump de la release API à la version 0.34.1. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)

### Autres changements
- Mise à jour des dépendances Docker de Keycloak (v26.7), Metabase (v0.62.4), Locust (v2.45.0), Curl (v8.21.0), Terraform (v1.15.8), et UV (v0.11.28).
- Mise à jour des actions GitHub (actions/checkout v7, astral-sh/setup-uv v8.3.2, actions/setup-python v6.3.0, zizmorcore/zizmor-action v0.5.7).
- Mise à jour des dépendances Python (pydantic-settings v2.14.2, python-multipart v0.0.31, pyjwt v2.13.0).
- Correction de vulnérabilités dans les dépendances.
