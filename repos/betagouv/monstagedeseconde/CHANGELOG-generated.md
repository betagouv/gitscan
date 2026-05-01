## Changelog : monstagedeseconde (30 derniers jours, au 29 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la stabilité et de la sécurité de l'application, avec de nombreuses mises à jour de dépendances. Des corrections de bugs ont été apportées, notamment concernant la gestion des candidatures, des conventions et des adresses. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des offres de stage.

### Évolutions fonctionnelles
- Correction d'un bug empêchant les étudiants de valider deux candidatures sur les semaines 1 et 2. [#842](https://github.com/betagouv/monstagedeseconde/issues/842)
- Correction d'un problème lié à l'affichage de la description des offres QPV. [#812](https://github.com/betagouv/monstagedeseconde/issues/812)
- Amélioration de la gestion des adresses des étudiants, avec une limitation du nombre de caractères. [#815](https://github.com/betagouv/monstagedeseconde/issues/815)
- Correction d'un bug empêchant la signature des accords pour les représentants légaux. [#775](https://github.com/betagouv/monstagedeseconde/issues/775)
- Correction d'un problème lié à l'affichage des informations du responsable d'établissement lors de l'édition des conventions. [#808](https://github.com/betagouv/monstagedeseconde/issues/808)
- Correction d'un bug lié à l'affichage du chef d'établissement sur les conventions. [#830](https://github.com/betagouv/monstagedeseconde/issues/830)
- Amélioration de la gestion des offres d'internat, notamment pour les statisticiens de l'académie.
- Correction d'un bug lié aux coordonnées des maisons d'internat.
- Amélioration de l'affichage des offres d'internat.

### Évolutions techniques
- Mise à jour de Rails en version 8.1. [#765](https://github.com/betagouv/monstagedeseconde/issues/765)
- Ajout de CodeQL pour l'analyse de la sécurité du code.
- Amélioration de la configuration du serveur MCP pour les projets Rails.
- Correction de plusieurs bugs liés à Sentry (gestion des erreurs et des notifications). [#833](https://github.com/betagouv/monstagedeseconde/issues/833), [#834](https://github.com/betagouv/monstagedeseconde/issues/834), [#843](https://github.com/betagouv/monstagedeseconde/issues/843), [#844](https://github.com/betagouv/monstagedeseconde/issues/845)
- Suppression d'une ancienne fonctionnalité. [#786](https://github.com/betagouv/monstagedeseconde/issues/786)
- Correction d'un bug lié à la suppression logique des données. [#784](https://github.com/betagouv/monstagedeseconde/issues/784)
- Correction d'un bug lié à l'export des candidatures. [#783](https://github.com/betagouv/monstagedeseconde/issues/783)
- Correction d'un bug lié à l'affichage des semaines vides lors de la recherche pour les étudiants. [#766](https://github.com/betagouv/monstagedeseconde/issues/766)
- Correction d'un bug empêchant une candidature retenue d'évoluer. [#762](https://github.com/betagouv/monstagedeseconde/issues/762)
- Correction d'un problème lié à la vérification de l'ID du groupe d'offres. [#761](https://github.com/betagouv/monstagedeseconde/issues/761)
- Amélioration de la gestion des doublons de comptes (employeur/étudiant). [#758](https://github.com/betagouv/monstagedeseconde/issues/758)

### Autres changements
- Mise à jour des dépendances (diverses bibliothèques Ruby et Node.js).
- Amélioration de la documentation.
- Nettoyage du code et suppression de fichiers inutiles.
- Correction de problèmes mineurs d'interface utilisateur.
- Amélioration des tests.
- Ajout de tests d'accessibilité (A11y).
- Amélioration de la configuration de l'environnement de développement (foreman).
