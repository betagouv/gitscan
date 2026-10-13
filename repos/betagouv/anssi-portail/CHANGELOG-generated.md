## Changelog : anssi-portail (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de l'interactivité du portail. Le lancement de la simulation "Réflexes cyber" et l'intégration d'un nouveau blog enrichissent l'expérience utilisateur. Parallèlement, le "Parcours de sécurisation" est désormais mieux mis en avant sur l'ensemble du site, et de nouveaux outils, comme le comparateur de financements, ont été déployés pour accompagner les organisations.

### Évolutions fonctionnelles
- **Simulation "Réflexes cyber"** : 
    - Mise en place d'une expérience immersive avec intégration du son, d'animations (transitions, pulsations, confettis) et d'un système de score.
    - Amélioration du parcours utilisateur (choix des rôles et scénarios, gestion du minuteur, feedback immédiat).
    - Optimisation de l'affichage sur petits écrans et amélioration de l'accessibilité (détection du mouvement réduit).
- **Blog et contenus** :
    - Déploiement d'une section blog complète (affichage des articles, gestion des résumés, sitemap).
    - Ajout d'un système de retours utilisateurs sur les articles pour améliorer la qualité du contenu.
- **Parcours de sécurisation** :
    - Meilleure visibilité du parcours via son intégration dans le menu principal, le pied de page, le héros de la page d'accueil et les résultats de tests.
    - Ajout d'animations sur les cartes et les vignettes pour dynamiser la navigation.
- **Mini-tests et outils** :
    - Amélioration des tests de maturité, d'exposition et "Vrai/Faux" (compatibilité mobile, animations et nouveaux indicateurs de score).
    - Mise en place d'un outil de comparaison des financements.
    - Refonte de la "Boîte à outils" incluant désormais un onglet dédié aux procédures prioritaires.
- **Sécurité et authentification** :
    - Renforcement de la sécurité avec l'exigence du MFA (authentification multi-facteurs) via ProConnect et l'ajout de limitations de débit (rate limiting) sur les routes de connexion.

### Évolutions techniques
- **Tests et qualité** :
    - Migration complète des moteurs de tests (frontend et backend) vers **Vitest** pour plus de rapidité et de fiabilité.
    - Amélioration de la couverture de tests et centralisation des mocks.
- **Infrastructure et déploiement** :
    - Optimisation des pipelines CI/CD (GitHub Actions) avec mise en cache des tests et mise à jour des runners.
    - Stabilisation des déploiements sur CleverCloud et gestion optimisée des versions de `pnpm`.
- **Architecture et performance** :
    - Refactoring de plusieurs composants pour une meilleure conformité au Design System (DSFR).
    - Optimisation des performances via la mise en cache des articles du blog et des données de recherche.
    - Centralisation de la gestion des dépendances via le catalogue `pnpm`.

### Autres changements
- **Contenu et SEO** : Mise à jour des métadonnées SEO (titres, descriptions, réseaux sociaux), de la politique de confidentialité et des informations de contact.
- **Maintenance** : Nettoyage du code (suppression des anciens services Crisp et des anciens "feature flags") et harmonisation de la terminologie (ex: passage de "tutoriels" à "procédures").
