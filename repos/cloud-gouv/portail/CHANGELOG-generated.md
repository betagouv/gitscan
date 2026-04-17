## Changelog : portail (30 derniers jours, au 17 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au portail au cours des 30 derniers jours. Les principales évolutions concernent la correction de bugs liés à la configuration TLS, l'ajout de tests d'intégration pour le proxy upstream Tinyproxy et l'initialisation de la version 1 des règles d'accès (ACL).

### Évolutions fonctionnelles
- Correction d'un bug empêchant la configuration correcte du nom de serveur TLS. [#75](https://github.com/cloud-gouv/portail/issues/75)
- Ajout de tests d'intégration de bout en bout (E2E) pour le proxy upstream Tinyproxy. [#70](https://github.com/cloud-gouv/portail/issues/70)
- Initialisation de la version 1 des règles d'accès (ACL). [#76](https://github.com/cloud-gouv/portail/issues/76)

### Évolutions techniques
- Ajout de commandes Cargo pour faciliter l'intégration continue (CI). [#68](https://github.com/cloud-gouv/portail/issues/68)
- Correction d'un `unwrap` potentiellement problématique dans le code. [#76](https://github.com/cloud-gouv/portail/issues/76)

### Autres changements
- Mise à jour de la dépendance `zlink` vers la version 0.4.1 (mise à jour automatique).
