## Changelog : mna-shared-bin (30 derniers jours)

### Résumé
Ce dépôt a connu des améliorations significatives concernant les scripts de sauvegarde et de restauration de base de données, ainsi qu'une refactorisation générale du code pour une meilleure maintenabilité et une mutualisation des fonctionnalités. Ces changements visent à faciliter l'administration et la gestion de l'infrastructure.

### Évolutions fonctionnelles
- Correction de la mise à jour des scripts de sauvegarde et de restauration de la base de données. [#1](https://github.com/mission-apprentissage/mna-shared-bin/issues/1)
- Mutualisation de la sous-commande `_help` pour une meilleure cohérence et réutilisation du code.

### Évolutions techniques
- Refactorisation des commandes `seed:apply` et `seed:update` pour améliorer leur structure et leur lisibilité.
- Correction de la commande `git submodule update` pour supprimer l'option `--recursive` non nécessaire.
- Refactorisation générale du code pour une meilleure organisation et maintenabilité.

### Autres changements
- Correction d'une faute de frappe.
- Initialisation du dépôt.
