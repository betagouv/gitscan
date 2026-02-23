## Changelog : matomo-to-pg (30 derniers jours)

### Résumé
Ce projet a connu des améliorations significatives concernant la performance et la pagination des requêtes, notamment pour la table `idlink_va`. Des corrections ont également été apportées pour assurer la compatibilité avec PostgreSQL et améliorer la robustesse du processus de synchronisation.

### Évolutions fonctionnelles
- Correction d'un problème de pagination sur la table `idlink_va` en remplaçant `OFFSET` par une pagination basée sur un curseur, améliorant ainsi les performances pour les grandes tables (#10).
- Amélioration de la synchronisation de la table `matomo_log_action` en utilisant `lastActionId` (#9).
- Correction de la syntaxe des contraintes de clé primaire dans le fichier `pg-init.sql` pour une meilleure compatibilité avec PostgreSQL (#6).

### Évolutions techniques
- Optimisation des performances des actions GitHub Actions (#8).
- Correction d'un problème de release (#5, #7).

### Autres changements
- Skip de la release 2025 (#4).
