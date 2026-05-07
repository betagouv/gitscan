## Changelog : infra (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'infrastructure a bénéficié d'une amélioration significative de sa sécurité avec la migration de la gestion des secrets d'Ansible Vault vers SOPS. Des corrections ont également été apportées à la configuration de SOPS et au système de notification Slack. Des mises à jour de sécurité pour Nginx et ModSecurity ont été intégrées, ainsi que des ajustements d'habilitation pour les projets LBA et Data.

### Évolutions fonctionnelles
- Correction de la configuration de SOPS et importation de la sous-clé OpenPGP dédiée au dépôt ([#214](https://github.com/mission-apprentissage/infra/issues/214)).
- Remplacement de l'action Slack `ravsamhq/notify-slack-action` par une alternative ([#213](https://github.com/mission-apprentissage/infra/issues/213)).
- Ajout d'une grappe MongoDB pour faciliter les tests ([#210](https://github.com/mission-apprentissage/infra/issues/210)).
- Correction concernant les adresses IP de confiance ([#213](https://github.com/mission-apprentissage/infra/issues/213)).

### Évolutions techniques
- Migration de la gestion des secrets d'Ansible Vault vers SOPS ([#211](https://github.com/mission-apprentissage/infra/issues/211)). Cette migration améliore la sécurité et la gestion des informations sensibles.
- Mise à jour des images Docker de Nginx et ModSecurity-CRS pour bénéficier des dernières corrections de sécurité et améliorations ([#215](https://github.com/mission-apprentissage/infra/issues/215)).
- Mise à jour des habilitations des projets LBA et Data ([#212](https://github.com/mission-apprentissage/infra/issues/212)).

### Autres changements
- Aucun changement significatif à signaler dans cette catégorie.
