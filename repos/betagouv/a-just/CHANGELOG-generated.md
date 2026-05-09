## Changelog : a-just (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la fiabilité des tests end-to-end (E2E), ainsi que sur la sécurisation de l'application. Des corrections ont été apportées pour stabiliser l'environnement de test et améliorer la gestion des variables d'environnement. Des ajustements de sécurité ont également été implémentés pour valider les URLs des iframes.

### Évolutions fonctionnelles
- Correction d'un test API qui échouait lors de la modification des données utilisateur. [#b80f8db9](https://github.com/betagouv/a-just/commit/b80f8db9)
- Amélioration de la sécurité : validation des URLs des iframes pour prévenir les attaques potentielles via des scripts malveillants. [#f25f8cc1](https://github.com/betagouv/a-just/commit/f25f8cc1)

### Évolutions techniques
- **Tests E2E :** Refonte de la gestion des variables d'environnement dans les tests Cypress, passant de `cy.env()` à `Cypress.expose()` pour une meilleure fiabilité. Plusieurs commits concernent ces améliorations : [#575a8c35](https://github.com/betagouv/a-just/commit/575a8c35), [#8f25df81](https://github.com/betagouv/a-just/commit/8f25df81), [#4b2e857b](https://github.com/betagouv/a-just/commit/4b2e857b)
- **Tests E2E :** Mise à jour de la configuration de `tsconfig.json` pour les tests E2E afin de corriger des erreurs et améliorer la compatibilité. Plusieurs commits concernent ces améliorations : [#7d27a047](https://github.com/betagouv/a-just/commit/7d27a047), [#4b6de590](https://github.com/betagouv/a-just/commit/4b6de590), [#8869bca3](https://github.com/betagouv/a-just/commit/8869bca3)
- **Docker :** Corrections et améliorations du Dockerfile pour l'environnement E2E, incluant la suppression de commentaires et la correction de la configuration. [#b5613a15](https://github.com/betagouv/a-just/commit/b5613a15), [#2bb0a43d](https://github.com/betagouv/a-just/commit/2bb0a43d)
- **Koa-smart :** Suppression de dépendances inutiles (babel-cli, esdoc, vendor smart) et ajustements de configuration pour alléger et sécuriser le composant. [#0d8b63da](https://github.com/betagouv/a-just/commit/0d8b63da), [#cf663c7c](https://github.com/betagouv/a-just/commit/cf663c7c), [#db2a99e5](https://github.com/betagouv/a-just/commit/db2a99e5), [#59f7daa5](https://github.com/betagouv/a-just/commit/59f7daa5), [#b926f2f2](https://github.com/betagouv/a-just/commit/b926f2f2)

### Autres changements
- Suppression de code dupliqué. [#ac89de7d](https://github.com/betagouv/a-just/commit/ac89de7d)
- Mise à jour de la version d'axios. [#db2a99e5](https://github.com/betagouv/a-just/commit/db2a99e5)
- Amélioration de la gestion des fichiers `package-lock.json` pour assurer la cohérence des dépendances. Plusieurs commits concernent ces améliorations : [#3b78c893](https://github.com/betagouv/a-just/commit/3b78c893), [#1db0b5ba](https://github.com/betagouv/a-just/commit/1db0b5ba), [#ca5f6acd](https://github.com/betagouv/a-just/commit/ca5f6acd), [#5111a177](https://github.com/betagouv/a-just/commit/5111a177)
