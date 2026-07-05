## Changelog : resorption-bidonvilles (30 derniers jours, au 25 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment au niveau du filtrage et de l'affichage des données, en particulier concernant les actions et les indicateurs scolaires. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des ajustements pour améliorer la qualité des données exportées.

### Évolutions fonctionnelles
- Ajout d'un onglet "Actions de ma structure" pour les opérateurs, permettant de filtrer les actions par organisation. [#2692](https://trello.com/c/wvr2hd4B/2692)
- Amélioration du filtre "Indicateurs" qui affiche désormais correctement les résultats. [#2701](https://trello.com/c/VuiTrNnL/2701)
- Ajout de validations de cohérence pour les indicateurs d'action (mineurs, ménages, santé, emploi, logement). [#2560](https://trello.com/c/fvbTRXQz/2560)
- Possibilité de filtrer les actions par structure côté frontend. [#2692](https://trello.com/c/wvr2hd4B/2692)
- Statistiques séparées pour les actions en cours et terminées. [#2692](https://trello.com/c/wvr2hd4B/2692)
- Correction de l'affichage des badges d'indicateurs, qui ne s'affichent désormais que s'il y a des actions. [#2701](https://trello.com/c/VuiTrNnL/2701)
- Ajout de l'option "Inconnu" au filtre "Type de propriétaire". [#2703](https://trello.com/c/9JS8SJF6/2703)

### Évolutions techniques
- Refactor de l'API pour utiliser des types plus cohérents et améliorer la validation des données. [#2560](https://trello.com/c/fvbTRXQz/2560)
- Amélioration de la performance du filtrage des données. [#2561](https://trello.com/c/sqy3f0kc/2561)
- Utilisation de `structuredClone` au lieu de `cloneDeep` pour améliorer la performance et la compatibilité. [#2560](https://trello.com/c/fvbTRXQz/2560)
- Suppression de code mort et nettoyage général du code. [#2560](https://trello.com/c/fvbTRXQz/2560)
- Correction de plusieurs erreurs relevées par SonarQube. [#2560](https://trello.com/c/fvbTRXQz/2560)
- Mise à jour des dépendances et correction de problèmes de linting.
- Amélioration de la gestion des erreurs et des messages d'erreur.

### Autres changements
- Mise à jour des conditions d'utilisation. [#2712](https://trello.com/c/PXmPMtEe/2712)
- Ajout de tests unitaires pour l'API. [#2706](https://trello.com/c/17BTTncn/2706)
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout d'un bandeau d'alerte pour la canicule.
- Mise à jour du numéro de version à v2.55.0 et v2.54.0.
- Correction de l'affichage de l'item actif dans le menu.
- Correction de la popup.
- Correction des coins vides des boutons de zoom.
- Correction de l'affichage de l'item actif dans le menu.
- Correction de l'affichage de l'item actif dans le menu.
- Correction de l'affichage de l'item actif dans le menu.
