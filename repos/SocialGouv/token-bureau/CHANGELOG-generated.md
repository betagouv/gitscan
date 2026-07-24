## Changelog : token-bureau (30 derniers jours, au 22 juillet 2026)

### Résumé
Les récentes mises à jour de token-bureau améliorent la flexibilité en permettant l'accès aux projets V2 et corrigent des problèmes liés à la configuration des permissions et au processus de publication. Ces changements permettent une meilleure gestion des droits d'accès et une intégration plus fluide avec GitHub.

### Évolutions fonctionnelles
- Ajout de la permission `organization_projects` pour les opérations d'écriture sur les projets V2. [#7](https://github.com/SocialGouv/token-bureau/issues/7)
- Correction de la lecture de la configuration des permissions à partir du fichier `PERMISSIONS_CONFIG_PATH`. [#ad1a07e](https://github.com/SocialGouv/token-bureau/commit/ad1a07eb53262dabe94200eebcce003365c232fa)

### Évolutions techniques
- Correction du workflow de publication pour utiliser un token d'application lors de la publication sur la branche `main`. [#7](https://github.com/SocialGouv/token-bureau/issues/7)

### Autres changements
- Publication des versions 0.0.8 et 0.0.9.
