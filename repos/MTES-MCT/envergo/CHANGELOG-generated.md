## Changelog : envergo (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, envergo a bénéficié d'améliorations significatives, notamment l'ajout de nouvelles fonctionnalités pour la gestion des ICPE (Installations Classées pour la Protection de l'Environnement) et une refonte de l'interface utilisateur pour une meilleure expérience. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- **ICPE :** Ajout de la gestion du cas par cas pour les ICPE, incluant des actions à entreprendre et des modèles spécifiques pour la création et la modification.  L'accès à certaines informations ICPE est désormais restreint au personnel autorisé.
- **Page d'accueil :** Refonte de la page d'accueil avec un nouveau sélecteur de département utilisant une fonctionnalité de recherche automatique et affichant des informations de contact et des alertes pour les départements non activés.
- **Notes de l'instructeur :**  Possibilité d'ajouter des notes privées pour les instructeurs, avec une interface améliorée pour la saisie et la consultation.
- **Cartographie :** Ajout de cartes de densité pour faciliter la visualisation des données.
- **Procédure d'urgence :** Implémentation d'une procédure d'urgence avec un formulaire dédié et une alerte d'information affichée aux utilisateurs.
- **Import multiple :** Possibilité d'importer plusieurs fichiers simultanément.

### Évolutions techniques
- **Refactoring :** Amélioration de la structure du code, notamment pour la gestion des critères ICPE et des actions à entreprendre.
- **Tests :** Ajout et mise à jour des tests unitaires et d'intégration, notamment pour les nouvelles fonctionnalités ICPE.
- **CI/CD :** Mise à jour des dépendances et configuration du pipeline CI/CD pour assurer une intégration et un déploiement continus.
- **Sécurité :** Sécurisation des URL et protection contre les géométries invalides.
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment Playwright et Node.js.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les modifications apportées.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de plusieurs bugs mineurs, notamment liés à l'affichage des données et à la gestion des erreurs.
- **Amélioration des messages d'erreur :** Clarification des messages d'erreur pour faciliter le diagnostic des problèmes.
- **Gestion des migrations :** Résolution de conflits de migrations et ajout de nouvelles migrations pour les nouvelles fonctionnalités.
