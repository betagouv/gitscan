## Changelog : matrix-authentication-service (30 derniers jours, au 27 avril 2026)

### Résumé
Cette mise à jour améliore la gestion des erreurs lors de l'authentification, notamment en cas de problèmes avec le serveur d'identité ou de configuration incorrecte. Elle facilite également la configuration du service grâce à l'utilisation de templates Jinja et permet une meilleure prise en charge des liens profonds Tchap dans la politique OIDC. Enfin, des améliorations mineures ont été apportées aux emails de vérification.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs d'authentification, notamment pour les erreurs liées au serveur d'identité et à la configuration du serveur. [#125](https://github.com/tchapgouv/matrix-authentication-service/issues/125)
- Prise en charge de liens profonds Tchap supplémentaires dans la politique OIDC, offrant une meilleure intégration avec l'application Tchap. [#123](https://github.com/tchapgouv/matrix-authentication-service/issues/123)
- Amélioration des labels dans les emails de vérification pour une meilleure clarté.

### Évolutions techniques
- Utilisation de templates Jinja pour la construction de la configuration du service, simplifiant ainsi la gestion et la personnalisation de la configuration. [#118](https://github.com/tchapgouv/matrix-authentication-service/issues/118)

### Autres changements
- Aucun changement significatif à signaler.
