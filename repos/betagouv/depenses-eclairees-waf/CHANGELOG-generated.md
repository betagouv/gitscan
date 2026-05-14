## Changelog : depenses-eclairees-waf (30 derniers jours, au 12 mai 2026)

### Résumé
Ce changelog détaille les premières étapes de configuration du Web Application Firewall (WAF) pour protéger l'application web de dépenses publiques. Les modifications récentes incluent la configuration initiale de Nginx, l'ajout de règles personnalisées pour Metabase, et l'amélioration de la résolution DNS et du transfert d'informations d'en-tête pour une meilleure sécurité et performance.

### Évolutions fonctionnelles
- Ajout de règles personnalisées pour Metabase afin de renforcer la sécurité de l'application. [#3274435](https://github.com/betagouv/depenses-eclairees-waf/commit/3274435)
- Amélioration de la résolution DNS pour garantir une connexion fiable et rapide. [#ec29890](https://github.com/betagouv/depenses-eclairees-waf/commit/ec29890)
- Ajout de la transmission des en-têtes HTTP d'origine pour une meilleure compatibilité et fonctionnalité de l'application. [#ec29890](https://github.com/betagouv/depenses-eclairees-waf/commit/ec29890)

### Évolutions techniques
- Configuration initiale de Nginx pour servir de base au WAF. [#5d05e45](https://github.com/betagouv/depenses-eclairees-waf/commit/5d05e45)
- Ajustements de la configuration Nginx pour optimiser la performance et la sécurité. [#e39cc3e](https://github.com/betagouv/depenses-eclairees-waf/commit/e39cc3e)
- Initialisation du dépôt avec un premier commit. [#5d05e45](https://github.com/betagouv/depenses-eclairees-waf/commit/5d05e45)
