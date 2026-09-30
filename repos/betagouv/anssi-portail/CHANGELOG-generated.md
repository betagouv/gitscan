## Changelog : anssi-portail (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois a été marqué par un développement intensif de nouveaux outils interactifs et une refonte majeure de l'expérience utilisateur. Le portail s'enrichit de nouveaux mini-tests (Vrai/Faux, Maturité Cyber) et d'un comparateur de financements. La simulation "Réflexes Cyber" a été profondément modernisée avec des animations, une intégration sonore et un parcours utilisateur plus fluide. L'ensemble de la plateforme a bénéficié d'améliorations de sécurité et d'une optimisation de l'accessibilité.

### Évolutions fonctionnelles
- **Nouveaux outils et tests interactifs** :
    - Déploiement des mini-tests "Vrai ou Faux" et "Maturité Cyber".
    - Mise en ligne d'un nouveau comparateur de financements.
    - Création d'une nouvelle page dédiée à l'outil d'exposition.
- **Amélioration de l'expérience utilisateur (UX/UI)** :
    - **Réflexes Cyber** : Refonte complète du parcours de simulation (choix des rôles et scénarios, nouvelles animations de transition, intégration du son et système de score amélioré).
    - **Interactivité** : Ajout d'un système de réactions et de retours utilisateurs sur les mini-tests.
    - **Visuels** : Intégration de nouveaux éléments graphiques (cartes animées, héros, confettis de succès, indicateurs de progression).
    - **Statistiques** : Amélioration de l'affichage des scores et du nombre de tests réalisés pour les utilisateurs et les administrateurs.
- **Optimisation des contenus** :
    - Mise à jour des données d'exposition (statistiques 2025) et des guides (NIS2, ReCyF).
    - Amélioration de la navigation mobile pour les parcours de sécurisation et les quiz.

### Évolutions techniques
- **Sécurité et Authentification** :
    - Renforcement de l'authentification avec l'exigence du MFA (Multi-Factor Authentication) via ProConnect.
    - Mise en place d'un *rate limiting* sur les routes de connexion pour prévenir les attaques par force brute.
- **Tests et Qualité** :
    - Migration massive de la suite de tests (frontend et backend) vers Vitest.
    - Amélioration de la couverture de tests et utilisation de mocks pour les environnements complexes.
- **Infrastructure et Déploiement** :
    - Optimisation de la gestion des dépendances avec pnpm (passage aux versions 11/12).
    - Mise à jour des runners GitHub Actions et amélioration des processus de déploiement des composants Web (WebC).
- **SEO et Web** :
    - Nettoyage des URLs pour le référencement (suppression des extensions `.html`).
    - Mise à jour du sitemap et gestion optimisée des ressources cross-origin (CORS).

### Autres changements
- **Accessibilité** :
    - Intégration de la détection du mode "réduction de mouvement" pour adapter les animations.
    - Amélioration de l'accessibilité des composants interactifs (boutons, radio, navigation).
- **Maintenance et Soin** :
    - Nettoyage général du code (suppression de dépendances, d'images et de styles en ligne inutilisés).
    - Corrections orthographiques et harmonisation du wording sur l'ensemble du portail.
    - Mise à jour de la politique de confidentialité.
