## Changelog : oauth2-deploy-demo (30 derniers jours, au 19 mars 2026)

### Résumé
Cette mise à jour apporte un ajustement de logging pour faciliter le débogage et la compréhension du fonctionnement de l'application. Plus précisément, les en-têtes JSON sont désormais affichés dans les logs, ce qui peut être utile pour diagnostiquer des problèmes liés à l'authentification ou à la communication avec le proxy OAuth2.

### Évolutions techniques
- Activation du logging des en-têtes JSON dans `index.js` pour une meilleure traçabilité des requêtes et réponses. [#1](https://github.com/betagouv/oauth2-deploy-demo/commit/d441291)
