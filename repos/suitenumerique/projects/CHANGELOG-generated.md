## Changelog : projects (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives en termes de performance, notamment lors de la manipulation de listes de cartes importantes. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant les filtres, l'édition de contenu et la gestion des erreurs. De plus, des améliorations de l'interface utilisateur et de la documentation ont été apportées.

### Évolutions fonctionnelles
- Ajout d'un modèle d'email personnalisé pour les notifications, améliorant ainsi l'expérience utilisateur lors de la réception d'alertes. [#62](https://github.com/suitenumerique/projects/issues/62) et [#64](https://github.com/suitenumerique/projects/issues/64)
- Ajout d'un tooltip pour le bouton "copier le lien" afin de faciliter son utilisation.
- Correction d'un bug qui empêchait l'affichage correct du markdown dans les commentaires.
- Correction d'un bug qui empêchait l'application des modifications lors de l'utilisation de l'éditeur MDX.
- Correction d'un bug qui empêchait l'affichage correct des paragraphes dans l'éditeur markdown.
- Correction d'un bug dans les filtres où la sélection multiple et la désélection provoquaient une erreur.
- Correction d'un bug aléatoire lors de la création de cartes.
- Correction d'un bug qui cachait la bannière de notification sous le contenu de la page.

### Évolutions techniques
- Optimisations de performance importantes concernant le drag-and-drop et le rendu des cartes, notamment en utilisant la mémoïsation et des composants intermédiaires pour éviter les rendus inutiles.
- Migration vers la dernière version de la librairie drag-drop pour tenter de résoudre les problèmes de performance.
- Suppression des hooks lint qui ralentissaient les opérations Git et npm, la CI/CD assurant désormais la qualité du code.
- Possibilité de désactiver l'indexation des moteurs de recherche pour les environnements non-production.
- Amélioration de la structure du code pour une meilleure performance lors du déplacement de cartes dans de longues listes.

### Autres changements
- Correction de quelques erreurs d'utilisation de linter.
- Mise à jour de la documentation.
