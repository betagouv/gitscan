## Changelog : betabot (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, betabot a bénéficié d'améliorations significatives concernant la gestion des conversations (retour aux threads Matrix), l'accès à la documentation (ajout de liens vers DSFR, FranceConnect et ProConnect), et l'indexation de contenu web. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité du bot, notamment dans la gestion des messages directs et l'affichage des réponses. Enfin, des bases de données SQLite ont été ajoutées pour des requêtes d'agrégation plus performantes.

### Évolutions fonctionnelles
- Retour à l'utilisation des threads dans les conversations Matrix, améliorant l'organisation et la lisibilité des échanges [#38a343b](https://github.com/betagouv/betabot/commit/38a343b).
- Ajout de liens vers la documentation de DSFR, FranceConnect et ProConnect, facilitant l'accès à ces ressources importantes [#2e81a0b](https://github.com/betagouv/betabot/commit/2e81a0b), [#5474cf7](https://github.com/betagouv/betabot/commit/5474cf7), [#6e36236](https://github.com/betagouv/betabot/commit/6e36236).
- Ajout d'une commande curl pour récupérer le flux vidéo de ruche_numerique [#f792415](https://github.com/betagouv/betabot/commit/f792415).
- Indexation des pages de site web pour améliorer les résultats de recherche [#3c66cb6](https://github.com/betagouv/betabot/commit/3c66cb6).
- Ajout d'une base de données SQLite pour permettre des requêtes d'agrégation plus performantes [#7a00773](https://github.com/betagouv/betabot/commit/7a00773).
- Ajout de l'incubateur dans la base de données [#de02739](https://github.com/betagouv/betabot/commit/de02739).

### Évolutions techniques
- Amélioration des schémas de base de données pour une meilleure gestion des données [#f8b9f13](https://github.com/betagouv/betabot/commit/f8b9f13).
- Ajout du champ `created_at` pour suivre la date de création des entrées [#3022759](https://github.com/betagouv/betabot/commit/3022759).
- Correction de problèmes liés à l'utilisation de threads dans les conversations en face à face [#d1f40d2](https://github.com/betagouv/betabot/commit/d1f40d2).
- Correction de bugs liés à l'affichage des réponses trop longues [#8359633](https://github.com/betagouv/betabot/commit/8359633).
- Correction de plusieurs bugs liés aux messages directs [#63eb8d6](https://github.com/betagouv/betabot/commit/63eb8d6), [#7afef1d](https://github.com/betagouv/betabot/commit/7afef1d), [#9230ec0](https://github.com/betagouv/betabot/commit/9230ec0), [#8dff61d](https://github.com/betagouv/betabot/commit/8dff61d), [#383c853](https://github.com/betagouv/betabot/commit/383c853), [#cc83fd4](https://github.com/betagouv/betabot/commit/cc83fd4).
- Mise à jour de la version de Node.js vers la version 24 [#85201d8](https://github.com/betagouv/betabot/commit/85201d8).
- Amélioration de la gestion des erreurs lors de l'intégration d'images [#26edf1c](https://github.com/betagouv/betabot/commit/26edf1c).

### Autres changements
- Mise à jour de la documentation et des instructions d'utilisation [#ff8f528](https://github.com/betagouv/betabot/commit/ff8f528), [#f18cec9](https://github.com/betagouv/betabot/commit/f18cec9), [#6180886](https://github.com/betagouv/betabot/commit/6180886).
- Nettoyage du code et suppression de code inutile [#9d90f0c](https://github.com/betagouv/betabot/commit/9d90f0c).
- Corrections de liens et d'URLs dans la documentation [#47f49e3](https://github.com/betagouv/betabot/commit/47f49e3), [#c1efe7e](https://github.com/betagouv/betabot/commit/c1efe7e), [#6b5e7a9](https://github.com/betagouv/betabot/commit/6b5e7a9).
- Corrections de problèmes liés au Dockerfile [#6bd909c](https://github.com/betagouv/betabot/commit/6bd909c), [#c8395cb](https://github.com/betagouv/betabot/commit/c8395cb), [#e617117](https://github.com/betagouv/betabot/commit/e617117), [#bbb9fe2](https://github.com/betagouv/betabot/commit/bbb9fe2).
