## Changelog : hub (30 derniers jours, au 20 mai 2026)

### Résumé
Le projet Hub a connu une refonte majeure de son frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte inclut l'implémentation d'une interface de chat avec une barre latérale et un panneau d'outils pour la gestion de documents, ainsi que des améliorations significatives de l'infrastructure de test et de déploiement.

### Évolutions fonctionnelles
- Ajout d'une interface de chat avec une liste de conversations (mockée) et une vue de conversation.
- Implémentation d'un panneau d'outils à droite de la vue de chat, incluant un outil de gestion de documents.
- Possibilité de prévisualiser les fichiers (PDF, images, vidéos, audio) dans l'outil de gestion de documents.
- Ajout d'un sélecteur de compte utilisateur avec support pour Gaufre et les profils utilisateurs.
- Ajout d'un composant Avatar.
- Mise en place d'une structure de pages et de vues de base (home, error).
- Redirection automatique vers la page de chat `/chat/new` lors de la visite de la page d'accueil.

### Évolutions techniques
- Refonte complète du frontend avec Next.js et TypeScript.
- Mise à jour de la configuration de build et des outils de développement.
- Restructuration du projet pour inclure des hooks personnalisés, des utilitaires et des styles globaux.
- Ajout de fonctionnalités de base telles que l'authentification, l'API, la configuration, les drivers et la gestion des erreurs.
- Mise à jour de la configuration de Playwright et des dépendances pour les tests E2E.
- Consolidation du stack Docker et de la base de données utilisée pour les tests E2E.
- Ajout de fixtures et de routes de test pour les tests E2E.
- Mise à jour de la configuration i18n et des traductions.
- Suppression de l'ancienne codebase frontend et des tests E2E legacy.
- Utilisation d'Architecture Decision Records (ADR) pour documenter les décisions architecturales.

### Autres changements
- Ajustement du fichier `README.md` pour le Docker.
- Mise à jour du changelog pour refléter les nouvelles fonctionnalités et changements.
- Suppression du package `eslint-plugin-docs`.
- Synchronisation de l'attribut `lang` de la balise `html` avec la langue active.
