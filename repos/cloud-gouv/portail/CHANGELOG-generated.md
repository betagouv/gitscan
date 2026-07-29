## Changelog : portail (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la correction de bugs, notamment concernant la gestion des connexions SOCKS5 et le fonctionnement de l'évaluation des règles d'accès (ACL). Des ajustements ont également été apportés à la configuration système pour une meilleure intégration avec systemd.

### Évolutions fonctionnelles
- Correction d'un bug dans les tests SOCKS5 pour assurer une connexion correcte. [#a5d0f21](https://github.com/cloud-gouv/portail/commit/a5d0f21)
- Désactivation du support UDP ASSOCIATE car les ACL ne sont pas évaluées correctement pour ce type de connexion. [#0017f76](https://github.com/cloud-gouv/portail/commit/0017f76)

### Évolutions techniques
- Assurance que les sockets sont toujours créés par systemd dans la configuration Nix. [#2bec618](https://github.com/cloud-gouv/portail/commit/2bec618)

### Autres changements
- Mise à jour de plusieurs dépendances Rust (uuid, anyhow, bytes, regex, rustls-pki-types) vers leurs dernières versions. Ces mises à jour sont gérées automatiquement par Renovate et visent à améliorer la sécurité et la stabilité du projet. (renovate bot commits)
