## Changelog : potentiel-integration-enedis (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des erreurs et la robustesse de l'application, notamment en ce qui concerne le traitement des fichiers et l'interaction avec l'API Enedis. Des corrections ont été apportées pour garantir une meilleure fiabilité du processus d'import/export des données de raccordement.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors de la récupération des informations de raccordement depuis l'API Enedis. [#42](https://github.com/MTES-MCT/potentiel-integration-enedis/issues/42)
- Correction d'un bug empêchant le traitement correct de certains fichiers S3.

### Évolutions techniques
- Ajout de logs plus détaillés pour faciliter le débogage des erreurs liées à l'API Enedis.
- Refactorisation du code de gestion des fichiers S3 pour une meilleure lisibilité et maintenabilité.

### Autres changements
- Mise à jour de la dépendance `esbuild` via Dependabot. [#43](https://github.com/MTES-MCT/potentiel-integration-enedis/pull/43)
