## Changelog : facili-tacct (30 derniers jours)

### Résumé
Les dernières mises à jour de facili-tacct se concentrent sur l'amélioration de la fonctionnalité "patch 4" avec des ajustements d'affichage, de données et de textes. Des corrections ont également été apportées concernant l'exportation de données et l'affichage des aléas. Des optimisations et des corrections mineures ont été réalisées sur l'interface utilisateur et la gestion des données.

### Évolutions fonctionnelles
- Amélioration de l'affichage et du fonctionnement de la fonctionnalité "patch 4" concernant les aléas et les niveaux d'aggravation.
- Correction de l'affichage des aléas dans une iframe [#1054](https://github.com/incubateur-ademe/facili-tacct/issues/1054).
- Correction de l'affichage de tous les aléas pour un niveau d'aggravation modéré.
- Amélioration de l'exportation des surfaces agricoles (données secrètes).
- Ajout d'une notice sur la page d'accueil.
- Mise à jour des titres d'articles.

### Évolutions techniques
- Mise à jour de la configuration de Prisma pour la génération des modèles.
- Refactoring du code pour utiliser `toSorted` au lieu de `sort`.
- Suppression de logs console inutiles.
- Suppression de la condition d'affichage pour l'intensité modérée dans "patch 4".
- Suppression du niveau d'aggravation dans la partie statique de l'interface.
- Activation/désactivation des cookies.
- Tests de régénération.

### Autres changements
- Mise à jour du budget.
- Intégration des tuiles de carte pour le débroussaillement.
- Mise à jour du menu latéral pour le débroussaillement.
- Mise à jour des textes de la fonctionnalité "patch 4".
- Préparation de la prochaine étape (MEP 16/02/2026).
- Corrections mineures de style et d'affichage dans "patch 4".
