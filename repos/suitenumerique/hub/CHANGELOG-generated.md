## Changelog : hub (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte inclut une amélioration de la configuration du projet, des tests, et de l'infrastructure, tout en préparant le terrain pour de futures fonctionnalités.

### Évolutions fonctionnelles
- Ajout de pages de base (accueil et gestion des erreurs).
- Mise en place de l'internationalisation (i18n) et des traductions.
- Ajout d'assets publics pour le frontend.
- Implémentation des fonctionnalités de base : authentification, accès à l'API, configuration, gestion des drivers et des erreurs.

### Évolutions techniques
- Refonte complète du frontend avec Next.js et TypeScript.
- Mise à jour de la configuration du build et des outils de développement.
- Restructuration des tests E2E et suppression des tests legacy.
- Consolidation du stack Docker et de la base de données pour les tests E2E.
- Ajout de fixtures et de routes de test pour le backend.
- Utilisation d'Architecture Decision Records (ADR) pour documenter les choix d'architecture.
- Mise à jour des workflows CI/CD pour intégrer le nouveau frontend et les tests E2E.
- Suppression de code legacy frontend.
- Mise à jour de la configuration Playwright et de ses dépendances.
- Ajout de hooks personnalisés, d'utilitaires et de styles globaux.

### Autres changements
- Mise à jour du fichier README.md pour refléter les changements Docker.
- Suppression du package `eslint-plugin-docs`.
- Mise à jour des dépendances du package i18n.
- Initialisation du projet Hub.
- Ajout d'entrées au changelog pour l'initialisation du frontend.
- Correction d'un problème de routage Nginx pour l'export statique.
