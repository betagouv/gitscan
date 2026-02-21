## Changelog : oauth2-deploy-demo (30 derniers jours)

### Résumé
Ce projet de démonstration a reçu quelques améliorations concernant la configuration et la documentation de l'authentification OAuth2. Plus précisément, la documentation a été mise à jour pour inclure des détails sur la variable d'environnement `OAUTH2_PROXY_FOOTER`, et l'expression régulière utilisée pour ignorer certaines routes lors de l'authentification a été affinée pour une meilleure flexibilité.

### Évolutions fonctionnelles
- Amélioration de la documentation pour inclure des informations sur la variable `OAUTH2_PROXY_FOOTER` permettant de personnaliser le pied de page OAuth2 Proxy. (#2)
- Affinement de l'expression régulière pour la variable `OAUTH2_PROXY_SKIP_AUTH_ROUTES` afin de permettre une configuration plus précise des routes exemptées d'authentification. (be57911)

### Évolutions techniques
- Fusion de la pull request #1 apportant une correction sur l'expression régulière `OAUTH2_PROXY_SKIP_AUTH_ROUTES`. (#1)
