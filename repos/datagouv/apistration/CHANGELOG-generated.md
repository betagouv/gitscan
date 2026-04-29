## Changelog : apistration (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation, la gestion des secrets, la robustesse des tests et l'ajout de nouvelles fonctionnalités pour les API, notamment concernant les données scolaires et les quotas d'utilisation. Des optimisations de performance et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout du paramètre `campaignYear` à l'API CNOUS pour les bourses étudiantes [#69](https://github.com/datagouv/apistration/pull/69).
- Implémentation d'une nouvelle fonctionnalité permettant de surveiller l'API DataSubvention via des sondes (ping) [#43](https://github.com/datagouv/apistration/pull/43).
- Ajout de scopes pour les données MEN (Ministère de l'Éducation Nationale) [#1](https://github.com/datagouv/apistration/pull/1) et [#2175](https://github.com/datagouv/apistration/pull/2175).
- Ajout de la gestion du régime de pensionnat dans l'API Scolarités (MEN) [#17](https://github.com/datagouv/apistration/pull/17).
- Amélioration de la gestion des quotas pour l'API GIP-MDS [#44](https://github.com/datagouv/apistration/pull/44).
- Ajout d'une bannière d'annonce pour signaler les maintenances programmées, comme celle de ProConnect [#33](https://github.com/datagouv/apistration/pull/33).

### Évolutions techniques
- Refactorisation de la gestion des secrets : remplacement des credentials chiffrés par des fichiers YAML en clair, avec une gestion plus robuste et sécurisée [#4](https://github.com/datagouv/apistration/pull/4) et [#2176](https://github.com/datagouv/apistration/pull/2176).
- Amélioration de la structure du code avec un passage à une architecture monorepo et une organisation des workflows CI/CD [#2](https://github.com/datagouv/apistration/pull/2), [#20](https://github.com/datagouv/apistration/pull/20) et [#26](https://github.com/datagouv/apistration/pull/26).
- Refactorisation des définitions d'endpoints pour une meilleure organisation et réutilisation [#55](https://github.com/datagouv/apistration/pull/55).
- Optimisation des tests : suppression de la collecte de déchets différée (DeferredGarbageCollection) et stub de DataEncryptor pour accélérer l'exécution [#12](https://github.com/datagouv/apistration/pull/12).
- Mise en place d'un système de tests local avec mocks pour faciliter le développement et les tests en environnement isolé [#58](https://github.com/datagouv/apistration/pull/58) et [#59](https://github.com/datagouv/apistration/pull/59).
- Amélioration de la gestion des erreurs et ajout de logs pour faciliter le débogage.
- Mise à jour des dépendances (Ruby, Rails, etc.) et des outils de développement (Node.js, Ruby setup) avec les dernières versions stables.

### Autres changements
- Amélioration de la documentation, notamment sur les routes de ping pour le monitoring [#70](https://github.com/datagouv/apistration/pull/70).
- Ajout d'une documentation sur la chaîne de résolution des utilisateurs.
- Ajout d'un fichier `CONTRIBUTING.md` pour encourager les contributions et protéger les mainteneurs.
- Mise à jour des références aux données de staging.
- Ajout d'une adresse email pour signaler les vulnérabilités de sécurité.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests pour les cas d'utilisation spécifiques (QF, EAJE).
- Suppression de liens obsolètes dans la documentation.
- Ajout de la possibilité de configurer un agent pour l'exécution des tests.
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances.
