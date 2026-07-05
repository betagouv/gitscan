## Changelog : hyyypertool (30 derniers jours, au 2 juillet 2026)

### Résumé
Cette version apporte des améliorations de sécurité en restreignant l'accès aux actions sensibles aux seuls utilisateurs autorisés (administrateurs et modérateurs). L'interface utilisateur a également été améliorée avec l'ajout d'informations sur les caractéristiques des organisations et des utilisateurs, ainsi que la pagination de l'historique de connexion OIDC. Des corrections et optimisations diverses ont également été apportées.

### Évolutions fonctionnelles
- Restriction de l'accès en écriture à la base de données aux rôles administrateur et modérateur. [#1695](https://github.com/proconnect-gouv/hyyypertool/issues/1695)
- Masquage des actions d'édition (suppression, réinitialisation) pour les utilisateurs en lecture seule. [#1697](https://github.com/proconnect-gouv/hyyypertool/issues/1697) et [#1696](https://github.com/proconnect-gouv/hyyypertool/issues/1696)
- Masquage du bouton "Retraiter" pour les utilisateurs en lecture seule.
- Pagination de l'historique de connexion OIDC sur la page utilisateur. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678)
- Affichage conditionnel de la section "Commentaires" uniquement si des commentaires existent. [#1679](https://github.com/proconnect-gouv/hyyypertool/issues/1679)
- Ajout de badges d'informations sur les caractéristiques des organisations et des utilisateurs. [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672)

### Évolutions techniques
- Remplacement des modals SSR par des "Preact islands" auto-contenues pour les modérations. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- Mise à jour de plusieurs dépendances : `@proconnect-gouv/proconnect.identite.database`, `hono`, `rate-limiter-flexible`, `actions/checkout`, `@preact/signals`, `tsx`, etc.
- Mise à jour de la version de `@electric-sql/pglite`. [#1691](https://github.com/proconnect-gouv/hyyypertool/issues/1691) et [#1543](https://github.com/proconnect-gouv/hyyypertool/issues/1543)

### Autres changements
- Mise à jour de la documentation et des configurations pour refléter les changements.
- Corrections mineures et optimisations diverses.
- Mises à jour des plugins de release (release-it-calver-plugin).
- Mises à jour de Cypress et des actions Github.
