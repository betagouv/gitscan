## Changelog : mon-entreprise (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des fiches de paie et des simulations, ainsi que sur la correction de bugs et l'optimisation de la sécurité du projet. Des efforts importants ont également été réalisés pour moderniser les dépendances et améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout de la fiche de paie pour les entrepreneurs individuels (SASU) avec calcul des cotisations et de la rémunération.
- Amélioration de la gestion des questions dans le parcours salarié, avec correction de l'ordre et ajout de questions manquantes.
- Ajout d'un avertissement spécifique pour Mayotte concernant les cotisations sociales.
- Prise en compte des cotisations mahoraises dans les calculs.
- Affichage d'un message d'erreur en cas de date de cessation d'activité invalide.
- Possibilité de rendre les messages d'information dismissibles (fermetures manuelles).
- Ajout d'un bandeau de notification pour indiquer que le simulateur est en version bêta.
- Amélioration de la présentation des frais professionnels dans la fiche de paie.
- Correction de la règle LODEOM pour une meilleure précision des calculs.
- Correction de la gestion du revenu cotisé pour la retraite de base à Mayotte.
- Ajout de la cotisation Apec pour les Sasu.

### Évolutions techniques
- Mise à jour de nombreuses dépendances pour corriger des vulnérabilités de sécurité (koa, handlebars, form-data, axios, storybook, etc.).
- Refactor de la gestion du thème (dark mode) avec utilisation de cookies et intégration via Next.js headers.
- Amélioration de la gestion des fonts avec Next.js font/local et utilisation de variables CSS.
- Refactor de la gestion de l'i18n (internationalisation) avec branchement de react-i18next côté client.
- Optimisation de la gestion des erreurs dans la simulation, avec une meilleure identification et gestion des règles invalides.
- Amélioration de la structure du code et suppression de code inutile.
- Utilisation de TypeScript pour améliorer la robustesse et la maintenabilité du code.
- Factorisation de la configuration i18n pour le serveur et le client.
- Renommage de fichiers pour éviter les erreurs de compilation avec SWC.

### Autres changements
- Correction de typos et améliorations de la documentation.
- Amélioration des couleurs des composants (Button, Message, Chip, Tag) pour une meilleure accessibilité.
- Suppression de code commenté inutile.
- Correction de l'affichage de la date sélectionnée par défaut.
- Amélioration de l'accessibilité avec l'ajout d'un rôle "status" à un composant.
- Mise à jour du guide IRCEC pour les artistes-auteurs.
- Correction de la description de l'IRCEC pour les artistes-auteurs.
