## Changelog : facili-tacct (30 derniers jours)

### Résumé
Les dernières mises à jour de Facili-tacct se concentrent sur l'amélioration de la fonctionnalité d'export de données, notamment pour les surfaces irriguées et les indicateurs, ainsi que sur des corrections de bugs liés à la génération de Prisma et à l'affichage des aléas. Des améliorations de l'interface utilisateur ont également été apportées, notamment concernant le patch 4 et la page d'accueil.

### Évolutions fonctionnelles
- Correction du bouton d'export [#1234](https://github.com/incubateur-ademe/facili-tacct/issues/1234)
- Correction de l'export des superficies irriguées.
- Correction de l'export des noms d'indicateurs pour PostHog.
- Amélioration de l'affichage des aléas dans le patch 4.
- Ajout de nouveaux textes et ajustements de l'affichage dans le patch 4.
- Correction de l'affichage des aléas dans une iframe.
- Affichage de tous les aléas pour un niveau d'aggravation modéré.
- Suppression du niveau d'aggravation dans la partie statique du patch 4.

### Évolutions techniques
- Mise à jour de la version de Node.js.
- Correction d'un bug de génération de Prisma lié à la sandbox users et à la génération générale [#1147](https://github.com/incubateur-ademe/facili-tacct/issues/1147).
- Refactoring du code pour utiliser `toSorted` pour le tri.
- Correction de problèmes liés à la génération de modèles Prisma.
- Suppression de `console.log` dans le code de déploiement.
- Correction de l'utilisation des secrets pour les statistiques des types de cultures.
- Suppression de l'affichage de cookies.
- Suppression du bandeau informationnel de la page d'accueil.

### Autres changements
- Préparation de la recette pour les collections.
- Mise à jour du budget.
- Suppression de la notice de la page d'accueil.
- Mise à jour du titre des articles.
- Intégration des corrections liées au débroussaillement (menu latéral, maptiles).
