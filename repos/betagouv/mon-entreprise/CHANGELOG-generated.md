## Changelog : mon-entreprise (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la précision des calculs pour les auto-entrepreneurs, la refactorisation de la fiche de paie pour une meilleure maintenabilité et l'ajout de la fiche de paie pour les SASU. Des mises à jour de sécurité importantes ont également été appliquées pour corriger des vulnérabilités dans les dépendances du projet. Enfin, l'infrastructure CI/CD a été revue pour plus de clarté et de robustesse.

### Évolutions fonctionnelles
- **Fiche de paie SASU :** Ajout de la fiche de paie pour les Sociétés par Actions Simplifiées Unipersonnelles (SASU).
- **Calcul IR Auto-Entrepreneur :** Correction du calcul de l'Impôt sur le Revenu (IR) pour les auto-entrepreneurs [#4105](https://github.com/betagouv/mon-entreprise/issues/4105).
- **Questions Salarié :** Amélioration de la liste des questions posées aux salariés, avec correction de l'ordre et ajout de questions manquantes concernant les caisses de CP.
- **Modèle Social :** Suppression de questions inutiles dans le modèle social.
- **Améliorations générales de la fiche de paie :** Correction de fautes, refactorisation du code et amélioration de la présentation des informations (frais professionnels, salaire net).
- **Internationalisation (i18n) :** Correction des clés de traduction pour le salaire net en SASU et implémentation d'une base pour la traduction de la page d'accueil avec Next.js.

### Évolutions techniques
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Koa, happy-dom, handlebars, form-data, axios, protobufjs, storybook, @babel/traverse, cypress).
- **Refactorisation de la simulation :** Amélioration de la gestion des erreurs et de la réactivité lors de la saisie de données dans la simulation, notamment en cas de règles invalides.
- **Infrastructure CI/CD :** Refonte complète des workflows GitHub Actions pour une meilleure organisation et clarté (renommage des workflows, séparation des tests E2E, gestion des secrets).
- **Next.js :** Mise en place de Next.js 16 avec support de l'internationalisation (SSR).
- **Design System :** Restriction des types de données acceptés pour `errorMessage` et `description` dans le design system.

### Autres changements
- **Documentation :** Ajout de documentation pour la nouvelle fonctionnalité Next.js.
- **Nettoyage de code :** Suppression de code commenté et de fichiers inutiles.
- **Tests :** Suppression d'un test fragile et ajout de tests pour les nouvelles fonctionnalités.
- **Algolia :** Amélioration du pipeline de mise à jour des données Algolia.
- **Flake.nix :** Correction du fichier flake.nix.
