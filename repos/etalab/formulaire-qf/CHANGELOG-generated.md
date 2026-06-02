## Changelog : formulaire-qf (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les mises à jour de formulaire-qf se sont concentrées sur la correction d'un bug affectant la sélection des collectivités et sur la mise à jour des dépendances du projet pour assurer sa sécurité et sa stabilité.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le bon fonctionnement de la sélection des collectivités dans certains cas [#347](https://github.com/etalab/formulaire-qf/pull/347). Le paramètre `id` est maintenant correctement conservé lors de la définition de la collectivité.

### Évolutions techniques
- Mise à jour des dépendances du projet :
    - Faraday (2.14.1 -> 2.14.2)
    - Rubocop et Rubocop-rails
    - Nokogiri (1.19.2 -> 1.19.3)
    - Net-imap (0.6.3 -> 0.6.4)
    - Diverses mises à jour des dépendances de production et de développement.

### Autres changements
- Amélioration de la qualité du code avec des corrections de linting [#342](https://github.com/etalab/formulaire-qf/pull/342).
