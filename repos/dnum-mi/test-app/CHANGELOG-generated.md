## Changelog : test-app (30 derniers jours, au 2026-08-12)

### Résumé
Le projet a franchi une étape majeure avec le passage à la version 1.0.0. Les évolutions récentes se concentrent sur l'ajout de nouvelles fonctionnalités et une optimisation significative de l'automatisation, de la sécurité et de la gestion des ressources au sein de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- Ajout de nouvelles fonctionnalités (feat-001 à feat-005).
- ⚠️ **Changement majeur** : la fonctionnalité `feat-005` introduit des modifications de rupture (breaking changes).
- Résolution de divers bugs (fix-031 à fix-039).

### Évolutions techniques
- **CI/CD & Sécurité** :
    - Renforcement de la sécurité des workflows via l'authentification par GitHub App et l'application du principe de moindre privilège.
    - Mise en place d'un nettoyage automatique et planifié des caches et des images obsolètes.
    - Optimisation de l'automatisation du versioning (upgrade type auto) et de la synchronisation des branches.
    - Amélioration de la gestion de la concurrence dans les pipelines pour éviter les conflits.
- **Déploiement** :
    - Évolution de la gestion des charts Helm, incluant le support monorepo et le dispatch distant.

### Autres changements
- Automatisation des processus de release pour l'application et les charts Helm.
