## Changelog : infra (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'infrastructure a bénéficié d'améliorations significatives en matière de sécurité avec la migration vers SOPS pour la gestion des secrets, remplaçant Ansible Vault. Des mises à jour de configuration et d'images Docker ont également été effectuées pour assurer la stabilité et la sécurité des services. Enfin, des ajustements ont été apportés aux habilitations des projets et une grappe MongoDB a été ajoutée pour les tests.

### Évolutions fonctionnelles
- Ajout d'une grappe MongoDB dédiée aux tests, facilitant le développement et la validation des fonctionnalités. [#210](https://github.com/mission-apprentissage/infra/issues/210)
- Correction de la configuration des adresses IP de confiance. [#210](https://github.com/mission-apprentissage/infra/issues/210)

### Évolutions techniques
- Migration de la gestion des secrets d'Ansible Vault vers SOPS, améliorant la sécurité et la flexibilité de la gestion des informations sensibles. [#211](https://github.com/mission-apprentissage/infra/issues/211)
- Mise à jour des images Docker de Nginx et de ModSecurity-CRS pour bénéficier des dernières corrections de sécurité et améliorations de performance. [#215](https://github.com/mission-apprentissage/infra/issues/215)
- Remplacement de l'action GitHub `ravsamhq/notify-slack-action` par une alternative. [#213](https://github.com/mission-apprentissage/infra/issues/213)
- Correction de la configuration de SOPS et importation de la sous-clé OpenPGP dédiée au dépôt. [#214](https://github.com/mission-apprentissage/infra/issues/214)

### Autres changements
- Mise à jour des habilitations des projets `lba` et `data`. [#212](https://github.com/mission-apprentissage/infra/issues/212)
