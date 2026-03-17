## Changelog : mongodb (30 derniers jours)

### Résumé
Ce changelog résume les modifications apportées à l'infrastructure MongoDB de la Mission Apprentissage au cours du dernier mois. Les principales évolutions concernent une amélioration de la sécurité avec la mise à jour des habilitations, une simplification de l'environnement en supprimant l'environnement de pentest, et une modernisation de la gestion des secrets avec la migration vers SOPS.

### Évolutions fonctionnelles
- Mise à jour des habilitations pour renforcer la sécurité des accès aux bases de données. [#61](https://github.com/mission-apprentissage/mongodb/issues/61)

### Évolutions techniques
- Migration de la gestion des secrets d'Ansible Vault vers SOPS, améliorant ainsi la sécurité et la flexibilité de la gestion des informations sensibles. [#59](https://github.com/mission-apprentissage/mongodb/issues/59)
- Mise à jour du sous-module `mna-shared-bin` pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Suppression de l'environnement de pentest, simplifiant ainsi l'infrastructure et réduisant les coûts de maintenance. [#60](https://github.com/mission-apprentissage/mongodb/issues/60)
