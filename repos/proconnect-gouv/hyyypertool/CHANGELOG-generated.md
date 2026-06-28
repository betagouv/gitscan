## Changelog : hyyypertool (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité et l'expérience utilisateur. L'accès aux fonctionnalités d'édition et de modification de données a été restreint aux utilisateurs autorisés (administrateurs et modérateurs).  Des améliorations ont également été apportées à la page utilisateur, notamment l'ajout de l'historique de connexion OIDC avec pagination, et des corrections mineures pour améliorer l'interface.

### Évolutions fonctionnelles
- Restriction de l'accès aux actions d'édition et de modification de données aux rôles administrateur et modérateur. [#1695](https://github.com/proconnect-gouv/hyyypertool/issues/1695)
- Affichage conditionnel de la section "Commentaires" : elle n'est visible que si des commentaires existent pour la modération concernée. [#1679](https://github.com/proconnect-gouv/hyyypertool/issues/1679)
- Pagination de l'historique de connexion OIDC sur la page utilisateur pour une meilleure lisibilité. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678)
- Affichage de l'historique de connexion OIDC sur la page utilisateur, incluant la date, le service et l'organisation. [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673)
- L'email des membres est désormais un lien vers leur profil utilisateur. [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653)
- Ajout des champs `end_user_reason` et `allow_editing` aux modérations. [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652)
- Correction d'une faute de frappe dans l'email automatisé. [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654)

### Évolutions techniques
- Remplacement des modals SSR par des "îles" Preact auto-contenues pour les modérations, améliorant potentiellement les performances et la maintenabilité. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- Mise à jour de la bibliothèque `@proconnect-gouv/proconnect.identite` dans le cadre de la migration vers une nouvelle version. [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651)
- Mise à jour des valeurs `acr` pour l'authentification. [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687)

### Autres changements
- Mises à jour de dépendances diverses (Cypress, oxc-parser, @csmith/release-it-calver-plugin, @preact/signals-core, rate-limiter-flexible, actions/checkout, @electric-sql/pglite, hono, type-fest, preact-render-to-string, tsx, @proconnect-gouv/proconnect.identite)
