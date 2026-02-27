## Changelog : hyyypertool (30 derniers jours)

### Résumé
Les dernières mises à jour de Hyyypertool se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière d'accessibilité et de notifications. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'outil, et des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance. L'intégration de Sentry a été améliorée pour un suivi plus précis des erreurs.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité des tableaux avec des liens d'ancrage appropriés et une navigation au clavier.
- Ajout de détails d'erreur dans les notifications, avec une section repliable pour plus d'informations.
- Correction d'un bug empêchant le chargement du script de débogage htmx en préproduction.
- Correction d'un bug lié à la disparition du tableau des domaines après actualisation et optimisation du filtrage des domaines libres.
- Correction d'un bug sur la modération des membres déjà liés.
- Ajout d'une section FranceConnect.
- Possibilité de définir une liste d'utilisateurs autorisés.

### Évolutions techniques
- Intégration de Sentry pour une initialisation précoce via `--import`, ajout du profiling et du SDK navigateur.
- Mise à jour de plusieurs dépendances : `@gouvfr/dsfr`, `zod`, `@preact/signals`, `pg`, `cypress`, `sentry`, `tailwindcss`, `dotenv`, `@happy-dom/global-registrator`, `type-fest`, `@proconnect-gouv/proconnect.identite`, `@proconnect-gouv/proconnect.identite.database`, `hono`, `hono-sessions`, `openid-client`, `release-it`, `prettier`, `oxc-parser`, `cypress-io/github-action`.
- Correction d'un problème de version de Node utilisé pour l'exécution.
- Amélioration de la gestion des scripts d'îlots Preact lors des échanges de contenu HTMX.
- Suppression d'une dépendance inutile pour `@sentry/profiling-node`.
- Suppression d'un workflow legacy de jointure d'organisation.
- Correction de la gestion des statuts de modération inconnus.
- Mise en place de tests E2E pour la validation des membres externes avec notification et domaine.
- Utilisation de fast-check pour une couverture de tests plus large.

### Autres changements
- Mise à jour de la politique de sécurité et ajout de directives de signalement.
- Mise à jour de la documentation pour refléter les changements apportés.
- Correction de la configuration de la commande changeset.
- Amélioration des tests unitaires pour les URLs hx.
- Suppression de l'extension `chunked-transfer` qui provoquait des erreurs.
- Correction de l'ordre de chargement du script `htmx-ext-debug`.
- Ajout de tests E2E pour la validation des membres externes avec notification et domaine.
- Correction d'un problème de permissions et de comportement d'exécution planifié du workflow de déforestation.
