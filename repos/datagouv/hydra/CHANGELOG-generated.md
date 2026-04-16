## Changelog : hydra (30 derniers jours, au 15 avril 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance et de fonctionnalités. L'extraction de données a été optimisée, notamment pour la conversion de CSV en Parquet, et le support des données OGC a été étendu avec l'ajout de l'analyse WMS. Des corrections de bugs et des améliorations de la robustesse ont également été implémentées.

### Évolutions fonctionnelles
- Ajout du support pour l'analyse des services WMS (Web Map Service) via OGC. [#401](https://github.com/datagouv/hydra/pull/401)
- Amélioration de la conversion de CSV en Parquet : la conversion se fait désormais directement à partir de la base de données PostgreSQL, évitant une relecture du fichier CSV. [#402](https://github.com/datagouv/hydra/pull/402)
- Ajout de statistiques détaillées sur les temps de conversion pour les formats GeoJSON et PMTiles, facilitant le monitoring des performances. [#403](https://github.com/datagouv/hydra/pull/403)
- Gestion améliorée de la taille maximale des fichiers inconnus, avec une valeur par défaut. [#414](https://github.com/datagouv/hydra/pull/414)

### Évolutions techniques
- Refactorisation des endpoints de statistiques pour une meilleure clarté et organisation. [#387](https://github.com/datagouv/hydra/pull/387)
- Ajout de vérification de type statique avec `mypy` pour améliorer la qualité du code. [#391](https://github.com/datagouv/hydra/pull/391)
- Utilisation d'un dossier temporaire configurable pour les téléchargements et nettoyage des fichiers temporaires après extraction de fichiers gzip. [#400](https://github.com/datagouv/hydra/pull/400)
- Correction d'une erreur qui empêchait l'insertion correcte de données dans `tables_index` en cas de valeurs `NaN` ou infinies. [#397](https://github.com/datagouv/hydra/pull/397)
- Correction d'une erreur qui provoquait une exception `FileNotFoundError` dans les workers d'analyse si le fichier temporaire était manquant. [#395](https://github.com/datagouv/hydra/pull/395)
- Correction d'une URL incorrecte dans les vérifications. [#406](https://github.com/datagouv/hydra/pull/406)

### Autres changements
- Suppression d'un avertissement de log superflu dans le module OGC. [#399](https://github.com/datagouv/hydra/pull/399)
- Correction du script de publication en CI pour les releases. [#398](https://github.com/datagouv/hydra/pull/398)
- Mise à jour de la dépendance `csv-detective` vers la version 0.11.2. [#407](https://github.com/datagouv/hydra/pull/407)
