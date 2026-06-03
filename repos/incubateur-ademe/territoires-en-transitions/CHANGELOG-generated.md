## Changelog : territoires-en-transitions (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la refactorisation du code pour une meilleure maintenabilité et performance, ainsi que l'ajout de nouvelles fonctionnalités pour faciliter la gestion des référentiels et des audits. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment au niveau des tableaux et des formulaires.

### Évolutions fonctionnelles
- Ajout d'une page publique pour la matrice d'impact.
- Possibilité de demander un audit directement depuis l'interface.
- Amélioration de la gestion des annexes des fiches action avec un nouveau point trpc pour l'ajout de documents.
- Vue tabulaire éditable des actions dans les référentiels.
- Amélioration de la gestion des statuts et priorités des actions dans les tableaux.
- Simplification de la vue checklist pour démarrer un audit.
- Ajout d'une page "mesure désactivée" pour une meilleure gestion des personnalisations.
- Amélioration de la synchronisation Calendly Airtable.
- Possibilité de filtrer les mesures désactivées par la personnalisation.
- Ajout d'un bandeau pour basculer vers la nouvelle vue de labellisation.
- Correction de la consommation des invitations et du feedback d'erreur.
- Correction du filtre par niveau de labellisation TE dans les collectivités.
- Correction de l'affichage du graph de comparaison d'audit.
- Correction de l'enregistrement des explications d'action lors de la navigation.

### Évolutions techniques
- Refactorisation importante du code, notamment migration vers tRPC pour plusieurs fonctionnalités (ressources, historique des référentiels, PDF export, etc.).
- Consolidation des libellés JSX vers un fichier centralisé `appLabels` pour une meilleure cohérence et maintenabilité.
- Suppression de code obsolète et de dépendances inutilisées.
- Migration des tests Storybook vers Vitest.
- Amélioration de la configuration CI/CD (restriction des permissions du token GITHUB_TOKEN, suppression de workflows inutilisés).
- Mise à jour de Playwright pour corriger un problème d'installation.
- Amélioration de la robustesse des tests, notamment pour l'import de spreadsheets et l'envoi de mails.
- Utilisation du backend pour le filtrage des mesures désactivées par la personnalisation.
- Amélioration de la gestion des erreurs et des validations.
- Correction de problèmes de sécurité (injection SQL, contrôle d'accès horizontal).
- Amélioration de la performance de l'import de plans.

### Autres changements
- Documentation de la création de `client_id/client_secret` via curl.
- Mise à jour de la configuration Tailwind.
- Ajout de métriques de suivi (PostHog) pour l'import de plans.
- Correction de typos et amélioration de la lisibilité du code.
- Amélioration des types TypeScript.
- Ajout de fixtures pour les tests.
- Mise à jour des dépendances.
- Amélioration de la gestion des fichiers et des assets Strapi.
- Suppression de la partie front liée à la complétion des actions dans un plan.
- Modification pour remplacer les stats d'usage par des stats d'impacts et de résultats.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
