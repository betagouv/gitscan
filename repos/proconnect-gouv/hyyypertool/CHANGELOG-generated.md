## Changelog : hyyypertool (30 derniers jours, au 2 juillet 2026)

### Résumé
Cette version apporte des améliorations de sécurité en restreignant l'accès aux actions sensibles aux seuls utilisateurs autorisés (administrateurs et modérateurs). L'interface utilisateur a également été améliorée avec l'ajout d'informations sur l'historique de connexion des utilisateurs et des badges d'informations sur les organisations et utilisateurs. Plusieurs corrections et optimisations ont été apportées, notamment au niveau de la gestion des commentaires et de l'affichage des informations.

### Évolutions fonctionnelles
- **Sécurité :** Restriction de l'accès en écriture à la base de données aux rôles administrateur et modérateur [#1695](https://github.com/proconnect-gouv/hyyypertool/issues/1695).
- **Interface utilisateur :** Masquage des actions d'édition et du bouton de retraitement pour les utilisateurs en lecture seule [#1696](https://github.com/proconnect-gouv/hyyypertool/issues/1696), [#1697](https://github.com/proconnect-gouv/hyyypertool/issues/1697).
- **Utilisateurs :** Affichage de l'historique de connexion OIDC sur la page utilisateur et pagination de cet historique [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673), [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678).
- **Commentaires :** La section des commentaires n'est affichée que s'il existe des commentaires pour une modération [#1679](https://github.com/proconnect-gouv/hyyypertool/issues/1679).
- **Informations :** Ajout de badges d'informations sur les organisations et utilisateurs [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672).
- **Modération :** Ajout des champs `end_user_reason` et `allow_editing` aux modérations [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652).
- **Email :** Correction d'une faute de frappe dans l'email automatisé [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654).
- **Profil utilisateur :** L'email du membre est désormais un lien vers son profil utilisateur [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653).

### Évolutions techniques
- **Refactoring :** Remplacement des modals SSR par des îles Preact autonomes pour la gestion des modérations [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627).
- **Dépendances :** Mise à jour de plusieurs dépendances (voir section "Autres changements").
- **Authentification :** Mise à jour des valeurs `acr` (assurance level) pour l'authentification [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687).

### Autres changements
- Mise à jour des dépendances :
    - `cypress` (dans `/e2e`)
    - `oxc-parser`
    - `@electric-sql/pglite`
    - `@csmith/release-it-calver-plugin`
    - `@preact/signals-core`
    - `tailwindcss`
    - `@happy-dom/global-registrator`
    - `ts-dedent`
    - `sentry`
    - `hono`
    - `@proconnect-gouv/proconnect.identite.database`
    - `@proconnect-gouv/proconnect.identite`
    - `preact-render-to-string`
    - `tsx`
    - `actions/checkout`
    - `rate-limiter-flexible`
    - `type-fest`
- Publication des versions : 2026.6.8, 2026.6.7, 2026.6.6, 2026.6.5, 2026.6.4, 2026.6.2, 2026.6.1.
