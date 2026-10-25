## Changelog : anssi-portail (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par une intégration massive des parcours de sécurisation à travers tout le portail afin de mieux guider les utilisateurs selon leur niveau de maturité. La boîte à outils a été considérablement enrichie avec de nouveaux modèles de documents et un système de retours utilisateurs plus robuste. En parallèle, un important travail de restructuration technique a été mené pour améliorer la maintenabilité de l'API et la gestion des fichiers.

### Évolutions fonctionnelles
- **Boîte à outils** : 
    - Ajout de nouveaux modèles de documents (revue des droits d'accès, revue de comptes utilisateurs, modification de mots de passe, listes d'activités).
    - Amélioration du système de retours utilisateurs (possibilité de laisser un avis, limitation de la fréquence des retours, obligation d'authentification pour certains retours).
    - Intégration de nouveaux outils et liens (jeux en ligne, jeux de cartes).
- **Parcours de sécurisation** : Visibilité accrue des parcours sur l'ensemble du portail (menu de navigation, page d'accueil, résultats des tests de maturité et des réflexes cyber).
- **Contacts** : Mise à jour et enrichissement des annuaires de contacts (données nationales, régionales et sectorielles).
- **Expérience utilisateur & Contenu** : 
    - Amélioration de l'interface (corrections sur les popovers, les modales et la navigation vers les landing pages).
    - Mise à jour des statistiques (nombre de diagnostics réalisés et de parcours démarrés).
    - Optimisation du blog (gestion des avis, intégration au sitemap).

### Évolutions techniques
- **Refactoring** : 
    - Réorganisation profonde des routes API et de la structure des dossiers (outils, contacts, annuaires, mini-tests).
    - Isolation de la logique métier, notamment pour la manipulation de fichiers XLSX, la gestion des cookies, du rate limiting et des redirections.
    - Mutualisation de la validation des retours et de la gestion des utilisateurs.
- **Architecture & Performance** : 
    - Introduction d'un pattern stratégie pour certains composants.
    - Mise en place du rendu côté serveur (SSR) pour les pages de conseils et mise en cache des articles du blog.
    - Importation dynamique des boîtes à outils personnalisées.
- **Infrastructure & Toolchain** : 
    - Mise à jour des runners GitHub et des outils de test (Playwright).
    - Mise à jour de dépendances critiques (Node.js types, lab-anssi-lib).

### Autres changements
- **SEO** : Optimisation des métadonnées, des descriptions et des titres pour le référencement et le partage sur les réseaux sociaux.
- **Qualité du code** : Nettoyage du linting (TypeScript-ESLint), suppression de commentaires et de fichiers obsolètes, et normalisation des fins de ligne.
