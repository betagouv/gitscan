## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 24 avril 2026)

### Résumé
Ce changelog fait état d'une période d'activité principalement axée sur la correction de bugs, l'adaptation aux changements de sources de données et l'amélioration de la robustesse des pipelines existants. Des refactorings ont été effectués pour optimiser certains traitements et faciliter la maintenance du code. Une attention particulière a été portée à l'amélioration du monitoring et des notifications.

### Évolutions fonctionnelles
- Correction de la récupération de l'ID maximum pour le pipeline des pétitions [#654](https://github.com/datagouv/datagouvfr_data_pipelines/issues/654).
- Ajout de nouvelles colonnes dans les tables météo.
- Correction du chemin vers le fichier geojson dans le pipeline IRVE.
- Exclusion du JDD consolidé du PAN pour le pipeline IRVE [#645](https://github.com/datagouv/datagouvfr_data_pipelines/issues/645).
- Ajout d'une nouvelle colonne dans un pipeline (détails non spécifiés).

### Évolutions techniques
- Refactoring du pipeline météo postgres pour une vérification plus précoce de l'insertion des données [#650](https://github.com/datagouv/datagouvfr_data_pipelines/issues/650).
- Déplacement de toutes les opérations liées au schéma dans un dossier dédié [#649](https://github.com/datagouv/datagouvfr_data_pipelines/issues/649).
- Amélioration de l'efficacité de la vérification de l'existence du fichier postgres.
- Suppression d'un DAG obsolète (SIRENE geocodage).
- Gestion améliorée des erreurs lors des requêtes PUT vers datagouv.
- Prévention des exécutions concurrentes de certains pipelines.
- Refactoring pour pousser le nouveau fichier même en l'absence de changement.

### Autres changements
- Suppression d'une vérification de santé inutile.
- Amélioration du linting du code.
- Ajustements pour s'adapter aux changements des sources de données (plusieurs occurrences).
- Ajout de notifications sur le canal simplifions.
- Ping sur Tchap [#648](https://github.com/datagouv/datagouvfr_data_pipelines/issues/648).
- Désactivation des notifications pour certains pipelines (tops).
- Restauration de la conversion restore>html.
- Suppression de l'utilisation de markdown temporaire.
