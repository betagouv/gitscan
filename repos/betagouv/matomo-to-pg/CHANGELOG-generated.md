## Changelog : matomo-to-pg (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances et la correction de problèmes liés à la pagination des données, notamment pour la table `idlink_va` et `matomo_log_action`. Ces corrections visent à améliorer la vitesse et la fiabilité de la synchronisation des données de Matomo vers PostgreSQL.

### Évolutions fonctionnelles
- Correction d'un problème de pagination pour la table `idlink_va` : remplacement de `OFFSET` par une pagination basée sur un curseur, améliorant ainsi les performances.  [#10](https://github.com/betagouv/matomo-to-pg/issues/10)
- Correction d'un problème lié à l'utilisation de `lastActionId` pour la table `matomo_log_action`. [#9](https://github.com/betagouv/matomo-to-pg/issues/9)

### Évolutions techniques
- Correction dans les workflows GitHub pour ignorer l'année 2025.

### Autres changements
- Aucune information disponible.
