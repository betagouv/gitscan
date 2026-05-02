## Changelog : apistration (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des erreurs, la sécurisation de l'accès aux données via de nouveaux mécanismes d'authentification et de délégation, ainsi que sur l'amélioration de la robustesse et de la maintenabilité du code. Des améliorations ont également été apportées à la documentation et aux processus de déploiement.

### Évolutions fonctionnelles
- Ajout de la gestion du paramètre `campaignYear` pour l'API CNOUS des bourses d'étudiants. [#69](https://github.com/datagouv/apistration/pull/69)
- Implémentation d'un système de délégation d'éditeur avec des tokens, permettant un accès plus granulaire aux données. [#31](https://github.com/datagouv/apistration/pull/31)
- Ajout de nouveaux scopes pour les données MEN (Ministère de l'Éducation Nationale) concernant les bourses. [#1](https://github.com/datagouv/apistration/pull/1)
- Ajout d'une bannière d'annonce pour communiquer les maintenances planifiées (ProConnect). [#33](https://github.com/datagouv/apistration/pull/33)
- Amélioration de la documentation des routes de ping pour le monitoring. [#72](https://github.com/datagouv/apistration/pull/72)
- Mise à jour de l'URL SIRENE dans la documentation pour pointer vers la nouvelle API. [#58](https://github.com/datagouv/apistration/pull/58)

### Évolutions techniques
- Refonte de la gestion des erreurs avec un registre centralisé et une meilleure propagation des informations d'erreur. [#74](https://github.com/datagouv/apistration/pull/74)
- Amélioration de la gestion des statuts HTTP et de leur mapping.
- Refactorisation de l'authentification et de la résolution des utilisateurs avec un middleware centralisé.
- Mise en place d'un système de limitation de débit (rate limiting) pour l'API GIP-MDS. [#48](https://github.com/datagouv/apistration/pull/48)
- Mise en place d'un système de cache pour les réponses de l'API GIP-MDS. [#44](https://github.com/datagouv/apistration/pull/44)
- Migration des informations d'identification vers des fichiers YAML pour une meilleure sécurité et gestion. [#4](https://github.com/datagouv/apistration/pull/4)
- Refonte de la structure des fichiers d'endpoints pour une meilleure organisation et réutilisation. [#55](https://github.com/datagouv/apistration/pull/55)
- Amélioration de la robustesse des tests et correction de tests aléatoires. [#17](https://github.com/datagouv/apistration/pull/17)
- Mise en place d'un système de déploiement en sandbox. [#75](https://github.com/datagouv/apistration/pull/75)
- Généralisation de l'utilisation de Sentry CLI pour la gestion des erreurs. [#76](https://github.com/datagouv/apistration/pull/76)
- Amélioration de la gestion des fichiers temporaires pour éviter les erreurs EBADF. [#7](https://github.com/datagouv/apistration/pull/7)

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Ajout d'un fichier `CONTRIBUTING.md` pour encourager les contributions et protéger les mainteneurs. [#35](https://github.com/datagouv/apistration/pull/35)
- Mise à jour des dépendances.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de mocks pour les tests, notamment pour les données CNAV.
- Ajout d'une configuration pour le travail en worktree. [#61](https://github.com/datagouv/apistration/pull/61)
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances. [#29](https://github.com/datagouv/apistration/pull/29)
- Mise à jour des références aux données de staging. [#14](https://github.com/datagouv/apistration/pull/14)
