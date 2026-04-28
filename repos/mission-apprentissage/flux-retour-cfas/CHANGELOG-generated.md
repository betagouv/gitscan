## Changelog : flux-retour-cfas (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités d'export de données utilisateurs, notamment avec l'intégration de données liées à l'apprentissage machine (ML) et aux collaborations. Des corrections importantes ont également été apportées à la chaîne de déploiement pour assurer une meilleure stabilité et fiabilité du service. Enfin, des améliorations de sécurité ont été implémentées en mettant à jour des dépendances vulnérables.

### Évolutions fonctionnelles
- Ajout d'une nouvelle fonctionnalité d'onboarding. [#4586](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4586)
- Extension des colonnes d'export utilisateur pour inclure des informations relatives aux collaborations, notamment pour les organisations de type ML/OFA. [#4587](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4587) et [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584)
- Amélioration de l'export utilisateur avec l'ajout de données issues de l'apprentissage machine (ML). [#4583](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4583)
- Ajout de feedbacks liés aux collaborations. [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585)
- Possibilité de désactiver l'envoi des effectifs à la ML pour un CFA spécifique. [#4581](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4581)
- Correction de la date utilisée pour l'ouverture des collaborations. [#4591](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4591)

### Évolutions techniques
- Migration de l'outil de gestion des secrets d'Ansible Vault vers SOPS, améliorant ainsi la sécurité et la gestion des informations sensibles. [#4571](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4571)
- Correction de plusieurs scripts liés à la chaîne de déploiement (app-build.sh, app-release.sh, sentry-release.sh, release.yml) pour améliorer la fiabilité et la robustesse du processus de déploiement. [#4580](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4580), [#4579](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4579), [#4578](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4578), [#4577](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4577), [#4576](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4576), [#4575](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4575), [#4574](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4574), [#4573](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4573), [#4572](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4572)
- Suppression de la modal de feedback du classifier et de la logique backend associée. [#4582](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4582)

### Autres changements
- Mise à jour des habilitations. [#4594](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4594)
- Ajout de nouveaux utilisateurs. [#4593](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4593) et [#4592](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4592)
- Correction de vulnérabilités de sécurité en mettant à jour les dépendances Handlebars et form-data. [#4589](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4589)
- Mise à jour de dépendances pour corriger des alertes de sécurité (Dependabot). [#4588](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4588)
