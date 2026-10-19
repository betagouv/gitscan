## Changelog : anssi-portail (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, le portail a franchi une étape majeure avec l'intégration complète du **parcours de sécurisation** à travers toutes les interfaces (accueil, menu, résultats de tests). L'expérience utilisateur a été considérablement enrichie par une refonte de la simulation **"Réflexes Cyber"**, devenue plus immersive grâce à l'ajout de sons et d'animations. La **boîte à outils** s'est également étoffée avec un nouveau modèle d'annuaire de crise téléchargeable et une base de contacts (nationaux, régionaux et sectoriels) mise à jour. Enfin, le lancement de la section **Blog** permet désormais de diffuser des contenus éditoriaux et de recueillir les avis des utilisateurs.

### Évolutions fonctionnelles
- **Parcours de sécurisation** : Intégration globale sur le portail (affichage dans le menu, le héros de la page d'accueil, les pieds de page et les résultats des tests de maturité/réflexes).
- **Réflexes Cyber (Simulation)** : 
    - Amélioration de l'interactivité avec l'ajout de sons, d'animations de transition et de retours visuels (pulsations, indicateurs de commandes bloquées).
    - Optimisation de l'interface pour les petits écrans et amélioration de la clarté des instructions.
    - Possibilité d'envoyer les résultats et retours directement via Mattermost.
- **Boîte à outils** : 
    - Mise à disposition d'un modèle d'annuaire de crise téléchargeable au format XLSX.
    - Enrichissement et mise à jour des listes de contacts (nationaux, régionaux et sectoriels).
    - Ajout d'un outil de rappel dans la procédure de gestion de crise.
- **Mini-tests** : 
    - Déploiement du nouveau test de maturité (compatible mode autonome avec recommandations personnalisées).
    - Amélioration des tests "Exposition" et "Vrai-Faux" (statistiques, affichage des scores et interface).
- **Blog** : Création de la section blog avec gestion des articles, des résumés et un système de collecte des retours utilisateurs.
- **Statistiques** : Mise à jour des compteurs d'organisations accompagnées et de diagnostics réalisés.
- **Badge Cyberdépart** : Ajout d'un badge de reconnaissance conditionnel selon le parcours de l'utilisateur.

### Évolutions techniques
- **Architecture & Modularité** : 
    - Refactoring massif pour isoler les responsabilités : routes (API, statiques, authentification), middlewares, configuration des cookies, du rate limiting et des redirections.
    - Création d'un module dédié pour la gestion des contacts sectoriels.
    - Mutualisation de la logique de traitement des utilisateurs et des composants de procédures.
- **Optimisation des performances** : 
    - Mise en place du rendu côté serveur (SSR) pour la page "Conseils Cyber" et le "Kit Relais".
    - Implémentation d'un système de mise en cache pour les articles du blog.
- **Infrastructure & Tooling** : 
    - Migration vers `pnpm` v12.
    - Amélioration des processus de déploiement des composants de mini-tests.
    - Renforcement de la suite de tests avec l'utilisation de spies Vitest.

### Autres changements
- **Contenu & SEO** : Mise à jour des métadonnées SEO, des titres pour les réseaux sociaux et harmonisation de la terminologie (ex: remplacement de "tutoriel" par "procédure").
- **Nettoyage** : Suppression des anciens services (Crisp), des drapeaux de fonctionnalités (feature flags) obsolètes et des dépendances inutiles.
- **Maintenance** : Corrections orthographiques et typographiques diverses sur l'ensemble du portail.
