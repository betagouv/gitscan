## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une refonte majeure de l'application, avec l'ajout de nombreuses nouvelles fonctionnalités et améliorations significatives.  Nous avons notamment amélioré l'authentification, l'intégration avec Notion, la gestion des tenants, et ajouté des outils pour faciliter le développement et le déploiement. L'expérience utilisateur a également été améliorée avec une nouvelle interface et des correctifs de bugs.

### Évolutions fonctionnelles
- Ajout d'un mode embarquable (iframe) pour les tableaux de bord et les roadmaps, permettant de les intégrer facilement dans d'autres applications. [#64](https://github.com/incubateur-ademe/roadmaps-faciles/issues/64)
- Refonte de la page des tenants avec une nouvelle interface utilisateur inspirée de GitHub. [#60](https://github.com/incubateur-ademe/roadmaps-faciles/issues/60)
- Amélioration de l'intégration avec Notion, avec une synchronisation bidirectionnelle des données. [#94](https://github.com/incubateur-ademe/roadmaps-faciles/issues/94)
- Ajout de la possibilité de créer des posts anonymes, avec des fonctionnalités de modération et de suppression. [#32](https://github.com/incubateur-ademe/roadmaps-faciles/issues/32)
- Ajout d'une vue liste compacte des posts sur le tableau de bord. [#55](https://github.com/incubateur-ademe/roadmaps-faciles/issues/55)
- Ajout d'un système de feature flags pour les super-admins. [#97](https://github.com/incubateur-ademe/roadmaps-faciles/issues/97)
- Amélioration de l'expérience utilisateur du wizard d'intégration. [#103](https://github.com/incubateur-ademe/roadmaps-faciles/issues/103)
- Ajout d'un système d'audit log et d'observabilité. [#23](https://github.com/incubateur-ademe/roadmaps-faciles/issues/23)
- Ajout de la gestion des domaines personnalisés (DNS). [#92](https://github.com/incubateur-ademe/roadmaps-faciles/issues/92)
- Ajout de l'internationalisation (français et anglais). [#21](https://github.com/incubateur-ademe/roadmaps-faciles/issues/21)
- Ajout de l'authentification à deux facteurs (2FA) avec passkey, OTP et email. [#61](https://github.com/incubateur-ademe/roadmaps-faciles/issues/61)
- Refonte des emails avec DSFR Mail et react-email. [#58](https://github.com/incubateur-ademe/roadmaps-faciles/issues/58)

### Évolutions techniques
- Mise en place d'un système de CI/CD basé sur GitHub Actions et Scalingo. [#90](https://github.com/incubateur-ademe/roadmaps-faciles/issues/90)
- Ajout d'une suite de tests complète avec Vitest et Playwright (tests E2E). [#63](https://github.com/incubateur-ademe/roadmaps-faciles/issues/63)
- Refonte de l'architecture d'authentification avec SSO OAuth pour les tenants. [#61](https://github.com/incubateur-ademe/roadmaps-faciles/issues/61)
- Mise à jour de la bibliothèque d'interface utilisateur avec shadcn/ui et une nouvelle palette de couleurs (French Blue). [#104](https://github.com/incubateur-ademe/roadmaps-faciles/issues/104)
- Amélioration de la sécurité avec l'ajout de Sentry pour la gestion des erreurs et PostHog pour le suivi des utilisateurs. [#98](https://github.com/incubateur-ademe/roadmaps-faciles/issues/98)
- Utilisation de release-please pour la gestion des releases. [#86](https://github.com/incubateur-ademe/roadmaps-faciles/issues/86)
- Mise en place d'un workflow de travail avec worktrees pour les sessions de développement parallèles. [#62](https://github.com/incubateur-ademe/roadmaps-faciles/issues/62)
- Correction de vulnérabilités identifiées par Dependabot. [#79](https://github.com/incubateur-ademe/roadmaps-faciles/issues/79)

### Autres changements
- Mise à jour de la documentation avec Fumadocs et synchronisation avec le README. [#57](https://github.com/incubateur-ademe/roadmaps-faciles/issues/57) [#59](https://github.com/incubateur-ademe/roadmaps-faciles/issues/59)
- Ajout de règles de création d'issues GitHub. [#83](https://github.com/incubateur-ademe/roadmaps-faciles/issues/83)
- Mise à jour des dépendances et des outils de développement.
- Corrections de bugs et améliorations de la qualité du code.
- Amélioration du script de build pour plus de sécurité. [#81](https://github.com/incubateur-ademe/roadmaps-faciles/issues/81)
- Optimisation des jobs CI pour ne déclencher les tests que sur les fichiers modifiés. [#80](https://github.com/incubateur-ademe/roadmaps-faciles/issues/80)
- Mise à jour du template GitHub. [#54](https://github.com/incubateur-ademe/roadmaps-faciles/issues/54)
