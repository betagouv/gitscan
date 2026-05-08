## Changelog : ami-fc-proxy (30 derniers jours, au 07 mai 2026)

### Résumé
Ce proxy pour FranceConnect a été amélioré pour mieux supporter les déploiements sur Scalingo, notamment en corrigeant des problèmes liés à la configuration et à la construction de l'application. Une nouvelle fonctionnalité permet de stocker l'origine de la requête lors de l'autorisation, améliorant ainsi la sécurité et la traçabilité.

### Évolutions fonctionnelles
- Amélioration du support des déploiements sur Scalingo, corrigeant des erreurs de configuration et de construction. [#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)
- L'origine de la requête est maintenant stockée lors de la phase d'autorisation, renforçant la sécurité et permettant un meilleur suivi des demandes. [#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)

### Évolutions techniques
- Suppression du buildpack Heroku `uv` pour améliorer la compatibilité avec Scalingo.
- Refonte du processus de construction pour les déploiements Scalingo.
- Proxy de l'endpoint d'autorisation pour permettre le stockage de l'origine de la requête. [#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)
