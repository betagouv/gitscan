## Changelog : territoires-en-transitions (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des audits, l'import de plans d'action (notamment via Excel), la sécurisation de l'application et l'amélioration de l'expérience utilisateur sur la plateforme, en particulier au niveau de l'édition et de la visualisation des données. Des refactorings importants ont également été réalisés pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- **Audits :**
    - Possibilité de verrouiller les preuves de labellisation une fois l'audit validé.
    - Limitation des preuves de l'archive au référentiel de l'audit.
    - Conservation du rôle auditeur pendant 15 jours après la clôture de l'audit.
    - Ajout d'une modale de clôture d'audit en deux étapes.
    - Autorisation pour les utilisateurs ADEME à lire les preuves stockées.
    - Ajout d'une fonctionnalité pour demander un audit.
- **Import de plans d'action :**
    - Amélioration du processus d'import de plans d'action, avec une gestion plus robuste des fichiers Excel et une meilleure validation des données.
    - Extraction structurée des actions à partir de différents formats de fichiers (PDF, CSV, Excel).
    - Mise en place d'un workflow d'import asynchrone avec plusieurs étapes (scoring, consolidation, enrichissement).
- **Sécurité :**
    - Correction de plusieurs vulnérabilités de sécurité identifiées lors de tests d'intrusion (injection SQL, phishing, SSRF).
    - Renforcement des contrôles d'accès pour protéger les données sensibles.
- **Interface utilisateur :**
    - Amélioration de l'affichage des badges d'audit et des indicateurs.
    - Refonte de la page "Toutes les actions" avec une vue tabulaire éditable.
    - Amélioration de l'expérience utilisateur pour la gestion des sous-mesures.
    - Ajout de la possibilité de filtrer les mesures désactivées par la personnalisation.
    - Amélioration de la gestion des champs de formulaire (RichTextEditor).
    - Nouvelle page "Plateforme numérique" sur le site web.
    - Amélioration de la gestion des états ouverts/fermés des sections dans la page d'une mesure.

### Évolutions techniques
- **Refactoring :**
    - Migration des labels JSX vers un système centralisé pour une meilleure maintenabilité.
    - Refactorisation du code lié à l'import de plans d'action pour une meilleure structure et une plus grande clarté.
    - Suppression de code obsolète et de dépendances inutiles.
    - Amélioration de la gestion des types et des interfaces.
- **Infrastructure :**
    - Mise à jour des dépendances (Next.js, eslint-config-next).
    - Amélioration de la configuration CI/CD.
- **Tests :**
    - Ajout de nouveaux tests unitaires et E2E pour garantir la qualité du code.
    - Migration des tests Storybook vers Vitest.
- **Base de données :**
    - Optimisation des requêtes SQL.
    - Ajout de nouvelles colonnes et index pour améliorer les performances.

### Autres changements
- Mise à jour de la documentation.
- Amélioration des messages de log.
- Correction de bugs mineurs.
- Ajout de fixtures pour les tests.
- Amélioration de la configuration de l'environnement.
