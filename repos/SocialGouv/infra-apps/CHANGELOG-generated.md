## Changelog : infra-apps (30 derniers jours, au 01 août 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la plateforme Iterion, avec des optimisations de performance, l'ajout de nouvelles fonctionnalités comme l'authentification OAuth et l'intégration de nouveaux outils comme KEDA pour l'autoscaling. Des améliorations ont également été apportées à la sécurité et à la gestion des secrets, ainsi que des corrections de bugs et des mises à jour de l'infrastructure.

### Évolutions fonctionnelles
- **Iterion:** Ajout de l'authentification OAuth pour les SDK tiers en production. [#49](https://github.com/SocialGouv/infra-apps/issues/49)
- **Iterion:** Intégration de l'accès à Claude Code via OAuth sur le runner, remplaçant une clé API obsolète.
- **Token Bureau:** Autorisation pour l'intégration continue d'Egapro à écrire sur les projets de l'organisation V2.
- **Iterion:** Possibilité de configurer le type de sandbox par défaut pour les runners.
- **Iterion:** Ajout d'un backend de recherche web souverain basé sur SearXNG.
- **Iterion:** Amélioration de la gestion des erreurs OOMKilled pour le web-scrape.
- **Huginn:** Correction du tri des événements RSS pour afficher les plus récents en premier.

### Évolutions techniques
- **Buildkit Operator:** Décommissionnement du service Buildkit, tout étant désormais géré par l'opérateur.
- **Huginn:** Décommissionnement de Huginn, la veille étant désormais gérée par Iterion.
- **Buildkit Operator:** Mises à jour multiples de l'opérateur Buildkit (v0.13.0, v0.14.2, v0.15.0, v0.16.0, v0.17.0, v0.18.0, v0.19.0, v0.20.0, v0.21.0) avec des améliorations de performance, de configuration et de gestion du cache S3.
- **Iterion:** Mise à jour du chart Iterion (0.33.0, 0.34.0, 0.35.0, 0.37.2, 0.50.0) avec diverses corrections et améliorations.
- **KEDA:** Intégration de l'opérateur KEDA pour l'autoscaling du runner Iterion en fonction de la profondeur de la queue.
- **Metabase:** Rotation de la clé de signature statique pour l'intégration.
- **Secrets Policies:** Correction pour permettre la resynchronisation sur les namespaces adoptés par Rancher.
- **Kata:** Déploiement de Kata dans l'espace de noms `buildkit-system` et activation de virtiofsd xattr pour améliorer le hachage du contenu dans les VM fork.
- **Iterion:** Amélioration de la gestion des erreurs de montage NFS sur le runner.

### Autres changements
- Documentation mise à jour concernant l'accès aux tokens et la configuration de l'opérateur Buildkit.
- Suppression de la configuration MB_ENABLE_EMBEDDING pour Metabase.
- Suppression du suivi des sous-charts empaquetés localement.
- Nettoyage et refactoring du code.
- Suppression de la configuration ITERION_RUNNER_CONCURRENCY.
- Suppression de l'ancienne clé API OpenAI pour Iterion.
- Suppression de la configuration ANTHROPIC_API_KEY.
- Désactivation des fonctionnalités IA de Metabase.
- Mise à jour de la version de Metabase (v0.63.2) sur tous les instances.
- Correction pour servir le certificat renouvelé pour Metabase.
- Ajustement des ressources CPU et stockage pour Metabase après une panne de WAL-full en production.
- Suppression du runner NFS build-cache sur ovh-prod pour éviter les blocages.
