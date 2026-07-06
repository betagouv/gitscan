## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce changelog présente les améliorations apportées aux pipelines de données de data.gouv.fr au cours du dernier mois. Les changements incluent des corrections de bugs, des améliorations de la gestion des données géographiques, des optimisations de l'infrastructure et des mises à jour pour supporter de nouveaux jeux de données et des sources de données externes.

### Évolutions fonctionnelles
- Ajout d'un déclencheur manuel pour forcer la reconstruction du pipeline Finess [#685](https://github.com/datagouv/datagouvfr_data_pipelines/issues/685).
- Ajout des données de population et des géométries pour les zones géographiques [#682](https://github.com/datagouv/datagouvfr_data_pipelines/issues/682).
- Reconstruction de la hiérarchie des parents/ancêtres à partir des relations INSEE pour les zones géographiques [#678](https://github.com/datagouv/datagouvfr_data_pipelines/issues/678).
- Ajout de nouveaux packs PNT [#669](https://github.com/datagouv/datagouvfr_data_pipelines/issues/669).
- Correction d'un problème de données manquantes pour les décès [#686](https://github.com/datagouv/datagouvfr_data_pipelines/issues/686).
- Correction d'un problème de timeout de connexion FTP [#689](https://github.com/datagouv/datagouvfr_data_pipelines/issues/689).
- Correction d'un problème d'upload de datasets et de timeout d'import pour les geozones [#684](https://github.com/datagouv/datagouvfr_data_pipelines/issues/684).
- Correction d'un problème d'alerte en cas d'ID de fichier non unique dans un dataset [#681](https://github.com/datagouv/datagouvfr_data_pipelines/issues/681).
- Correction d'un problème de contournement de la vérification de mise à jour pour le dataset décès en mode manuel [#677](https://github.com/datagouv/datagouvfr_data_pipelines/issues/677).

### Évolutions techniques
- Mise à jour de la version de Python pour correspondre à la version de production [#688](https://github.com/datagouv/datagouvfr_data_pipelines/issues/688).
- Migration vers les buckets OVH pour le stockage des données [#670](https://github.com/datagouv/datagouvfr_data_pipelines/issues/670) et [#675](https://github.com/datagouv/datagouvfr_data_pipelines/issues/675).
- Utilisation de l'Airflow SDK pour les imports [#674](https://github.com/datagouv/datagouvfr_data_pipelines/issues/674).
- Amélioration de la gestion des connexions FTP pour une récupération plus fiable des données.
- Optimisations diverses pour améliorer la performance et la robustesse des pipelines.
- Modification de la logique de nettoyage des dossiers temporaires pour éviter les erreurs.
- Ajout de logs plus détaillés pour faciliter le débogage.
- Mise à jour des propriétaires par défaut des DAGs [#690](https://github.com/datagouv/datagouvfr_data_pipelines/issues/690).

### Autres changements
- Affichage uniquement des DAGs PE actifs [#680](https://github.com/datagouv/datagouvfr_data_pipelines/issues/680).
- Ajout d'informations sur le traitement des données pour faciliter le monitoring [#679](https://github.com/datagouv/datagouvfr_data_pipelines/issues/679).
- Suppression de notifications potentiellement spammantes [#667](https://github.com/datagouv/datagouvfr_data_pipelines/issues/667).
- Suppression de variables inutilisées et nettoyage du code.
- Augmentation des timeouts pour certains DAGs (météo, etc.).
- Suppression régulière des digests anciens [#672](https://github.com/datagouv/datagouvfr_data_pipelines/issues/672).
- Correction de la gestion des types de contenu sur S3.
- Correction de problèmes liés aux préfixes et aux appels de fonctions sur S3.
