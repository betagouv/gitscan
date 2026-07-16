## Changelog : qualicharge (30 derniers jours, au 14 juillet 2026)

### Résumé
Les dernières mises à jour de QualiCharge améliorent la robustesse des calculs de supervision des bornes de recharge, notamment en incluant les bornes hors service et en corrigeant des erreurs dans les requêtes de données. Une nouvelle information (indicateur e1-DMR) a été ajoutée aux données de supervision. L'API a été renforcée pour exiger au moins une cible lors de la création d'un tarif.

### Évolutions fonctionnelles
- L'API requiert désormais au moins une cible lors de la création d'un tarif. [#e80764c](https://github.com/MTES-MCT/qualicharge/commit/e80764c)
- Ajout de l'indicateur e1-DMR aux données de supervision. [#e916431](https://github.com/MTES-MCT/qualicharge/commit/e916431)
- Ajout de l'indicateur e5 aux données de supervision. [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)

### Évolutions techniques
- Correction d'une erreur dans la définition de la plage de temps pour les requêtes utilisant la table `lateststatus` dans Prefect. [#fa87d3c](https://github.com/MTES-MCT/qualicharge/commit/fa87d3c)
- Inclusion des points de recharge hors service dans les calculs Prefect. [#217e5b2](https://github.com/MTES-MCT/qualicharge/commit/217e5b2)
- Correction d'un décalage de 15 jours pour les indicateurs de session dans Prefect. [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
- Mise à jour de la version de Keycloak (Docker) vers v26.7.
- Mise à jour de la version de Metabase (Docker) vers v0.62.4.
- Mise à jour de la version de Locust (Docker) vers v2.45.0.
- Mise à jour de la version de Curl (Docker) vers v8.21.0.
- Mise à jour de la version de Terraform (Docker) vers v1.15.8.
- Mise à jour de l'action GitHub `actions/checkout` vers v7.
- Mise à jour de l'action GitHub `astral-sh/setup-uv` vers v8.3.2.
- Mise à jour de l'action GitHub `actions/setup-python` vers v6.3.0.
- Mise à jour de l'action GitHub `zizmorcore/zizmor-action` vers v0.5.7.
- Mise à jour de la version de `uv` vers v0.11.28.

### Autres changements
- Publication de la version 0.34.1 de l'API. [#bd84d50](https://github.com/MTES-MCT/qualicharge/commit/bd84d50)
- Mise à jour des dépendances Python pour corriger des vulnérabilités de sécurité.
- Correction de vulnérabilités de dépendances transitives.
- Mise à jour de `pydantic-settings` vers v2.14.2.
- Mise à jour de `python-multipart` vers v0.0.31.
- Mise à jour de `pyjwt` vers v2.13.0.
