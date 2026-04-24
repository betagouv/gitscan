## Changelog : st-deploycenter (30 derniers jours, au 23 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives pour le suivi et l'administration des services, notamment l'export régulier des jeux de données vers datagouv, la possibilité de récupérer des métriques par ID de service, et l'introduction de clés API spécifiques à chaque service. Des optimisations ont également été apportées pour garantir la fiabilité des tâches planifiées.

### Évolutions fonctionnelles
- Ajout de la possibilité de récupérer des métriques par ID de service. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)
- Introduction de nouvelles clés API avec une portée spécifique à chaque service. [#53](https://github.com/suitenumerique/st-deploycenter/issues/53)
- Export régulier des jeux de données vers datagouv toutes les 4 heures.
- Ajout d'un rôle administrateur opérateur avec accès complet, ainsi qu'une route pour les métriques et des fonctionnalités opérationnelles potentielles. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)

### Évolutions techniques
- Augmentation de la taille du dyno utilisé pour les tâches planifiées afin d'améliorer leur fiabilité.
- Amélioration de la documentation du Makefile pour inclure la commande `restart`.

### Autres changements
- Aucune information supplémentaire.
