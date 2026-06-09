## Changelog : monstagedeseconde (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'optimisation de certaines fonctionnalités existantes. Des améliorations ont été apportées à la gestion des conventions, à la recherche d'établissements et à la gestion des applications. Des corrections ont également été apportées pour éviter la duplication d'offres et améliorer la gestion des dates.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la publication d'une offre après un clic intempestif sur le bouton de validation. [#907](https://github.com/betagouv/monstagedeseconde/pull/907)
- Amélioration de la gestion des conventions : les établissements peuvent désormais voir les conventions signées par l'employeur. [#891](https://github.com/betagouv/monstagedeseconde/pull/891)
- Correction d'un problème de duplication d'applications. [#901](https://github.com/betagouv/monstagedeseconde/pull/901)
- Correction d'un bug empêchant l'affichage correct des semaines vides dans le planning. [#899](https://github.com/betagouv/monstagedeseconde/pull/899)
- Amélioration de la gestion des applications : correction d'un problème de renvoi d'application. [#904](https://github.com/betagouv/monstagedeseconde/pull/904)
- Ajout de la possibilité de gérer le niveau d'étude des étudiants au sein des établissements. [#883](https://github.com/betagouv/monstagedeseconde/pull/883)
- Amélioration de la gestion des URL des ressources affichées. [#872](https://github.com/betagouv/monstagedeseconde/pull/872)
- Mise à jour de la formulation concernant la récupération des candidatures. [#876](https://github.com/betagouv/monstagedeseconde/pull/876)
- Ajout de la possibilité d'importer des étudiants depuis l'espace administrateur. [#880](https://github.com/betagouv/monstagedeseconde/pull/880)
- Correction d'un problème lié à l'affichage des places restantes à zéro. [#9534f8f6](https://github.com/betagouv/monstagedeseconde/commit/9534f8f6)
- Ajout d'un chatbot Crisp pour l'assistance utilisateur. [#879](https://github.com/betagouv/monstagedeseconde/pull/879)
- Amélioration de la gestion des types d'utilisateurs lors de l'inscription. [#866](https://github.com/betagouv/monstagedeseconde/pull/866)
- Ajout du préfixe téléphonique de la Guadeloupe. [#859](https://github.com/betagouv/monstagedeseconde/pull/859)

### Évolutions techniques
- Refactorisation de l'utilisation des "abilities" (permissions) pour une meilleure organisation et maintenabilité. [#889](https://github.com/betagouv/monstagedeseconde/pull/889)
- Mise à jour de la version de Ruby à 3.4.9. [#884](https://github.com/betagouv/monstagedeseconde/pull/884)
- Amélioration de la gestion des erreurs liées à l'API Sygne, avec l'ajout d'exceptions spécifiques pour une meilleure identification des problèmes. [#898](https://github.com/betagouv/monstagedeseconde/pull/898)
- Optimisation des requêtes pour la reconstruction de l'index de recherche, améliorant ainsi les performances.
- Mise à jour des dépendances : `qs`, `webpack-dev-server`, `faraday`, `jwt`, `nokogiri`, `view_component`, `devise`.
- Amélioration de la gestion des erreurs et des tests.
- Correction de problèmes de syntaxe et de typographie.

### Autres changements
- Suppression d'une dépendance tierce inutile. [#120b5b14](https://github.com/betagouv/monstagedeseconde/commit/120b5b14)
- Nettoyage du code et suppression de fichiers inutiles.
- Mise à jour de la documentation.
- Amélioration de la configuration et des scripts de déploiement.
- Ajout de compétences pour l'IA Claude.
- Correction de la configuration de l'environnement de test.
- Suppression de fichiers de dump inutiles.
- Correction de problèmes de CSP (Content Security Policy).
- Mise à jour de la gestion des jetons de signature.
- Amélioration de la gestion des autorisations pour les statisticiens.
- Correction de la gestion des dates de signature des conventions.
- Amélioration de la validation des adresses et de la géolocalisation.
