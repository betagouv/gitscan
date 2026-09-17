## Changelog : anssi-portail (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, le portail a connu une évolution majeure avec le déploiement de nouveaux outils interactifs, notamment les mini-tests (Réflexes Cyber, Vrai/Faux) et une refonte du test d'Exposition. L'expérience utilisateur a été enrichie par des animations et un meilleur suivi de progression. En parallèle, une modernisation profonde de l'infrastructure technique a été opérée, incluant une migration vers Svelte 5 et un renforcement des mesures de sécurité.

### Évolutions fonctionnelles
- **Mini-tests et simulations** : 
    - Lancement et amélioration des mini-tests (Réflexes Cyber, Vrai/Faux) avec gestion des scores, des scénarios de simulation et des rôles.
    - Ajout de fonctionnalités de feedback permettant aux utilisateurs de laisser des réactions et des avis.
    - Intégration d'animations (confettis, transitions) pour rendre les parcours plus engageants.
- **Test d'Exposition** : 
    - Création d'une nouvelle interface dédiée incluant des cartes interactives, des radars animés et des badges de statistiques.
    - Mise en place de la collecte des retours utilisateurs et des réponses au questionnaire.
- **Parcours de sécurisation** : 
    - Amélioration de la navigation avec des fils d'Ariane plus complets et une meilleure gestion du mobile.
    - Ajout d'animations de progression et de modales de félicitations lors de la complétion des modules.
- **Outils et contenus** : 
    - Ajout d'un comparateur de financements pour aider les organisations dans leurs démarches.
    - Mise à jour des contenus relatifs à la directive NIS2 et aux guides de bonnes pratiques.

### Évolutions techniques
- **Modernisation du framework** : Migration massive de l'ensemble des composants vers **Svelte 5** (utilisation des "runes") pour améliorer la réactivité et la maintenance.
- **Tests et Qualité** : 
    - Migration complète du moteur de tests vers **Vitest**.
    - Amélioration de la couverture de tests (backend et frontend) et optimisation de la gestion des mocks.
- **Sécurité** : 
    - Renforcement de la protection contre les attaques par force brute via l'ajout de *rate limiting* sur les routes de connexion.
    - Amélioration de la gestion du MFA (Multi-Factor Authentication) et du contrôle d'identité.
- **Infrastructure et DevOps** : 
    - Optimisation du processus de déploiement (gestion de pnpm et intégration avec CleverCloud).
    - Mise à jour des workflows CI/CD (Nix, Ruby, Playwright).
    - Amélioration de l'expérience de développement (support du développement en LAN).
- **Optimisation du code** : 
    - Nettoyage important du projet : suppression de nombreux composants, styles CSS, images et dépendances inutilisés.
    - Refactorisation de l'architecture des composants pour favoriser la réutilisation.

### Autres changements
- **SEO et visibilité** : Optimisation du référencement naturel via la simplification des URLs (suppression des extensions `.html`) et la mise à jour du sitemap.
- **Documentation** : Mise à jour des fichiers de configuration et ajout de la page `llms.txt`.
