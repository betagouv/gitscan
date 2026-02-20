## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de la plateforme, notamment en matière de sécurité avec l'ajout de l'authentification à deux facteurs, d'administration avec la gestion des tenants et des utilisateurs, et de fonctionnalités pour les utilisateurs finaux comme l'embarquement de roadmaps via iframe et la page de roadmap. De plus, une documentation utilisateur a été ajoutée et les tests ont été renforcés.

### Évolutions fonctionnelles
- **Authentification :** Ajout de l'authentification à deux facteurs (passkey/OTP/email) et intégration de l'authentification SSO pour les tenants (#61).
- **Roadmap :** Création d'une page de roadmap accessible pour le "dogfooding" (test interne) (#49, #65).
- **Embarquement :** Possibilité d'intégrer des boards et des roadmaps via un mode iframe embarquable (#50, #64).
- **Tenants :** Refonte de la page de gestion des tenants avec une présentation de type GitHub et un formulaire simplifié (#60).
- **Posts :** Ajout de la possibilité de créer des posts anonymes, avec modération et suppression (#32).
- **Documentation :** Ajout d'un site de documentation utilisateur avec Fumadocs (#57).
- **Interface :** Correction d'un bug d'affichage de la checkbox de thème (#56).
- **Vue des posts :** Ajout d'une vue liste compacte des posts sur le board (#55).

### Évolutions techniques
- **Tests :** Implémentation d'une suite de tests complète avec Vitest et Playwright pour les tests E2E (#63).
- **Emails :** Refonte des emails avec le Design System de l'État (DSFR) et l'utilisation de `react-email` (#58).
- **Internationalisation :** Ajout de la gestion de l'internationalisation avec `next-intl` (français et anglais) (#21).
- **Architecture :** Ajout d'un provider DNS (#9d6e96c).
- **Administration :** Implémentation de l'administration root, du profil utilisateur, d'un pont SSO et de la gestion des domaines personnalisés (#20).
- **Audit :** Ajout d'un audit log et de l'observabilité (#23).
- **Tooling :** Mise en place d'un tooling worktree pour des sessions parallèles avec Claude (#62).
- **DSFR :** Correction de l'initialisation du DSFR lors de l'hydratation (#51, #53).

### Autres changements
- Mise à jour du template GitHub (#54a85dc).
- Synchronisation de la liste des tâches avec les tickets GitHub et mise à jour du fichier `todo.md` (#8680eda, #6094a2e).
- Nettoyage des composants MDX, du layout Fumadocs et de la navigation (#0570f4f).
- Ajout de fichiers ADR (Architectural Decision Records) (#f753b27).
- Documentation du workflow, de Git, de GitHub et renforcement de la sécurité (#1f3f804).
