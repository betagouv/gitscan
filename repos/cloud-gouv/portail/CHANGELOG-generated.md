## Changelog : portail (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette mise à jour corrige un problème empêchant l'évaluation des règles d'accès pour le protocole UDP, désactivant ainsi temporairement cette fonctionnalité. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'évaluation des ACLs pour le trafic UDP, ce qui désactive temporairement le protocole UDP ASSOCIATE. [#issue à investiguer](https://github.com/cloud-gouv/portail/issues)

### Évolutions techniques
- Mise à jour de la crate Rust `uuid` vers la version 1.23.4.
- Mise à jour de la crate Rust `anyhow` vers la version 1.0.103.
- Mise à jour de la crate Rust `bytes` vers les versions 1.12.0 et 1.12.1.
- Mise à jour de la crate Rust `regex` vers la version 1.12.4.
- Mise à jour de la crate Rust `rustls-pki-types` vers la version 1.15.0.
