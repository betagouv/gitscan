## Changelog : anssi-portail (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois-ci, le portail a franchi des étapes importantes avec la refonte complète des simulations de hameçonnage et l'enrichissement de la boîte à outils avec de nombreux nouveaux modèles pratiques. L'expérience utilisateur est également renforcée par l'introduction d'un espace connecté (tableau de bord, favoris) et d'un système de collecte d'avis pour les parcours de sécurisation.

### Évolutions fonctionnelles
- **Simulation de hameçonnage** : Refonte majeure incluant une interface de boîte mail simulée, de nouveaux scénarios (Orange, La Poste, CPF, Inpi, etc.), l'affichage des scores, la gestion des réponses et une adaptation optimisée pour mobiles et tablettes.
- **Boîte à outils** : Enrichissement avec de nouveaux modèles (RACI, revue des droits d'accès, revue de comptes, interconnexions, liste d'activités, etc.) et ajout de fonctionnalités de prévisualisation et de téléchargement.
- **Espace connecté** : Mise en place d'un squelette de tableau de bord, d'une section "Favoris" et d'une section "Autres ressources".
- **Parcours de sécurisation** : Intégration de modules de collecte d'avis pour recueillir les retours des utilisateurs à la complétion des parcours.
- **Kit de sensibilisation** : Création d'un kit comprenant des animations, des outils de téléchargement et une gestion du mode hors connexion.
- **Améliorations diverses** : Correction de filtres de recherche, mise à jour des informations de contact et optimisation de la navigation (fil d'Ariane, lien "Haut de page").

### Évolutions techniques
- **Infrastructure & CI/CD** : Migration de la stack vers Node.js 26, remplacement de `s3cmd` par la CLI AWS officielle dans la CI et optimisation de la gestion des environnements de développement (Nix, `.nvmrc`).
- **Architecture & Refactoring** : Modélisation du temps et des durées via un adaptateur "Temporal", centralisation du signalement des erreurs et refactorisation importante des composants Svelte pour améliorer la réutilisabilité et la maintenance.
- **Performance & Sécurité** : Optimisation du chargement (images et dépendances PDF en différé), renforcement des politiques de sécurité (CSP) et correction de vulnérabilités (body-parser).
- **Base de données** : Mise à jour de l'environnement PostgreSQL local vers la version 18.7.

### Autres changements
- **Qualité & Linting** : Normalisation des espaces typographiques (notamment les espaces insécables) dans les fichiers Markdown, HTML et Svelte.
- **Maintenance** : Nettoyage des anciens "feature flags" (NIS2) et suppression de code ou de propriétés inutilisés.
