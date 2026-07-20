## Changelog : sfor (30 derniers jours, au 07 juillet 2026)

### Résumé
Les dernières mises à jour de sfor se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des alertes et des listes d'entreprises. Des optimisations ont été apportées à la performance et à la robustesse de l'application, ainsi qu'à la gestion des erreurs. De nouvelles fonctionnalités comme le suivi des départements d'entreprises et la gestion de la précision des alertes ont été ajoutées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des listes d'entreprises avec ajout du suivi du département [#60261bd](https://github.com/signaux-faibles/sfor/commit/60261bd).
- Ajout de la gestion de la précision des alertes dans l'interface d'administration [#210f131](https://github.com/signaux-faibles/sfor/commit/210f131).
- Modification de la logique d'affichage des widgets de détection pour les alertes de type "Plans" [#7f8c7d5](https://github.com/signaux-faibles/sfor/commit/7f8c7d5).
- Amélioration de l'export Excel des trackings [#9254a1b](https://github.com/signaux-faibles/sfor/commit/9254a1b).
- Ajout d'un composant d'indicateur de chargement (ellipsis) et mise à jour de l'affichage des listes [#90eeaac](https://github.com/signaux-faibles/sfor/commit/90eeaac).
- Notifications par email lors de modifications des trackings [#c12c20d](https://github.com/signaux-faibles/sfor/commit/c12c20d).
- Amélioration de la clarté de la sortie de la méthode `format_sjcf` [#340fb3d](https://github.com/signaux-faibles/sfor/commit/340fb3d).

### Évolutions techniques
- Amélioration de la gestion des erreurs et de la journalisation dans `BaseApiService` [#ec74bb3](https://github.com/signaux-faibles/sfor/commit/ec74bb3).
- Ajout d'une tâche de dénormalisation pour optimiser les performances [#5ace871](https://github.com/signaux-faibles/sfor/commit/5ace871).
- Amélioration de la gestion des erreurs et des timeouts pour le widget INSEE [#de27744](https://github.com/signaux-faibles/sfor/commit/de27744).
- Refactorisation de la vue de détail des alertes pour utiliser des badges [#365c21b](https://github.com/signaux-faibles/sfor/commit/365c21b).
- Suppression d'un lien FCE obsolète [#86fe848](https://github.com/signaux-faibles/sfor/commit/86fe848).
- Suppression temporaire de l'algorithme de Shapley pour le graphique en cascade en production [#9e46121](https://github.com/signaux-faibles/sfor/commit/9e46121).
- Ajout de l'algorithme de contribution de Shapley pour le graphique en cascade [#09f8b98](https://github.com/signaux-faibles/sfor/commit/09f8b98).

### Autres changements
- Mise à jour du fichier README avec les durées estimées révisées pour les tâches Rake [#187e059](https://github.com/signaux-faibles/sfor/commit/187e059).
- Corrections mineures de linting [#87b82f7](https://github.com/signaux-faibles/sfor/commit/87b82f7).
