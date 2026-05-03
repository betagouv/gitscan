## Changelog : monstagedeseconde (30 derniers jours, au 29 avril 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la stabilité et de la correction de bugs, notamment concernant la gestion des candidatures, des conventions et des offres de stage. Des corrections ont été apportées pour résoudre des erreurs Sentry et améliorer l'expérience utilisateur, en particulier pour les étudiants et les établissements. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Correction d'un bug empêchant les étudiants de valider deux candidatures sur les semaines 1 et 2. [#842](https://github.com/betagouv/monstagedeseconde/issues/842)
- Amélioration de la gestion des établissements : correction du nom et de l'email du responsable d'établissement lors de l'édition des conventions. [#808](https://github.com/betagouv/monstagedeseconde/issues/808) et [#830](https://github.com/betagouv/monstagedeseconde/issues/830)
- Correction d'un problème lié à l'affichage de la description des offres QPV. [#812](https://github.com/betagouv/monstagedeseconde/issues/812)
- Amélioration de la gestion des adresses des étudiants, avec une limitation du nombre de caractères pour éviter des erreurs. [#815](https://github.com/betagouv/monstagedeseconde/issues/815)
- Correction d'un bug empêchant la relance du processus de signature pour les représentants légaux.
- Correction d'un problème d'affichage des coordonnées des maisons d'accueil.
- Suppression d'une fonctionnalité obsolète. [#786](https://github.com/betagouv/monstagedeseconde/issues/786)
- Correction d'un bug lié à l'export des candidatures. [#783](https://github.com/betagouv/monstagedeseconde/issues/783) et [#766](https://github.com/betagouv/monstagedeseconde/issues/766)
- Amélioration de l'affichage des offres d'internat. [#787](https://github.com/betagouv/monstagedeseconde/issues/787)

### Évolutions techniques
- Mise à jour de Rails en version 8.1. [#765](https://github.com/betagouv/monstagedeseconde/issues/765)
- Ajout de CodeQL pour l'analyse de la sécurité du code.
- Amélioration de la configuration du serveur MCP pour les projets Rails.
- Correction de plusieurs erreurs Sentry pour améliorer la robustesse de l'application. [#843](https://github.com/betagouv/monstagedeseconde/issues/843), [#844](https://github.com/betagouv/monstagedeseconde/issues/844), [#834](https://github.com/betagouv/monstagedeseconde/issues/834), [#833](https://github.com/betagouv/monstagedeseconde/issues/833)
- Optimisation de la gestion des erreurs et des logs.
- Amélioration de la gestion des dépendances et des mises à jour.
- Correction de problèmes liés à la gestion des sessions et des identités.
- Correction de bugs liés à l'importation des maisons d'accueil.

### Autres changements
- Mise à jour de la documentation.
- Amélioration des tests et de la couverture de code.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des dépendances npm et bundler.
- Correction de messages d'erreur pour une meilleure clarté.
- Suppression de l'affichage des maisons d'accueil pour les statisticiens de l'académie.
- Amélioration de la gestion des champs obligatoires et de la validation des données.
