## Changelog : territoires-en-transitions (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations sur la gestion des référentiels, notamment en préparation de la bascule vers le référentiel "Territoires en Transitions" (TE).  De nouvelles fonctionnalités ont été ajoutées pour la gestion des preuves, des indicateurs et des audits, avec une attention particulière portée à la sécurité et à l'expérience utilisateur. Des optimisations de performance et des refactorings techniques ont également été réalisés.

### Évolutions fonctionnelles
- **Gestion des référentiels :** Préparation de la bascule vers le référentiel TE avec ajout de jalons et de règles de migration.
- **Audits et labellisations :**
    - Amélioration de l'interface et du workflow d'audit, avec une nouvelle checklist et une gestion des documents simplifiée.
    - Possibilité pour l'auditeur de remplacer le rapport d'audit.
    - Gestion des permissions et des rôles affinée pour les différentes actions (lecture, modification, etc.).
    - Ajout d'un badge de statut d'audit sur l'onglet.
- **Indicateurs :**
    - Nouvelle grille de saisie tabulaire pour les indicateurs, avec édition en ligne et possibilité de collage de données.
    - Amélioration de la gestion des données open data et de leur affichage.
    - Possibilité de réordonner les colonnes et les lignes de la grille.
- **Sécurité :**
    - Correction de failles potentielles d'injection IDOR (Insecure Direct Object Reference) dans les plans et les discussions.
    - Validation des fichiers et des identifiants pour éviter les accès non autorisés.
- **Import IA :** Ajout de la fonctionnalité d'import de plans via l'IA, avec suivi de progression et reprise.
- **Plans :** Ajout de dates de début et de fin aux plans.

### Évolutions techniques
- **Refactoring :**
    - Migration vers le pattern `Result` pour une meilleure gestion des erreurs et des succès.
    - Refactorings importants du code lié aux indicateurs, aux audits et aux référentiels pour améliorer la maintenabilité et la performance.
    - Suppression de code obsolète et simplification de certaines structures de données.
- **Dépendances :**
    - Mise à jour de Next.js, TypeScript et d'autres dépendances.
- **CI/CD :**
    - Amélioration du pipeline CI/CD pour accélérer les tests et les déploiements.
    - Parallélisation des tests e2e.
- **Infrastructure :**
    - Mise à jour de la configuration de Content Security Policy (CSP).
    - Optimisation de la gestion des caches.
- **Base de données :** Suppression de l'implémentation RLS (Row-Level Security) de DatabaseService.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements techniques.
- **Tests :** Ajout de nouveaux tests unitaires et e2e pour garantir la qualité du code.
- **Divers :**
    - Amélioration de l'expérience utilisateur avec des corrections de bugs et des améliorations de l'interface.
    - Mise à jour des libellés et des textes pour une meilleure clarté.
    - Migration du système de création de tickets bugs/supports vers le SDK Notion 5.
    - Suppression de dépendances inutilisées.
    - Amélioration des performances générales de l'application.
