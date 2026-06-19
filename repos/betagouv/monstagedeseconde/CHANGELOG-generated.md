## Changelog : monstagedeseconde (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la gestion des utilisateurs et des établissements, ainsi que sur la correction de bugs et l'optimisation de l'expérience utilisateur. Des améliorations ont été apportées à la gestion des candidatures, à la duplication d'offres, et à la gestion des accès pour les différents rôles.

### Évolutions fonctionnelles
- Possibilité d'associer un personnel pédagogique à un ou plusieurs établissements [#881](https://github.com/betagouv/monstagedeseconde/pull/881).
- Amélioration de la gestion des doublons de candidatures, notamment pour éviter les soumissions multiples accidentelles [#908](https://github.com/betagouv/monstagedeseconde/pull/908).
- Les représentants légaux peuvent désormais modifier leur adresse email [#813](https://github.com/betagouv/monstagedeseconde/pull/813).
- Possibilité d'importer des étudiants depuis l'interface d'administration [#883](https://github.com/betagouv/monstagedeseconde/pull/883).
- Gestion améliorée des conventions de stage, notamment pour la signature et l'affichage des informations [#892](https://github.com/betagouv/monstagedeseconde/pull/892).
- Ajout d'un chatbot Crisp pour l'assistance utilisateur [#899](https://github.com/betagouv/monstagedeseconde/pull/899).
- Amélioration de la gestion des semaines vides dans les offres de stage [#851](https://github.com/betagouv/monstagedeseconde/pull/851).
- Ajout de préfixes téléphoniques pour la Guadeloupe [#859](https://github.com/betagouv/monstagedeseconde/pull/859).
- Amélioration de la gestion des droits d'accès pour les statisticiens.
- Possibilité pour un utilisateur d'école de changer d'établissement.
- Correction d'un bug empêchant la suppression des offres par les opérateurs [#907](https://github.com/betagouv/monstagedeseconde/pull/907).

### Évolutions techniques
- Refactorisation de l'architecture des autorisations (abilities) pour une meilleure organisation et maintenabilité [#889](https://github.com/betagouv/monstagedeseconde/pull/889).
- Mise à jour de la version de Ruby à 3.4.9 [#884](https://github.com/betagouv/monstagedeseconde/pull/884).
- Amélioration de la gestion des erreurs Sygne avec la création d'exceptions spécifiques.
- Ajout de tests pour la gestion des utilisateurs et des écoles.
- Amélioration de la gestion des dépendances (shell-quote, net-imap, puma).
- Refonte de la recherche d'établissements pour une meilleure performance et accessibilité.
- Ajout d'une étape de mise à jour des informations des établissements dans le processus de reconstruction de la base de données.
- Amélioration de la gestion des sessions et des tokens JWT.
- Mise en place de mécanismes pour éviter les candidatures multiples pour une même offre et un même étudiant.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de configurations inutiles.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de syntaxe et de style dans le code.
- Amélioration de la gestion des logs et des erreurs.
- Ajout d'un mécanisme pour éviter la duplication d'approbations de candidatures.
- Ajout d'une limite de taille pour les images téléchargées.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression d'un add-on tiers inutile.
- Mise à jour de la configuration Redis.
- Amélioration de la gestion des variables d'environnement.
- Ajout d'une protection contre les attaques XSS.
- Correction de problèmes de sécurité liés à l'authentification.
- Amélioration de la gestion des erreurs de signature de code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de problèmes de performance et d'optimisation du code.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
