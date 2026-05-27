## Changelog : territoires-en-transitions (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des actions et des référentiels. Des refactorings importants ont été réalisés pour optimiser le code et préparer le terrain pour de futures fonctionnalités. L'accent a également été mis sur la correction de bugs et l'amélioration de la performance.

### Évolutions fonctionnelles
- **Gestion des actions :**
    - Possibilité d'éditer directement les actions dans un tableau.
    - Ajout d'un menu contextuel pour les actions du tableau, remplaçant le bouton de suppression.
    - Amélioration du filtrage des actions (par priorité et statut).
    - Ouverture des actions depuis le tableau, avec indication si l'action est privée.
- **Référentiels :**
    - Amélioration de l'interface pour la création et la gestion des audits.
    - Génération asynchrone d'archives ZIP des preuves d'audit.
    - Simplification de la vue checklist pour démarrer un audit.
    - Ajout d'une modale pour demander un audit.
    - Migration du tableau de bord EDL vers une nouvelle structure de données.
- **Collectivités :**
    - Ajout d'un type de structure "sans statut juridique".
    - Correction du filtre par niveau de labellisation TE.
- **Site web :**
    - Nouvelle page "Plateforme numérique" avec FAQ.
    - Améliorations visuelles et de la hiérarchie des titres sur différentes pages.
    - Ajout d'une page publique "matrice d'impact".
- **Autres :**
    - Amélioration de la gestion des fichiers dans les formulaires d'import.
    - Amélioration de la synchronisation Calendly/Airtable.
    - Correction de bugs liés à l'affichage des badges de statut et de priorité.

### Évolutions techniques
- **Refactoring :**
    - Suppression de fichiers et de symboles exportés inutilisés dans divers packages.
    - Migration de plusieurs endpoints vers tRPC pour améliorer la performance et la sécurité.
    - Remplacement de composants dépréciés.
    - Rationalisation du code et suppression de duplications.
    - Migration des labels JSX vers un catalogue centralisé.
- **Infrastructure :**
    - Mise à jour des dépendances.
    - Amélioration de la configuration CI/CD.
    - Optimisation des index de la base de données.
- **Tests :**
    - Ajout et mise à jour de tests unitaires et E2E.
    - Correction de tests existants.

### Autres changements
- Documentation mise à jour pour la création de client_id/client_secret.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de suivi PostHog pour certaines actions utilisateurs.
- Suppression de code obsolète.
- Correction de typos et amélioration de la lisibilité du code.
