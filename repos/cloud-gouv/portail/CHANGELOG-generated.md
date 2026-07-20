## Changelog : portail (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette mise à jour corrige un problème empêchant l'évaluation des règles d'accès pour le protocole UDP, désactivant ainsi temporairement cette fonctionnalité. Plusieurs dépendances Rust ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction : Désactivation du protocole UDP ASSOCIATE car les règles d'accès (ACL) ne sont pas évaluées correctement. [#issue à investiguer](https://github.com/cloud-gouv/portail/issues)

### Évolutions techniques
- Mise à jour de la crate Rust `uuid` vers la version 1.23.4.
- Mise à jour de la crate Rust `anyhow` vers la version 1.0.103.
- Mise à jour de la crate Rust `bytes` vers les versions 1.12.0 et 1.12.1.
- Mise à jour de la crate Rust `regex` vers la version 1.12.4.
- Mise à jour de la crate Rust `rustls-pki-types` vers la version 1.15.0.
