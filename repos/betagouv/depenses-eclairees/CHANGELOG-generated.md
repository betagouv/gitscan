## Changelog : depenses-eclairees (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'amélioration de la qualité de l'extraction d'informations des documents, notamment grâce à des ajustements des prompts utilisés par l'IA, et sur l'optimisation du traitement des fichiers, en particulier les fichiers Excel volumineux. Des métriques d'évaluation de la qualité de l'extraction ont également été ajoutées pour un suivi plus précis des performances.

### Évolutions fonctionnelles
- Amélioration de la reconnaissance des informations dans les documents : actes d'engagement (AE), conventions de commande publique (CCAP), devis et documents DC4. Les prompts utilisés par l'IA ont été affinés pour une meilleure extraction des données.
- Correction du schéma pour les RIB dans les documents DC4 [#125](https://github.com/betagouv/depenses-eclairees/issues/125).
- Ajout d'une fonction pour lister les erreurs d'extraction par type (faux positifs, faux négatifs) [#124](https://github.com/betagouv/depenses-eclairees/issues/124).
- Amélioration de la gestion des numéros de compte et des informations bancaires (RIB) dans les documents.
- Ajout de métriques (précision, rappel, hallucinations) pour évaluer la qualité de l'extraction des données [#110](https://github.com/betagouv/depenses-eclairees/issues/110).
- Renommage des modèles de données `DataEngagement` en `Engagement` et `DataBatch` en `EngagementTag` [#122](https://github.com/betagouv/depenses-eclairees/issues/122).

### Évolutions techniques
- Gestion améliorée des erreurs de décodage JSON dans le client LLM avec une logique de nouvelle tentative [#123](https://github.com/betagouv/depenses-eclairees/issues/123).
- Refactorisation de la définition des schémas de données [#120](https://github.com/betagouv/depenses-eclairees/issues/120).
- Optimisation du traitement des fichiers Excel volumineux :
    - Limitation de la taille des fichiers Excel traités à 2Mo, avec un statut "skipped" pour les fichiers plus grands [#119](https://github.com/betagouv/depenses-eclairees/issues/119).
    - Accélération de l'extraction des données des fichiers Excel [#116](https://github.com/betagouv/depenses-eclairees/issues/116).
    - Ajout de la dépendance `pyxlsb` pour supporter les fichiers Excel au format .xlsb [#118](https://github.com/betagouv/depenses-eclairees/issues/118).
- Mise en place d'une file d'attente dédiée pour le traitement OCR.
- Amélioration de la gestion de la mémoire lors du traitement des fichiers Excel pour éviter les erreurs de type "Out Of Memory" (OOM) [#115](https://github.com/betagouv/depenses-eclairees/issues/115).
- Refactorisation des tests de bout en bout (e2e) pour une meilleure clarté et maintenabilité.
- Ajout de paramètres stricts pour le parsing JSON.
- Suppression de la dépendance `jupyter`.
- Ajout de métriques de token counting et de date de traitement [#128](https://github.com/betagouv/depenses-eclairees/issues/128).

### Autres changements
- Nettoyage du code et suppression d'imports inutilisés.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de détails aux erreurs dans l'API OCR.
- Suppression du paramètre `--force-analyze` dans le cron.
