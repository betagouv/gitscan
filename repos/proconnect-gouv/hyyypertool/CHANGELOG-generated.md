## Changelog : hyyypertool (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur et la gestion des accès. Des restrictions ont été ajoutées pour limiter l'écriture en base de données aux rôles d'administrateur et de modérateur. L'interface utilisateur a été améliorée avec l'ajout de l'historique de connexion OIDC sur la page utilisateur et des badges de caractéristiques sur les fiches organisation. Des corrections et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'outil.

### Évolutions fonctionnelles
- **Sécurité :** Restriction des écritures en base de données aux rôles d'administrateur et de modérateur. [#1695](https://github.com/proconnect-gouv/hyyypertool/issues/1695)
- **Utilisateurs :** Affichage de l'historique de connexion OIDC (avec pagination) sur la page utilisateur. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678) et [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673)
- **Organisations & Utilisateurs :** Ajout de badges de caractéristiques (type de service public, statut de diffusion, activité, etc.) sur les fiches organisation et utilisateur. [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672)
- **Modération :** Ajout des champs "raison de refus" et "autorisation de modification" aux modérations. [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652)
- **Modération :** Correction d'une faute de frappe dans l'email automatique. [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654)
- **Utilisateurs :** Le mail des membres est désormais un lien vers le profil utilisateur. [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653)
- **Interface :** Masquage de la section commentaires si aucun commentaire n'est présent. [#1679](https://github.com/proconnect-gouv/hyyypertool/issues/1679)

### Évolutions techniques
- **Architecture :** Remplacement des modals SSR par des îles Preact auto-contenues pour les modérations. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- **Dépendances :** Mise à jour de plusieurs dépendances (voir section "Autres changements").
- **Authentification :** Mise à jour des valeurs `acr` pour l'authentification. [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687)
- **Base de données :** Ajout de la colonne `end_user_reason` à la table `response_templates`. [#1632](https://github.com/proconnect-gouv/hyyypertool/issues/1632)
- **Bibliothèques :** Mise à niveau de `@proconnect-gouv/proconnect.identite`. [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651)

### Autres changements
- Mises à jour de dépendances : `@preact/signals`, `rate-limiter-flexible`, `actions/checkout`, `@electric-sql/pglite`, `hono`, `@proconnect-gouv/proconnect.identite.database`, `sentry`, `tsx`, `@types/bun`, `docker/setup-compose-action`, `openid-client`, `tailwind-merge`, `@preact/signals-core`, `zod`, `prettier-plugin-gherkin`, `jose`, `@hono/zod-validator`, `@hono/node-server`, `pg`, `preact`.
- Publication des versions : 2026.6.0, 2026.6.1, 2026.6.2, 2026.6.3, 2026.6.4, 2026.6.5, 2026.6.6.
