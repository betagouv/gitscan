## Changelog : projects (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des tableaux de bord, notamment l'exportation des données, la duplication de tableaux et la gestion des filtres. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'affichage et l'interaction avec les éléments de l'interface. Enfin, une API pour les statistiques a été implémentée.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données des tableaux de bord au format CSV.
- Les filtres appliqués sont maintenant inclus dans l'URL, permettant de les partager et de les conserver.
- Après la duplication d'un tableau de bord, la nouvelle carte s'ouvre automatiquement.
- Amélioration de l'interface utilisateur des actions sur les tableaux de bord pour une meilleure harmonisation.
- Les notifications ne sont plus automatiquement marquées comme lues lors d'un clic.
- Implémentation d'une API pour les statistiques, accessible via un nouveau endpoint. [#67](https://github.com/suitenumerique/projects/issues/67)

### Évolutions techniques
- Correction de problèmes liés à la récupération des tableaux de bord lors de la duplication.
- Correction de problèmes lors de la création de tableaux de bord à partir de modèles.
- Correction de bugs liés à la mise à jour des tableaux de bord.
- Correction de problèmes d'affichage des activités.
- Correction de bugs concernant les droits d'accès dans les organisations. [#68](https://github.com/suitenumerique/projects/issues/68)
- Correction de problèmes d'affichage des couleurs des dates d'échéance.
- Correction d'un bug empêchant l'ouverture des cartes avec Cmd+Enter sur Mac.
- Correction d'un bug qui pouvait entraîner la duplication d'utilisateurs dans la modale de partage.
- Correction d'un problème d'affichage si le nom d'un tableau de bord est trop long.

### Autres changements
- Mise en place d'une étape de staging dans le processus de déploiement. [#69](https://github.com/suitenumerique/projects/issues/69)
- Le sélecteur de projet n'est plus affiché en mode organisation.
