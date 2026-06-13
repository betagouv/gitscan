## Changelog : roles.data (30 derniers jours, au 3 juin 2026)

### Résumé
Ce changelog couvre les évolutions du projet roles.data sur les 30 derniers jours. Les principales améliorations concernent la gestion de la confidentialité des données (anonymisation des emails dans les logs Sentry) et l'amélioration de la robustesse de l'API (logging des détails d'erreurs). Des corrections ont également été apportées à la gestion des groupes d'utilisateurs.

### Évolutions fonctionnelles
- Correction : Normalisation des adresses email avant l'ajout d'utilisateurs à un groupe par un administrateur. Cela permet d'éviter les doublons et d'assurer une gestion correcte des appartenances aux groupes. [#160](https://github.com/datagouv/roles.data/issues/160)
- Amélioration : L'API enregistre désormais les détails des erreurs `HttpException` dans les logs, facilitant ainsi le diagnostic et la résolution des problèmes. [#161](https://github.com/datagouv/roles.data/issues/161)

### Évolutions techniques
- Sécurité : Anonymisation des adresses email des utilisateurs dans les exceptions envoyées à Sentry, améliorant ainsi la protection de la vie privée. [#162](https://github.com/datagouv/roles.data/issues/162)

### Autres changements
- Modifications mineures sur le site web (www) et dans le code de développement (dev). Ces changements n'impactent pas directement l'utilisateur final.
