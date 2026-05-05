## Changelog : st-deploycenter (30 derniers jours, au 29 avril 2026)

### Résumé
Ce déploiement apporte des améliorations significatives à la gestion des droits et des métriques, ainsi qu'une nouvelle fonctionnalité permettant la création de clés API spécifiques à un service. Des optimisations de performance ont également été apportées pour l'exportation des jeux de données et le chargement des organisations.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des clés API spécifiques à un service. [#53](https://github.com/suitenumerique/st-deploycenter/issues/53)
- Affichage de la raison pour laquelle un utilisateur n'a pas le droit de télécharger des fichiers (drive resolver).
- Possibilité de récupérer les métriques par identifiant de service.

### Évolutions techniques
- Optimisation des performances lors du chargement des organisations, en évitant de charger toutes les organisations pour les petits lots.
- Augmentation de la taille du dyno utilisé pour la tâche planifiée (cron) afin d'améliorer sa fiabilité.
- Mise en place d'une exportation des jeux de données toutes les 4 heures.

### Autres changements
- Aucun changement significatif à signaler.
