## Changelog : projects (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la stabilité et de l'expérience utilisateur, notamment en corrigeant des bugs liés à la duplication de tableaux, à l'ouverture de cartes et à l'affichage des activités. De nouvelles fonctionnalités ont également été ajoutées, comme l'intégration des filtres dans l'URL et la possibilité de ne pas marquer automatiquement les notifications comme lues. Une API pour les statistiques a été implémentée.

### Évolutions fonctionnelles
- Les filtres sont désormais inclus dans l'URL, permettant de les partager et de les retrouver facilement. [#69](https://github.com/suitenumerique/projects/pull/69)
- Après la duplication d'une carte, celle-ci s'ouvre automatiquement.
- Correction d'un bug empêchant l'ouverture des cartes avec la combinaison de touches Cmd+Enter sur Mac.
- Les notifications ne sont plus automatiquement marquées comme lues lorsqu'on clique dessus.
- Amélioration de l'affichage des activités.
- Implémentation d'une API pour les statistiques, accessible via un nouveau point de terminaison. [#67](https://github.com/suitenumerique/projects/issues/67)
- Correction d'un bug qui affichait parfois un sélecteur de projet inutile en mode organisation.
- Correction des droits d'accès en mode organisation. [#68](https://github.com/suitenumerique/projects/issues/68)

### Évolutions techniques
- Corrections liées à la duplication de tableaux (résolution de problèmes de récupération et de création).
- Correction d'un bug empêchant la mise à jour des tableaux.
- Amélioration de la gestion des couleurs des badges de date d'échéance.

### Autres changements
- Staging de modifications. [#69](https://github.com/suitenumerique/projects/pull/69)
- Correction d'un bug empêchant l'ajout de plusieurs utilisateurs dans la modale de partage.
