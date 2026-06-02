## Changelog : graal (30 derniers jours, au 1er juin 2026)

### Résumé
Les dernières mises à jour de Graal se concentrent sur la correction de bugs et l'amélioration de la stabilité, notamment en ajustant les dépendances et en corrigeant des problèmes liés à l'interface utilisateur et à la gestion des tâches. Une nouvelle version a été publiée (1.51.1) intégrant ces corrections.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la suppression de bases de données et de fichiers de configuration par les utilisateurs. [#229](https://github.com/SocialGouv/graal/issues/229)
- Possibilité de supprimer les bases de données et les fichiers de configuration par les utilisateurs. [#36f58e7](https://github.com/SocialGouv/graal/commit/36f58e71fbf73506841093487371f20882e02163)
- Autorisation des accents pour le champ "projet d'origine". [#ce7412f](https://github.com/SocialGouv/graal/commit/ce7412f9d4fffe6a42dcfa14a76f47b666154329)
- Ajout de boutons de connexion en environnement de développement pour faciliter les tests et les revues. [#846fd14](https://github.com/SocialGouv/graal/commit/846fd14f2da9df41)
- Correction de l'affichage du texte des boutons de connexion en environnement de développement. [#8d4350d](https://github.com/SocialGouv/graal/commit/8d4350d05aeb6079f0bf1a5075f47c3f7a94c2e1)

### Évolutions techniques
- Mise à jour de la version de `rapidfuzz` pour corriger des problèmes de build. [#3fd7288](https://github.com/SocialGouv/graal/commit/3fd7288817791372763793f7f96a7d7614d43464)
- Rétrogradation d'un package Python pour éviter les échecs de build. [#b4ee2f0](https://github.com/SocialGouv/graal/commit/b4ee2f016a020092326b2e120e4c8dcc23a58c15)
- Mise à jour du tag Docker Python vers la version 3.14. [#602766c](https://github.com/SocialGouv/graal/commit/602766c99946815778a3325898638611c839112d)
- Amélioration de la configuration de `VITE_ENABLE_DEV_LOGIN`. [#0190356](https://github.com/SocialGouv/graal/commit/019035628c3560996139d3536cbaab42baceeea0)
- Correction de la mise à jour du job store après l'exécution des tâches. [#71cbcfe](https://github.com/SocialGouv/graal/commit/71cbcfe52a3f34afcd4ac14921e4abe13a8c4c6f)
- Diminution du niveau de log pour les messages d'authentification par requête de INFO à DEBUG. [#4069114](https://github.com/SocialGouv/graal/commit/40691143b1b10a10c39a2cc214b18e58a0c2956c)

### Autres changements
- Publication de la version 1.51.1. [#7bc1a0a](https://github.com/SocialGouv/graal/commit/7bc1a0a6b25a169066941592673561034846687f)
- Ajout de limites de taux et de concurrence pour les requêtes LLM. [#d128676](https://github.com/SocialGouv/graal/commit/d1286766147de46d9a32cc8770a61d7de0719273)
- Ajout de la configuration du nombre maximum de requêtes LLM concurrentes à la base de données et à l'interface utilisateur. [#22f6bd3](https://github.com/SocialGouv/graal/commit/22f6bd325f48b4c4c6c9712ec88589d484f3f67f) et [#0af4c4d](https://github.com/SocialGouv/graal/commit/0af4c4ddb2ae15d9b2e07582a09b28bd5ec9d785)
