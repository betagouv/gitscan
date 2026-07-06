## Changelog : envergo (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment sur les pages d'accueil et de gestion des notes d'instruction. Des corrections et des refactorings ont été effectués concernant la gestion des haies, des critères Natura 2000 et des procédures ICPE. Des optimisations de sécurité et de performance ont également été apportées.

### Évolutions fonctionnelles
- Refonte de la page d'accueil avec l'ajout de contacts et d'informations sur l'état d'activation des départements.
- Amélioration de la page de gestion des notes d'instruction avec ajout de notes privées et d'un nouveau design.
- Ajout de la possibilité de créer des critères Natura 2000 via une commande moulinette.
- Amélioration de l'affichage des cartes de densité.
- Ajout d'une procédure d'urgence avec affichage d'une alerte.
- Mise en place d'une gestion des URL alternatives pour les simulations, avec validation et affichage des erreurs.
- Amélioration de la sélection des modèles pour les ICPE.
- Ajout d'une fonctionnalité permettant de gérer les cas par cas pour les ICPE.
- Affichage des informations sur les haies dans le contexte des projets.
- Ajout de la possibilité d'importer plusieurs éléments en une seule fois.

### Évolutions techniques
- Refactoring du code lié aux critères Natura 2000 et aux haies.
- Mise à jour des dépendances (Playwright, Node.js).
- Amélioration de la gestion des erreurs et des timeouts dans les tâches asynchrones.
- Sécurisation des URL mappings.
- Optimisation des tests et correction de bugs liés aux tests E2E.
- Utilisation de `EnrichedChoices` pour améliorer la gestion des choix dans les formulaires.
- Migration vers une nouvelle méthode de gestion des catégories de haies.
- Correction de problèmes de synchronisation entre les templates HTML et texte pour les avis.
- Suppression de code obsolète et amélioration de la structure du code.
- Mise en place de secrets pour les URLs publiques.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour clarifier le code.
- Amélioration des messages d'erreur.
- Correction de problèmes de migration.
- Suppression de données sensibles dans les tests.
- Mise à jour des noms de variables et de fonctions pour plus de clarté.
- Suppression de code mort.
- Correction de problèmes d'indentation.
- Uniformisation des espaces insécables.
- Correction de bugs mineurs dans l'interface utilisateur.
- Ajout de badges sur les détails des projets.
- Amélioration de l'affichage des noms des projets.
