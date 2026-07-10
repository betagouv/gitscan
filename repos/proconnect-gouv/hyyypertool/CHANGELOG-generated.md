## Changelog : hyyypertool (30 derniers jours, au 2026-07-09)

### Résumé
Les récentes mises à jour de Hyyypertool améliorent l'expérience utilisateur en ajoutant des informations plus claires sur les organisations et les utilisateurs, notamment des badges de comptage et des sections repliables. Des restrictions d'accès ont été mises en place pour les utilisateurs non-administrateurs, et des corrections ont été apportées pour améliorer la convivialité et la sécurité.

### Évolutions fonctionnelles
- Ajout d'une colonne "Externe" avec un indicateur visuel (✅/❌) dans le tableau des organisations de la page utilisateur.
- Ajout de badges avec des émojis pour indiquer le nombre d'organisations, de modérations et de connexions OIDC sur la page utilisateur.
- Les sections d'organisations, de modérations et d'historique OIDC sur la page utilisateur sont maintenant repliables pour une meilleure lisibilité.
- Ajout d'une colonne "Type de vérification" dans le tableau des organisations.
- Possibilité d'éditer le motif de refus lors de la modération.
- Restriction de l'accès aux actions de modification et de traitement pour les utilisateurs non-administrateurs ou modérateurs.

### Évolutions techniques
- Extraction du composant d'actions sur les membres de la table d'organisation pour une réutilisation accrue.
- Mise à jour de plusieurs dépendances, incluant `tailwindcss`, `@csmith/release-it-calver-plugin`, `@types/node`, `oxc-parser`, `sentry`, `release-it`, `pg`, `docker/setup-compose-action`, `cypress-io/github-action`, `hono`, `@electric-sql/pglite`, `cypress`, `type-fest`, `@proconnect-gouv/proconnect.identite`, et `rate-limiter-flexible`.

### Autres changements
- Documentation mise à jour.
- Corrections mineures et améliorations de la qualité du code.
