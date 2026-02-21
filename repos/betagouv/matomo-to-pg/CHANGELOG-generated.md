## Changelog : matomo-to-pg (30 derniers jours)

### Résumé
Ce projet a bénéficié d'améliorations significatives de performance et de corrections de bugs pour une synchronisation plus fiable des données de Matomo vers PostgreSQL. Les optimisations apportées visent à gérer plus efficacement les volumes importants de données, notamment pour la table `idlink_va`. Une correction a également été apportée à la syntaxe des contraintes de clé primaire dans le script d'initialisation PostgreSQL.

### Évolutions fonctionnelles
- Correction d'un problème de pagination sur la table `idlink_va` en remplaçant `OFFSET` par une pagination basée sur un curseur, améliorant ainsi les performances. (#10)
- Amélioration de la synchronisation de la table `matomo_log_action` en utilisant `lastActionId`. (#9)
- Correction de la syntaxe des contraintes de clé primaire dans le script `pg-init.sql` pour assurer la cohérence des données dans PostgreSQL. (#6)

### Évolutions techniques
- Amélioration des performances des actions CI/CD. (#8)
- Préparation et publication de nouvelles versions du projet. (#8, #6)
