## Changelog : anssi-portail (30 derniers jours, au 09/09/2026)

### Résumé
Ce mois a été marqué par une transformation majeure du portail, tant sur le plan visuel que fonctionnel. L'évolution principale concerne le lancement de nouveaux mini-tests interactifs (notamment le format "Vrai-Faux") et une refonte graphique globale (nouvelle direction artistique) visant à moderniser l'expérience utilisateur. Parallèlement, une migration technique profonde vers Svelte 5 a été entreprise pour garantir la pérennité et la performance de l'application.

### Évolutions fonctionnelles
- **Nouveaux Mini-tests** : 
    - Introduction du format de quiz "Vrai-Faux" avec affichage des scores, animations de succès (confettis) et possibilité de laisser un avis.
    - Amélioration de l'interactivité des tests avec des animations de choix et des estimations de temps de complétion.
    - Mise en place d'un système de statistiques permettant de voir le nombre de tests réalisés.
- **Parcours de Sécurisation** : 
    - Amélioration du suivi de progression (déblocage de badges, comptabilisation des mesures prises en compte).
    - Optimisation de l'expérience mobile et ajout de nouveaux éléments visuels (illustrations animées, nouveaux héros).
    - Meilleure intégration du suivi utilisateur via l'outil Brevo pour les événements de complétion.
- **Nouvelle page "Exposition"** : Création d'une page dédiée permettant de mesurer son exposition avec des cartes interactives et des règles conformes aux spécifications.
- **Contenus et Navigation** :
    - Mise à jour des contenus relatifs à la directive NIS2 et aux référentiels (ReCyF, CyFun).
    - Amélioration de la navigation via l'harmonisation des fils d'Ariane sur l'ensemble du site.
    - Refonte visuelle globale : nouvelles illustrations, palettes de couleurs modernisées et utilisation accrue des composants du Design System (DSFR).

### Évolutions techniques
- **Migration Framework** : Migration massive de la majorité des composants vers **Svelte 5** (utilisation des *runes*) pour améliorer la réactivité et la maintenabilité.
- **Architecture et API** :
    - Refonte de la logique métier des mini-tests (utilisation d'entrepôts de données et d'objets métier).
    - Enrichissement de l'API de statistiques pour inclure la satisfaction utilisateur.
    - Centralisation et optimisation de la gestion des redirections d'URLs historiques.
- **SEO et Performance** :
    - Optimisation du référencement naturel par la suppression des extensions `.html` dans les URLs des services, ressources et contacts.
    - Mise à jour du sitemap pour inclure les nouvelles pages de landing.
- **Infrastructure et Toolchain** :
    - Migration vers **pnpm 11**.
    - Amélioration de l'environnement de développement local (support LAN, configuration Nix).
    - Mise à jour des workflows CI/CD et des outils de test (Playwright, Vitest).

### Autres changements
- **Nettoyage du code** : Suppression massive de composants, de styles CSS, d'images et de variables inutilisés pour alléger l'application.
- **Documentation** : Mise à jour des guides de développement et des procédures d'exploitation.
- **Qualité** : Renforcement des règles de linting et de formatage du code.
