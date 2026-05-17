## Changelog : a-just (30 derniers jours, au 15 mai 2026)

### Résumé
Les dernières mises à jour d'a-just se concentrent principalement sur l'amélioration de la qualité et de la fiabilité des tests end-to-end (E2E) et la correction de bugs mineurs. Des ajustements ont été apportés à la configuration de Cypress, à l'accès aux variables d'environnement et à la validation de la sécurité. Une correction a également été apportée au calcul du nombre de jours pour la projection de simulateur.

### Évolutions fonctionnelles
- Correction d'un bug dans le calcul du nombre de jours pour la projection du simulateur [#1b8c8737](https://github.com/betagouv/a-just/commit/1b8c8737).
- Correction d'un problème avec la configuration de Quill JS [#fee012c6](https://github.com/betagouv/a-just/commit/fee012c6).
- Correction d'un problème avec la configuration de toastr [#7e9c83d6](https://github.com/betagouv/a-just/commit/7e9c83d6).
- Amélioration de la sécurité en validant les URLs `src` des `iframe` par rapport à une liste blanche avant de contourner le sanitizer Angular [#f25f8cc1](https://github.com/betagouv/a-just/commit/f25f8cc1).

### Évolutions techniques
- Mise à jour de Cypress et adaptation des tests E2E pour la compatibilité avec la version 15 [#520609b2](https://github.com/betagouv/a-just/commit/520609b2).
- Refactorisation de l'accès aux variables d'environnement dans `loginApi` pour plus de robustesse [#dadb82f6](https://github.com/betagouv/a-just/commit/dadb82f6), [#5c54f3f1](https://github.com/betagouv/a-just/commit/5c54f3f1).
- Amélioration de la méthode de récupération de l'URL du serveur dans les tests E2E de connexion [#74920f8b](https://github.com/betagouv/a-just/commit/74920f8b).
- Mise à jour de la configuration `tsconfig.json` pour les tests E2E [#7d27a047](https://github.com/betagouv/a-just/commit/7d27a047), [#4b6de590](https://github.com/betagouv/a-just/commit/4b6de590), [#8869bca3](https://github.com/betagouv/a-just/commit/8869bca3), [#c76918ac](https://github.com/betagouv/a-just/commit/c76918ac).
- Suppression de code dupliqué [#ac89de7d](https://github.com/betagouv/a-just/commit/ac89de7d).

### Autres changements
- Ajout d'un fichier `.env.example` pour les tests end-to-end [#aa479cde](https://github.com/betagouv/a-just/commit/aa479cde).
- Corrections de tests API, notamment sur la modification des données utilisateur [#b80f8db9](https://github.com/betagouv/a-just/commit/b80f8db9).
- Mises à jour de modules pour les tests E2E (ngx-env/builder, navigateur) [#a4aee3ed](https://github.com/betagouv/a-just/commit/a4aee3ed), [#36678fbb](https://github.com/betagouv/a-just/commit/36678fbb), [#ba76ecfa](https://github.com/betagouv/a-just/commit/ba76ecfa).
- Suppression des types dans les fichiers `package.json` [#c5583572](https://github.com/betagouv/a-just/commit/c5583572).
- Suppression du lockfile pnpm du front-admin [#9c88e14e](https://github.com/betagouv/a-just/commit/9c88e14e).
- Mise à jour des dépendances `@emnapi` et suppression des entrées obsolètes esbuild [#ced7d647](https://github.com/betagouv/a-just/commit/ced7d647).
