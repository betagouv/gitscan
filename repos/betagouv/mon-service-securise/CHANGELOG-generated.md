## Changelog : mon-service-securise (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des risques, notamment avec l'introduction des risques v2 et l'ajout de tests d'accessibilité pour garantir une meilleure expérience utilisateur. Des corrections et des optimisations ont également été apportées à l'interface utilisateur et aux processus de déploiement.

### Évolutions fonctionnelles
- Ajout de la gestion des risques v2, incluant l'affichage des risques spécifiques, la possibilité de les modifier et de les supprimer.
- Implémentation d'un tiroir pour la gestion des risques v2 avec affichage des mesures associées.
- Possibilité de refuser une demande d'homologation et gestion des dossiers refusés (affichage, archivage, notifications).
- Amélioration de l'affichage des informations sur les services, incluant le nom du service dans l'en-tête et les indices cyber.
- Ajout d'une fonctionnalité d'export CSV des risques v1.
- Ajout d'une question supplémentaire de validation lors de l'homologation.
- Affichage d'un message de confirmation lors d'un refus d'homologation.

### Évolutions techniques
- Mise en place de tests d'accessibilité avec Playwright et Axe pour améliorer l'inclusivité du service.
- Publication des rapports d'accessibilité dans Mattermost.
- Refonte de l'architecture du menu de navigation avec un composant Svelte.
- Conversion de plusieurs composants en TypeScript pour une meilleure typage et maintenabilité.
- Optimisation des workflows de déploiement Clever Cloud.
- Mise à jour de nombreuses dépendances (Express, PostgreSQL, Svelte, Vite, etc.).
- Amélioration de la gestion des feature flags.
- Suppression de code obsolète et refactoring de certains composants.

### Autres changements
- Amélioration de la documentation et des commentaires.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur (espacement, typographie, etc.).
- Ajout de badges et d'infobulles pour une meilleure clarté.
- Correction de problèmes de 404 sur les pages de risques v2 et de création de compte.
- Ajout d'un retry sur la recherche d'entreprise.
- Amélioration de la gestion des erreurs et des exceptions.
