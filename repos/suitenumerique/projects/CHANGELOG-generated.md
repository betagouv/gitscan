## Changelog : projects (30 derniers jours)

### Résumé
Ce mois-ci, l'outil de gestion de projet a bénéficié d'améliorations significatives en termes de fonctionnalités et de sécurité. Les utilisateurs profiteront d'une meilleure expérience avec l'ajout d'indicateurs de nombre d'éléments dans les listes, l'assignation automatique de membres et de labels lors de la création de cartes, et une gestion améliorée des activités sur les cartes. Des corrections de bugs et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un badge indiquant le nombre d'éléments dans l'en-tête de chaque liste (#58)
- Lors de la création d'une carte, les membres et les labels filtrés sont automatiquement assignés (#57)
- Affichage par défaut de toutes les activités sur une carte, avec la possibilité de les masquer (#56)
- Amélioration de l'affichage des tableaux partagés dans le menu latéral (#59)
- Correction d'un bug empêchant l'affichage correct des utilisateurs promus (#60)
- Suppression de la fenêtre contextuelle d'ajout de pièces jointes.

### Évolutions techniques
- Mise à jour de la librairie UI Kit (v2) (#54)
- Suppression de l'outil pnpm au profit de npm pour simplifier la gestion des dépendances et éviter les confusions.
- Correction de problèmes liés aux versions de Node.js dans les différents environnements.
- Correction d'une vulnérabilité XSS dans la librairie `react-photoswipe-gallery` (#53)
- Suppression du script de sauvegarde PostgreSQL Scalingo.
- Amélioration de la performance de la recherche d'utilisateurs en ne récupérant plus tous les utilisateurs au démarrage.
- Masquage des adresses e-mail des utilisateurs lors de l'accès à un tableau public sans être connecté (#53)

### Autres changements
- Mise à jour de la version de publication à 1.2.0 (#1a2f13f)
- Mise à jour de la version de publication à 1.1.0 (#686cb54)
- Correction de la configuration ESLint.
- Ajout de correctifs pour les dépendances via `patch-package` dans l'environnement de développement.
