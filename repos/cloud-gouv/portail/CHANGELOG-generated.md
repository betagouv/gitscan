## Changelog : portail (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la correction de bugs, notamment concernant la gestion des connexions SOCKS5 et le support UDP. Des ajustements ont également été apportés à la configuration système pour une meilleure intégration avec systemd.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'évaluation des ACLs pour les paquets UDP ASSOCIATE. [#0017f76](https://github.com/cloud-gouv/portail/commit/0017f76)
- Amélioration des tests SOCKS5 pour assurer une connexion correcte. [#a5d0f21](https://github.com/cloud-gouv/portail/commit/a5d0f21)

### Évolutions techniques
- Configuration systemd : S'assurer que les sockets sont toujours gérés par systemd. [#2bec618](https://github.com/cloud-gouv/portail/commit/2bec618)

### Autres changements
- Mise à jour des dépendances Rust : `uuid` (v1.23.4), `anyhow` (v1.0.103), `bytes` (v1.12.1 et v1.12.0), `regex` (v1.12.4), `rustls-pki-types` (v1.15.0). Ces mises à jour sont gérées automatiquement par Renovate et visent à maintenir la sécurité et la compatibilité du projet.
