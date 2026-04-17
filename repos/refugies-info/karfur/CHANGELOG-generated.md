## Changelog : karfur (30 derniers jours, au 15 avril 2026)

### Résumé
Cette version apporte des améliorations de sécurité en corrigeant des vulnérabilités identifiées par Dependabot, ainsi que des optimisations de performance, notamment au niveau des requêtes MongoDB et de la gestion des statistiques de traduction. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur, en particulier sur l'application mobile et lors de la gestion des fiches en brouillon.

### Évolutions fonctionnelles
- Amélioration de la gestion des fiches en brouillon : correction d'une erreur 500 lors de l'accès aux fiches RCO provenant du playground.
- Amélioration de la recherche : correction d'un bug empêchant l'affichage des résultats de recherche en ligne sur mobile.
- Amélioration de l'expérience utilisateur mobile : correction de problèmes d'affichage des champs de saisie et amélioration de la gestion des favoris.
- Amélioration de l'affichage des validations et publications : correction d'un problème d'affichage sur la page dédiée.
- Mise à jour de l'accessibilité : amélioration de la conformité RGAA, notamment avec la publication d'une déclaration d'accessibilité partiellement conforme.
- Ajout d'une fonctionnalité de débogage : ajout d'un outil pour investiguer les erreurs 500 sur le service backend.

### Évolutions techniques
- Sécurité : correction de plusieurs vulnérabilités de sécurité identifiées par Dependabot dans diverses dépendances (Next.js, axios, vite, handlebars, node-forge, brace-expansion, etc.).
- Performance : optimisation des requêtes MongoDB pour améliorer les performances, notamment au niveau des statistiques de traduction et de la récupération des dispositifs.
- Infrastructure : simplification du pipeline de release et ajout de tests pour prévenir les régressions.
- Amélioration de la robustesse : gestion améliorée des erreurs et des cas limites dans le code, notamment lors de la manipulation de données et de l'accès aux bases de données.
- Mise à jour des dépendances : passage à Expo SDK 54 pour l'application mobile.
- Refactoring : amélioration de la qualité du code et de sa maintenabilité grâce à des refactorings divers.

### Autres changements
- Documentation : ajout d'une documentation pour la nouvelle fonctionnalité de débogage.
- Configuration : mise à jour de la configuration du pipeline de release.
- Nettoyage du code : suppression de code obsolète et amélioration de la lisibilité du code.
- Ajout d'un skill pour la gestion des alertes de sécurité Dependabot.
- Amélioration des tests unitaires et d'intégration.
