## Changelog : formulaire-qf (30 derniers jours, au 08 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la correction d'un bug affectant la sélection des collectivités et sur la maintenance générale du projet, incluant la mise à jour des dépendances pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le bon fonctionnement de la sélection des collectivités dans certains cas. Le paramètre `id` est maintenant correctement conservé lors de l'appel à `set_collectivity` [#347](https://github.com/etalab/formulaire-qf/pull/347).

### Évolutions techniques
- Mise à jour de plusieurs dépendances Ruby, notamment `rubocop-rails` (de 2.35.1 à 2.35.4), `faraday` (à 2.14.2) et divers paquets du groupe `production-dependencies` et `development-dependencies` pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la qualité du code via des corrections de linting [#346](https://github.com/etalab/formulaire-qf/pull/346).

### Autres changements
- Aucune information significative à signaler.
