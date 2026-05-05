## Changelog : a-just (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog couvre une période d'amélioration de la sécurité, de corrections de tests et d'optimisations de l'infrastructure. Des efforts ont été déployés pour renforcer la validation des URL des iframes, améliorer la stabilité des tests E2E et simplifier la configuration du projet en supprimant des dépendances inutiles. Des corrections ont également été apportées à l'affichage des données dans le cockpit.

### Évolutions fonctionnelles
- Correction de la visualisation des dernières données dans le cockpit. [#21721ffd](https://github.com/betagouv/a-just/commit/21721ffd)
- Amélioration de la sécurité : validation des URLs des iframes pour éviter les injections potentielles. [#f25f8cc1](https://github.com/betagouv/a-just/commit/f25f8cc1)

### Évolutions techniques
- Mise à jour de la configuration des tests E2E, incluant la mise à jour du navigateur et la correction de problèmes liés à l'environnement de test. [#a4aee3ed](https://github.com/betagouv/a-just/commit/a4aee3ed), [#36678fbb](https://github.com/betagouv/a-just/commit/36678fbb), [#ba76ecfa](https://github.com/betagouv/a-just/commit/ba76ecfa)
- Correction d'un test API concernant la modification des données utilisateur. [#b80f8db9](https://github.com/betagouv/a-just/commit/b80f8db9)
- Refactorisation de la gestion de l'environnement Cypress pour utiliser `Cypress.expose()` au lieu de `cy.env()`. [#575a8c35](https://github.com/betagouv/a-just/commit/575a8c35)
- Simplification de la configuration Docker pour les tests E2E. [#b5613a15](https://github.com/betagouv/a-just/commit/b5613a15)
- Suppression de la dépendance `koa-smart` et remplacement par une implémentation personnalisée. [#47452fac](https://github.com/betagouv/a-just/commit/47452fac)
- Suppression de `compodoc` et migration vers des scripts en ligne pour la documentation. [#d412ca33](https://github.com/betagouv/a-just/commit/d412ca33), [#8604534d](https://github.com/betagouv/a-just/commit/8604534d)

### Autres changements
- Mise à jour de plusieurs dépendances, notamment `axios`. [#db2a99e5](https://github.com/betagouv/a-just/commit/db2a99e5)
- Nettoyage de la configuration du projet et suppression de fichiers inutiles (package-lock.json, commentaires, documentation temporaire). [#5df5e348](https://github.com/betagouv/a-just/commit/5df5e348), [#9017c45d](https://github.com/betagouv/a-just/commit/9017c45d), [#bc0abba9](https://github.com/betagouv/a-just/commit/bc0abba9)
- Amélioration de la gestion des logs et des warnings. [#5111a177](https://github.com/betagouv/a-just/commit/5111a177)
- Corrections de la configuration de build et des scripts npm. [#0ec55f6c](https://github.com/betagouv/a-just/commit/0ec55f6c), [#5e54ffc2](https://github.com/betagouv/a-just/commit/5e54ffc2), [#5aee2964](https://github.com/betagouv/a-just/commit/5aee2964), [#3e4979ac](https://github.com/betagouv/a-just/commit/3e4979ac), [#d45eabfc](https://github.com/betagouv/a-just/commit/d45eabfc), [#19898990](https://github.com/betagouv/a-just/commit/19898990), [#e5c76048](https://github.com/betagouv/a-just/commit/e5c76048)
- Ajout d'options pour la ventilation des dates. [#7e63cc22](https://github.com/betagouv/a-just/commit/7e63cc22)
- Ajout d'un package optionnel. [#010d2c2b](https://github.com/betagouv/a-just/commit/010d2c2b)
