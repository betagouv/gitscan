## Changelog : st-deploycenter (30 derniers jours, au 24 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des droits et des métriques, ainsi qu'une nouvelle fonctionnalité permettant la création de clés API spécifiques à un service. Des optimisations ont également été apportées à la planification des tâches et à la documentation.

### Évolutions fonctionnelles
- Ajout d'une indication de la raison pour laquelle un utilisateur peut ou non télécharger des fichiers dans l'interface d'administration des droits.
- Possibilité de récupérer les métriques par identifiant de service.
- Ajout d'un rôle administrateur opérateur permettant de passer les métriques.
- Création de nouvelles clés API avec une portée limitée à un service spécifique [#53](https://github.com/suitenumerique/st-deploycenter/issues/53).
- Export des jeux de données Datagouv toutes les 4 heures.

### Évolutions techniques
- Augmentation de la taille du dyno utilisé pour les tâches planifiées afin d'améliorer leur fiabilité.
- Ajout d'une route pour les métriques.

### Autres changements
- Documentation de la commande `make restart` dans le fichier README.
- Ajout de la possibilité pour les opérateurs d'accéder aux métriques et à d'autres fonctionnalités opérationnelles [#52](https://github.com/suitenumerique/st-deploycenter/issues/52).
