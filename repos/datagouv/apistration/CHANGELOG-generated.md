## Changelog : apistration (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout du nouveau point de terminaison DGFIP TVA, l'amélioration de la sécurité avec l'ajout de délais d'inactivité et la gestion des sessions, ainsi que des améliorations de la documentation et de l'expérience utilisateur pour les éditeurs et les développeurs. Plusieurs corrections de typos et mises à jour de dépendances ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un nouveau point de terminaison pour la TVA DGFIP ([#125](https://github.com/datagouv/apistration/pull/125)).
- Amélioration de la documentation pour le nouveau point de terminaison DGFIP TVA, incluant la génération du SDK Node.js et la mise à jour des mocks.
- Ajout de la possibilité de récupérer les délégations d'éditeur via une nouvelle API ([#142](https://github.com/datagouv/apistration/pull/142), [#147](https://github.com/datagouv/apistration/pull/147)).
- Amélioration de l'interface utilisateur pour la gestion des délégations d'éditeur, avec l'ajout de colonnes étendues et de filtres ([#142](https://github.com/datagouv/apistration/pull/142)).
- Ajout de la gestion des données de la région PACA pour la v5 des données de scolarité ([#141](https://github.com/datagouv/apistration/pull/141)).
- Amélioration de la documentation des scopes d'API Particulier, avec l'ajout de labels et d'explications.
- Ajout d'une protection contre les attaques CSRF et une expiration des sessions après 12 heures d'inactivité, avec un délai maximal de 24 heures ([#182](https://github.com/datagouv/apistration/pull/182)).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (Ruby, Rails, RSpec, Webmock, Rubocop, etc.).
- Correction d'une fuite de mémoire dans les tests avec Timecop ([#181](https://github.com/datagouv/apistration/pull/181)).
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes de CORS pour les fichiers OpenAPI.
- Mise à jour des mocks et de la documentation Swagger.
- Amélioration de la sécurité en limitant l'accès à certains endpoints.

### Autres changements
- Correction de typos dans le code et la documentation ([#184](https://github.com/datagouv/apistration/pull/184), [#185](https://github.com/datagouv/apistration/pull/185)).
- Ajout d'un lien vers le Bureau Ouvert dans la documentation.
- Amélioration du changelog pour les API liasses fiscales.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de la documentation pour l'utilisation de FranceConnect.
- Suppression de code obsolète.
- Amélioration de la configuration et de l'infrastructure.
- Ajout de suivi des activités des administrateurs pour l'audit.
- Correction d'erreurs mineures et amélioration de la qualité du code.
