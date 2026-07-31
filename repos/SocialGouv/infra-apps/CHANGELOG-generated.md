## Changelog : infra-apps (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'infrastructure Iterion, avec des optimisations de performance, l'ajout de nouvelles fonctionnalités comme l'autoscaling et l'intégration de nouveaux services (SearXNG, Claude). Des corrections et améliorations ont également été apportées à Buildkit, Huginn et Token Bureau. Plusieurs applications ont été décommissionnées car leurs fonctionnalités sont désormais gérées par d'autres services.

### Évolutions fonctionnelles
- **Iterion:** Intégration de l'authentification OAuth pour ChatGPT, permettant une utilisation plus sécurisée et contrôlée. [#49](https://github.com/SocialGouv/infra-apps/issues/49)
- **Iterion:** Ajout d'un backend de recherche web souverain basé sur SearXNG.
- **Iterion:** Possibilité d'utiliser des sandboxes automatiques pour les exécutions, améliorant l'isolation et la sécurité.
- **Token Bureau:** Autorisation de l'accès en écriture aux projets V2 pour le CI d'egapro.
- **Buildkit Operator:** Amélioration de la gestion du cache S3 avec des politiques de cycle de vie pour optimiser le stockage.

### Évolutions techniques
- **Iterion:** Mise en place d'un autoscaler basé sur KEDA pour ajuster dynamiquement le nombre de runners en fonction de la charge.
- **Iterion:** Mise à jour du chart vers la version 0.50.0, incluant des corrections et des améliorations de performance.
- **Buildkit Operator:** Mises à jour régulières vers les versions 0.13.0, 0.14.2, 0.15.0, 0.16.0, 0.17.0, 0.18.0, 0.19.0, 0.20.0 et 0.21.0, apportant des optimisations et des corrections.
- **Huginn:** Décommissionnement du service, ses fonctionnalités étant désormais gérées par Iterion.
- **Buildkit Service:** Décommissionnement du service, les builds étant désormais gérés par l'opérateur Buildkit.
- **Kata:** Amélioration de la configuration pour une meilleure compatibilité avec Buildkit.
- **Metabase:** Augmentation des ressources allouées pour résoudre les problèmes de performance liés aux journaux WAL.
- **Secrets Policies:** Correction pour permettre la resynchronisation dans les namespaces adoptés par Rancher.

### Autres changements
- Documentation mise à jour concernant l'absence de token bearer pour Buildkit Operator.
- Nettoyage et simplification de la configuration de Kata.
- Correction de problèmes liés à l'OOMKilled sur les workers Iterion.
- Diverses corrections et améliorations de la configuration d'Iterion pour une meilleure stabilité et performance.
