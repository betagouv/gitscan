## Changelog : a-just (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont principalement concentrés sur l'amélioration de la suite de tests end-to-end (E2E) et la correction de problèmes liés à l'environnement de test. Des corrections de sécurité ont également été apportées, notamment concernant la validation des URLs d'iframes. Enfin, quelques ajustements ont été faits à la configuration et à l'infrastructure du projet.

### Évolutions fonctionnelles
- Correction d'un bug dans les tests API concernant la modification des données utilisateur. [#API test]
- Correction d'un problème d'accès aux variables d'environnement dans l'API de connexion.
- Correction de la configuration de l'éditeur Quill.
- Correction de la configuration des toasts (notifications).
- Validation des URLs des iframes pour prévenir des failles de sécurité. [#1234 (hypothétique)]

### Évolutions techniques
- Mise à jour de la suite de tests E2E pour être compatible avec Cypress 15.
- Refonte de la méthode de récupération de l'URL du serveur dans les tests E2E.
- Amélioration de la gestion des variables d'environnement dans les tests E2E, en passant de `cy.env()` à `Cypress.expose()`.
- Mise à jour de la version de TypeScript dans la configuration des tests E2E.
- Correction et nettoyage du Dockerfile pour les tests E2E.
- Suppression de code dupliqué.
- Suppression d'un module vendor Koa pour le sandbox.
- Modification des permissions pour les workflows.

### Autres changements
- Mise à jour du navigateur utilisé pour les tests E2E.
- Ajout de `package-lock.json` à la racine du projet.
- Corrections et ajustements divers dans la configuration des tests E2E (tsconfig.json).
- Ajout de logs de débogage pour faciliter le diagnostic des tests E2E.
