## Changelog : st-ansible (30 derniers jours, au 2 mai 2026)

### Résumé
Cette nouvelle version apporte des améliorations sur le déploiement de RSPAMD, corrige un problème de gestion des permissions pour les applications Podman et optimise la structure des tâches Ansible pour les rôles drive, messages et keycloak, facilitant ainsi leur maintenance et leur réutilisation.

### Évolutions fonctionnelles
- Amélioration du déploiement de RSPAMD : refactorisation des messages pour une meilleure configuration. [#22](https://github.com/suitenumerique/st-ansible/issues/22)
- Correction d'un problème de permissions : la gestion des permissions des fichiers d'applications déployées avec `st_podman_application_files` a été corrigée. [#20](https://github.com/suitenumerique/st-ansible/issues/20)

### Évolutions techniques
- Refactorisation des tâches Ansible : séparation des tâches principales et importation des fichiers `deploy.yml` pour les rôles `drive`, `messages` et `keycloak`, améliorant la modularité et la lisibilité du code. [#20](https://github.com/suitenumerique/st-ansible/issues/20)
