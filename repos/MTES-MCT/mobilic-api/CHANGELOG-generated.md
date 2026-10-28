## Changelog : mobilic-api (30 derniers jours, au 27/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité du système suite à un audit, l'amélioration de la fiabilité des données (notamment pour les immatriculations et les exports) et l'optimisation des performances de l'interface d'administration. L'expérience utilisateur a également été fluidifiée par l'ajout de nouvelles options de filtrage et de pagination.

### Évolutions fonctionnelles
- **Gestion des véhicules** : Amélioration de la saisie des immatriculations avec une normalisation automatique et le rejet des formats vides ou invalides [#855](https://github.com/MTES-MCT/mobilic-api/pull/855) [#856](https://github.com/MTES-MCT/mobilic-api/pull/856).
- **Exports et rapports** : Amélioration de la mise en forme des rapports Excel (centrage des cellules) et ajout d'un système de sauvegarde des exports en base de données pour garantir leur disponibilité [#827](https://github.com/MTES-MCT/mobilic-api/pull/827) [#848](https://github.com/MTES-MCT/mobilic-api/pull/848) [#851](https://github.com/MTES-MCT/mobilic-api/pull/851).
- **Navigation et filtrage** : Ajout de la pagination pour les listes d'activités et les jours de travail, et introduction de nouveaux filtres pour faciliter la recherche d'activités [#802](https://github.com/MTES-MCT/mobilic-api/pull/802) [#828](https://github.com/MTES-MCT/mobilic-api/pull/828) [#836](https://github.com/MTES-MCT/mobilic-api/pull/836).
- **Conformité et missions** : Optimisation de l'évaluation de l'activité des clients et amélioration de la gestion des missions annulées [#840](https://github.com/MTES-MCT/mobilic-api/pull/840) [#e4c66ee8](https://github.com/MTES-MCT/mobilic-api/commit/e4c66ee8).
- **Notifications** : Correction du lien de réservation envoyé par email après une inscription [#808](https://github.com/MTES-MCT/mobilic-api/pull/808).

### Évolutions techniques
- **Sécurité** : Résolution de vulnérabilités critiques identifiées lors d'un audit de sécurité et mise en place d'un scan automatique des secrets (Gitleaks) dans le pipeline de développement [#798](https://github.com/MTES-MCT/mobilic-api/pull/798) [#812](https://github.com/MTES-MCT/mobilic-api/pull/812).
- **Performance** : Optimisation des recherches d'activité des entreprises dans l'interface administrateur et réduction des appels de données superflus [#761](https://github.com/MTES-MCT/mobilic-api/pull/761) [#814](https://github.com/MTES-MCT/mobilic-api/pull/814).
- **Fiabilité du système** : 
    - Optimisation du processus d'auto-validation pour prévenir les erreurs de saturation de mémoire (OOM) via un traitement par lots plus efficace [#831](https://github.com/MTES-MCT/mobilic-api/pull/831).
    - Passage des envois d'emails de synchronisation en tâches asynchrones (Celery) pour éviter de bloquer les requêtes utilisateurs [#805](https://github.com/MTES-MCT/mobilic-api/pull/805).
- **Données et Infrastructure** : Résolution de conflits de migrations de base de données et renforcement de la gestion du stockage des fichiers d'export [#d91aee54](https://github.com/MTES-MCT/mobilic-api/commit/d91aee54) [#850](https://github.com/MTES-MCT/mobilic-api/pull/850).

### Autres changements
- Augmentation significative de la couverture des tests, notamment sur la gestion du changement d'heure (DST), la sécurité des jetons (TOTP) et les nouveaux processus de conformité.
