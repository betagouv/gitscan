## Changelog : flux-retour-cfas (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités liées à l'apprentissage machine (ML) et à la collaboration, notamment en intégrant des données ML dans les exports utilisateurs et en ajoutant des colonnes de collaboration. Des corrections importantes ont également été apportées à la chaîne de déploiement pour une meilleure stabilité et fiabilité.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données utilisateurs enrichies avec des informations issues de l'apprentissage machine. [#4583](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4583)
- Intégration de nouvelles collaborations ML/OFA. [#4558](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4558)
- Ajout de colonnes de collaboration au traitement et à l'export des données ML. [#4584](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4584)
- Ajout d'un classificateur (classifier) pour les indicateurs. [#4568](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4568)
- Possibilité de filtrer les retours (feedbacks) uniquement pour le classificateur indicateur. [#4569](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4569)
- Suppression de la modal et de la logique backend liées au feedback du classificateur. [#4582](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4582)
- Désactivation de l'effectif pour le ML sur les CFA sélectionnés. [#4581](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4581)
- Ajout de feedbacks collaboratifs. [#4585](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4585)

### Évolutions techniques
- Migration de l'outil de gestion des secrets Ansible Vault vers SOPS, améliorant la sécurité et la gestion des configurations. [#4571](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4571)
- Corrections et améliorations significatives de la chaîne de déploiement (scripts `app-build.sh`, `app-release.sh`, `release.yml`, `sentry-release.sh`) pour une meilleure fiabilité et automatisation. [#4573](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4573) [#4574](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4574) [#4575](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4575) [#4576](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4576) [#4577](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4577) [#4578](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4578) [#4579](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4579) [#4580](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4580)

### Autres changements
- Déclenchement manuel d'un workflow (chore). [#4572](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4572)
