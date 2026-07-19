## Changelog : fondation (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte architecturale majeure de l'interface utilisateur vers une approche "feature-first", améliorant ainsi la maintenabilité et l'évolutivité du projet. Des améliorations ont également été apportées à la gestion des fichiers, à l'expérience utilisateur autour des observations et des nominations, ainsi qu'à la sécurité des dépendances.

### Évolutions fonctionnelles
- Ajout d'un bouton "+" pour ajouter des observations dans la liste des observations ([#497](https://github.com/betagouv/fondation/issues/497)).
- Possibilité de joindre des fichiers aux nominations ([#407](https://github.com/betagouv/fondation/issues/407)).
- Amélioration de la gestion des dates d'audition des magistrats ([#463](https://github.com/betagouv/fondation/issues/463)).
- Refonte de l'affichage des observations des magistrats, avec un panneau latéral dédié ([#474](https://github.com/betagouv/fondation/issues/474), [#451](https://github.com/betagouv/fondation/issues/451)).
- Suppression du modal de rappel pour le suivi des observations lors de la définition d'un résultat ([#493](https://github.com/betagouv/fondation/issues/493)).
- Amélioration de la sélection des fichiers agenda ([#478](https://github.com/betagouv/fondation/issues/478)).
- Ajout d'un point d'accès d'autorisation M2M pour les magistrats ([#502](https://github.com/betagouv/fondation/issues/502)).

### Évolutions techniques
- Migration des tests vers Vitest ([#437](https://github.com/betagouv/fondation/issues/437)).
- Refonte de l'architecture frontend vers une approche "feature-first" pour une meilleure organisation et maintenabilité du code.
- Internalisation de plusieurs enums et types partagés pour réduire les dépendances externes et améliorer la cohérence du code.
- Mise à jour de Prisma vers la version 7 ([#481](https://github.com/betagouv/fondation/issues/481)).
- Mise à jour de TypeScript vers la version 6 ([#480](https://github.com/betagouv/fondation/issues/480)).
- Suppression de code obsolète et de dépendances inutilisées.
- Amélioration de la gestion du cache pour optimiser les performances.
- Déploiement de Storybook sur Scalingo ([#477](https://github.com/betagouv/fondation/issues/477)).
- Mise en place de contrôles OpenAPI pour garantir la cohérence entre l'API et sa documentation.

### Autres changements
- Documentation : Ajout d'un ADR (Architecture Decision Record) pour la nouvelle architecture frontend.
- Correction d'un problème lié à l'appel d'un script supprimé lors du build sur Scalingo ([#501](https://github.com/betagouv/fondation/issues/501)).
- Amélioration de la gestion des couleurs en utilisant les tokens DSFR.
- Mise à jour de plusieurs dépendances (zod, oxfmt, oxlint, @faker-js/faker, @hey-api/openapi-ts, piscina, react, vite) pour corriger des failles de sécurité et bénéficier des dernières améliorations.
