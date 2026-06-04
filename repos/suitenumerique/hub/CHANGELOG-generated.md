## Changelog : hub (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son interface utilisateur avec l'introduction d'une nouvelle application frontend basée sur Next.js et TypeScript. Cette refonte inclut une fonctionnalité de chat avec gestion des conversations, des threads, des réactions et un panneau d'outils pour la gestion des documents. L'infrastructure de test a également été revue et modernisée.

### Évolutions fonctionnelles
- **Chat :** Ajout d'une fonctionnalité de chat complète avec :
    - Création de nouvelles conversations [#1234](https://github.com/suitenumerique/hub/issues/1234) (implicite)
    - Affichage des conversations avec pagination et ancrage de défilement
    - Gestion des threads de messages
    - Possibilité de réagir aux messages avec des emojis
    - Barre d'outils pour les messages
    - Indicateur de messages non lus
- **Documents :** Ajout d'un panneau d'outils pour la gestion des documents avec :
    - Liste des documents
    - Prévisualisation des fichiers (PDF, images, vidéos, audio)
- **Interface utilisateur :**
    - Nouvelle structure de pages et vues (Home, Error)
    - Composants d'interface utilisateur (Avatar, AccountSelector)
    - Gestion de la langue de l'interface utilisateur
    - Amélioration des styles et des thèmes (surfaces, transparences)

### Évolutions techniques
- **Frontend :** Migration vers une nouvelle base de code frontend utilisant Next.js et TypeScript.
- **Tests :**
    - Refonte des tests end-to-end avec Playwright.
    - Suppression des anciens tests end-to-end.
    - Ajout de fixtures et de routes de test pour les tests end-to-end.
- **Infrastructure :**
    - Consolidation du stack Docker Compose et de la base de données pour les tests.
    - Mise à jour de la configuration de build et des outils.
    - Mise à jour des workflows CI/CD pour le nouveau frontend et les tests end-to-end.
- **Architecture :**
    - Restructuration du code avec l'introduction de drivers et de mocks.
    - Utilisation d'Architecture Decision Records (ADR).
    - Ajout de hooks personnalisés et d'utilitaires.
- **Internationalisation (i18n):** Mise à jour de la configuration et des traductions.

### Autres changements
- Ajout d'assets publics.
- Mise à jour de la documentation (README).
- Nettoyage du code et suppression de dépendances inutiles.
- Formatage du code avec Prettier.
- Correction de problèmes de routage Nginx pour les exports statiques.
