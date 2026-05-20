## Changelog : depenses-eclairees (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la qualité de l'extraction des données, notamment grâce à des ajustements des prompts utilisés par les modèles d'IA, et sur la gestion des erreurs et des performances, en particulier pour le traitement des fichiers Excel volumineux. Des améliorations de l'interface d'administration et du système de permissions ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'extraction d'informations pour différents types de documents : Acte d'Engagement (AE), Convention Collective Applicables aux Professions (CCAP), Devis et Documents de Consultation des Marchés Publics (DC4).
- Ajout de la conservation du numéro de compte bancaire (AE, DC4) et amélioration de la logique de post-processing des RIB.
- Ajout d'un post-processing pour le nom des sociétés et des cotraitants.
- Correction du schéma pour les DC4 [#125](https://github.com/betagouv/depenses-eclairees/issues/125).
- Correction de l'alignement du schéma RIB pour la sous-traitance.
- Amélioration de la gestion des erreurs de décodage JSON dans le client LLM avec une logique de nouvelle tentative [#123](https://github.com/betagouv/depenses-eclairees/issues/123).
- Ajout d'une fonction pour lister les erreurs d'un certain type (Faux Positifs, Faux Positifs 2, Faux Négatifs) [#124](https://github.com/betagouv/depenses-eclairees/issues/124).
- Amélioration du système de permissions avec la prise en charge des scopes wildcard [#114](https://github.com/betagouv/depenses-eclairees/issues/114).
- Amélioration de l'interface d'administration avec des filtres et une meilleure organisation [#112](https://github.com/betagouv/depenses-eclairees/issues/112).

### Évolutions techniques
- Refactorisation de la définition des schémas de données [#120](https://github.com/betagouv/depenses-eclairees/issues/120).
- Renommage de `DataEngagement` en `Engagement` et `DataBatch` en `EngagementTag` [#122](https://github.com/betagouv/depenses-eclairees/issues/122).
- Ajout de métriques pour évaluer la détection, la précision et les hallucinations des modèles d'IA [#110](https://github.com/betagouv/depenses-eclairees/issues/110).
- Amélioration des tests de bout en bout (e2e) avec l'ajout de métriques de rappel et de précision.
- Refactorisation des tests e2e pour simplifier la gestion des colonnes et améliorer les vérifications des valeurs nulles.
- Optimisation du traitement des fichiers Excel volumineux pour éviter les erreurs de mémoire (OOM) [#115](https://github.com/betagouv/depenses-eclairees/issues/115) et accélérer l'extraction [#116](https://github.com/betagouv/depenses-eclairees/issues/116).
- Mise en place d'une file d'attente dédiée pour le traitement OCR.
- Utilisation de la nouvelle API `list_ej_place` pour la synchronisation [#117](https://github.com/betagouv/depenses-eclairees/issues/117).
- Suppression de la dépendance `jupyter` et restauration de `ipython`.
- Suppression de la commande `--force-analyze` dans le cron.
- Ajout de la dépendance `pyxlsb` pour la prise en charge des fichiers Excel au format .xlsb.
- Amélioration de la gestion des erreurs dans l'API OCR avec des détails supplémentaires.
- Limitation de la taille maximale des fichiers Excel à 2Mo.

### Autres changements
- Nettoyage du code [#118](https://github.com/betagouv/depenses-eclairees/issues/118).
- Correction de la précision du prompt DC4 pour la date de dernière signature.
- Mise à jour des dépendances [#113](https://github.com/betagouv/depenses-eclairees/issues/113).
- Suppression des répertoires `__MACOSX` lors de l'extraction des fichiers zip [#119](https://github.com/betagouv/depenses-eclairees/issues/119).
- Correction d'un bug dans le filtre `filter_stuck_batches` [#111](https://github.com/betagouv/depenses-eclairees/issues/111).
