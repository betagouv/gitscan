## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les pipelines de données ont bénéficié d'améliorations significatives en termes de robustesse et de performance, notamment pour les pipelines météo, carburants, et géozones. Des corrections ont été apportées pour résoudre des problèmes de timeout, de gestion des erreurs et de consommation de ressources. L'ajout de pre-commit améliore la qualité du code.

### Évolutions fonctionnelles
- Correction d'un problème qui faisait planter les pipelines de l'API métrique [#673](https://github.com/datagouv/datagouvfr_data_pipelines/issues/673).
- Amélioration de la gestion des données de décès [#686](https://github.com/datagouv/datagouvfr_data_pipelines/issues/686).
- Ajout d'un déclencheur manuel pour forcer la reconstruction des données Finess [#685](https://github.com/datagouv/datagouvfr_data_pipelines/issues/685).
- Mise à jour des données géographiques (geozones) avec ajout de populations et de géométries [#682](https://github.com/datagouv/datagouvfr_data_pipelines/issues/682), et reconstruction de la hiérarchie parent/ancêtre [#678](https://github.com/datagouv/datagouvfr_data_pipelines/issues/678).
- Publication des fichiers de la pétition du Sénat [#699](https://github.com/datagouv/datagouvfr_data_pipelines/issues/699).
- Amélioration de l'alerte en cas d'ID de fichier non unique dans un dataset [#681](https://github.com/datagouv/datagouvfr_data_pipelines/issues/681).
- Ajout d'insights pour les DAG de traitement des données [#679](https://github.com/datagouv/datagouvfr_data_pipelines/issues/679).
- Suppression du DAG de formation [#703](https://github.com/datagouv/datagouvfr_data_pipelines/issues/703).

### Évolutions techniques
- Ajout de pre-commit pour améliorer la qualité du code [#687](https://github.com/datagouv/datagouvfr_data_pipelines/issues/687).
- Augmentation du nombre maximal de runs actifs pour certains DAGs (de 2 à 6) [#702](https://github.com/datagouv/datagouvfr_data_pipelines/issues/702).
- Amélioration de la gestion des timeouts et ajout de mécanismes de retry et de backoff pour les requêtes vers les sites web [#707](https://github.com/datagouv/datagouvfr_data_pipelines/issues/707), [#708](https://github.com/datagouv/datagouvfr_data_pipelines/issues/708), [#709](https://github.com/datagouv/datagouvfr_data_pipelines/issues/709).
- Optimisation de la gestion des connexions FTP pour éviter les timeouts [#689](https://github.com/datagouv/datagouvfr_data_pipelines/issues/689).
- Mise à jour de la version de Python pour correspondre à l'environnement de production [#688](https://github.com/datagouv/datagouvfr_data_pipelines/issues/688).
- Correction de problèmes de mémoire (OOM) et d'amélioration des retries pour le pipeline de contrôle sanitaire de l'eau [#691](https://github.com/datagouv/datagouvfr_data_pipelines/issues/691).
- Augmentation du timeout pour les DAGs de contrôle de l'eau et des carburants [#697](https://github.com/datagouv/datagouvfr_data_pipelines/issues/697), [#698](https://github.com/datagouv/datagouvfr_data_pipelines/issues/698).
- Amélioration de la gestion des erreurs et ajout de logs pour le pipeline météo [#700](https://github.com/datagouv/datagouvfr_data_pipelines/issues/700), [#701](https://github.com/datagouv/datagouvfr_data_pipelines/issues/701), [#704](https://github.com/datagouv/datagouvfr_data_pipelines/issues/704), [#705](https://github.com/datagouv/datagouvfr_data_pipelines/issues/705), [#710](https://github.com/datagouv/datagouvfr_data_pipelines/issues/710), [#711](https://github.com/datagouv/datagouvfr_data_pipelines/issues/711), [#712](https://github.com/datagouv/datagouvfr_data_pipelines/issues/712), [#713](https://github.com/datagouv/datagouvfr_data_pipelines/issues/713), [#721](https://github.com/datagouv/datagouvfr_data_pipelines/issues/721).
- Correction du typage de la date pour la comparaison minimale [#724](https://github.com/datagouv/datagouvfr_data_pipelines/issues/724).
- Mise à jour des noms des DAGs DVF [#722](https://github.com/datagouv/datagouvfr_data_pipelines/issues/722).

### Autres changements
- Suppression de configurations obsolètes (REF_CC/ETP_DECAD et NIVO) [#720](https://github.com/datagouv/datagouvfr_data_pipelines/issues/720).
- Suppression de données anciennes [#715](https://github.com/datagouv/datagouvfr_data_pipelines/issues/715).
- Correction de linting [#719](https://github.com/datagouv/datagouvfr_data_pipelines/issues/719).
- Modification du processus de téléchargement des fichiers DVF (suppression du décompression et utilisation du nouveau format de nom de fichier) [#714](https://github.com/datagouv/datagouvfr_data_pipelines/issues/714).
- Mise à jour des noms des propriétaires par défaut des DAGs [#690](https://github.com/datagouv/datagouvfr_data_pipelines/issues/690).
- Correction temporaire d'un problème SSH pour IRVE (puis annulée) [#695](https://github.com/datagouv/datagouvfr_data_pipelines/issues/695).
- Modification temporaire de l'écriture des fichiers météo vers /tmp [#696](https://github.com/datagouv/datagouvfr_data_pipelines/issues/696) (puis annulée).
- Mise à jour de la connexion SSH [#706](https://github.com/datagouv/datagouvfr_data_pipelines/issues/706).
- Amélioration de la gestion des fichiers CSV pour le stockage d'objets [#692](https://github.com/datagouv/datagouvfr_data_pipelines/issues/692).
- Affichage uniquement des DAGs PE actifs [#680](https://github.com/datagouv/datagouvfr_data_pipelines/issues/680).
