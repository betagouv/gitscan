## Changelog : monstagedeseconde (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des utilisateurs et des établissements, la correction de bugs liés à la manipulation des candidatures et des conventions, ainsi que des optimisations de sécurité et de performance. Des améliorations ont également été apportées à l'interface utilisateur et à l'intégration avec des services externes comme Sygne.

### Évolutions fonctionnelles
- Possibilité d'associer un personnel pédagogique à un ou plusieurs établissements. [#881](https://github.com/betagouv/monstagedeseconde/pull/881)
- Amélioration de la gestion des adresses email des représentants légaux. [#813](https://github.com/betagouv/monstagedeseconde/issues/813)
- Les établissements peuvent désormais voir les conventions signées par l'employeur. [#891](https://github.com/betagouv/monstagedeseconde/issues/891)
- Ajout de la possibilité d'importer des étudiants depuis l'administration. [#883](https://github.com/betagouv/monstagedeseconde/pull/883)
- Amélioration de la gestion des semaines vides dans les candidatures. [#899](https://github.com/betagouv/monstagedeseconde/pull/899)
- Ajout d'un chatbot Crisp pour l'assistance utilisateur. [#895](https://github.com/betagouv/monstagedeseconde/pull/895)
- Possibilité de gérer le niveau d'un étudiant dans l'établissement. [#882](https://github.com/betagouv/monstagedeseconde/pull/882)
- Amélioration de l'affichage des ressources avec URL. [#872](https://github.com/betagouv/monstagedeseconde/pull/872)
- Mise à jour de la formulation lors de la récupération d'une candidature. [#876](https://github.com/betagouv/monstagedeseconde/pull/876)
- Amélioration de la gestion des applications avec une limitation à une seule candidature par étudiant et par offre. [#893](https://github.com/betagouv/monstagedeseconde/pull/893)

### Évolutions techniques
- Refactorisation de l'implémentation d'Ability pour une meilleure organisation et maintenabilité. [#889](https://github.com/betagouv/monstagedeseconde/pull/889)
- Mise à jour de la version de Ruby à 3.4.9. [#884](https://github.com/betagouv/monstagedeseconde/pull/884)
- Amélioration de la gestion des erreurs Sygne avec la création d'une classe d'erreur dédiée. [#835](https://github.com/betagouv/monstagedeseconde/issues/835)
- Refactorisation de la gestion des utilisateurs et des rôles, notamment pour les gestionnaires d'établissement.
- Ajout de tests pour la gestion des utilisateurs et des rôles.
- Correction de problèmes de duplication de candidatures lors de la validation des plannings.
- Correction d'un bug empêchant la création d'utilisateurs lors de la reconstruction des données.
- Amélioration de la gestion des sessions et des tokens JWT.
- Ajout de tests pour la gestion des utilisateurs et des rôles.
- Mise en place d'un verrouillage en base de données pour éviter les approbations multiples d'une même candidature.
- Optimisation de la gestion des données et des requêtes en base de données.
- Mise à jour des dépendances (qs, webpack-dev-server, faraday, jwt).

### Autres changements
- Ajout de documentation et de commentaires dans le code.
- Mise à jour de la configuration de l'environnement de développement.
- Suppression de fichiers inutiles.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de syntaxe et de style dans le code.
- Ajout de nouvelles compétences pour l'outil d'IA Claude.
- Mise à jour des préfixes téléphoniques pour la Guadeloupe.
- Correction de problèmes de sécurité XSS.
- Amélioration de la gestion des images (taille maximale).
- Correction de problèmes de tests.
- Ajout de la gestion du mode maintenance.
- Amélioration de la gestion des liens et des URLs.
