## Changelog : a-just (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la suite de tests end-to-end (E2E) et la correction de problèmes liés à la configuration de l'environnement de test. Des améliorations de sécurité ont également été apportées en validant les URL des iframes. Enfin, des ajustements ont été faits concernant l'utilisation de librairies externes et les permissions des workflows.

### Évolutions fonctionnelles
- **Sécurité :** Validation des URL des iframes pour prévenir les attaques potentielles via des URL non autorisées [#1234](https://github.com/betagouv/a-just/issues/1234).
- **Tests E2E :** Correction d'un test API concernant la modification des données utilisateur.

### Évolutions techniques
- **Tests E2E :**
    - Mise à jour de la méthode de récupération de l'URL du serveur dans les tests E2E.
    - Migration de `cy.env()` vers `Cypress.expose()` pour la gestion de l'environnement de test.
    - Mise à jour de la version de TypeScript dans la configuration des tests E2E.
    - Correction de la configuration du fichier `tsconfig.json` pour les tests E2E.
    - Mise à jour du navigateur utilisé pour les tests E2E.
    - Amélioration de la gestion des variables d'environnement dans les tests E2E.
- **Infrastructure :** Correction du Dockerfile pour les tests E2E et suppression de commentaires inutiles.
- **Librairies :** Suppression d'une librairie externe (`koa-smart`) pour renforcer la sécurité.
- **CI/CD:** Modification des permissions des workflows.

### Autres changements
- Suppression de code dupliqué.
- Ajout de `package-lock.json` à la racine du projet.
- Correction de l'accès aux variables d'environnement dans l'API de connexion.
- Suppression de types inutiles dans les fichiers `package.json`.
- Ajout de logs de débogage pour faciliter l'identification des problèmes dans les tests E2E.
