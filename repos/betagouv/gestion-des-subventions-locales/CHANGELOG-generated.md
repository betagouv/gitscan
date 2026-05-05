## Changelog : gestion-des-subventions-locales (30 derniers jours, au 04 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de l'application, notamment au niveau de l'intégration avec les Démarches Numériques (DN) et de la synchronisation des données. Des améliorations ont également été apportées à l'interface utilisateur, avec l'ajout de filtres et l'amélioration de l'affichage des informations, ainsi que des corrections de bugs.

### Évolutions fonctionnelles
- Ajout de filtres pour le cofinancement, le zonage et la contractualisation sur les pages projet, programmation et simulation. [#642](https://github.com/betagouv/gestion-des-subventions-locales/issues/642)
- Amélioration de l'affichage des cofinancements sur la page de détail d'un projet. [#643](https://github.com/betagouv/gestion-des-subventions-locales/issues/643)
- Affichage de la priorité du dossier si plusieurs ont été déposés par le même demandeur. [#654](https://github.com/betagouv/gestion-des-subventions-locales/issues/654)
- Possibilité de changer le statut en masse des projets sur la page de simulation. [#661](https://github.com/betagouv/gestion-des-subventions-locales/issues/661)
- Ajout d'une action pour déplacer les projets acceptés de 2026 vers l'enveloppe 2025. [#654](https://github.com/betagouv/gestion-des-subventions-locales/issues/654)
- Correction du lien "Annulation" dans la création/modification d'un arrêté/lettre et affichage du statut du projet dans l'onglet notifications. [#655](https://github.com/betagouv/gestion-des-subventions-locales/issues/655)
- Amélioration de la mise en page des arrêtés et lettres. [#659](https://github.com/betagouv/gestion-des-subventions-locales/issues/659)
- Renommage de "Arrêté et lettre signés" en "Lettre et arrêté signés". [#693](https://github.com/betagouv/gestion-des-subventions-locales/issues/693)

### Évolutions techniques
- Implémentation d'un proxy GraphQL pour l'API DS, filtré par les instructeurs autorisés. [#641](https://github.com/betagouv/gestion-des-subventions-locales/issues/641)
- Optimisation des requêtes GraphQL vers DN pour limiter les timeouts. [#691](https://github.com/betagouv/gestion-des-subventions-locales/issues/691)
- Restriction des champs renvoyés par le proxy DN pour améliorer la performance. [#692](https://github.com/betagouv/gestion-des-subventions-locales/issues/692) et [#699](https://github.com/betagouv/gestion-des-subventions-locales/issues/699)
- Amélioration de la gestion des erreurs lors de l'import de dossiers depuis DS. [#652](https://github.com/betagouv/gestion-des-subventions-locales/issues/652)
- Ajout de tests CI avec SQLite pour accélérer les tests. [#596](https://github.com/betagouv/gestion-des-subventions-locales/issues/596)
- Mise en place d'un workflow de déploiement en production via GitHub Actions. [#647](https://github.com/betagouv/gestion-des-subventions-locales/issues/647)
- Ajout d'un déploiement pour l'environnement de démo.
- Amélioration de la configuration CI pour limiter les permissions du token GitHub.
- Utilisation d'une base de données SQLite en mémoire pour les tests CI.
- Ajout d'un heartbeat streamé pour éviter les timeouts Scalingo du proxy DS.
- Correction de l'URL du script HeatmapSessionRecording de Matomo. [#687](https://github.com/betagouv/gestion-des-subventions-locales/issues/687)

### Autres changements
- Ajout d'une FAQ. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Ajout de la librairie django-query-counter pour le profiling des requêtes. [#671](https://github.com/betagouv/gestion-des-subventions-locales/issues/671)
- Documentation ajoutée pour les releases en production.
- Suppression des logs verbeux de fontTools en production. [#684](https://github.com/betagouv/gestion-des-subventions-locales/issues/684)
- Suppression du demandeur en doublon pour ne conserver que le demandeur au niveau du dossier. [#670](https://github.com/betagouv/gestion-des-subventions-locales/issues/670)
- Correction de typos et améliorations de la qualité du code.
- MEP (Mise en Production) du 08/04/2026. [#645](https://github.com/betagouv/gestion-des-subventions-locales/issues/645)
