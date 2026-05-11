## Changelog : monstagedeseconde (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la correction de bugs, l'amélioration de la stabilité et de la performance de la plateforme, ainsi que sur l'ajout de fonctionnalités pour faciliter la gestion des stages et des candidatures, notamment pour les stages de seconde. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des données.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la validation de candidatures pour les élèves de lycée postulant sur une semaine spécifique. [#819](https://github.com/betagouv/monstagedeseconde/pull/819)
- Possibilité pour un élève d'avoir deux stages valides simultanément. [#836](https://github.com/betagouv/monstagedeseconde/pull/836)
- Amélioration de l'affichage des offres d'entreprises et correction d'un problème d'affichage de la description pour les offres QPV. [#812](https://github.com/betagouv/monstagedeseconde/pull/812)
- Correction d'un problème lié à l'ordre des offres dans le tableau de bord. [#818](https://github.com/betagouv/monstagedeseconde/pull/818)
- Correction d'un bug empêchant l'export des candidatures. [#783](https://github.com/betagouv/monstagedeseconde/pull/783)
- Correction d'un bug lié à la suppression logique (soft delete) des données. [#786](https://github.com/betagouv/monstagedeseconde/pull/786)
- Amélioration de la gestion des adresses et des champs associés dans le formulaire d'identité.
- Correction d'un problème d'affichage des statistiques pour les maisons d'accueil.
- Suppression de l'envoi de l'email de confirmation de candidature. [#838](https://github.com/betagouv/monstagedeseconde/pull/838)

### Évolutions techniques
- Mise à jour de plusieurs dépendances (gems et npm) pour améliorer la sécurité et la stabilité de la plateforme.
- Amélioration de la configuration SSH pour les environnements de production.
- Ajout de tests CodeQL pour améliorer la sécurité du code.
- Optimisation de la gestion des sessions.
- Amélioration de la performance des requêtes SQL.
- Correction de plusieurs erreurs signalées par Sentry, le système de surveillance des erreurs.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de Rails en version 8.1. [#831](https://github.com/betagouv/monstagedeseconde/pull/831)

### Autres changements
- Documentation des changements possibles concernant les statuts des candidatures.
- Correction de liens brisés dans la FAQ. [#841](https://github.com/betagouv/monstagedeseconde/pull/841)
- Amélioration des messages d'erreur affichés aux utilisateurs.
- Suppression de fonctionnalités obsolètes.
- Mise à jour de la configuration de l'environnement de développement avec Foreman.
- Ajout de commentaires et de documentation au code.
- Correction de problèmes de validation et de formatage des données.
- Correction de problèmes liés aux conventions d'affichage des informations sur les établissements.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
