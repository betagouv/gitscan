## Changelog : st-deploycenter (30 derniers jours, au 18 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives pour le suivi et la gestion des services, notamment avec l'ajout de clés API spécifiques à chaque service et la possibilité de récupérer des métriques par identifiant de service. Des ajustements ont également été effectués pour améliorer la fiabilité des tâches planifiées.

### Évolutions fonctionnelles
- Ajout de la possibilité de récupérer des métriques par identifiant de service. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)
- Introduction de nouvelles clés API spécifiques à chaque service, offrant un contrôle d'accès plus granulaire. [#53](https://github.com/suitenumerique/st-deploycenter/issues/53)
- Ajout d'un rôle administrateur opérateur permettant de passer les droits d'administration. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)

### Évolutions techniques
- Augmentation de la taille du dyno utilisé pour les tâches planifiées afin d'améliorer leur stabilité. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)

### Autres changements
- Documentation de la commande `make restart` dans le fichier README. [#52](https://github.com/suitenumerique/st-deploycenter/issues/52)
