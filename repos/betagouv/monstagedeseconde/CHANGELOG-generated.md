## Changelog : monstagedeseconde (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la stabilité et de la performance de l'application, ainsi que sur l'ajout de nouvelles fonctionnalités pour faciliter la gestion des stages et des candidatures, notamment pour les stages en internat et les offres d'entreprises. Des corrections ont également été apportées à l'interface et aux données affichées.

### Évolutions fonctionnelles
- Possibilité pour un élève d'avoir deux stages valides simultanément. [#836](https://github.com/betagouv/monstagedeseconde/pull/836)
- Amélioration de la recherche pour ne pas être affectée par l'année en cours lors de la sélection des semaines. [#853](https://github.com/betagouv/monstagedeseconde/pull/853)
- Correction du lien vers la FAQ qui ne fonctionnait pas. [#841](https://github.com/betagouv/monstagedeseconde/pull/841)
- Amélioration du message de validation de candidature pour les élèves de lycée postulant sur une semaine spécifique. [#819](https://github.com/betagouv/monstagedeseconde/pull/819)
- Ajout de statistiques pour les maisons d'accueil. [#848](https://github.com/betagouv/monstagedeseconde/pull/848)
- Suppression de l'envoi de l'email de confirmation de candidature. [#838](https://github.com/betagouv/monstagedeseconde/pull/838)
- Amélioration de l'affichage des offres d'entreprises. [#812](https://github.com/betagouv/monstagedeseconde/pull/812)
- Possibilité pour les référents d'inviter des collègues. [#779](https://github.com/betagouv/monstagedeseconde/pull/779)
- Correction de l'affichage des adresses des entreprises. [#825](https://github.com/betagouv/monstagedeseconde/pull/825)
- Correction d'un bug empêchant la modification d'une candidature retenue. [#762](https://github.com/betagouv/monstagedeseconde/pull/762)
- Correction d'un bug lié à l'export des candidatures. [#783](https://github.com/betagouv/monstagedeseconde/pull/783)
- Correction d'un bug lié à l'affichage des semaines vides lors de la recherche pour les élèves. [#766](https://github.com/betagouv/monstagedeseconde/pull/766)

### Évolutions techniques
- Mise à jour de Rails en version 8.1. [#808](https://github.com/betagouv/monstagedeseconde/pull/808)
- Amélioration de la gestion des erreurs Sentry avec mise en cache. [#843](https://github.com/betagouv/monstagedeseconde/pull/843) et [#826](https://github.com/betagouv/monstagedeseconde/pull/826)
- Ajout de CodeQL pour l'analyse de la sécurité du code.
- Amélioration de la configuration SSH pour les déploiements.
- Refactorisation de la logique de validation des candidatures.
- Amélioration de la gestion des permissions et des droits d'accès.
- Correction de plusieurs vulnérabilités de sécurité identifiées par Sentry.
- Mise à jour des dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour de plusieurs dépendances (gems et npm) via Dependabot.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la documentation.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la configuration du pipeline CI/CD.
- Suppression de fonctionnalités anciennes et inutilisées.
- Correction de problèmes de performance.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de l'affichage des maisons d'accueil dans le tableau de bord pour les statisticiens académiques.
- Correction de l'import des maisons d'accueil.
- Correction de l'affichage des coordonnées des maisons d'accueil.
- Correction de l'affichage des titres dans le tableau de bord des offres.
- Correction d'un problème lié aux champs d'adresse trop longs.
- Ajout de validations pour le nombre minimum de caractères dans les champs de description.
- Correction d'un bug lié à l'affichage des offres QPV.
- Correction d'un bug lié à la signature des conventions par les représentants légaux.
- Amélioration de la gestion des erreurs dans les logs Sentry.
- Correction d'un bug lié à la suppression logique des données.
