## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les pipelines de données ont bénéficié d'améliorations significatives en termes de gestion des données géographiques (ajout de populations et de géométries), de migration vers l'infrastructure OVH pour le stockage, et d'optimisations pour la récupération et le traitement des données depuis diverses sources comme FTP et S3. Des corrections ont également été apportées pour améliorer la robustesse et la fiabilité des pipelines existants.

### Évolutions fonctionnelles
- Ajout de données de population et de géométries pour les zones géographiques. [#682](https://github.com/datagouv/datagouvfr_data_pipelines/pull/682)
- Amélioration de la gestion des jeux de données de décès, permettant de contourner la vérification de mise à jour lorsqu'ils sont mis à jour manuellement. [#677](https://github.com/datagouv/datagouvfr_data_pipelines/issues/677)
- Ajout de nouveaux packs PNT. [#669](https://github.com/datagouv/datagouvfr_data_pipelines/pull/669)
- Reconstruction de la hiérarchie des parents/ancêtres des zones géographiques à partir des relations INSEE. [#678](https://github.com/datagouv/datagouvfr_data_pipelines/pull/678)

### Évolutions techniques
- Migration du stockage vers l'infrastructure OVH Minio, abandonnant l'utilisation de l'ancien service. [#675](https://github.com/datagouv/datagouvfr_data_pipelines/pull/675) et [#670](https://github.com/datagouv/datagouvfr_data_pipelines/pull/670)
- Utilisation de l'Airflow SDK pour les imports, modernisant ainsi le code. [#674](https://github.com/datagouv/datagouvfr_data_pipelines/pull/674)
- Amélioration de la gestion des connexions Airflow, permettant la spécification du port. [#676](https://github.com/datagouv/datagouvfr_data_pipelines/pull/676)
- Suppression périodique des anciens digests pour optimiser le stockage. [#672](https://github.com/datagouv/datagouvfr_data_pipelines/pull/672)
- Optimisations diverses pour la récupération de données depuis FTP et S3, incluant la gestion des en-têtes, des timeouts et des erreurs de fichiers manquants.
- Correction d'un problème d'indempotence lors de la création de répertoires pour les zones géographiques. [#683](https://github.com/datagouv/datagouvfr_data_pipelines/pull/683)

### Autres changements
- Suppression des notifications spam inutiles. [#667](https://github.com/datagouv/datagouvfr_data_pipelines/pull/667)
- Augmentation des timeouts pour certains DAGs (météo, général).
- Amélioration de la gestion des fichiers de schémas sur S3.
- Corrections mineures et refactorings pour améliorer la lisibilité et la maintenabilité du code.
