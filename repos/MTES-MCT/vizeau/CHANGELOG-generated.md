## Changelog : vizeau (30 derniers jours)

### Résumé
Les dernières mises à jour de Vizeau se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des parcelles et des exploitations. De nouvelles fonctionnalités ont été ajoutées, comme la planification des tâches, la catégorisation des exploitations et la gestion des tags. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et fluidité de l'application.

### Évolutions fonctionnelles
- Ajout de la planification des tâches [#221](https://github.com/MTES-MCT/vizeau/pulls/221).
- Ajout de la gestion des tags d'exploitation [#232](https://github.com/MTES-MCT/vizeau/pulls/232).
- Ajout de la catégorisation des exploitations.
- Possibilité d'ajouter un titre aux notes.
- Amélioration de l'affichage des informations dans le composant LabelInfo et la liste des tags [#234](https://github.com/MTES-MCT/vizeau/pulls/234).
- Affichage des informations de la parcelle dans la barre latérale gauche.
- Ajout de boutons pour l'attribution de parcelles.
- Amélioration de la gestion de la longueur du texte dans les champs de saisie [#248](https://github.com/MTES-MCT/vizeau/pulls/248).
- Amélioration de la gestion du centrage de la carte sur une exploitation [#289](https://github.com/MTES-MCT/vizeau/pulls/289).
- Correction de l'affichage des informations de contact [#283](https://github.com/MTES-MCT/vizeau/pulls/283).
- Correction de l'affichage des couleurs des légendes [#295](https://github.com/MTES-MCT/vizeau/pulls/295), [#296](https://github.com/MTES-MCT/vizeau/pulls/296).
- Correction du titre des entrées de journal sur la page d'accueil [#297](https://github.com/MTES-MCT/vizeau/pulls/297).
- Ajout de la suppression de documents [#287](https://github.com/MTES-MCT/vizeau/pulls/287).
- Ajout de l'upload de documents liés aux entrées de journal.
- Amélioration de la visibilité des actions de la carte.

### Évolutions techniques
- Mise à niveau d'Adonis pour corriger des failles de sécurité.
- Simplification de la requête de lecture d'entrées de journal de la page d'accueil.
- Suppression des données de démo du MVP et de l'exploitation démo.
- Refactoring du code pour une meilleure architecture et documentation.
- Suppression de dépendances inutiles.
- Implémentation de seeders idempotents [#299](https://github.com/MTES-MCT/vizeau/pulls/299).
- Correction de problèmes d'accès utilisateur dans le front-end.
- Correction de bugs et améliorations de la gestion des erreurs.
- Utilisation de `map.once('load')` au lieu de `setTimeout`.
- Ajout de tests unitaires et d'intégration.

### Autres changements
- Corrections de formatage et de style (ESLint).
- Amélioration de la gestion des erreurs et des alertes.
- Mise à jour des dépendances pour réduire les alertes de sécurité [#247](https://github.com/MTES-MCT/vizeau/pulls/247), [#288](https://github.com/MTES-MCT/vizeau/pulls/288), [#257](https://github.com/MTES-MCT/vizeau/pulls/257).
- Correction de problèmes liés à Copilot.
- Amélioration de la documentation.
- Suppression d'icônes inutiles.
- Ajout de composants UI réutilisables (LegendItem, TruncatedText).
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
