## Changelog : projects (30 derniers jours, au 2026-05-24)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des tableaux de bord, notamment l'exportation des données, la duplication de tableaux et la correction de plusieurs bugs affectant l'interface utilisateur et le comportement de l'application. L'expérience utilisateur a été améliorée grâce à des corrections de bugs et des ajustements d'interface.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données des tableaux de bord au format CSV. [#69](https://github.com/suitenumerique/projects/pull/69)
- Les filtres appliqués sont désormais inclus dans l'URL, permettant de les partager et de les conserver.
- Après la duplication d'une carte, celle-ci s'ouvre automatiquement.
- Amélioration de l'interface utilisateur des actions sur les tableaux de bord pour une meilleure harmonisation.

### Évolutions techniques
- Correction d'un problème empêchant la récupération correcte des tableaux de bord lors de la duplication.
- Correction d'un problème lié à l'ID du projet cible lors de la duplication de modèles de tableaux de bord.
- Correction de la création de tableaux de bord à partir de modèles.
- Correction de la mise à jour des tableaux de bord.
- Les notifications ne sont plus automatiquement marquées comme lues lors d'un clic.
- Correction de problèmes d'affichage des activités.

### Autres changements
- Correction d'un problème d'affichage si le nom d'un tableau de bord est trop long.
- Correction d'un bug empêchant l'ajout de plusieurs utilisateurs dans la modale de partage.
- Correction d'un bug lié à l'ouverture des cartes avec Cmd+Enter sur Mac.
- Correction de la couleur de fond des badges de date d'échéance.
