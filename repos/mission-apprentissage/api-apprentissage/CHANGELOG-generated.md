## Changelog : api-apprentissage (30 derniers jours, au 2026-06-04)

### Résumé
Ce changelog présente les récentes améliorations apportées à l'API Mission Apprentissage. Les changements incluent la suppression de modules d'infrastructure obsolètes, des corrections de fautes de frappe, la migration du serveur de recette et l'ajout d'un timeout pour améliorer la robustesse des requêtes vers LBA.

### Évolutions fonctionnelles
- Correction de fautes de frappe dans le code. [#489](https://github.com/mission-apprentissage/api-apprentissage/issues/489)
- Ajout d'un timeout sur les requêtes forwardées vers LBA pour éviter les blocages et améliorer la réactivité. [#485](https://github.com/mission-apprentissage/api-apprentissage/issues/485)

### Évolutions techniques
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` qui ne sont plus utilisés. [#488](https://github.com/mission-apprentissage/api-apprentissage/issues/488)
- Migration du serveur `api-recette`. [#487](https://github.com/mission-apprentissage/api-apprentissage/issues/487) et [#486](https://github.com/mission-apprentissage/api-apprentissage/issues/486)
