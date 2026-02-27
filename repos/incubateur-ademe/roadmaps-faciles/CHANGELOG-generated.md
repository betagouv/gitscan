## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Le projet a connu une période d'évolution très active au cours des 30 derniers jours. De nouvelles fonctionnalités majeures ont été implémentées, notamment l'authentification à deux facteurs, l'intégration SSO, un éditeur Markdown enrichi avec gestion d'images, et la possibilité d'intégrer des roadmaps via iframe. L'infrastructure a également été améliorée avec un nouveau système de CI/CD et une meilleure gestion des tenants. De nombreuses améliorations de la documentation et de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un éditeur Markdown enrichi avec la possibilité de télécharger des images via S3 (#93).
- Implémentation de l'authentification à deux facteurs (2FA) via passkey, OTP et email (#61).
- Possibilité d'intégrer des roadmaps et des tableaux de bord via un mode iframe embarquable (#64).
- Ajout d'un système de feature flags accessible aux super-admins (#97).
- Refonte de la page de gestion des tenants avec une interface de type GitHub (#60).
- Ajout d'une page `/roadmap` pour le "dogfooding" (test interne) (#65).
- Ajout de la possibilité de créer des posts anonymes avec modération et suppression (#32).
- Ajout d'un journal d'audit pour suivre les actions des utilisateurs (#23).
- Ajout de la gestion des zones DNS (#92).
- Implémentation de l'internationalisation avec support du français et de l'anglais (#21).
- Ajout d'un rôle administrateur root, d'un profil utilisateur, d'un pont SSO et de la gestion des domaines personnalisés (#20).
- Ajout d'un connecteur pour synchroniser les données avec Notion (#94).
- Amélioration de la gestion des utilisateurs et des rôles, notamment pour les créateurs de tenants (#65).
- Ajout d'un système de redirection canonique via le domaine de la plateforme (#92).
- Ajout d'un tenant épinglé qui remplace la variable d'environnement `ROADMAP_TENANT_SUBDOMAIN` (#83).

### Évolutions techniques
- Mise en place d'un nouveau système de CI/CD basé sur GitHub Actions et Scalingo (#90, #89, #85).
- Refonte des emails avec le Design System de l'État (DSFR) et `react-email` (#58).
- Ajout d'une suite de tests complète avec Vitest et Playwright pour les tests E2E (#63).
- Amélioration de la configuration du build pour sécuriser les variables d'environnement (#81).
- Optimisation des jobs CI pour ne déclencher les tests que sur les fichiers modifiés (#80).
- Mise à jour des dépendances pour corriger des vulnérabilités (hono, lodash) (#79).
- Utilisation de `release-please` pour automatiser les releases (#86).
- Amélioration de la gestion des worktrees pour faciliter le développement parallèle (#62).
- Refonte de la structure des fichiers de documentation (#59).
- Correction de problèmes liés à l'initialisation du thème DSFR (#51, #53).
- Ajout d'un provider de tracking Sentry et PostHog (#98).
- Correction de problèmes de CSP pour les domaines PostHog (#5d99311).

### Autres changements
- Synchronisation de la documentation avec le stack documentation et ajout de règles de création d'issues GitHub (#244f9f3, #1bdb9a4).
- Refonte des captures d'écran dans la documentation pour les rendre compatibles avec le thème (#51faffd).
- Mise à jour du template GitHub (#54a85dc).
- Ajout de fichiers ADR (Architecture Decision Records) (#f753b27).
- Mise à jour du fichier `todo.md` (#6094a2e, #8680eda).
