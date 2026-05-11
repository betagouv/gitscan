## Changelog : projects (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des tableaux de bord, notamment en ajoutant la possibilité d'exporter les données au format CSV, en améliorant la duplication des tableaux et en corrigeant plusieurs bugs liés à l'interface utilisateur et au comportement des cartes. Des améliorations ont également été apportées aux notifications et aux statistiques.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données d'un tableau de bord au format CSV.
- Les filtres appliqués à un tableau de bord sont désormais inclus dans l'URL, permettant de les partager facilement.
- Après la duplication d'une carte, celle-ci s'ouvre automatiquement.
- Amélioration de l'interface utilisateur des actions sur les tableaux de bord pour une meilleure harmonisation.
- Les notifications ne sont plus automatiquement marquées comme lues lorsqu'on clique dessus.
- Une API pour les statistiques a été implémentée [#67](https://github.com/suitenumerique/projects/issues/67).

### Évolutions techniques
- Correction d'un problème d'affichage des activités.
- Correction de plusieurs bugs liés à la duplication des tableaux de bord, notamment des problèmes de récupération et de création de modèles.
- Correction d'un bug empêchant la mise à jour des tableaux de bord.
- Correction d'un bug lié à l'ajout de doublons d'utilisateurs dans la fenêtre de partage.
- Correction d'un bug lié à l'ouverture des cartes avec la combinaison de touches Cmd+Enter sur Mac.
- Correction de la couleur de fond des badges de date d'échéance.
- Correction d'un problème d'affichage des noms de tableaux de bord trop longs.
- Correction des droits d'accès dans les organisations [#68](https://github.com/suitenumerique/projects/issues/68).
- Intégration de la phase de staging [#69](https://github.com/suitenumerique/projects/issues/69).

### Autres changements
- Le sélecteur de projet n'est plus affiché en mode organisation.
- Amélioration de la documentation et du code.
