## Changelog : portail (30 derniers jours, au 2026-04-17)

### Résumé
Ce changelog présente les améliorations apportées au portail au cours du dernier mois. Les modifications incluent des corrections de bugs liés à la configuration TLS et à la gestion des erreurs, l'ajout d'un test d'intégration pour le proxy upstream Tinyproxy, et l'amélioration du processus d'intégration continue avec l'ajout de commandes Cargo.

### Évolutions fonctionnelles
- Ajout d'un test d'intégration de bout en bout (E2E) pour le proxy upstream Tinyproxy [#70](https://github.com/cloud-gouv/portail/issues/70).

### Évolutions techniques
- Correction d'une erreur potentielle de panique due à l'utilisation de `unwrap` [#76](https://github.com/cloud-gouv/portail/issues/76).
- Correction d'un problème de configuration TLS manquant du nom du serveur [#75](https://github.com/cloud-gouv/portail/issues/75).
- Ajout de commandes Cargo pour l'intégration continue [#68](https://github.com/cloud-gouv/portail/issues/68).

### Autres changements
- Mise à jour de la dépendance `zlink` vers la version 0.4.1 (mise à jour automatique).
