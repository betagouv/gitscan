## Changelog : graal (30 derniers jours, au 11 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des bases de données et des configurations par les utilisateurs, notamment la possibilité de supprimer leurs propres bases de données et fichiers. Des corrections de bugs ont également été implémentées, améliorant la robustesse et l'expérience utilisateur. De nouvelles fonctionnalités concernant la configuration et la limitation de l'utilisation des modèles de langage (LLM) ont été ajoutées.

### Évolutions fonctionnelles
- Les utilisateurs peuvent maintenant supprimer leurs propres bases de données et fichiers de configuration. [#36f58e7](https://github.com/SocialGouv/graal/commit/36f58e71fbf73506841093487371f20882e02163)
- Correction d'un bug empêchant l'utilisation d'accents dans le champ "projet d'origine". [#ce7412f](https://github.com/SocialGouv/graal/commit/ce7412f9d4fffe6a42dcfa14a76f47b666154329)
- Ajout de la possibilité de définir un nombre maximal de requêtes simultanées aux LLM, configurable par l'utilisateur. [#22f6bd3](https://github.com/SocialGouv/graal/commit/22f6bd325f48b4c4c6c9712ec88589d484f3f67f) et [#0af4c4d](https://github.com/SocialGouv/graal/commit/0af4c4ddb2ae15d9b2e07582a09b28bd5ec9d785)
- Ajout d'une limite de taux (nombre de requêtes par minute) pour l'utilisation des LLM. [#d128676](https://github.com/SocialGouv/graal/commit/d1286766147de46d9a32cc8770a61d7de0719273)
- Possibilité de supprimer des fichiers des bases de données d'amendements avec reconstruction. [#2cda56b](https://github.com/SocialGouv/graal/commit/2cda56b34ade40d22f6dc4c58ae81189e4617c74)
- Ajout de boutons de connexion en mode développement pour faciliter les tests en environnements de revue. [#846fd14](https://github.com/SocialGouv/graal/commit/846fd14f2da9df411fc7e95713b8a6c0b8393a29)
- Ajout de la configuration des LLM dans la base de données. [#93d95c5](https://github.com/SocialGouv/graal/commit/93d95c5c6409459d0af2a9fd22b7038f81cc9290)

### Évolutions techniques
- Amélioration de la couverture des tests de configuration. [#0dc3ee9](https://github.com/SocialGouv/graal/commit/0dc3ee945252016905562119901838990b604623)
- Simplification du fichier README pour une meilleure clarté. [#5d487b9](https://github.com/SocialGouv/graal/commit/5d487b9636a982269669532f91649606d5354450)
- Correction d'un problème de configuration de la variable d'environnement `VITE_ENABLE_DEV_LOGIN`. [#0190356](https://github.com/SocialGouv/graal/commit/019035628c3560996139d3536cbaab42baceeea0)
- Correction d'un problème empêchant l'affichage du texte sur les boutons de connexion en développement. [#8d4350d](https://github.com/SocialGouv/graal/commit/8d4350d05aeb6079f0bf1a5075f47c3f7a94c2e1)
- Correction d'un problème lié à la mise à jour du job store après l'exécution des tâches. [#71cbcfe](https://github.com/SocialGouv/graal/commit/71cbcfe52a3f34afcd4ac14921e4abe13a8c4c6f)
- Diminution du niveau de log pour les messages d'authentification par requête de INFO à DEBUG. [#4069114](https://github.com/SocialGouv/graal/issues/236)
