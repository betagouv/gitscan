## Changelog : api-engagement (30 derniers jours)

### Résumé
Cette période a été marquée par une amélioration significative de la stabilité et de la performance de l'API et des applications associées. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, notamment en matière d'accessibilité et de gestion des missions. Des refactorings importants ont été réalisés pour optimiser le code et préparer l'infrastructure pour l'avenir, notamment en passant à Node 24 et en améliorant la gestion des index de la base de données.

### Évolutions fonctionnelles

- Ajout d'un bouton "événements en direct" sur les listes de campagnes et de widgets (#809).
- Amélioration de l'accessibilité avec l'utilisation d'éléments de bouton sémantiques (#771).
- Ajout de l'ID de l'éditeur comme préfixe d'URL (#807).
- Affichage de l'adresse de la mission lors de la modération (#814).
- Correction d'un bug empêchant le refus automatique des missions en modération (#813).
- Correction de l'affichage des organisations dans l'application (#778).
- Amélioration de la gestion des missions désactivées et réactivées (#783).
- Correction d'un bug de déconnexion pour l'utilisateur "my-missions" (#799).
- Ajout de la possibilité de définir la taille maximale de l'espace mémoire pour le widget (#794).
- Correction de l'affichage du nom de la ville et de l'organisation dans le widget (#761).

### Évolutions techniques

- Mise à jour de Node.js vers la version 24 (#802).
- Refactorisation de la logique d'agrégation des widgets (#790).
- Amélioration de la gestion des exceptions et ajout de logs Sentry (#797).
- Ajout d'un middleware dédié pour l'analyse des requêtes (#800).
- Ajout d'un index partiel sur la table `mission` pour optimiser les requêtes de recherche géographique (#806).
- Refactorisation des modèles d'analyse (#751, #782).
- Migration des activités de mission vers une table de jointure N-N (#757).
- Suppression de l'utilisation de MongoDB (#761).
- Amélioration de la gestion des requêtes de recherche avec `ilike` (#788).
- Ajout de tests d'intégration pour les endpoints du widget (#750).
- Ajout d'un header `request-id` avec support Sentry (#780).
- Amélioration de la configuration des conteneurs du widget (#786).
- Ajout de tracing pour le widget dans Sentry (#756).
- Refactorisation de la gestion des règles de recherche optimisées (#782).
- Ajout de migrations Prisma pendant le workflow CI (#804).
- Correction d'un problème de mismatch du client Prisma (#801).

### Autres changements

- Mise à jour des dépendances (express, @types/express, next, @sentry/cli, @next/eslint-plugin-next, etc.).
- Amélioration des logs et instrumentation du widget (#792).
- Suppression de la tâche `letudiant` (#210e6e4).
- Ajout d'alias pour simplifier les imports (#2bdc525).
- Suppression de messages Sentry inutiles (#729).
- Correction de l'optimisation des images dans le widget (#793).
- Suppression de vues matérielles obsolètes (#772).
- Ajout de workflows Claude pour la revue de code (#717).
- Mise à jour de la librairie `react-datepicker` (#728).
- Amélioration de la gestion des erreurs dans les jobs (#790).
- Ajout de tests E2E pour le SDK jstag.js (#715).
