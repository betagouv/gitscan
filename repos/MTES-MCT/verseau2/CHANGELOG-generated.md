## Changelog : verseau2 (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des transferts de fichiers, notamment avec l'ajout d'un support client FTP et des optimisations pour le SFTP des agences de l'eau. Des corrections et des ajustements ont également été effectués sur la configuration des tests et l'infrastructure DevOps.

### Évolutions fonctionnelles
- Ajout d'un client FTP pour la gestion des agences de l'eau, permettant une plus grande flexibilité dans les transferts de fichiers. [#134](https://github.com/MTES-MCT/verseau2/issues/134)
- Amélioration de la journalisation lors de l'envoi de fichiers SFTP pour un meilleur suivi et diagnostic.

### Évolutions techniques
- Refactoring des transferts de fichiers pour supporter SFTP, les agences de l'eau, les agents Verseau et FTP. [#134](https://github.com/MTES-MCT/verseau2/issues/134)
- Mise à jour de `pg-boss` et ajout du tableau de bord `pg-boss` pour une meilleure gestion des tâches asynchrones.
- Les tests non applicables sont maintenant ignorés, améliorant la robustesse et la clarté des tests. [#135](https://github.com/MTES-MCT/verseau2/issues/135)
- Amélioration de la gestion des tables exclues dans la fonction `parseExcludedTables`. [#136](https://github.com/MTES-MCT/verseau2/issues/136)

### Autres changements
- Mise à jour de la documentation des commandes et correction de la description des tests.
- Correction de la configuration des tests.
- Annulation temporaire de la désactivation de la synchronisation de la base de données. [#137](https://github.com/MTES-MCT/verseau2/issues/137)
- Annulation d'une modification temporaire pour les tests SFTP des agences de l'eau.
