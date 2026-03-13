## Changelog : facili-tacct (30 derniers jours)

### Résumé
Les dernières mises à jour de facili-tacct se concentrent sur l'amélioration de l'exportation des données, notamment pour les superficies irriguées et les indicateurs, ainsi que sur la correction de bugs liés à l'affichage et à la génération des données. Des améliorations ont également été apportées à l'interface utilisateur, en particulier concernant le patch4 et les articles, avec des ajustements de texte et de style. Enfin, des mises à jour de l'infrastructure et de la base de données ont été réalisées.

### Évolutions fonctionnelles
- Correction de l'exportation des superficies irriguées [#1054](https://github.com/incubateur-ademe/facili-tacct/issues/1054).
- Amélioration de l'exportation des noms d'indicateurs (Posthog).
- Correction du bouton d'exportation.
- Amélioration de l'affichage des tags avec icônes sur les articles.
- Correction de la redirection vers la page d'accueil.
- Mise à jour du texte et de l'affichage du patch4 (aléas, aggravation modérée).
- Ajout de la possibilité de déclencher une enquête lors de l'exportation.
- Correction de l'affichage des aléas dans un iframe.
- Affichage de tous les aléas pour un niveau d'aggravation modéré.

### Évolutions techniques
- Mise à jour de Node.js.
- Correction de bugs liés à la génération du schéma Prisma et à la sandbox utilisateur.
- Refactoring du code pour utiliser `toSorted` au lieu de `sort`.
- Mise à jour des modèles et régénération de Prisma.
- Correction de bugs liés à la génération de Prisma.
- Mise à jour de la base de données avec de nouvelles tables.
- Suppression de logs de console en production.
- Suppression de code inutile (bandeau informationnel, niveau d'aggravation dans la partie statique).

### Autres changements
- Ajout d'une notice sur la page d'accueil.
- Désactivation des cookies.
- Mise à jour du texte de la page d'accueil.
- Amélioration de l'affichage de la modale des collections.
- Mise à jour des secrets pour les statistiques (types de cultures, surfaces agricoles).
- Mise à jour du titre des articles.
