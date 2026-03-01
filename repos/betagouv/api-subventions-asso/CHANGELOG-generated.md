## Changelog : api-subventions-asso (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API apportent des améliorations significatives à l'importation des données Chorus, notamment en termes de performance. Des informations plus détaillées sur les consommateurs de l'API sont désormais disponibles, et des corrections de bugs ont été implémentées pour améliorer la gestion des SIREN/RNA et l'analyse des fichiers XLSX. L'interface de dépôt de fichiers a également été légèrement améliorée.

### Évolutions fonctionnelles
- Amélioration de la performance de l'importation des fichiers Chorus [#3809](https://github.com/betagouv/api-subventions-asso/issues/3809).
- Ajout d'informations sur l'administrateur dans les données de suivi (datalog) [#3813](https://github.com/betagouv/api-subventions-asso/issues/3813).
- Correction d'un bug concernant la détection de la plage de données dans les fichiers XLSX [#3801](https://github.com/betagouv/api-subventions-asso/issues/3801).
- Correction d'un bug lié à la gestion des SIREN/RNA multiples avec des valeurs indéfinies [#3797](https://github.com/betagouv/api-subventions-asso/issues/3797).
- Amélioration de la formulation lors du processus de dépôt de fichiers [#3836](https://github.com/betagouv/api-subventions-asso/issues/3836).
- Ajout de statistiques détaillées sur les consommateurs de l'API [#3826](https://github.com/betagouv/api-subventions-asso/issues/3826).

### Évolutions techniques
- Refactorisation du code pour homogénéiser les services "plats" [#3815](https://github.com/betagouv/api-subventions-asso/issues/3815).
- Refactorisation du code avec l'utilisation de patterns Mapper, Port et Adapter [#3828](https://github.com/betagouv/api-subventions-asso/issues/3828).
- Mise à jour de la configuration TypeScript [#3799](https://github.com/betagouv/api-subventions-asso/issues/3799).

### Autres changements
- Publication des versions 0.80.1, 0.80.0 et 0.79.0.
