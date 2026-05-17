## Changelog : infra (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, l'infrastructure a bénéficié d'améliorations significatives en matière de sécurité, notamment avec la correction de vulnérabilités critiques et la migration vers un système de gestion des secrets plus robuste (SOPS). Des mises à jour de l'infrastructure de test ont également été effectuées pour faciliter le développement et la validation.

### Évolutions fonctionnelles
- Correction d'une vulnérabilité critique affectant la gestion des fragments TCP (Dirty Frag et Fragnesia) [#216](https://github.com/mission-apprentissage/infra/issues/216).
- Rétablissement des tags Git, permettant une meilleure gestion des versions et un suivi des modifications [#217](https://github.com/mission-apprentissage/infra/issues/217).

### Évolutions techniques
- Migration d'Ansible Vault vers SOPS pour une gestion des secrets plus sécurisée et flexible [#211](https://github.com/mission-apprentissage/infra/issues/211).
- Configuration de SOPS et import de la sous-clé OpenPGP dédiée au dépôt [#214](https://github.com/mission-apprentissage/infra/issues/214).
- Remplacement de l'action Slack `ravsamhq/notify-slack-action` par une alternative plus maintenue [#213](https://github.com/mission-apprentissage/infra/issues/213).
- Mise à jour des images Docker de Nginx et ModSecurity-CRS [#215](https://github.com/mission-apprentissage/infra/issues/215).
- Mise à jour des habilitations des projets LBA et Data [#212](https://github.com/mission-apprentissage/infra/issues/212).

### Autres changements
- Ajout d'une grappe MongoDB pour faciliter les tests [#210](https://github.com/mission-apprentissage/infra/issues/210).
