## Changelog : iterion (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois-ci, iterion a franchi une étape majeure dans la sécurisation et la robustesse de l'exécution des agents IA. Les développements se sont concentrés sur l'isolation stricte des environnements d'exécution (sandboxing), la fiabilisation des connecteurs et une amélioration significative de l'accessibilité de l'interface Studio. L'accent a été mis sur la protection des secrets et le contrôle granulaire des ressources pour garantir des workflows d'agents plus sûrs et prévisibles.

### Évolutions fonctionnelles
- **Connecteurs & Intégrations** : Amélioration de la gestion des abonnements liés aux packages de connecteurs [#3334](https://github.com/SocialGouv/iterion/issues/3334) et mise en place d'un système de livraison vérifiée (ingress lane) pour sécuriser l'entrée des données [#3307](https://github.com/SocialGouv/iterion/issues/3307).
- **Interface Studio** : Mise en conformité majeure avec les normes d'accessibilité (RGAA), incluant une meilleure visibilité du focus, un étiquetage précis des formulaires et une amélioration de la lisibilité de la barre latérale [#2556](https://github.com/SocialGouv/iterion/issues/2556), [#2622](https://github.com/SocialGouv/iterion/issues/2622).
- **Expérience Agent (Revi/Claw)** : Amélioration du mode conversation de `revi` pour une meilleure isolation des outils utilisés et une meilleure transparence des rapports d'exécution [#3339](https://github.com/SocialGouv/iterion/issues/3339).
- **Gestion des ressources** : Introduction de mécanismes de contrôle des "usage windows" pour mieux gérer la durée de vie et les budgets des exécutions.

### Évolutions techniques
- **Sécurité & Isolation (Sandboxing)** : Renforcement massif de l'isolation des processus via gVisor et protection contre l'injection de variables d'environnement non autorisées via des fichiers `.env` [#3291](https://github.com/SocialGouv/iterion/issues/3291), [#3268](https://github.com/SocialGouv/iterion/issues/3268).
- **DSL & Codemode** : Introduction de l'attribut `codemode:` dans le langage de description (DSL) et amélioration du binding des outils pour les scripts exécutés [#3301](https://github.com/SocialGouv/iterion/issues/3301), [#3186](https://github.com/SocialGouv/iterion/issues/3186).
- **Infrastructure & CI/CD** : Optimisation de la chaîne de déploiement avec l'ajout de tests de conformité (vendor-check, mongo-conformance) [#3187](https://github.com/SocialGouv/iterion/issues/3187) et le partitionnement (sharding) des tests E2E pour accélérer les cycles de validation [#3007](https://github.com/SocialGouv/iterion/issues/3007).
- **Gestion des identités & Clés** : Amélioration de la gestion des pools de clés (key pools) et sécurisation de l'authentification par jetons d'équipe (team-tokens) [#3152](https://github.com/SocialGouv/iterion/issues/3152), [#3117](https://github.com/SocialGouv/iterion/issues/3117).
- **Architecture Connecteurs** : Refonte de la configuration des connecteurs via l'introduction de `triggers.yaml` pour définir précisément les modalités de lecture et de filtrage des livraisons [#3282](https://github.com/SocialGouv/iterion/issues/3282).

### Autres changements
- **Documentation** : Enrichissement important de la documentation technique via de nouveaux ADR (Architecture Decision Records) traitant de la sécurité des secrets et de la structure des connecteurs [#3301](https://github.com/SocialGouv/iterion/issues/3301), [#3277](https://github.com/SocialGouv/iterion/issues/3277).
- **Documentation** : Ajout de nouveaux diagrammes de base de données (ERD) et de flux de fonctionnalités pour faciliter la compréhension de l'architecture globale.
