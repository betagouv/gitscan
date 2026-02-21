## Changelog : hyyypertool (30 derniers jours)

### Résumé
Les dernières mises à jour de Hyyypertool améliorent la stabilité, la performance et l'expérience utilisateur de l'outil de modération. Des corrections de bugs ont été apportées, notamment concernant la pagination et la modération des membres. L'intégration de Sentry a été renforcée pour un meilleur suivi des erreurs et des performances. De plus, des améliorations ont été apportées à la gestion des domaines et des organisations.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la réinitialisation de la page lors d'une recherche sur les listes de domaines, d'organisations et d'utilisateurs. (#1408)
- Correction d'un bug lié à la modération des membres déjà liés. (#1405)
- Optimisation du filtrage des domaines gratuits et correction d'un problème d'affichage du tableau des domaines à vérifier. (#1404)
- Ajout d'un lien vers les EHPAD dans les actions d'investigation. (#1383)
- Ajout d'une section FranceConnect. (#1360)
- Possibilité de gérer les utilisateurs autorisés à utiliser l'outil. (#1307)

### Évolutions techniques
- Intégration complète de Sentry pour le suivi des erreurs, le profiling serveur et le SDK navigateur (Web Vitals, suivi des assets, temps de chargement des pages). (#1406)
- Suppression de dépendances inutiles pour Sentry. (#1407)
- Mise à jour de la version de Node utilisée pour l'application à la version 24. (#1410)
- Refactorisation du code pour supprimer l'ancienne logique de jointure forcée des organisations. (#1393)
- Amélioration de la robustesse des tests E2E en corrigeant un problème de fluctuation. (#1392)

### Autres changements
- Mise à jour de plusieurs dépendances (zod, @proconnect-gouv/proconnect.identite, pg, @preact/signals, etc.).
- Amélioration de la documentation et des exemples de commandes changeset.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour de la configuration de Tailwind.
- Formatage des fichiers Gherkin avec Prettier.
