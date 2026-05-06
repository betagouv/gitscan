## Changelog : monstagedeseconde (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la correction de bugs, l'amélioration de la stabilité de l'application et l'optimisation de l'expérience utilisateur, notamment au niveau des conventions et des candidatures. Des mises à jour de sécurité et de dépendances ont également été intégrées pour assurer la pérennité du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la comparaison correcte des semaines dans l'interface utilisateur [#1643](https://github.com/betagouv/monstagedeseconde/issues/1643).
- Amélioration de la gestion des adresses des étudiants, avec une limitation du nombre de caractères pour éviter des erreurs.
- Correction d'un problème lié à l'affichage de la description des offres QPV.
- Les étudiants de seconde peuvent maintenant valider deux candidatures sur les semaines 1 et 2.
- Correction d'un bug empêchant l'édition des conventions par les établissements avec les bonnes informations.
- Amélioration de la gestion des établissements et des responsables d'établissement dans les conventions.
- Possibilité pour les référents d'inviter des collègues.
- Correction d'un bug empêchant la signature des accords pour les représentants légaux.
- Amélioration de l'affichage des offres d'accueil.
- Correction d'un bug empêchant la suppression logicielle des candidatures.
- Correction d'un bug lors de l'export des candidatures.
- Correction d'un bug lié à l'affichage des semaines vides lors de la recherche pour les étudiants.
- Correction d'un bug empêchant l'évolution d'une candidature retenue.
- Correction d'un bug lié à l'affichage de l'identifiant de groupe d'offre.
- Correction d'un bug lié à la création de nouvelles offres.
- Amélioration de la gestion des adresses dans les candidatures.
- Correction d'un bug lié à la duplication de compte pour les employeurs et les étudiants.
- Amélioration de l'affichage des informations sur les offres d'accueil.

### Évolutions techniques
- Mise à jour de Rails vers la version 8.1.
- Refonte de la gestion des notifications et des permissions.
- Amélioration de la gestion des erreurs Sentry, avec des corrections spécifiques pour divers problèmes (dialogue d'invitation, informations sur les offres, etc.).
- Ajout de tests CodeQL pour améliorer la sécurité du code.
- Amélioration de la configuration du serveur avec Clever Tools.
- Optimisation des performances de l'application.
- Simplification et débogage de la logique d'accès (ability).
- Mise en place de workflows CI/CD améliorés.
- Amélioration de la gestion des dépendances et des versions.
- Ajout de la possibilité d'uploader des bases de données.
- Amélioration de la gestion des logs Sentry.

### Autres changements
- Mise à jour de la documentation.
- Suppression de code obsolète.
- Amélioration de la configuration du projet (gitignore).
- Corrections de style et de formatage du code.
- Mise à jour des dépendances npm et bundler.
- Amélioration de la gestion des tests.
- Correction de l'ordre des offres dans le tableau de bord.
- Correction d'un bug lié aux coordonnées des maisons d'accueil.
- Suppression de l'affichage de la maison d'accueil dans le tableau de bord pour les statisticiens de l'académie.
- Correction d'un bug lié à l'import des maisons d'accueil.
