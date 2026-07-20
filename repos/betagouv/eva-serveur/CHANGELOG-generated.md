## Changelog : eva-serveur (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des évaluations, notamment avec la création d'un nouveau menu dédié et la séparation des modèles d'évaluation "eva" et "evapro". Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier lors de l'importation et de la modification des évaluations.

### Évolutions fonctionnelles
- Ajout d'un menu "Evaluation" avec deux pages distinctes pour les évaluations "eva" et "evapro" pour les super-administrateurs.
- Création des pages d'administration pour les évaluations "evapro".
- Export PDF possible pour les évaluations "evapro".
- Correction du formulaire de modification d'une évaluation.
- Correction d'un bug empêchant l'inscription sans proposition de rejoindre des structures administratives.
- Amélioration du message affiché pour la durée estimée d'une évaluation "evapro" [#bf30d45](https://github.com/betagouv/eva-serveur/commit/bf30d45).

### Évolutions techniques
- Séparation des modèles d'évaluation en `EvaluationEva` et `EvaluationEvapro` [#3bbc730](https://github.com/betagouv/eva-serveur/commit/3bbc730).
- Refactorisation des partials et des traductions liés aux évaluations "evapro".
- Ajout d'inflexions pour les modèles `EvaluationEva` et `EvaluationEvapro`.
- Suppression de méthodes et partials inutilisés.
- Correction d'un crash lors de l'importation avec de nombreuses erreurs.
- Permet l'import de questions avec des `nom_technique` de choix existants.

### Autres changements
- Correction de la redirection après suppression ou erreur lors de la génération d'un PDF [#d682da6](https://github.com/betagouv/eva-serveur/commit/d682da6).
- Suppression d'un warning concernant un nom de vue sans extension `.html.erb` [#0a3563e](https://github.com/betagouv/eva-serveur/commit/0a3563e).
- Mise à jour des dépendances view_component et dsfr-view-components.
- Correction suite à la mise à jour de view-component.
