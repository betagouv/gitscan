## Changelog : depenses-eclairees (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité de l'extraction d'informations à partir des documents financiers, notamment grâce à l'affinage des prompts utilisés par l'IA et à l'ajout de post-traitements pour normaliser les données extraites. Des améliorations ont également été apportées à l'infrastructure et aux tests pour une meilleure fiabilité et une meilleure évaluation des performances.

### Évolutions fonctionnelles
- Amélioration de l'extraction d'informations pour les avenants, avec extraction enrichie, post-traitements et tests de qualité sur Grist. [#131](https://github.com/betagouv/depenses-eclairees/issues/131)
- Amélioration des prompts d'extraction pour les actes d'engagement (AE), les conventions de commande (CCAP), les devis et les documents DC4, pour une meilleure précision. [#126](https://github.com/betagouv/depenses-eclairees/issues/126)
- Amélioration du schéma de données pour les RIB des sous-traitants, aligné sur celui des mandataires. [#125](https://github.com/betagouv/depenses-eclairees/issues/125)
- Ajout de post-traitements pour la normalisation des noms de sociétés et des RIB. [#127](https://github.com/betagouv/depenses-eclairees/issues/127)
- Clarification des règles d'extraction pour les reconductions dans les actes d'engagement.
- Ajout de la fonction `check_quality_by_error_type` pour évaluer la qualité de l'extraction en fonction des erreurs (faux négatifs, faux positifs). [#124](https://github.com/betagouv/depenses-eclairees/issues/124)
- Ajout de métriques (rappel et précision) pour évaluer la qualité de l'extraction des valeurs présentes. [#110](https://github.com/betagouv/depenses-eclairees/issues/110)

### Évolutions techniques
- Refactorisation des schémas de données pour une meilleure organisation et maintenabilité. [#120](https://github.com/betagouv/depenses-eclairees/issues/120)
- Gestion améliorée des erreurs de décodage JSON dans le client LLM avec une logique de nouvelle tentative. [#123](https://github.com/betagouv/depenses-eclairees/issues/123)
- Ajout de métriques pour évaluer le nombre de tokens utilisés et la date de traitement. [#128](https://github.com/betagouv/depenses-eclairees/issues/128)
- Refactorisation des tests de bout en bout (e2e) pour une meilleure clarté et une meilleure gestion des colonnes et des valeurs nulles.
- Amélioration de la gestion des fichiers Excel volumineux dans le pipeline, avec une limite de taille réduite à 2Mo.
- Suppression de la dépendance à Jupyter et restauration de IPython pour une meilleure expérience en ligne de commande.
- Suppression de la directive `--force-analyze` dans le cron.
- Ajout de détails aux erreurs de l'API OCR.
- Utilisation de la nouvelle API `list_ej_place` pour la synchronisation. [#117](https://github.com/betagouv/depenses-eclairees/issues/117)

### Autres changements
- Renommage de `DataEngagement` en `Engagement` et de `DataBatch` en `EngagementTag`. [#122](https://github.com/betagouv/depenses-eclairees/issues/122)
- Nettoyage du code. [#118](https://github.com/betagouv/depenses-eclairees/issues/118)
- Ajout de la dépendance `pyxlsb` pour la gestion des fichiers Excel au format `.xlsb`.
- Suppression des répertoires `__MACOSX` lors de l'extraction des fichiers ZIP. [#119](https://github.com/betagouv/depenses-eclairees/issues/119)
- Application d'un paramètre JSON strict et d'une température de 0 pour les tests e2e. [#121](https://github.com/betagouv/depenses-eclairees/issues/121)
