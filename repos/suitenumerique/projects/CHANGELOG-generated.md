## Changelog : projects (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des performances de l'application, en particulier lors de la manipulation de listes de cartes importantes. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant les filtres, l'édition de contenu et la gestion des utilisateurs. Enfin, des améliorations ont été apportées à l'interface utilisateur et aux notifications.

### Évolutions fonctionnelles
- Ajout d'un badge de nombre sur les en-têtes de liste pour indiquer le nombre de cartes. (#58)
- Les membres et les étiquettes filtrés sont maintenant automatiquement attribués aux cartes créées. (#57)
- Les activités des cartes sont maintenant affichées par défaut et peuvent être masquées. (#56)
- Ajout d'un bouton "Copier le lien" avec un tooltip pour faciliter le partage des tâches.
- Les commentaires sont maintenant rendus en Markdown, améliorant la lisibilité et le formatage.
- Ajout de modèles d'emails personnalisés pour les notifications. (#62, #64)
- Correction d'un bug empêchant la sélection multiple de filtres. (#62)
- Correction d'un bug empêchant l'application des modifications lors de l'édition de contenu MDX.
- Correction d'un bug aléatoire lors de la création de cartes.
- Correction d'un bug d'affichage des tableaux partagés dans le menu latéral. (#59)

### Évolutions techniques
- Optimisation des performances lors du déplacement de cartes dans les tableaux Kanban, notamment en utilisant la mémoïsation et en évitant les rendus inutiles.
- Migration vers la dernière version de la librairie de drag-and-drop pour tenter de résoudre les problèmes de performance.
- Suppression de la logique de chargement initial de tous les utilisateurs pour améliorer les performances et la confidentialité.
- Masquage des adresses email des utilisateurs lors de l'accès à un tableau public sans être connecté.
- Mise à jour de la librairie UI Kit (v2). (#54)
- Suppression du popup d'attachement.
- Suppression des hooks lint ralentissant les opérations Git et npm.

### Autres changements
- Ajout d'une option pour désactiver l'indexation des moteurs de recherche pour les environnements non de production.
- Correction de l'affichage des paragraphes dans l'éditeur Markdown.
- Correction d'erreurs d'utilisation incorrecte de l'outil de linting.
- Bump de la version de release à 1.2.0. (#60)
- Bump de la version de release à 1.1.0.
