## Changelog : oidc2fer (30 derniers jours, au 18 juin 2026)

### Résumé
Cette nouvelle version apporte des améliorations à la gestion des erreurs d'affiliation lors de l'authentification OIDC, ainsi que des mises à jour pour les tests d'intégration et la gestion des identifiants SIRET. Une nouvelle version (v1.0.15) a été publiée en production.

### Évolutions fonctionnelles
- Amélioration du message d'erreur renvoyé en cas d'échec de la vérification de l'affiliation `eduPersonAffiliation` pour fournir plus de détails. [#42](https://github.com/proconnect-gouv/oidc2fer/pull/42)
- Mise à jour du client de test ProConnect utilisé pour les tests d'intégration.
- Ajout de nouvelles entités à la correspondance SIRET, incluant EURECOM.
- Ajout de nouvelles entités à la correspondance SIRET.

### Évolutions techniques
- Exclusion du répertoire de construction (build) de l'analyse Pylint pour améliorer la performance et réduire les faux positifs.

### Autres changements
- Publication de la version v1.0.15 en production.
- Publication de la version v1.0.15.
