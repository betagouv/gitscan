## Changelog : apistration (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la maintenabilité de l'infrastructure, l'ajout de SDK Ruby pour faciliter l'intégration avec l'API, et l'amélioration de la documentation et des outils de développement. Des corrections de bugs et des améliorations de la gestion des erreurs ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de rendre le lieu de naissance optionnel pour les endpoints CNAV [#91](https://github.com/datagouv/apistration/pull/91).
- Ajout d'un indicateur de campagne pour l'API CNOUS sur la scolarité des étudiants [#69](https://github.com/datagouv/apistration/pull/69).
- Publication de la version 0.1.1 de l'API Particulier et intégration des informations dans un skill pour faciliter la diffusion des informations. [#97](https://github.com/datagouv/apistration/pull/97)
- Ajout d'une bannière d'annonce pour communiquer les maintenances planifiées (ProConnect) [#33](https://github.com/datagouv/apistration/pull/33).
- Amélioration de la documentation pour les routes de ping de monitoring [#72](https://github.com/datagouv/apistration/pull/72).

### Évolutions techniques
- Intégration de SDK Ruby officiels pour l'API Entreprise et l'API Particulier, incluant des workflows CI/CD pour leur publication et maintenance [#37](https://github.com/datagouv/apistration/pull/37).
- Refactorisation de la gestion des erreurs avec un nouveau registre d'erreurs et une meilleure gestion des exceptions [#74](https://github.com/datagouv/apistration/pull/74).
- Amélioration de la gestion des fichiers temporaires pour éviter les erreurs EBADF sous Puma [#2179](https://github.com/datagouv/apistration/pull/2179).
- Refactorisation de l'authentification et de l'autorisation avec l'introduction d'un middleware de résolution d'utilisateur [#2179](https://github.com/datagouv/apistration/pull/2179).
- Migration des credentials Rails chiffrés vers des fichiers YAML en clair pour une meilleure gestion et sécurité [#4](https://github.com/datagouv/apistration/pull/4).
- Amélioration de la configuration et de la gestion des dépendances avec des mises à jour et des corrections de dépendances.
- Refactorisation de la structure des fichiers d'endpoints pour une meilleure organisation et réutilisation [#35](https://github.com/datagouv/apistration/pull/35).
- Ajout de tests d'acceptation pour les API SIADE et Site [#88](https://github.com/datagouv/apistration/pull/88).
- Amélioration de la gestion des quotas pour l'API GIP-MDS [#44](https://github.com/datagouv/apistration/pull/44).

### Autres changements
- Ajout d'un workflow pour la génération automatique du changelog [#39](https://github.com/datagouv/apistration/pull/39).
- Documentation du workflow de création du changelog dans un fichier CLAUDE.md.
- Ajout d'une skill CLAUDE pour documenter les gotchas liés à la publication des SDK Ruby.
- Ajout de documentation sur le flux de publication des SDK Ruby.
- Mise à jour de la documentation pour refléter les changements et les nouvelles fonctionnalités.
- Ajout d'un système de refroidissement (cooldown) pour les mises à jour de dépendances afin d'éviter les interruptions de CI/CD.
- Amélioration des tests et correction de tests flaky.
- Ajout de mocks pour les tests, notamment pour les cas spécifiques liés à la civilité et à l'année scolaire.
- Import du projet site depuis admin_api_entreprise.
- Mise à jour des credentials HubEE.
- Ajout de tests pour les pings CNETP.
- Ajout de la possibilité de configurer des variables d'environnement pour les tests.
- Ajout de la documentation sur l'utilisation des mocks.
