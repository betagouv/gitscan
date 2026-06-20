## Changelog : apistration (30 derniers jours, au 20 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la documentation de l'API, notamment avec l'ajout de la gestion des délégations d'éditeurs et l'intégration de FranceConnect. Des corrections et améliorations ont également été apportées à la gestion des données TVA et à la robustesse générale de l'application.

### Évolutions fonctionnelles
- Ajout de la gestion des délégations d'éditeurs avec une API dédiée et une interface d'administration améliorée [#142](https://github.com/datagouv/apistration/pull/142).
- Intégration de FranceConnect pour les endpoints de civilité, avec gestion des cas où le token est manquant [#152](https://github.com/datagouv/apistration/pull/152).
- Ajout d'un endpoint DGFIP pour la vérification du numéro de TVA, avec remplacement de l'ancien service européen [#125](https://github.com/datagouv/apistration/pull/125).
- Amélioration de la documentation des scopes d'API Particulier, avec affichage des scopes sur les endpoints et dans la documentation technique [#168](https://github.com/datagouv/apistration/pull/168).
- Ajout de données régionales pour la v5 des données de scolarité, notamment pour la région PACA [#141](https://github.com/datagouv/apistration/pull/141).
- Ajout d'une page de sitemap pour satisfaire les exigences RGAA 12.1 [#207](https://github.com/datagouv/apistration/pull/207).

### Évolutions techniques
- Renforcement de la sécurité des sessions utilisateurs avec un délai d'inactivité et une protection anti-fixation [#182](https://github.com/datagouv/apistration/pull/182).
- Amélioration de la gestion des erreurs et de la documentation pour les endpoints FranceConnect.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité [#144](https://github.com/datagouv/apistration/pull/144).
- Mise à jour des dépendances (Ruby, Rails, RSpec, Webmock, etc.) et des actions GitHub.
- Amélioration de la gestion des erreurs CORS pour les fichiers OpenAPI.
- Correction d'une fuite de mémoire avec Timecop dans les tests.
- Ajout d'un volume commun pour les conteneurs Docker [#197](https://github.com/datagouv/apistration/pull/197).

### Autres changements
- Correction de typos dans le code et la documentation [#184](https://github.com/datagouv/apistration/pull/184), [#185](https://github.com/datagouv/apistration/pull/185).
- Ajout de tests et d'exemples pour les nouvelles fonctionnalités.
- Amélioration de la documentation pour l'intégration des éditeurs.
- Suppression de code obsolète.
- Ajout de logs pour faciliter le débogage.
- Mise à jour de la documentation pour les endpoints de l'API Entreprise.
- Correction de liens brisés dans la documentation.
- Ajout de commentaires pour améliorer la compréhension du code.
