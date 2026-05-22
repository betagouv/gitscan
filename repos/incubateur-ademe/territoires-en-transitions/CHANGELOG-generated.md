## Changelog : territoires-en-transitions (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des référentiels, des plans et des fiches action, avec un accent particulier sur la personnalisation et l'édition en ligne. Des optimisations techniques ont été apportées pour améliorer la performance et la robustesse de la plateforme, notamment en migrant des fonctionnalités vers tRPC et en améliorant les tests.

### Évolutions fonctionnelles

*   **Référentiels :**
    *   Possibilité de demander un audit via une nouvelle modale. [#1234](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1234)
    *   Génération asynchrone d'archives ZIP des preuves d'audit (backend).
    *   Simplification de la vue checklist pour démarrer un audit.
    *   Réservation de la génération d'archive de preuves aux auditeurs.
    *   Exposition de l'ID de l'action dans le mapping du suivi d'audit.
*   **Plans :**
    *   Amélioration de la gestion des utilisateurs/tags lors de l'import de plans.
    *   Optimisation de l'import de plans et sécurisation de la création de fiches.
    *   Migration des mutations de fiche de Supabase vers tRPC.
    *   Possibilité pour les contributeurs pilotes de créer, modifier et supprimer des sous-actions.
*   **Fiches Action :**
    *   Nouvelle interface pour la personnalisation des fiches action, incluant des questions et une interface de réponse.
    *   Possibilité d'ajouter des documents à une fiche action via un nouveau point tRPC.
    *   Amélioration de l'édition en ligne avec des composants Select et RichTextEditor plus performants et intégrés.
    *   Ajout de la dernière note dans les rapports.
    *   Remplacement des verbes de placeholder par l'infinitif dans la nouvelle fiche action.
*   **Collectivités :**
    *   Ajout d'une structure sans statut juridique pour les collectivités.
    *   Correction du filtre par niveau de labellisation TE.
    *   Correction de la recherche de collectivités.
*   **Site Web :**
    *   Nouvelle page "Plateforme numérique" avec FAQ et informations mises à jour.
    *   Mise à jour de la page "Programme".
    *   Ajout d'une page publique "Matrice d'impact".

### Évolutions techniques

*   **Architecture :**
    *   Migration de nombreux endpoints vers tRPC pour améliorer la performance et la sécurité.
    *   Suppression de fonctions et vues SQL inutilisées.
*   **Frontend :**
    *   Migration des labels JSX vers un catalogue centralisé pour une meilleure maintenabilité.
    *   Utilisation des composants du Design System (DS) pour une cohérence visuelle accrue.
    *   Amélioration des composants Select, Checkbox et Table pour une meilleure expérience utilisateur.
*   **Tests :**
    *   Amélioration de l'isolation et de la parallélisation des tests.
    *   Ajout de tests E2E pour couvrir les nouvelles fonctionnalités.
*   **Infrastructure :**
    *   Mise à jour de la configuration Tailwind.
    *   Amélioration de la gestion des backups et de la restauration de l'environnement de staging.
    *   Mise à jour de l'adresse d'envoi d'emails.

### Autres changements

*   Ajout d'événements PostHog pour le suivi des imports de plans.
*   Mise à jour de la documentation.
*   Nettoyage du code et suppression de fichiers inutilisés.
*   Correction de typos et amélioration de la lisibilité du code.
*   Amélioration de la synchronisation Calendly Airtable.
*   Mise à jour des dépendances.
*   Ajout d'index sur les tables d'historique pour améliorer la performance des requêtes.
*   Correction de bugs mineurs et améliorations de la stabilité.
