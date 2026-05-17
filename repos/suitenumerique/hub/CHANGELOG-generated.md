## Changelog : hub (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte inclut une nouvelle structure de pages, des composants d'interface utilisateur modernes et une infrastructure de tests complète.  Une fonctionnalité de chat est en cours de développement et des composants de base sont déjà implémentés. Des améliorations ont également été apportées à l'infrastructure et à la configuration du projet.

### Évolutions fonctionnelles
- **Chat :** Ajout des composants de base pour la fonctionnalité de chat, incluant la liste des conversations, la présentation des messages et la gestion de la pagination et du défilement.  Une première version de l'interface utilisateur du chat est disponible.
- **Authentification :**  Amélioration de la gestion de la langue pour l'attribut `lang` des pages HTML, assurant une meilleure internationalisation.
- **Pages :** Restructuration des pages et ajout de vues "home" et "error" de base.
- **Composants UI :** Ajout d'un composant Avatar et d'un sélecteur de comptes (AccountSelector) intégrant Gaufre et le profil utilisateur.

### Évolutions techniques
- **Frontend :** Migration complète du frontend vers Next.js et TypeScript, remplaçant la codebase legacy.
- **Tests :** Mise en place d'une nouvelle infrastructure de tests E2E avec Playwright et réécriture des tests existants. Suppression des anciens tests E2E.
- **Infrastructure :** Consolidation du stack Docker Compose et unification de la base de données pour les tests E2E.
- **CI/CD :** Mise à jour des workflows CI pour prendre en compte le nouveau frontend et les tests E2E.
- **Architecture :** Introduction de l'utilisation d'Architecture Decision Records (ADR) pour documenter les choix architecturaux.
- **Configuration :** Mise à jour de la configuration du build et des outils de développement.
- **Packages :** Mise à jour des dépendances et suppression de packages inutiles (eslint-plugin-docs).

### Autres changements
- Mise à jour de la documentation README du projet Docker.
- Ajout d'assets publics au projet.
- Ajout de hooks et d'utilitaires globaux pour le frontend.
- Ajout de fonctionnalités de base (authentification, API, configuration, drivers, gestion des erreurs) au backend.
- Correction d'un problème de routage Nginx pour l'export statique.
- Initialisation du projet Hub avec un commit de base.
