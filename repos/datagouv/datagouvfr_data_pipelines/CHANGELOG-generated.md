## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce changelog présente les améliorations apportées aux pipelines de données de data.gouv.fr au cours du dernier mois. Les modifications incluent des corrections de bugs pour améliorer la fiabilité des pipelines, des optimisations de performance, et des mises à jour de l'infrastructure pour supporter de nouveaux jeux de données et des fonctionnalités améliorées. Des efforts ont également été faits pour améliorer la gestion des erreurs et le monitoring des pipelines.

### Évolutions fonctionnelles
- Ajout de la prise en charge de nouveaux packs PNT [#669](https://github.com/datagouv/datagouvfr_data_pipelines/issues/669).
- Amélioration de la gestion des fichiers de schémas sur S3 pour une meilleure fiabilité des uploads.
- Publication des fichiers pour la pétition du Sénat [#699](https://github.com/datagouv/datagouvfr_data_pipelines/issues/699).
- Ajout d'un déclencheur manuel pour reconstruire les données Finess [#685](https://github.com/datagouv/datagouvfr_data_pipelines/issues/685).
- Suppression du DAG de formation [#703](https://github.com/datagouv/datagouvfr_data_pipelines/issues/703).
- Ajout de la gestion des populations et des géométries pour les données Géozones [#678](https://github.com/datagouv/datagouvfr_data_pipelines/issues/678).

### Évolutions techniques
- Mise à jour de Python à la même version que l'environnement de production [#688](https://github.com/datagouv/datagouvfr_data_pipelines/issues/688).
- Ajout de `pre-commit` pour améliorer la qualité du code [#687](https://github.com/datagouv/datagouvfr_data_pipelines/issues/687).
- Utilisation de l'Airflow SDK pour les imports [#674](https://github.com/datagouv/datagouvfr_data_pipelines/issues/674).
- Migration vers les buckets OVH pour le stockage des données [#670](https://github.com/datagouv/datagouvfr_data_pipelines/issues/670).
- Amélioration de la gestion des erreurs et ajout de mécanismes de retry avec backoff pour les requêtes vers les services externes [#707](https://github.com/datagouv/datagouvfr_data_pipelines/issues/707), [#708](https://github.com/datagouv/datagouvfr_data_pipelines/issues/708).
- Augmentation du timeout pour les DAGs `controle eau` et `carburants` pour éviter les échecs [#697](https://github.com/datagouv/datagouvfr_data_pipelines/issues/697), [#698](https://github.com/datagouv/datagouvfr_data_pipelines/issues/698).
- Augmentation du nombre maximal de runs actifs de 2 à 6 [#702](https://github.com/datagouv/datagouvfr_data_pipelines/issues/702).
- Optimisation de l'instanciation des clients S3 pour éviter les redondances [#694](https://github.com/datagouv/datagouvfr_data_pipelines/issues/694).

### Autres changements
- Mise à jour des propriétaires par défaut des DAGs [#690](https://github.com/datagouv/datagouvfr_data_pipelines/issues/690).
- Correction de problèmes de timeout de connexion FTP [#689](https://github.com/datagouv/datagouvfr_data_pipelines/issues/689).
- Amélioration de la gestion des notifications et suppression des notifications potentiellement spammantes [#691](https://github.com/datagouv/datagouvfr_data_pipelines/issues/691), [#667](https://github.com/datagouv/datagouvfr_data_pipelines/issues/667).
- Corrections diverses pour les pipelines météo [#700](https://github.com/datagouv/datagouvfr_data_pipelines/issues/700), [#701](https://github.com/datagouv/datagouvfr_data_pipelines/issues/701), [#704](https://github.com/datagouv/datagouvfr_data_pipelines/issues/704), [#705](https://github.com/datagouv/datagouvfr_data_pipelines/issues/705), [#709](https://github.com/datagouv/datagouvfr_data_pipelines/issues/709), [#710](https://github.com/datagouv/datagouvfr_data_pipelines/issues/710), [#711](https://github.com/datagouv/datagouvfr_data_pipelines/issues/711), [#712](https://github.com/datagouv/datagouvfr_data_pipelines/issues/712).
- Corrections pour le pipeline metric-api [#673](https://github.com/datagouv/datagouvfr_data_pipelines/issues/673).
- Correction pour le pipeline décès [#686](https://github.com/datagouv/datagouvfr_data_pipelines/issues/686).
- Suppression de digests anciens [#672](https://github.com/datagouv/datagouvfr_data_pipelines/issues/672).
- Amélioration de la gestion des erreurs pour les données géozones [#683](https://github.com/datagouv/datagouvfr_data_pipelines/issues/683), [#684](https://github.com/datagouv/datagouvfr_data_pipelines/issues/684).
