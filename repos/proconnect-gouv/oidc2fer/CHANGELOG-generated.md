## Changelog : oidc2fer (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections concernant la gestion des identifiants SIRET pour les établissements CNAM et PSL, améliorant ainsi la précision de l'identification des utilisateurs et des organisations. Une nouvelle version (v1.0.15) a été déployée en production.

### Évolutions fonctionnelles
- Correction de l'identifiant SIRET pour l'établissement CNAM. [#27b79f8](https://github.com/proconnect-gouv/oidc2fer/commit/27b79f8)
- Correction de l'identifiant SIRET pour l'établissement PSL. [#626380c](https://github.com/proconnect-gouv/oidc2fer/commit/626380c)
- Amélioration de la gestion des erreurs d'affiliation `eduPersonAffiliation` en renvoyant une erreur OIDC détaillée. [#42](https://github.com/proconnect-gouv/oidc2fer/pull/42)

### Évolutions techniques
- Exclusion du répertoire `build` de l'analyse Pylint pour optimiser le processus de linting. [#9d3a43c](https://github.com/proconnect-gouv/oidc2fer/commit/9d3a43c)
- Déploiement de la version v1.0.15 en production. [#4f1e941](https://github.com/proconnect-gouv/oidc2fer/commit/4f1e941)

### Autres changements
- Publication de la version v1.0.15. [#7f62737](https://github.com/proconnect-gouv/oidc2fer/commit/7f62737)
