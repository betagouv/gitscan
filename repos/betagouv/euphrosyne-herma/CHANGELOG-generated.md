## Changelog : euphrosyne-herma (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment un dialogue de connexion plus clair et une meilleure expérience de démarrage. Des corrections ont été apportées pour gérer les erreurs d'authentification et les échecs de téléchargement avec AzCopy.  De nouvelles fonctionnalités comme un bouton de rafraîchissement et un mode CLI ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout d'un bouton de rafraîchissement pour actualiser l'état des données [#8](https://github.com/betagouv/euphrosyne-herma/pull/8).
- Amélioration de l'interface utilisateur : dialogue de connexion plus large et sélection de l'environnement de connexion [#5](https://github.com/betagouv/euphrosyne-herma/pull/5).
- Ajout d'un mode CLI (ligne de commande) pour une utilisation en script [#601b42c](https://github.com/betagouv/euphrosyne-herma/commit/601b42c).
- Possibilité de spécifier des chemins de dossiers typés pour les données à uploader [#34fa0e5](https://github.com/betagouv/euphrosyne-herma/commit/34fa0e5).
- Amélioration de l'expérience utilisateur au démarrage de l'application [#071811d](https://github.com/betagouv/euphrosyne-herma/commit/071811d).
- Ajout d'un bouton de déconnexion dans la fenêtre de téléchargement et utilisation du trousseau pour la gestion des identifiants [#6ad2d58](https://github.com/betagouv/euphrosyne-herma/commit/6ad2d58).
- Gestion améliorée des erreurs d'authentification lors des téléchargements [#ab9f0a6](https://github.com/betagouv/euphrosyne-herma/commit/ab9f0a6).
- Correction de la gestion des projets manquants ou invalides au démarrage de l'application [#a5102e7](https://github.com/betagouv/euphrosyne-herma/commit/a5102e7).

### Évolutions techniques
- Correction du chemin d'installation d'AzCopy pour l'application macOS packagée [#f9d8a3b](https://github.com/betagouv/euphrosyne-herma/pull/7).
- Correction d'un problème où `selected` n'acceptait qu'un argument de valeur 0 [#339de39](https://github.com/betagouv/euphrosyne-herma/pull/6).
- Correction de l'installation des dépendances système dans le workflow de build release [#e6f08af](https://github.com/betagouv/euphrosyne-herma/pull/3 et #cb23e1b](https://github.com/betagouv/euphrosyne-herma/pull/2).
- Utilisation des slugs de projet au lieu des noms pour les requêtes d'outils [#d05d03b](https://github.com/betagouv/euphrosyne-herma/commit/d05d03b).
- Ajout de tests [#edda61d](https://github.com/betagouv/euphrosyne-herma/commit/edda61d).
- Suppression de la vérification du linter lors de la construction pour accélérer le processus [#02db288](https://github.com/betagouv/euphrosyne-herma/commit/02db288).
- Correction de problèmes liés aux permissions dans les workflows CI/CD [#0e7c60a](https://github.com/betagouv/euphrosyne-herma/commit/0e7c60a).
- Amélioration de la gestion des erreurs de téléchargement AzCopy et signalement correct des échecs [#b7d30c5](https://github.com/betagouv/euphrosyne-herma/commit/b7d30c5).

### Autres changements
- Documentation : Ajout de notes sur les découvertes faites lors du développement [#d115969](https://github.com/betagouv/euphrosyne-herma/commit/d115969).
- Correction du Makefile [#a6c2c87](https://github.com/betagouv/euphrosyne-herma/commit/a6c2c87).
- Formatage du code et nettoyage général.
