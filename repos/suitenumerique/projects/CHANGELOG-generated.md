## Changelog : projects (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des tableaux de bord, notamment l'exportation des données, la duplication de tableaux et la correction de plusieurs bugs liés à l'interface utilisateur et au comportement de l'application. Des améliorations ont également été apportées aux notifications et à l'affichage des activités.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données des tableaux de bord au format CSV.
- Les filtres appliqués sont maintenant inclus dans l'URL, permettant de les partager et de les conserver.
- Après la duplication d'un tableau, la nouvelle carte s'ouvre automatiquement.
- Amélioration de l'interface utilisateur des actions sur les tableaux de bord pour une meilleure harmonisation.
- Les notifications ne sont plus automatiquement marquées comme lues lors d'un clic.
- Implémentation d'une API pour les statistiques (endpoint).

### Évolutions techniques
- Correction d'un problème d'affichage des noms de tableaux de bord trop longs.
- Correction de plusieurs bugs liés à la duplication de tableaux de bord, notamment des problèmes de récupération des données et de création de tableaux à partir de modèles.
- Correction d'un bug empêchant la duplication d'utilisateurs dans la modale de partage.
- Correction d'un bug lié à l'ouverture des cartes avec la combinaison de touches Cmd+Enter sur Mac.
- Correction de la couleur de fond des badges de date d'échéance.
- Correction de problèmes d'affichage des activités.

### Autres changements
- Correction d'un bug empêchant l'affichage du sélecteur de projet en mode organisation.
- Correction des droits d'accès en mode organisation [#68](https://github.com/suitenumerique/projects/issues/68).
- Staging de modifications [#69](https://github.com/suitenumerique/projects/pull/69).
