## Changelog : qualicharge (30 derniers jours, au 4 juillet 2026)

### Résumé
Les récentes évolutions de Qualicharge se concentrent sur l'amélioration de la gestion des indicateurs de session, l'ajout du support des tarifs dans l'API, et des mises à jour de sécurité des dépendances. Ces changements visent à offrir une meilleure analyse des données de recharge et à renforcer la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout du support des tarifs via l'API. [#37a19af](https://github.com/MTES-MCT/qualicharge/pull/37a19af)
- Ajout d'un indicateur e5 pour Prefect. [#d2027c1](https://github.com/MTES-MCT/qualicharge/commit/d2027c1)

### Évolutions techniques
- Correction d'un bug dans Prefect concernant le décalage des indicateurs de session (ajout d'un offset de 15 jours). [#9154a3b](https://github.com/MTES-MCT/qualicharge/commit/9154a3b)
- Mise à jour de la version du conteneur `ghcr.io/astral-sh/uv` vers la v0.11.19. [#7f0a6b4](https://github.com/MTES-MCT/qualicharge/commit/7f0a6b4)

### Autres changements
- Mise à jour de la dépendance `pyarrow` vers la version 23.0.1 pour des raisons de sécurité. [#9cfc1a2](https://github.com/MTES-MCT/qualicharge/commit/9cfc1a2)
- Mise à jour de la dépendance `starlette` vers au moins la version 1.0.1 pour des raisons de sécurité. [#6960978](https://github.com/MTES-MCT/qualicharge/commit/6960978)
- Mise à jour de la dépendance `data7` vers la version 1.0.2 pour des raisons de sécurité. [#82d7b18](https://github.com/MTES-MCT/qualicharge/commit/82d7b18)
