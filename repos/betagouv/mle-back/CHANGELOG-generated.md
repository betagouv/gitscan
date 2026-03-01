## Changelog : mle-back (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la recherche de logements, avec l'ajout de nouveaux critères comme le prix minimum et maximum, ainsi que l'intégration de nouvelles sources de données (SAIEM Dragouignan, Cardinal Campus, Logis Métropole, ACM Habitat, Groupe 3F Centre Val de Loire). Des fonctionnalités de notification ont été implémentées pour informer les utilisateurs des changements pertinents. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de critères de prix minimum et maximum dans la recherche de logements. [#38b7682](https://github.com/betagouv/mle-back/commit/38b7682)
- Intégration de nouvelles sources de logements : SAIEM Dragouignan, Cardinal Campus, Logis Métropole, ACM Habitat, Groupe 3F Centre Val de Loire. [#35dc494](https://github.com/betagouv/mle-back/commit/35dc494), [#fbef5a3](https://github.com/betagouv/mle-back/commit/fbef5a3), [#ddc94fc](https://github.com/betagouv/mle-back/commit/ddc94fc), [#0d23ae2](https://github.com/betagouv/mle-back/commit/0d23ae2), [#9eacf0e](https://github.com/betagouv/mle-back/commit/9eacf0e)
- Implémentation d'un système de notifications pour informer les utilisateurs des changements (en production et en staging). [#5409543](https://github.com/betagouv/mle-back/commit/5409543), [#16a050b](https://github.com/betagouv/mle-back/commit/16a050b), [#c634b1b](https://github.com/betagouv/mle-back/commit/c634b1b)
- Ajout de la possibilité de rafraîchir les données des étudiants. [#1523685](https://github.com/betagouv/mle-back/commit/1523685)
- Ajout du champ "wifi" aux logements. [#778eb69](https://github.com/betagouv/mle-back/commit/778eb69)
- Amélioration du classement des logements dans les résultats de recherche. [#c0949ff](https://github.com/betagouv/mle-back/commit/c0949ff)
- Possibilité d'exporter les logements au format Excel avec des informations complètes (disponibilité, prix, etc.). [#a806af1](https://github.com/betagouv/mle-back/commit/a806af1), [#d86b071](https://github.com/betagouv/mle-back/commit/d86b071), [#cdd8e14](https://github.com/betagouv/mle-back/commit/cdd8e14)

### Évolutions techniques
- Intégration de Matomo pour le suivi des événements et l'analyse des données. [#3e99f65](https://github.com/betagouv/mle-back/commit/3e99f65)
- Amélioration de la recherche avec l'utilisation de FTS (Full Text Search) et un fallback vers trigram. [#0d6bff9](https://github.com/betagouv/mle-back/commit/0d6bff9)
- Mise à jour des dépendances : Ruff (0.14.11 -> 0.14.13 -> 0.14.14 -> 0.15.0), Sentry SDK (2.49.0 -> 2.50.0 -> 2.51.0 -> 2.52.0), djangorestframework-stubs (3.16.6 -> 3.16.7).
- Refactorisation du code pour améliorer la gestion des images et des URLs. [#ea50a3e](https://github.com/betagouv/mle-back/commit/ea50a3e), [#e6c0926](https://github.com/betagouv/mle-back/commit/e6c0926)
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des variables d'environnement. [#a32c2e9](https://github.com/betagouv/mle-back/commit/a32c2e9), [#b2e3b03](https://github.com/betagouv/mle-back/commit/b2e3b03)

### Autres changements
- Réduction de la durée de vie du token d'accès à 5 minutes. [#2535e68](https://github.com/betagouv/mle-back/commit/2535e68)
- Préparation de la branche `develop` pour la fusion avec `main`. [#bdd2758](https://github.com/betagouv/mle-back/commit/bdd2758)
- Ajout d'une commande pour importer les prix du CROUS. [#d37f968](https://github.com/betagouv/mle-back/commit/d37f968)
