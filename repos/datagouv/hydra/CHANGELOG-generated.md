## Changelog : hydra (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la performance et aux fonctionnalités d'Hydra. L'extraction de données depuis PostgreSQL a été optimisée, le support des WMS a été ajouté, et des corrections ont été apportées pour une meilleure gestion des fichiers et des statistiques. Des ajustements ont également été faits pour clarifier les informations exposées via l'API.

### Évolutions fonctionnelles
- Ajout du support pour l'analyse des WMS (Web Map Service) [#401](https://github.com/datagouv/hydra/pull/401).
- Amélioration de la gestion de la taille maximale des fichiers pour les formats inconnus [#414](https://github.com/datagouv/hydra/pull/414).
- Optimisation de l'extraction de données : génération de fichiers Parquet directement à partir de la base de données PostgreSQL au lieu de relire les fichiers CSV [#402](https://github.com/datagouv/hydra/pull/402).
- Correction de l'utilisation du nom de fichier de base dans les jobs [#416](https://github.com/datagouv/hydra/issues/416).

### Évolutions techniques
- Refactorisation des endpoints de statistiques pour une meilleure clarté et séparation [#387](https://github.com/datagouv/hydra/pull/387).
- Suppression d'une importation inutile [#10481b1](https://github.com/datagouv/hydra/commit/10481b1).

### Autres changements
- Publication de la version 2.8.0 [#12a4e16](https://github.com/datagouv/hydra/commit/12a4e16).
