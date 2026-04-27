## Changelog : euphrosyne-herma (30 derniers jours, au 24 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau de la connexion et de l'expérience de démarrage. Des corrections ont été apportées pour gérer les erreurs d'authentification et les échecs de téléchargement avec AzCopy. De nouvelles fonctionnalités, comme le mode CLI et l'utilisation du trousseau pour l'authentification, ont été ajoutées. Des améliorations ont également été apportées au processus de construction et de déploiement.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur pour une meilleure expérience globale [#5](https://github.com/betagouv/euphrosyne-herma/pull/5).
- Ajout d'une sélection d'environnement lors de la connexion [#4bba940](https://github.com/betagouv/euphrosyne-herma/commit/4bba940).
- Ajout d'un bouton de déconnexion à la fenêtre de téléchargement [#6ad2d58](https://github.com/betagouv/euphrosyne-herma/commit/6ad2d58).
- Utilisation du trousseau pour stocker les informations d'authentification, améliorant ainsi la sécurité et la commodité [#6ad2d58](https://github.com/betagouv/euphrosyne-herma/commit/6ad2d58).
- Ajout d'un mode CLI pour une utilisation en ligne de commande [#601b42c](https://github.com/betagouv/euphrosyne-herma/commit/601b42c).
- Amélioration de l'expérience de démarrage de l'application [#071811d](https://github.com/betagouv/euphrosyne-herma/commit/071811d).
- Possibilité de démarrer le téléchargement pour des chemins de dossiers typés [#34fa0e5](https://github.com/betagouv/euphrosyne-herma/commit/34fa0e5).

### Évolutions techniques
- Correction du chemin d'installation d'AzCopy pour l'application macOS regroupée [#f9d8a3b](https://github.com/betagouv/euphrosyne-herma/commit/f9d8a3b).
- Correction de l'argument attendu par la fonction `selected` [#339de39](https://github.com/betagouv/euphrosyne-herma/commit/339de39).
- Correction de l'installation des dépendances système dans le workflow de construction de la release [#552968f](https://github.com/betagouv/euphrosyne-herma/commit/552968f) et [#cb23e1b](https://github.com/betagouv/euphrosyne-herma/commit/cb23e1b).
- Utilisation des slugs de projet au lieu des noms pour les requêtes d'outils [#d05d03b](https://github.com/betagouv/euphrosyne-herma/commit/d05d03b).
- Amélioration de la gestion des erreurs d'authentification lors des téléchargements [#ab9f0a6](https://github.com/betagouv/euphrosyne-herma/commit/ab9f0a6).
- Amélioration du reporting des échecs de téléchargement AzCopy [#b7d30c5](https://github.com/betagouv/euphrosyne-herma/commit/b7d30c5).
- Gestion des projets manquants ou invalides au démarrage [#a5102e7](https://github.com/betagouv/euphrosyne-herma/commit/a5102e7).
- Ajout de tests [#edda61d](https://github.com/betagouv/euphrosyne-herma/commit/edda61d).

### Autres changements
- Suppression de la vérification du linter lors de la construction [#02db288](https://github.com/betagouv/euphrosyne-herma/commit/02db288).
- Ajout de checks au workflow CI [#9e1d5f5](https://github.com/betagouv/euphrosyne-herma/commit/9e1d5f5).
- Correction du Makefile [#a6c2c87](https://github.com/betagouv/euphrosyne-herma/commit/a6c2c87).
- Ajout de documentation sur les découvertes [#d115969](https://github.com/betagouv/euphrosyne-herma/commit/d115969).
- Correction du CI [#4b91c00](https://github.com/betagouv/euphrosyne-herma/commit/4b91c00) et [#0e7c60a](https://github.com/betagouv/euphrosyne-herma/commit/0e7c60a).
