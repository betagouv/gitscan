## Changelog : territoires-en-transitions (30 derniers jours, au 14 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des indicateurs, des audits et des référentiels. Des corrections de sécurité importantes ont été apportées, ainsi que des optimisations de performance et des refactorings techniques pour préparer les futures évolutions de la plateforme. L'importation de plans par IA est en cours de développement.

### Évolutions fonctionnelles
- **Indicateurs :**
    - Ajout d'une grille de saisie tabulaire pour une édition plus efficace des données.
    - Possibilité de copier-coller des données dans la grille.
    - Ajout d'une indication visuelle de la couverture des données open data.
    - Amélioration de la navigation et de l'édition des données.
- **Audits & Labellisations :**
    - Refonte de l'interface d'audit avec une nouvelle checklist et une gestion améliorée des documents.
    - Possibilité de remplacer le rapport d'audit.
    - Amélioration de la gestion des droits d'accès aux documents.
    - Ajout d'un bandeau d'information pour les audits clôturés.
- **Référentiels :**
    - Ajout d'un panneau d'archives pour les preuves.
    - Amélioration de la gestion des statuts et des actions.
    - Préparation de la bascule vers le nouveau référentiel TE.
- **Plans :**
    - Ajout de dates de début et de fin aux plans.
- **Sécurité :**
    - Correction de failles de sécurité potentielles (injection IDOR) dans les plans et les annexes.
    - Validation des fichiers et des identités pour prévenir les accès non autorisés.

### Évolutions techniques
- **Refactoring :**
    - Refactorings importants du code pour améliorer la maintenabilité et la performance.
    - Migration vers TypeScript 6/7.
    - Utilisation de `Result` pour une meilleure gestion des erreurs.
    - Suppression de code obsolète et simplification de l'architecture.
- **Infrastructure :**
    - Mise à jour des dépendances (Next.js, swc).
    - Amélioration de la configuration de la sécurité (CSP).
    - Optimisation des tests CI/CD (parallélisation, timeouts).
- **Autres :**
    - Migration vers un nouveau SDK Notion pour la gestion des tickets.
    - Amélioration de la gestion des dates et des fuseaux horaires.
    - Utilisation de `date-fns` au lieu de `luxon`.

### Autres changements
- Documentation mise à jour pour les nouvelles fonctionnalités et les changements d'architecture.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des logs et du monitoring.
