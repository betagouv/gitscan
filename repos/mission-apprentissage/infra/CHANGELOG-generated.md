## Changelog : infra (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'infrastructure a bénéficié d'améliorations significatives en matière de sécurité avec la migration vers SOPS pour la gestion des secrets, ainsi que de l'ajout d'une grappe MongoDB dédiée aux tests. Des corrections et mises à jour d'habilitation ont également été apportées pour améliorer la stabilité et la gestion des accès.

### Évolutions fonctionnelles
- Ajout d'une grappe MongoDB pour les tests, permettant un environnement de test plus isolé et fiable. [#210](https://github.com/mission-apprentissage/infra/issues/210)
- Correction concernant les adresses IP de confiance. [#210](https://github.com/mission-apprentissage/infra/issues/210)

### Évolutions techniques
- Migration de la gestion des secrets d'Ansible Vault vers SOPS, améliorant la sécurité et la flexibilité de la gestion des informations sensibles. [#211](https://github.com/mission-apprentissage/infra/issues/211)
- Remplacement de l'action Slack `ravsamhq/notify-slack-action` par une alternative. [#213](https://github.com/mission-apprentissage/infra/issues/213)

### Autres changements
- Mise à jour des habilitations des projets LBA et Data, améliorant la gestion des accès et la sécurité. [#212](https://github.com/mission-apprentissage/infra/issues/212)
