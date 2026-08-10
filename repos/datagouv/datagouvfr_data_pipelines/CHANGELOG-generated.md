## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 04/08/2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'optimisation des pipelines de données immobilières (DVF) et la fiabilisation des connexions aux services de stockage (S3, SFTP). Des corrections ont également été apportées pour garantir la précision des données météo et la robustesse des traitements de fichiers.

### Évolutions fonctionnelles
- Correction de la couverture temporelle pour le traitement des données météo [#721](https://github.com/datagouv/datagouvfr_data_pipelines/issues/721).
- Mise à jour de la nomenclature des DAGs pour les données DVF [#722](https://github.com/datagouv/datagouvfr_data_pipelines/issues/722).

### Évolutions techniques
- **Optimisation du pipeline DVF** : passage au format compressé `.gz`, suppression de l'étape de décompression et automatisation du téléchargement des années manquantes [#714](https://github.com/datagouv/datagouvfr_data_pipelines/issues/714), [#715](https://github.com/datagouv/datagouvfr_data_pipelines/issues/715).
- **Fiabilisation des connexions de stockage** : corrections sur les connexions S3 et mise à jour du protocole SFTP pour Datalma [#725](https://github.com/datagouv/datagouvfr_data_pipelines/issues/725), [#727](https://github.com/datagouv/datagouvfr_data_pipelines/issues/727), [#728](https://github.com/datagouv/datagouvfr_data_pipelines/issues/728).
- **Correction de bugs de traitement** : résolution de problèmes de typage (dates) et mise à jour des expressions régulières pour le pattern de nommage des fichiers [#713](https://github.com/datagouv/datagouvfr_data_pipelines/issues/713), [#724](https://github.com/datagouv/datagouvfr_data_pipelines/issues/724).

### Autres changements
- **Nettoyage de la configuration** : suppression de jeux de données et de configurations obsolètes (SIM, REF_CC, ETP_DECAD, NIVO) [#720](https://github.com/datagouv/datagouvfr_data_pipelines/issues/720), [#729](https://github.com/datagouv/datagouvfr_data_pipelines/issues/729).
- **Maintenance** : mise à jour du linting [#719](https://github.com/datagouv/datagouvfr_data_pipelines/issues/719).
