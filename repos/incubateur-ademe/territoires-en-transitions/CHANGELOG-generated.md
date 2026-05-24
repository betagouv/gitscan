## Changelog : territoires-en-transitions (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'édition et de la visualisation des données dans les référentiels. Des optimisations ont été apportées à la gestion des audits, des plans et des collectivité, ainsi que des corrections de bugs et des refactorings techniques pour une meilleure performance et maintenabilité du code. L'ajout de nouvelles fonctionnalités comme la personnalisation des référentiels et la matrice d'impact renforcent l'utilité de la plateforme.

### Évolutions fonctionnelles
- **Référentiels :**
    - Possibilité de générer une archive ZIP des preuves d'audit (backend).
    - Simplification de la vue checklist pour démarrer un audit.
    - Ajout d'une modale pour demander un audit.
    - Amélioration de l'affichage du tableau de bord EDL.
    - Vue tabulaire éditable des référentiels.
    - Réservation de la génération d'archive de preuves aux auditeurs.
- **Collectivités :**
    - Ajout d'un type de structure sans statut juridique.
    - Correction du filtre par niveau de labellisation TE.
    - Migration des endpoints vers tRPC pour une meilleure performance.
- **Plans :**
    - Migration des mutations de fiche vers tRPC.
    - Amélioration de la gestion des imports de plans.
    - Suppression de la complétion d'actions dans un plan (simplification de l'interface).
- **Interface utilisateur :**
    - Amélioration de l'espacement des badges de taille "sm".
    - Correction de l'affichage des options de menu en mode mobile.
    - Ajout de la page publique matrice d'impact.
    - Amélioration de l'édition de texte riche dans les tableaux.
- **Personnalisation :**
    - Implémentation de la personnalisation des référentiels avec des questions et réponses, et un bandeau intégré aux pages des sous-mesures.
- **Autres :**
    - Amélioration de la synchronisation Calendly/Airtable.
    - Correction de typos et amélioration de la hiérarchie des titres sur le site public.

### Évolutions techniques
- **Refactoring :**
    - Migration de nombreux labels JSX vers un catalogue centralisé (`appLabels`).
    - Migration de plusieurs endpoints SQL vers tRPC pour améliorer la performance et la cohérence.
    - Suppression de code inutilisé et simplification de certaines fonctions.
- **Tests :**
    - Suppression de tests Cypress dépréciés.
    - Ajout de tests unitaires et E2E pour les nouvelles fonctionnalités.
    - Amélioration de l'isolation et de la parallélisation des tests.
- **Infrastructure :**
    - Mise à jour de la configuration Tailwind.
    - Amélioration de la gestion des backups et restores (staging).
    - Ajout d'index sur les tables d'historique pour optimiser les requêtes.
- **Performance :**
    - Optimisation de l'import de plans.
    - Débounce des RichTextEditor pour réduire les appels au serveur.

### Autres changements
- Documentation de la création de `client_id/client_secret` via curl.
- Ajout de suivi Posthog sur la visualisation des référentiels par utilisateur.
- Mise à jour de l'adresse d'envoi d'email.
- Ajout de metadata pour la nouvelle page plateforme du site.
- Suppression de fichiers et dossiers inutilisés.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout d'un système de bannière pour remplacer Stonly.
