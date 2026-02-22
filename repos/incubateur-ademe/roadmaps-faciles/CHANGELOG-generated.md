## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Le projet a connu une période d'activité intense, avec de nombreuses améliorations axées sur la sécurité, l'expérience utilisateur et les fonctionnalités d'administration. L'ajout de l'authentification à deux facteurs, la refonte de la gestion des tenants et l'implémentation d'un système d'audit log sont des avancées majeures. Des améliorations significatives ont également été apportées à la documentation et aux tests.

### Évolutions fonctionnelles
- Ajout d'une page `/roadmap` pour le "dogfooding" (test interne) (#49, #65).
- Implémentation d'un mode iframe embarquable pour les boards et la roadmap, permettant de les intégrer facilement sur d'autres sites (#50, #64).
- Refonte de la page `/tenant` avec une nouvelle interface utilisateur inspirée de GitHub et un formulaire simplifié (#60).
- Ajout de la possibilité de créer des posts anonymes, avec des fonctionnalités de modération et de suppression (#32).
- Implémentation de l'authentification à deux facteurs (2FA) via passkey, OTP et email, ainsi que l'intégration SSO OAuth pour les tenants (#61).
- Ajout d'un site de documentation utilisateur avec Fumadocs (#57).
- Ajout d'une vue liste compacte des posts sur le board (#55).
- Le tenant épinglé remplace désormais la variable d'environnement `ROADMAP_TENANT_SUBDOMAIN` (#83).
- Amélioration de l'héritage des droits pour le super admin et le créateur de tenant (#69).

### Évolutions techniques
- Suite complète de tests avec Vitest et Playwright pour les tests E2E (#63).
- Refonte des emails avec le Design System de l'État (DSFR) et la librairie `react-email` (#58).
- Mise en place d'un système d'audit log et d'observabilité (#23).
- Ajout de la gestion des zones DNS (#69).
- Implémentation de l'internationalisation avec `next-intl` (français et anglais) (#21).
- Amélioration de la configuration du build pour supprimer `NODE_ENV` des fichiers `.env` et sécuriser le script (#70, #81).
- Optimisation du CI pour ne déclencher les tests qu'en cas de modifications pertinentes (#80).
- Filtrage des jobs CI par fichiers modifiés (#73).
- Mise en place d'un "worktree" pour faciliter le développement avec des sessions Claude parallèles (#62).
- Correction de vulnérabilités identifiées par Dependabot (hono, lodash) (#79).
- Correction d'un problème d'affichage des checkboxes avec le thème DSFR (#56).
- Ajout de `StartDsfrOnHydration` dans le root layout pour une meilleure intégration du DSFR (#51, #53).

### Autres changements
- Synchronisation de la documentation `CLAUDE.md` et `README` avec la documentation principale (#82).
- Refonte des screenshots pour refléter le thème actuel et audit de la documentation (#82).
- Ajout de règles de création d'issues GitHub (#83).
- Mise à jour du modèle GitHub (#54).
- Nettoyage des composants MDX, du layout Fumadocs et de la navigation (#59).
- Mise à jour du fichier `todo.md` (#78, #68).
- Ajout de fichiers ADR (Architecture Decision Records) (#18).
- Correction de bugs mineurs et améliorations de la qualité du code.
