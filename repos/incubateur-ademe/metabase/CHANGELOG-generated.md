## Changelog : metabase (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce dépôt a connu une refonte importante au cours des dernières semaines, axée sur l'automatisation du déploiement de Metabase sur Scalingo et l'amélioration de la gestion des environnements. Les changements permettent désormais un déploiement plus rapide et plus fiable des nouvelles versions de Metabase, ainsi qu'une meilleure prise en charge de plusieurs environnements Scalingo pour différentes équipes. La documentation a également été traduite en français.

### Évolutions fonctionnelles
- **Déploiement automatisé :** Mise en place d'un workflow CI/CD qui déploie automatiquement les nouvelles versions de Metabase sur Scalingo après approbation manuelle. [#1](https://github.com/incubateur-ademe/metabase/pull/1)
- **Gestion multi-environnements :** Possibilité de gérer plusieurs environnements Scalingo (un par équipe) via un seul dépôt GitHub. [#4](https://github.com/incubateur-ademe/metabase/pull/4)
- **Rapports d'URL :** Ajout d'une étape pour signaler l'URL du rapport après déploiement. [#4b42e58](https://github.com/incubateur-ademe/metabase/commit/4b42e58)
- **Informations de version :** Affichage de la version de Metabase et de l'environnement dans les noms des exécutions de workflow et dans un résumé de déploiement. [#2a10f9c](https://github.com/incubateur-ademe/metabase/commit/2a10f9c), [#3d44679](https://github.com/incubateur-ademe/metabase/commit/3d44679), [#6af0618](https://github.com/incubateur-ademe/metabase/commit/6af0618)

### Évolutions techniques
- **Refactorisation des workflows :** Regroupement du déploiement dans le workflow `check-metabase-release` pour une meilleure organisation et une approbation groupée. [#20aeb14](https://github.com/incubateur-ademe/metabase/commit/20aeb14)
- **Synchronisation avec l'upstream :** Ajout d'un workflow pour synchroniser régulièrement le dépôt avec le projet Metabase original. [#2a59259](https://github.com/incubateur-ademe/metabase/commit/2a59259)
- **Permissions CI/CD :** Correction des permissions pour le déploiement et ajout du workflow de synchronisation upstream. [#2a59259](https://github.com/incubateur-ademe/metabase/commit/2a59259)
- **Suppression du préfixe `metabase-` :** Simplification de la gestion des environnements en supprimant le préfixe `metabase-`. [#6809d38](https://github.com/incubateur-ademe/metabase/commit/6809d38)
- **Correction d'un problème d'API :** Suppression d'une étape de déploiement cassée en raison d'une API non supportée par le token GitHub. [#23d0235](https://github.com/incubateur-ademe/metabase/commit/23d0235)

### Autres changements
- **Documentation :** Traduction du README en français pour faciliter la mise en place du fork. [#3](https://github.com/incubateur-ademe/metabase/pull/3)
- **Correction de la documentation :** Correction du nombre de workflows mentionnés dans le README. [#c89eef3](https://github.com/incubateur-ademe/metabase/commit/c89eef3)
- **Mise à jour de la documentation SE :** Délégation de la configuration des variables d'environnement et des secrets à un administrateur pour les nouveaux arrivants SE. [#e5422ae](https://github.com/incubateur-ademe/metabase/commit/e5422ae)
- **Remplacement de Heroku par Scalingo :** Mise à jour de toutes les occurrences de "Heroku" par "Scalingo" dans le code. [#30](https://github.com/incubateur-ademe/metabase/pull/30), [#42dadae](https://github.com/incubateur-ademe/metabase/commit/42dadae)
- **Améliorations de la structure du workflow :** Ajout d'emojis aux noms des étapes du workflow pour une meilleure lisibilité. [#9a769f9](https://github.com/incubateur-ademe/metabase/commit/9a769f9)
