## Changelog : territoires-en-transitions (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment autour des indicateurs et des audits. L'accent a été mis sur l'ergonomie, la gestion des données et la sécurité. L'importation de plans via IA a également progressé, avec des fonctionnalités de création, de suivi et de reprise. Des corrections de bugs et des optimisations de performance ont été apportées pour améliorer la stabilité et la réactivité de la plateforme.

### Évolutions fonctionnelles
- **Indicateurs :**
    - Ajout d'une grille de saisie tabulaire pour une édition plus efficace des données.
    - Possibilité de copier-coller des données dans la grille.
    - Affichage de l'impact en pourcentage de l'objectif dans la grille.
    - Gestion de l'affichage des données Open Data avec une pastille et un sélecteur.
    - Possibilité de modifier l'année de référence des indicateurs.
    - Amélioration de l'affichage et de la gestion des valeurs dans la grille.
- **Audits et Labellisation :**
    - Refonte de l'interface d'audit avec une nouvelle checklist et une gestion des documents améliorée.
    - Simplification du processus de demande d'audit.
    - Possibilité de remplacer le rapport d'audit.
    - Amélioration de la gestion des rôles et des permissions.
    - Ajout d'une archive des preuves d'audit téléchargeable.
    - Clôture d'audit en deux étapes avec une modale de confirmation.
- **Import IA :**
    - Intégration de l'importation de plans via IA avec création, suivi de progression et reprise.
    - Amélioration de la robustesse du parsing PDF lors de l'importation.
- **Référentiels :**
    - Amélioration de l'affichage des archives de preuves.
    - Possibilité de masquer les colonnes d'audit.
    - Affichage d'un bandeau pour les référentiels archivés ou en lecture seule.
- **Autres :**
    - Amélioration de la navigation et de l'ergonomie générale de l'interface.
    - Ajout de la possibilité de rechercher des actions.

### Évolutions techniques
- **Sécurité :**
    - Correction de failles de sécurité potentielles (IDOR, SSRF, phishing).
    - Renforcement de la sécurité des accès aux données.
    - Mise à jour des dépendances de sécurité.
- **Infrastructure :**
    - Mise à jour de Nx et des dépendances.
    - Amélioration des performances des tests CI/CD.
    - Optimisation de la configuration de l'environnement.
- **Code :**
    - Refactoring de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
    - Migration de modules vers le domaine `metrics`.
    - Suppression de code obsolète.
    - Utilisation de TypeScript pour une meilleure typage et détection d'erreurs.
- **Tests :**
    - Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
    - Amélioration de la couverture des tests.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs.
- Amélioration des messages d'erreur.
- Optimisation des performances.
- Mise à jour des libellés et des textes de l'interface utilisateur.
- Ajout de la gestion des thématiques SGPE dans le référentiel TE.
- Migration des tickets bugs/supports sur le SDK Notion 5.
- Ajout de la date de création des comptes dans crm-personnes-sync.
