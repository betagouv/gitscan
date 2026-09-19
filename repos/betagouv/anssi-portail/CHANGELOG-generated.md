## Changelog : anssi-portail (30 derniers jours, au 18/09/2026)

### Résumé
Ce mois a été marqué par un enrichissement important des outils interactifs, notamment avec le lancement d'un nouveau mini-test "Vrai ou Faux" et l'amélioration de l'expérience utilisateur sur les parcours de sécurisation et le test d'exposition. Parallèlement, une modernisation technique majeure a été opérée avec la migration de l'interface vers Svelte 5 et une refonte complète de la suite de tests.

### Évolutions fonctionnelles
- **Nouveaux mini-tests** : Lancement du test "Vrai ou Faux" incluant un système de score, des animations (confettis), et la possibilité pour les utilisateurs de laisser des réactions/avis.
- **Parcours de sécurisation** : Amélioration de l'engagement utilisateur via des animations de progression, des modales de félicitations lors de la complétion de modules/parcours, et une meilleure ergonomie sur mobile.
- **Test d'exposition** : Création d'une page dédiée, ajout de nouvelles animations, et mise en place d'un système de collecte des résultats et des avis utilisateurs.
- **Outils de financement** : Ajout d'un outil de comparaison des financements et automatisation de la publication des informations.
- **Contenus et guides** : Mise à jour des informations relatives à la directive NIS2 (référentiel ReCyF) et amélioration de la clarté des guides pratiques.

### Évolutions techniques
- **Migration Framework** : Migration massive de la bibliothèque de composants vers Svelte 5 (utilisation du mode Runes) pour améliorer les performances et la maintenabilité.
- **Tests et Qualité** : Migration complète de la suite de tests (frontend et backend) vers Vitest et amélioration de la couverture via des mocks plus robustes.
- **Infrastructure et CI/CD** : Transition vers `pnpm` pour la gestion des dépendances et optimisation des workflows de déploiement (mise en cache, gestion des versions Ruby/Nix).
- **Sécurité** : Renforcement de la protection des routes d'authentification par l'ajout de limites de débit (*rate limiting*) et amélioration des flux MFA (authentification multi-facteurs).
- **Architecture** : Refonte de l'adaptateur Brevo pour une meilleure gestion des événements de parcours et des statistiques utilisateurs.

### Autres changements
- **Optimisation SEO** : Nettoyage des URLs (suppression des extensions `.html`) et ajout de métadonnées de modification pour les services et ressources.
- **Maintenance et Nettoyage** : Suppression importante de composants, de styles CSS et d'images inutilisés pour alléger le projet.
- **Documentation** : Mise à jour de la politique de confidentialité et ajout du fichier `llms.txt`.
