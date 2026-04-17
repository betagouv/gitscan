## Changelog : proconnect-identite (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et de la performance de ProConnect Identité. Des corrections de fuites mémoire et des optimisations ont été apportées. De plus, des mises à jour de dépendances ont été réalisées pour assurer la sécurité et la compatibilité du système. Des améliorations ont également été apportées à la gestion des annuaires d'entreprises et à la logique de détermination des petites structures.

### Évolutions fonctionnelles
- Ajout de routes de ping pour les services externes, améliorant la surveillance de la disponibilité du service.
- Publication du package `annuaire_entreprises`, rendant les fonctionnalités associées accessibles.
- Amélioration de l'algorithme de détermination des "petites associations" pour une meilleure précision.
- Correction d'un problème empêchant la configuration de l'authentification à deux facteurs (2FA).
- Ajout du champ "tranche-effectifs-unite-legale" à l'index pour une meilleure gestion des informations sur les effectifs.

### Évolutions techniques
- Correction d'une fuite mémoire dans la gestion des requêtes HTTP, améliorant la stabilité du service.
- Remplacement de l'utilisation de `axios` par `fetch` (puis rétablissement d'axios suite à des problèmes), optimisant la gestion des requêtes réseau.
- Mise à jour de la base image Node.js vers la version 24-slim pour une meilleure sécurité et performance.
- Refactorisation de l'utilisation des repositories de l'API entreprise pour une meilleure organisation du code.
- Suppression de tables temporaires inutiles lors de la création de dumps.
- Remplacement de l'importation directe d'axios par une utilisation plus modulaire.
- Simplification du typage de la fonction `isPublicService`.
- Rendre les dépendances peer optionnelles dans le package `identite`.

### Autres changements
- Mises à jour de plusieurs dépendances : `hono`, `nodemailer`, `vite`, `cypress`, `sentry`, `drizzle-orm`, `path-to-regexp`, `brace-expansion`, `picomatch`, `dotenvx`, `lodash-es`, `follow-redirects`.
- Ajout de tests unitaires et d'intégration pour valider les corrections et les nouvelles fonctionnalités.
- Amélioration de la documentation interne et des commentaires dans le code.
- Nettoyage du code et suppression de code obsolète.
- Ajout de changements pour la gestion des versions des packages.
- Suppression d'instructions `it.only` résiduelles dans les tests Cypress.
