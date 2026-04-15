## Changelog : st-deploycenter (30 derniers jours, au 8 avril 2026)

### Résumé
Cette version apporte des améliorations à l'export des services vers DataGouv, des corrections d'affichage et de gestion des descriptions, ainsi qu'une amélioration de la gestion des tâches planifiées. De plus, un rôle administrateur opérateur est ajouté avec des routes de métriques pour les opérations.

### Évolutions fonctionnelles
- Correction de l'affichage des cartes : la description n'est affichée que si elle contient du contenu.
- Amélioration de l'export des services vers DataGouv : les services sont exportés par ordre de priorité décroissante.
- Ajout du champ `description` pour les services dans l'export DataGouv.
- Ajout d'un rôle administrateur opérateur avec accès aux métriques opérationnelles [#52](https://github.com/suitenumerique/st-deploycenter/issues/52).

### Évolutions techniques
- Utilisation d'un dyno plus important pour la tâche planifiée afin d'améliorer sa fiabilité.
- Restauration de la prise en charge des listes séparées par des virgules pour les webhooks.
- Petites améliorations apportées aux modèles et à l'interface d'administration.

### Autres changements
- Documentation de la commande `make restart` dans le fichier README.
