## Changelog : apistration (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations en matière d'accessibilité, de correction de bugs et d'ajout de nouvelles fonctionnalités, notamment l'intégration de l'API DGFIP TVA et l'amélioration de l'expérience utilisateur pour les éditeurs DataPass. Des efforts considérables ont également été déployés pour moderniser la documentation et l'infrastructure du projet.

### Évolutions fonctionnelles
- Ajout de l'API CNAV Allocation Rentrée Scolaire ([#164](https://github.com/datagouv/apistration/pull/164)).
- Intégration de l'API DGFIP TVA, incluant la gestion des nouveautés et la correction de problèmes de CI ([#125](https://github.com/datagouv/apistration/pull/125), [#184](https://github.com/datagouv/apistration/pull/184)).
- Simplification du processus d'intégration des éditeurs DataPass en remplaçant le formulaire par un questionnaire Typeform ([#255](https://github.com/datagouv/apistration/pull/255)).
- Amélioration de la gestion des délégations d'éditeurs, avec création automatique au webhook DataPass ([#246](https://github.com/datagouv/apistration/pull/246)).
- Ajout de la possibilité de filtrer les statuts des requêtes dans le tableau de bord des fournisseurs ([#216](https://github.com/datagouv/apistration/pull/216)).
- Affichage de l'ID interne de l'utilisateur sur la page du compte ([#217](https://github.com/datagouv/apistration/pull/217)).
- Mise à jour de la documentation pour les éditeurs DataPass et les tokens éditeur ([#178](https://github.com/datagouv/apistration/pull/178)).

### Évolutions techniques
- Améliorations significatives de l'accessibilité (a11y) du site web, incluant la correction de nombreux problèmes identifiés par des audits et l'ajout de balises ARIA, de liens avec attributs `new-window` et d'améliorations de la structure HTML ([#238](https://github.com/datagouv/apistration/pull/238), [#240](https://github.com/datagouv/apistration/pull/240)).
- Refactorisation du code pour améliorer la robustesse et la maintenabilité, notamment dans la gestion des associations DJEPVA/MI et la simplification de la logique de cache.
- Mise à jour des dépendances et des outils de développement (Ruby, Rails, Docker, etc.).
- Amélioration de la gestion des erreurs et de la sécurité, notamment la correction de vulnérabilités potentielles liées à l'injection de code et au tabnapping ([#240](https://github.com/datagouv/apistration/pull/240)).
- Migration des tests vers JSON pour une meilleure lisibilité et maintenabilité.
- Amélioration de la gestion des incidents avec l'ajout d'une skill Hyperping.

### Autres changements
- Mise à jour de la documentation et des exemples de code.
- Correction de fautes de frappe et amélioration de la qualité du code.
- Ajout de jeux de données de test pour le CNous.
- Amélioration de la gestion des logs et du monitoring.
- Suppression de code obsolète et simplification de certaines parties du code.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour des workflows CI/CD pour automatiser le processus de déploiement.
- Amélioration de la configuration et de l'infrastructure du projet.
- Ajout de la gestion du type de token dans les logs d'accès.
