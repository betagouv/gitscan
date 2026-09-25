## Changelog : metabase-datasource-sync (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois marque le lancement de la première version fonctionnelle du réconciliateur de sources de données. L'outil est désormais capable de synchroniser les connexions Metabase et intègre des fonctionnalités essentielles pour un déploiement stable en environnement Kubernetes, notamment via des sondes de santé et une gestion corrigée des secrets.

### Évolutions fonctionnelles
- **Nouveauté** : Mise en service du réconciliateur de sources de données Metabase.
- **Monitoring** : Ajout d'une sonde de santé (`--liveness`) intégrée au binaire pour permettre un pilotage efficace par Kubernetes.
- **Correction** : Résolution d'un problème de lecture des secrets Kubernetes (gestion des liens symboliques) qui empêchait le fonctionnement correct en cluster.

### Évolutions techniques
- **Environnement de développement** : Mise en place d'un socle de développement standardisé utilisant Devbox et Taskfile [#1](https://github.com/SocialGouv/metabase-datasource-sync/pull/1).
- **Qualité et Tests** : Implémentation de tests d'acceptation complets s'exécutant contre de véritables instances Metabase et PostgreSQL.
- **Fiabilité du Build** : Stabilisation du processus de compilation (alignement des versions Cargo.lock/Cargo.toml et gestion des builds `--locked`) et initialisation des workflows de CI/CD.

### Autres changements
- **Documentation** : Mise à jour du README pour rendre le dépôt prêt pour une publication publique.
