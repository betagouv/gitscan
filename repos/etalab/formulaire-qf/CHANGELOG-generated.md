## Changelog : formulaire-qf (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la correction d'un bug affectant la sélection des collectivités et sur la maintenance des dépendances du projet. Ces mises à jour assurent la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le bon fonctionnement de la sélection des collectivités. L'identifiant `params[:id]` est maintenant correctement conservé lors de la définition de la collectivité. [#347](https://github.com/etalab/formulaire-qf/pull/347)

### Évolutions techniques
- Mise à jour des dépendances Ruby, incluant `rubocop-rails`, `faraday`, et divers paquets de production et de développement. Ces mises à jour visent à améliorer la sécurité, la performance et la compatibilité du projet.
- Amélioration du linting du code. [#346](https://github.com/etalab/formulaire-qf/pull/346)

### Autres changements
- Mises à jour de dépendances de routine via Dependabot (non listées individuellement).
