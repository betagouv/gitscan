## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les pipelines de données ont bénéficié d'améliorations significatives en termes de robustesse et de gestion des erreurs, notamment pour les données météo, DVF et les pipelines liés à l'eau. Des corrections ont été apportées pour gérer les timeouts, les erreurs de connexion et les problèmes de mémoire. L'ajout de pre-commit et la mise à jour de la version de Python contribuent à améliorer la qualité du code et la cohérence de l'environnement.

### Évolutions fonctionnelles
- Correction d'un problème qui faisait planter les pipelines metric-api en production. [#673](https://github.com/datagouv/datagouvfr_data_pipelines/issues/673)
- Amélioration de la gestion des fichiers CSV pour l'upload vers le stockage objet. [#692](https://github.com/datagouv/datagouvfr_data_pipelines/issues/692)
- Ajout d'un déclencheur de reconstruction manuelle pour le pipeline Finess. [#685](https://github.com/datagouv/datagouvfr_data_pipelines/issues/685)
- Correction de la gestion des données manquantes pour les décès. [#686](https://github.com/datagouv/datagouvfr_data_pipelines/issues/686)
- Publication des fichiers de la pétition Sénat. [#699](https://github.com/datagouv/datagouvfr_data_pipelines/issues/699)
- Augmentation du timeout pour les DAGs "controle eau" et "carburants" afin d'éviter les échecs. [#697](https://github.com/datagouv/datagouvfr_data_pipelines/issues/697) et [#698](https://github.com/datagouv/datagouvfr_data_pipelines/issues/698)
- Ajout d'indicateurs pour les DAGs de traitement des données. [#679](https://github.com/datagouv/datagouvfr_data_pipelines/issues/679)
- Ajout d'alertes si l'ID d'un fichier n'est pas unique dans un dataset. [#681](https://github.com/datagouv/datagouvfr_data_pipelines/issues/681)
- Reconstruction de la hiérarchie des parents/ancêtres à partir des relations INSEE pour les géozones. [#678](https://github.com/datagouv/datagouvfr_data_pipelines/issues/678)
- Ajout de la population et des géométries pour les géozones. [#682](https://github.com/datagouv/datagouvfr_data_pipelines/issues/682)

### Évolutions techniques
- Ajout de pre-commit pour améliorer la qualité du code. [#687](https://github.com/datagouv/datagouvfr_data_pipelines/issues/687)
- Mise à jour de la version de Python pour correspondre à la version de production. [#688](https://github.com/datagouv/datagouvfr_data_pipelines/issues/688)
- Augmentation du nombre maximal de runs actifs de 2 à 6. [#702](https://github.com/datagouv/datagouvfr_data_pipelines/issues/702)
- Amélioration de la gestion des connexions FTP et ajout de délais pour éviter les erreurs. [#709](https://github.com/datagouv/datagouvfr_data_pipelines/issues/709) et [#689](https://github.com/datagouv/datagouvfr_data_pipelines/issues/689)
- Ajout de mécanismes de retry et de backoff pour les requêtes. [#708](https://github.com/datagouv/datagouvfr_data_pipelines/issues/708)
- Correction du typage de la date pour la comparaison minimale. [#724](https://github.com/datagouv/datagouvfr_data_pipelines/issues/724)

### Autres changements
- Corrections et mises à jour diverses pour les DAGs DVF, notamment la gestion des noms de fichiers et des données manquantes. [#722](https://github.com/datagouv/datagouvfr_data_pipelines/issues/722), [#715](https://github.com/datagouv/datagouvfr_data_pipelines/issues/715), [#714](https://github.com/datagouv/datagouvfr_data_pipelines/issues/714), [#713](https://github.com/datagouv/datagouvfr_data_pipelines/issues/713)
- Suppression de configurations obsolètes. [#720](https://github.com/datagouv/datagouvfr_data_pipelines/issues/720)
- Suppression du DAG "formation". [#703](https://github.com/datagouv/datagouvfr_data_pipelines/issues/703)
- Suppression de l'étape de décompression pour le pipeline DVF. [#719](https://github.com/datagouv/datagouvfr_data_pipelines/issues/719)
- Correction de la gestion des fichiers temporaires pour le pipeline météo. [#705](https://github.com/datagouv/datagouvfr_data_pipelines/issues/705) et [#696](https://github.com/datagouv/datagouvfr_data_pipelines/issues/696)
- Suppression de données anciennes. [#716](https://github.com/datagouv/datagouvfr_data_pipelines/issues/716)
- Ajout de commentaires pour faciliter une future refactorisation du pipeline météo. [#710](https://github.com/datagouv/datagouvfr_data_pipelines/issues/710)
- Correction de l'affichage des DAGs PE (Production Exécutable). [#680](https://github.com/datagouv/datagouvfr_data_pipelines/issues/680)
- Correction de la gestion des répertoires inexistants. [#701](https://github.com/datagouv/datagouvfr_data_pipelines/issues/701)
- Correction de la gestion du dossier TMP pour le pipeline météo. [#700](https://github.com/datagouv/datagouvfr_data_pipelines/issues/700)
- Mise à jour des propriétaires par défaut des DAGs. [#690](https://github.com/datagouv/datagouvfr_data_pipelines/issues/690)
- Correction d'une erreur d'instanciation du client S3. [#694](https://github.com/datagouv/datagouvfr_data_pipelines/issues/694)
- Rétablissement d'une correction temporaire pour la connexion SSH. [#695](https://github.com/datagouv/datagouvfr_data_pipelines/issues/695)
