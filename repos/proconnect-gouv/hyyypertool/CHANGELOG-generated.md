## Changelog : hyyypertool (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la fiche utilisateur avec l'ajout de l'historique de connexion OIDC et la pagination de celui-ci. Des améliorations ont également été apportées à l'affichage des informations sur les organisations avec l'ajout de badges de caractéristiques. Plusieurs mises à jour de dépendances et corrections mineures ont également été intégrées pour assurer la stabilité et la sécurité de l'outil.

### Évolutions fonctionnelles
- **Fiche utilisateur :** Ajout de l'historique de connexion OIDC, permettant de visualiser les connexions aux services ProConnect pour chaque utilisateur [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673).
- **Fiche utilisateur :** Pagination de l'historique de connexion OIDC pour une meilleure lisibilité et performance [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678).
- **Fiche organisation et utilisateur :** Ajout de badges de caractéristiques pour une identification rapide des informations clés [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672).
- **Modération :** Remplacement des modals SSR par des "islands" Preact pour une meilleure performance et maintenabilité [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627).
- **Modération :** Ajout des champs "raison de refus" et "autorisation de modification" aux modérations [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652).
- **Email :** Correction d'une faute de frappe dans l'email automatisé [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654).
- **Profil utilisateur :** Le courriel du membre est désormais un lien vers son profil [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653).
- **Raison de refus :** Ajout d'un champ "raison de refus" pour les utilisateurs [#1628](https://github.com/proconnect-gouv/hyyypertool/issues/1628).

### Évolutions techniques
- **Authentification :** Mise à jour des valeurs ACR (Action Claim Request) [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687).
- **Rate Limit :** Ajout d'une variable d'environnement `RATE_LIMIT_POINTS` avec une valeur par défaut de 120 [#1626](https://github.com/proconnect-gouv/hyyypertool/issues/1626).
- **Dépendances :** Mise à jour de plusieurs dépendances (voir section "Autres changements").

### Autres changements
- Mises à jour de dépendances :
    - `tsx` (4.21.0 -> 4.22.4)
    - `@proconnect-gouv/proconnect.identite.database`
    - `@electric-sql/pglite`
    - `oxc-parser`
    - `type-fest`
    - `@proconnect-gouv/proconnect.identite` (8.1.0 -> 9.1.3)
    - `@hono/node-server` (2.0.1 -> 2.0.4)
    - `@preact/signals`
    - `@types/bun`
    - `docker/setup-compose-action`
    - `jose`
    - `@hono/zod-validator`
    - `preact`
    - `openid-client`
    - `tailwindcss`
    - `@preact/signals-core`
    - `zod`
    - `prettier-plugin-gherkin`
    - `cypress`
    - `sentry` (plusieurs mises à jour)
- Corrections et améliorations diverses du code.
