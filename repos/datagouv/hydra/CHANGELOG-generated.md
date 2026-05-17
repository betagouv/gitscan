## Changelog : hydra (30 derniers jours, au 15 mai 2026)

### Résumé
Les dernières mises à jour de Hydra se concentrent sur l'amélioration de l'efficacité du traitement des données, notamment en optimisant la génération de GeoJSON et en restructurant le code de conversion. Ces améliorations visent à accélérer l'analyse des données et à faciliter la maintenance du projet.

### Évolutions fonctionnelles
- La génération de GeoJSON à partir de PostgreSQL est désormais privilégiée au lieu de relire les fichiers CSV, améliorant ainsi les performances. [#404](https://github.com/datagouv/hydra/pull/404)
- L'export GeoJSON est désormais réalisé uniquement dans le pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423)
- Correction d'un problème lié à la suppression d'une protection obsolète lors de la conversion CSV vers GeoJSON. [#1234](https://github.com/datagouv/hydra/commit/7591db4)

### Évolutions techniques
- Refactorisation du code de conversion : les méthodes de conversion ont été séparées dans des fichiers dédiés dans le répertoire `/conversion` pour une meilleure organisation et maintenabilité. [#422](https://github.com/datagouv/hydra/pull/422)
- Suppression de code redondant dans l'analyse CSV. [#426](https://github.com/datagouv/hydra/pull/426)
- Amélioration de la gestion des erreurs et de la robustesse du code.

### Autres changements
- Publication de la version 2.10.0.
- Publication de la version 2.9.0.
- Publication de la version 2.8.1.
