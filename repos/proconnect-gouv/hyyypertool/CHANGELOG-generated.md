## Changelog : hyyypertool (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout du mode sombre, des améliorations de l'interface et des corrections de bugs. Des améliorations techniques ont également été apportées, notamment la suppression de dépendances obsolètes et l'optimisation du cache. L'outil de gestion des réponses a été enrichi avec des fonctionnalités d'édition et de suppression.

### Évolutions fonctionnelles
- Ajout du mode sombre pour une meilleure lisibilité et un confort visuel accru.
- Possibilité de filtrer les modérations par statut de décision (accepté, rejeté, réouvert).
- Ajout d'une action de suppression pour les modèles de réponse.
- Possibilité d'éditer les modèles de réponse directement dans l'interface.
- Amélioration de l'interface utilisateur des modèles de réponse (tri alphabétique, taille du titre).
- Correction d'un bug empêchant l'affichage correct de la liste des responsables.
- Correction d'un bug lié au seed des modèles de réponse, assurant que tous les modèles sont correctement chargés.
- Suppression de l'affichage des prénoms et noms dans les emails de rejet.
- Correction d'un bug empêchant l'envoi correct de l'en-tête de cache pour les ressources statiques.
- Amélioration de l'accessibilité et de la lisibilité avec l'ajout d'accents manquants.
- Ajout de la possibilité de trier les colonnes dans la liste des modérations.

### Évolutions techniques
- Suppression des mocks pour les services `entreprise.api.gouv.fr`, `api.crisp.chat`, `agentconnect` et `support.etalab.gouv.fr`, remplacés par des routes de développement.
- Mise à jour de plusieurs dépendances : `hono`, `preact`, `drizzle-kit`, `jose`, `actions/upload-artifact`, `drizzle-orm`, `cypress`, `tailwindcss`, `sentry`, `@proconnect-gouv/proconnect.identite`, `@preact/signals`, `@csmith/release-it-calver-plugin`, `@types/bun`, `prettier-plugin-tailwindcss`, `type-fest`, `youch`.
- Correction d'un problème empêchant le middleware de cache d'ajouter l'en-tête `Cache-Control`.
- Amélioration de la gestion du nonce pour l'auto-chargement depuis le contexte de la requête.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et corrections.
- Nettoyage du code et suppression de code obsolète.
- Corrections mineures de style et d'interface utilisateur.
