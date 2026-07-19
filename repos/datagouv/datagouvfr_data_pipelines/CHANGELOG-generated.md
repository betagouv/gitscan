## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la fiabilité des pipelines de données existants, notamment ceux liés à la météo, aux données de santé (déces, contrôles sanitaires de l'eau) et aux zones géographiques. Des corrections de bugs ont été apportées pour gérer les erreurs de connexion, les timeouts et les problèmes de stockage. L'infrastructure a également été mise à jour avec l'ajout de pre-commit et la migration vers OVH pour le stockage objet.

### Évolutions fonctionnelles
- Ajout d'un déclencheur de reconstruction manuelle pour le pipeline Finess [#685](https://github.com/datagouv/datagouvfr_data_pipelines/issues/685).
- Amélioration du pipeline geozones avec la reconstruction de la hiérarchie parents/ancêtres à partir des relations INSEE [#678](https://github.com/datagouv/datagouvfr_data_pipelines/issues/678) et l'ajout de données de population et de géométries [#682](https://github.com/datagouv/datagouvfr_data_pipelines/issues/682).
- Ajout d'insights pour les DAG de traitement de données [#679](https://github.com/datagouv/datagouvfr_data_pipelines/issues/679).
- Suppression du DAG de formation [#703](https://github.com/datagouv/datagouvfr_data_pipelines/issues/703).
- Correction de la publication des fichiers pour le pipeline des pétitions du Sénat [#699](https://github.com/datagouv/datagouvfr_data_pipelines/issues/699).

### Évolutions techniques
- Ajout de pre-commit pour améliorer la qualité du code [#687](https://github.com/datagouv/datagouvfr_data_pipelines/issues/687).
- Migration du stockage objet vers OVH [#670](https://github.com/datagouv/datagouvfr_data_pipelines/issues/670) et [#675](https://github.com/datagouv/datagouvfr_data_pipelines/issues/675).
- Mise à jour de la version de Python pour correspondre à l'environnement de production [#688](https://github.com/datagouv/datagouvfr_data_pipelines/issues/688).
- Utilisation de l'Airflow SDK pour les imports [#674](https://github.com/datagouv/datagouvfr_data_pipelines/issues/674).
- Amélioration de la gestion des erreurs et des timeouts pour les connexions FTP et les requêtes HTTP (pipelines météo, contrôles sanitaires de l'eau).
- Optimisation de l'instanciation des clients S3 et de la gestion des fichiers temporaires.
- Correction d'un problème de fuite de mémoire dans le pipeline de contrôle sanitaire de l'eau [#691](https://github.com/datagouv/datagouvfr_data_pipelines/issues/691).

### Autres changements
- Augmentation du nombre maximal de runs actifs pour certains DAGs (de 2 à 6) [#702](https://github.com/datagouv/datagouvfr_data_pipelines/issues/702).
- Correction de problèmes de linting [#719](https://github.com/datagouv/datagouvfr_data_pipelines/issues/719).
- Diverses corrections et améliorations de la documentation et de la configuration.
- Suppression de code obsolète et nettoyage du code.
- Ajout de logs et de messages d'erreur pour faciliter le débogage.
- Correction de la gestion des noms de fichiers pour le pipeline DVF [#715](https://github.com/datagouv/datagouvfr_data_pipelines/issues/715), [#714](https://github.com/datagouv/datagouvfr_data_pipelines/issues/714) et [#713](https://github.com/datagouv/datagouvfr_data_pipelines/issues/713).
