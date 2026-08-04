## Changelog : buildkit-operator (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois a été marqué par une phase intensive de stabilisation et de sécurisation de l'infrastructure. Les efforts se sont concentrés sur la fiabilité des processus de build (pour éviter toute interruption en cours de travail), l'optimisation de la gestion du stockage (S3) et le renforcement de la sécurité des accès. L'outil est désormais plus flexible pour s'adapter à différents environnements Kubernetes.

### Évolutions fonctionnelles
- **Flexibilité de configuration** : Possibilité de personnaliser les valeurs par défaut pour les environnements cloud (Kubernetes générique) [#3](https://github.com/SocialGouv/buildkit-operator/issues/3).
- **Gestion des architectures** : Introduction d'une option pour fixer l'architecture des daemons via le `nodeSelector` (pinning) [#2](https://github.com/SocialGouv/buildkit-operator/issues/2).
- **Nouveaux paramètres Helm** : Ajout de la gestion du temps maximum de build (`maxBuildSeconds`) et du cycle de vie des buckets S3.
- **Configuration par projet** : Introduction de paramètres par défaut déclaratifs appliqués dès la création d'un projet.

### Évolutions techniques
- **Fiabilité et Résilience** : 
    - Amélioration majeure de la gestion du cycle de vie des daemons pour empêcher toute disparition ou interruption pendant un build (mécanismes de drainage avant mise à jour et protection lors des rollouts de la gateway).
    - Suivi précis des builds en cours via des entrées horodatées pour une meilleure gestion des états.
- **Optimisation du Stockage et du Cache** : 
    - Mise en place d'une nouvelle politique de "cache à froid" sur S3 (import systématique, export cadencé).
    - Limitation de la croissance automatique des volumes de cache et automatisation du nettoyage (GC) des buckets S3 (expiration et interruption des uploads multipartites).
    - Mise en œuvre d'un système de "keep-warm" adaptatif qui ajuste la période d'inactivité selon la cadence des builds.
- **Sécurité** : 
    - Durcissement de l'authentification en privilégiant OIDC et en supprimant la compatibilité avec les tokens en clair.
    - Renforcement des politiques de sécurité S3 et de la gestion de la taille des ressources (auto-grow/fork sizing) suite à des revues de sécurité.
- **Infrastructure et CI/CD** : 
    - Support étendu des architectures avec la publication d'images (buildd, companion, gateway) pour ARM64 et AMD64.
    - Automatisation de la gestion des tags de release.

### Autres changements
- **Documentation** : Mise à jour des guides concernant les valeurs Helm, les garanties de cycle de vie des daemons et les recommandations de configuration par projet.
