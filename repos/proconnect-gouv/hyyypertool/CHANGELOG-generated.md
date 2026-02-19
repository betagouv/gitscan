## Changelog : hyyypertool (30 derniers jours)

### Résumé
Les dernières mises à jour de hyyypertool améliorent la stabilité et la performance de l'outil de modération, notamment au niveau de la recherche et de la gestion des domaines. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, et l'intégration de Sentry a été renforcée pour une meilleure surveillance des erreurs. Des améliorations ont également été apportées à la gestion des utilisateurs et des organisations.

### Évolutions fonctionnelles
- Ajout d'un lien de recherche annuaire EHPAD sur la fiche modération (#1383).
- Amélioration du filtrage des domaines gratuits et correction du rafraîchissement du tableau des domaines à vérifier (#1404).
- Correction d'un bug empêchant la modération des membres déjà liés (#1405).
- Correction d'un bug qui empêchait le tableau des domaines de s'afficher correctement après un rafraîchissement (#1404).
- Ajout d'un filtre pour rechercher les modérations par modérateur (#1393).
- Correction d'un bug lié à la restauration de l'action "vérifié par une coopérative de médiation numérique" (#1369).
- Amélioration de la lisibilité de la section commentaire avec des niveaux d'opacité (#1317).
- Correction d'un bug d'affichage de l'icône d'oeil avec les cases à cocher associées (#1316).

### Évolutions techniques
- Intégration précoce de Sentry avec initialisation via `--import`, ajout du profiling et du SDK navigateur (#1406).
- Suppression de dépendances inutiles pour `@sentry/profiling-node` (#1407).
- Mise à jour de plusieurs dépendances : `@proconnect-gouv/proconnect.identite`, `type-fest`, `openid-client`, `pg`, `@preact/signals`, `@happy-dom/global-registrator`, `dotenv`, `@preact/signals-core`, `drizzle-kit`, `oxc-parser`, `@types/bun`, `preact`, `cypress`, `release-it`, `prettier-plugin-organize-imports`, `ts-pattern`, `oven-sh/setup-bun`, `cypress-io/github-action`.
- Correction du comportement du workflow de deforestation et de son exécution planifiée (#1364).
- Suppression du code legacy lié à la jointure forcée d'organisations (#1393).
- Amélioration de la robustesse des tests E2E avec correction d'un problème de flakiness lié aux notifications (#1392).
- Mise à jour de la configuration Tailwind CSS (#1380).
- Utilisation de classes utilitaires DSFR pour la taille des icônes (#1317).
- Correction d'un problème lié à l'exportation dupliquée dans Bun (#1356).

### Autres changements
- Documentation : Mise à jour de la documentation pour refléter le format de la commande changeset (#1358, #1363).
- Diverses corrections et améliorations de la configuration du CI/CD.
- Mise à jour des fichiers de release notes (#1371).
- Passage de la branche principale à `main` (#142b402).
