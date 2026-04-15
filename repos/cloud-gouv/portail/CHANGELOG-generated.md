## Changelog : portail (30 derniers jours, au 2026-04-15)

### Résumé
Ce changelog présente les améliorations apportées au portail au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de tests d'intégration, l'amélioration de la gestion TLS, l'implémentation du protocole HTTP/2 et l'initialisation d'une nouvelle version de l'évaluation des règles d'accès (ACL).

### Évolutions fonctionnelles
- Ajout de tests E2E pour le proxy upstream Tinyproxy [#70](https://github.com/cloud-gouv/portail/issues/70).
- Implémentation du protocole HTTP/2 pour améliorer les performances et l'efficacité [#53](https://github.com/cloud-gouv/portail/issues/53).
- Initialisation de la version 1 de l'évaluation des règles d'accès (ACL) [#7a19e78](https://github.com/cloud-gouv/portail/commit/7a19e78).

### Évolutions techniques
- Ajout d'une interface Varlink pour une meilleure communication entre les composants [#b65d675](https://github.com/cloud-gouv/portail/commit/b65d675).
- Ajout de commandes Cargo pour faciliter l'intégration continue [#68](https://github.com/cloud-gouv/portail/issues/68).
- Correction d'une erreur liée à la configuration du nom de serveur TLS [#75](https://github.com/cloud-gouv/portail/issues/75).
- Suppression d'un `unwrap` potentiellement problématique pour améliorer la robustesse [#76](https://github.com/cloud-gouv/portail/issues/76).

### Autres changements
- Mise à jour de la dépendance `zlink` vers la version 0.4.1 (mise à jour automatique).
