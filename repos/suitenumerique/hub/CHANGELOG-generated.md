## Changelog : hub (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte inclut l'implémentation d'une première version de l'interface de chat, avec des composants de base et des tests associés. Des améliorations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Chat :** Implémentation d'une interface de chat avec une liste de conversations simulée, des composants de conversation et une gestion de la pagination et de l'ancrage de défilement. [#1234](https://github.com/suitenumerique/hub/issues/1234)
- **Authentification :** Ajout d'un sélecteur de compte permettant de choisir entre Gaufre et le profil utilisateur.
- **Langue :** Synchronisation de l'attribut `lang` des pages HTML avec la langue active.
- **Pages :** Restructuration des pages avec l'ajout de vues "home" et "error".
- **Assets :** Ajout d'assets publics pour le frontend.

### Évolutions techniques
- **Frontend :** Migration complète du frontend vers Next.js et TypeScript. Suppression de l'ancienne codebase frontend.
- **Tests :** Refonte des tests E2E avec Playwright, incluant la mise à jour de la configuration et des dépendances. Suppression des anciens tests E2E.
- **CI/CD :** Mise à jour des workflows CI pour intégrer le nouveau frontend et les tests E2E.
- **Infrastructure :** Consolidation du stack Docker Compose et de la base de données utilisée pour les tests E2E.
- **Architecture :** Introduction de l'utilisation d'Architecture Decision Records (ADR) pour documenter les choix architecturaux.
- **Configuration :** Mise à jour de la configuration du build et des outils de développement.
- **Backend :** Ajout de fixtures et de routes de test pour les tests E2E.
- **i18n :** Mise à jour de la configuration i18n et des traductions.

### Autres changements
- Mise à jour du fichier README pour refléter les changements dans le Dockerfile.
- Ajout d'un changelog initial pour le projet.
- Suppression d'un plugin ESLint obsolète.
- Mise à jour des dépendances du projet.
