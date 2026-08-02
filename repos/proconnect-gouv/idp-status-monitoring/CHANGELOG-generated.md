## Changelog : idp-status-monitoring (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les mises à jour du projet se sont principalement concentrées sur la maintenance et la mise à niveau des dépendances. Une amélioration notable concerne la configuration des tests d'intégration, désormais générée à partir des exemples disponibles.

### Évolutions fonctionnelles
- Amélioration de la configuration des tests d'intégration : la matrice de tests est maintenant générée dynamiquement à partir des exemples, facilitant l'ajout de nouveaux tests et assurant une meilleure couverture. [#138](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/138)

### Évolutions techniques
- Mise à jour de TypeScript : passage de la version 6.0.3 à la version 7.0.2. [#136](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/136)
- Mises à jour de Hono : plusieurs mises à jour mineures de la librairie Hono ont été appliquées (4.12.27 -> 4.12.29 -> 4.12.30 -> 4.12.32). [#134](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/134), [#135](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/135), [#140](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/140), [#142](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/142)
- Mises à jour des actions Docker : plusieurs actions Docker utilisées dans le workflow CI/CD ont été mises à jour vers leurs dernières versions (build-push-action, login-action, setup-compose-action, setup-buildx-action, metadata-action). [#127](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/127), [#128](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/128), [#129](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/129), [#130](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/130), [#131](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/131)
- Mise à jour de Prettier : passage de la version 3.8.5 à la version 3.9.6. [#133](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/133), [#137](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/137), [#141](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/141)
- Mise à jour de uuid : passage de la version 14.0.0 à la version 14.0.1. [#132](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/132)
- Mise à jour de @hono/zod-validator : mise à jour vers la dernière version. [#139](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/139)
