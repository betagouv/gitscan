## Changelog : projects (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur la performance et la correction de bugs, notamment au niveau de l'interface utilisateur et de l'édition de contenu. Des améliorations ont également été apportées aux notifications et à la gestion des filtres.

### Évolutions fonctionnelles
- Ajout d'un modèle d'email personnalisé pour les notifications. [#62](https://github.com/suitenumerique/projects/issues/62) et [#64](https://github.com/suitenumerique/projects/issues/64)
- Ajout d'un tooltip pour le bouton "copier le lien" d'une tâche.
- Correction d'un bug empêchant la sélection multiple d'éléments dans les filtres.
- Correction d'un bug où le contenu markdown des commentaires n'était pas rendu correctement.
- Correction d'un bug qui faisait que l'éditeur MDX sortait du mode édition sans appliquer les modifications.
- Correction d'un bug aléatoire lors de la création de cartes.
- Correction d'un bug où un banner était masqué par le contenu de la page.

### Évolutions techniques
- Optimisations significatives des performances du drag-and-drop, notamment en évitant les rendus inutiles et en utilisant la mémoïsation.
- Amélioration de l'indexation pour empêcher l'indexation par les moteurs de recherche en environnement non-production.
- Suppression des hooks lint ralentissant les opérations Git et npm, la CI/CD assurant la qualité du code.
- Correction d'erreurs d'utilisation incorrecte de l'outil de linting.

### Autres changements
- Amélioration de la séparation des paragraphes dans l'éditeur de contenu markdown.
- Mise à jour de la librairie de drag-and-drop vers la dernière version pour tenter de résoudre les problèmes de performance.
