## Changelog : hydra (30 derniers jours, au 13 mai 2026)

### Résumé
Les dernières mises à jour de Hydra se concentrent sur l'amélioration de la conversion de données, notamment en permettant la génération de GeoJSON directement à partir de la base de données PostgreSQL, et en restructurant le code pour une meilleure organisation et clarté. Des corrections et des améliorations mineures ont également été apportées pour optimiser les performances et la stabilité.

### Évolutions fonctionnelles
- Ajout de la génération de GeoJSON à partir de PostgreSQL au lieu de relire les fichiers CSV, améliorant ainsi les performances et l'efficacité. [#404](https://github.com/datagouv/hydra/pull/404)
- Correction de l'utilisation du nom de fichier de base comme paramètre dans les tâches, résolvant un problème potentiel lié au traitement des fichiers. [#416](https://github.com/datagouv/hydra/pull/416)
- Séparation des points de terminaison de statistiques en deux, avec des clés renommées pour une meilleure clarté. [#387](https://github.com/datagouv/hydra/pull/387)
- Ajout de l'export GeoJSON depuis la base de données uniquement dans le pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423)

### Évolutions techniques
- Refactorisation du code de conversion, avec séparation des méthodes de conversion dans des fichiers dédiés dans le répertoire `/conversion` pour une meilleure organisation. [#422](https://github.com/datagouv/hydra/pull/422)
- Suppression d'importations inutilisées pour nettoyer le code.
- Suppression de `__all__` redondant dans l'analyse CSV. [#426](https://github.com/datagouv/hydra/pull/426)

### Autres changements
- Publication de la version 2.9.0.
- Publication de la version 2.8.1.
- Publication de la version 2.8.0.
