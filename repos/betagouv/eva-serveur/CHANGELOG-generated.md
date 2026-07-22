## Changelog : eva-serveur (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette mise à jour majeure introduit une nouvelle section dédiée aux évaluations "evaPro" dans l'interface d'administration, offrant une gestion distincte pour ces types d'évaluations. Des corrections de bugs ont également été apportées, notamment concernant l'importation de questions, la modification d'évaluations et la gestion des structures administratives lors de l'inscription.

### Évolutions fonctionnelles
- Ajout d'un menu "Evaluation" avec deux pages distinctes : "eva" et "evaPro" pour les super-administrateurs.
- Création de la page "EvaluationEvapro" pour la gestion des évaluations de type "evaPro".
- Export PDF des évaluations "evaPro".
- Correction du formulaire de modification d'une évaluation [#39044c4](https://github.com/betagouv/eva-serveur/commit/39044c4).
- Lors de l'inscription, les utilisateurs ne sont plus invités à rejoindre des structures administratives [#b123c23](https://github.com/betagouv/eva-serveur/commit/b123c23).
- Correction de l'affichage de la durée estimée d'une évaluation "evaPro" [#bf30d45](https://github.com/betagouv/eva-serveur/commit/bf30d45).

### Évolutions techniques
- Création des modèles `EvaluationEva` et `EvaluationEvapro` pour distinguer les types d'évaluations [#3bbc730](https://github.com/betagouv/eva-serveur/commit/3bbc730).
- Refactoring du code lié aux évaluations "evaPro" : déplacement de partials et de traductions.
- Ajout d'une inflexion pour le modèle `EvaluationEvapro` pour une meilleure gestion des routes.
- Suppression de méthodes et partials inutilisés.
- Correction suite à la mise à jour de `view-component`.

### Autres changements
- Correction d'un crash lors de l'importation de questions avec trop d'erreurs [#b18d7a8](https://github.com/betagouv/eva-serveur/commit/b18d7a8).
- Permet d'importer des questions avec des `nom_technique` de choix existant sur d'autres questions [#5aeb734](https://github.com/betagouv/eva-serveur/commit/5aeb734).
- Correction d'une redirection après suppression ou erreur lors de la génération d'un PDF [#d682da6](https://github.com/betagouv/eva-serveur/commit/d682da6).
- Suppression d'un warning concernant un nom de vue sans extension `.html.erb` [#0a3563e](https://github.com/betagouv/eva-serveur/commit/0a3563e).
