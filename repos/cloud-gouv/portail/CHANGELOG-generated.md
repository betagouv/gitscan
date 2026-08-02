## Changelog : portail (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la correction de bugs, notamment concernant la gestion des connexions SOCKS5 et le fonctionnement des ACLs. Des ajustements ont également été apportés à la configuration système pour une meilleure intégration avec systemd.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'évaluation des ACLs pour les connexions UDP ASSOCIATE. [#0017f76](https://github.com/cloud-gouv/portail/commit/0017f76)
- Amélioration des tests SOCKS5 pour assurer une connexion correcte. [#a5d0f21](https://github.com/cloud-gouv/portail/commit/a5d0f21)

### Évolutions techniques
- Configuration systemd : les sockets sont maintenant systématiquement gérés par systemd, améliorant la robustesse et la gestion des ressources. [#2bec618](https://github.com/cloud-gouv/portail/commit/2bec618)

### Autres changements
- Mise à jour de plusieurs dépendances Rust (uuid, anyhow, bytes, regex, rustls-pki-types) pour bénéficier des dernières corrections et améliorations. (renovate bots)
