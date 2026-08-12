## Changelog : buildkit-operator (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la stabilité du système, suite à des revues de sécurité approfondies. Les utilisateurs bénéficient désormais d'une plus grande flexibilité de configuration (gestion du cloud, de l'architecture et des paramètres par projet) et d'une gestion plus robuste des ressources pour éviter toute interruption de build lors des mises à jour.

### Évolutions fonctionnelles
- Délivrance automatique de certificats clients dans les namespaces consommateurs [#20](https://github.com/SocialGouv/buildkit-operator/issues/20).
- Flexibilité accrue de la configuration :
    - Gestion configurable des paramètres par défaut pour le cloud [#3](https://github.com/SocialGouv/buildkit-operator/issues/3).
    - Possibilité de verrouiller la sélection de nœuds par architecture (daemonScheduling.pinArch) [#2](https://github.com/SocialGouv/buildkit-operator/issues/2).
    - Définition de paramètres par défaut déclaratifs lors de la création de projets.
- Ajout de la possibilité de configurer la durée maximale des builds via le chart Helm (`maxBuildSeconds`).

### Évolutions techniques
- **Sécurité et conformité** : 
    - Durcissement des rôles RBAC [#19](https://github.com/SocialGouv/buildkit-operator/issues/19).
    - Sécurisation des politiques de cache S3 et de la croissance automatique des volumes.
    - Migration vers une authentification basée exclusivement sur OIDC (suppression de la compatibilité avec les tokens en clair).
- **Fiabilité et cycle de vie** : 
    - Amélioration de la gestion des mises à jour pour prévenir l'interruption des builds (drainage des daemons avant le remplacement des pods, protection contre la disparition des ressources pendant un build).
    - Meilleure traçabilité des builds en cours via un suivi par horodatage.
- **Optimisation des performances et du stockage** : 
    - Mise en place d'une politique de "keep-warm" adaptative pour les daemons selon la cadence des builds.
    - Nouvelle gestion du cache froid sur S3 (import systématique et export cadencé).
    - Mise en œuvre d'un nettoyage automatique (GC) des buckets S3 via des jobs de hook.
- **Infrastructure et CI/CD** : 
    - Publication d'images multi-architectures (amd64 et arm64) pour les composants buildd, companion et gateway.

### Autres changements
- Mise à jour de la documentation concernant les valeurs Helm, les garanties de cycle de vie des daemons et les options d'authentification.
