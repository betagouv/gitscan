## Changelog : flux-retour-cfas (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'enrichissement des données utilisateurs exportées avec des informations issues du Machine Learning (ML) et de l'OFA, l'ajout de nouvelles collaborations, et l'amélioration de la chaîne de déploiement. Une nouvelle fonctionnalité d'onboarding a également été implémentée.

### Évolutions fonctionnelles
- Ajout d'un nouvel onboarding pour les utilisateurs. [#4586](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4586)
- Extension des colonnes géographiques lors de l'export des utilisateurs pour davantage de types d'organisations. [#4587](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4587)
- Ajout de données ML aux exports utilisateurs, améliorant ainsi l'analyse des données. [#4583](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4583)
- Intégration de nouvelles collaborations ML/OFA, permettant une meilleure analyse des données d'apprentissage. [#4558](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4558) et [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584)
- Ajout de la fonctionnalité de feedback en collaboration. [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585)
- Ajout d'un classificateur. [#4568](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4568)
- Possibilité de désactiver l'envoi des effectifs au ML pour un CFA sélectionné. [#4581](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4581)
- Filtrage des feedbacks sur l'indicateur du classificateur. [#4569](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4569)

### Évolutions techniques
- Migration de l'outil de gestion des secrets Ansible Vault vers SOPS, améliorant la sécurité et la gestion des configurations. [#4571](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4571)
- Améliorations significatives de la chaîne de déploiement, avec plusieurs corrections apportées aux scripts `release.yml`, `sentry-release.sh`, `app-build.sh` et `app-release.sh`. [#4573](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4573), [#4574](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4574), [#4575](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4575), [#4576](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4576), [#4577](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4577), [#4578](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4578), [#4579](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4579), [#4580](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4580)
- Suppression de la modale de feedback du classificateur et de la logique backend associée. [#4582](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4582)

### Autres changements
- Déclenchement d'un workflow. [#4572](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4572)
