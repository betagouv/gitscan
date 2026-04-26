## Changelog : monstagedeseconde (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la gestion des offres de stage et des candidatures, ainsi que des optimisations de la sécurité et de la performance. Des validations ont été ajoutées pour améliorer la qualité des données saisies et des corrections ont été apportées à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage de la description des offres QPV [#812](https://github.com/betagouv/monstagedeseconde/issues/812).
- Amélioration de l'ordre des offres dans le tableau de bord [#818](https://github.com/betagouv/monstagedeseconde/issues/818).
- Correction d'un bug empêchant la signature des accords pour les représentants légaux [#775](https://github.com/betagouv/monstagedeseconde/issues/775).
- Correction d'un problème empêchant les référents d'inviter des collègues [#779](https://github.com/betagouv/monstagedeseconde/issues/779).
- Ajout de la possibilité pour les étudiants légaux de relancer les représentants pour redémarrer le processus de signature [#1234](https://github.com/betagouv/monstagedeseconde/issues/1234).
- Amélioration de la gestion des adresses des étudiants, avec une limitation du nombre de caractères à 170 [#825](https://github.com/betagouv/monstagedeseconde/issues/825).
- Correction d'un bug lié à la gestion des codes postaux des maisons d'accueil [#810](https://github.com/betagouv/monstagedeseconde/issues/810).
- Correction d'un bug empêchant la création d'offres pendant certaines heures [#821](https://github.com/betagouv/monstagedeseconde/issues/821).
- Amélioration de la gestion des candidatures avec la documentation des avis possibles [#780](https://github.com/betagouv/monstagedeseconde/issues/780).
- Suppression d'une ancienne fonctionnalité [#810](https://github.com/betagouv/monstagedeseconde/issues/810).

### Évolutions techniques
- Mise à jour de plusieurs dépendances Ruby (activesupport, actionview, activestorage, rack-session, bcrypt, json, loofah, devise) et npm (flatted, yaml, follow-redirects, picomatch).
- Ajout d'un workflow CodeQL pour l'analyse de la sécurité du code.
- Configuration du serveur MCP pour les projets Rails.
- Amélioration de la configuration SSH pour utiliser Clever Tools et les variables d'environnement.
- Optimisation du nombre de workers pour les tests.
- Suppression de code obsolète.
- Amélioration de la logique du contrôleur du tableau de bord des offres de stage.

### Autres changements
- Ajout d'une validation pour limiter le nombre de caractères dans les champs d'adresse des étudiants.
- Suppression du tableau de bord des maisons d'accueil pour les statisticiens de l'académie.
- Correction de messages d'erreur.
- Amélioration de la documentation.
- Ajout de règles `.gitignore` pour ignorer le répertoire `solid`.
- Correction de la gestion des autorisations pour les notifications.
- Correction de la gestion des adresses en minuscules.
- Correction d'une erreur Sentry liée aux accords mono.
- Correction d'un bug Sentry général.
- Correction d'un bug lié aux doublons de comptes (employeur/étudiant).
- Amélioration de la gestion des coordonnées des maisons d'accueil.
- Correction d'un problème lié à l'affichage des titres sur la page de l'offre dans le tableau de bord [#814](https://github.com/betagouv/monstagedeseconde/issues/814).
- Correction d'un problème d'adresse manquante pour les accords [#807](https://github.com/betagouv/monstagedeseconde/issues/807).
- Correction d'un bug lié à l'importation des maisons d'accueil.
- Correction d'un bug lié à l'affichage des internats.
- Suppression d'un template d'email obsolète.
