## Changelog : ami-app-ios (30 derniers jours, au 06/10/2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations majeures pour fluidifier la navigation et faciliter l'utilisation des services. Les utilisateurs peuvent désormais télécharger plus de types de fichiers, utiliser des liens de téléphone directement et profiter d'une navigation plus intuitive. En parallèle, des optimisations techniques ont renforcé la sécurité (Passkeys, gestion des cookies) et la stabilité de l'application.

### Évolutions fonctionnelles
- **Navigation et interface** :
    - Amélioration du comportement du bouton "Retour" pour assurer un retour direct à l'écran d'accueil [#186](https://github.com/numerique-gouv/ami-app-ios/pull/186).
    - Optimisation de la navigation vers les services tiers qui s'effectue désormais dans la même vue web au lieu d'en ouvrir une nouvelle [#180](https://github.com/numerique-gouv/ami-app-ios/pull/180).
    - Suppression du bouton de téléchargement des logs pour simplifier l'interface utilisateur [#192](https://github.com/numerique-gouv/ami-app-ios/pull/192).
- **Gestion des fichiers et liens** :
    - Extension des types de fichiers autorisés au téléchargement et prise en charge des liens de type téléphone (`tel:`) [#183](https://github.com/numerique-gouv/ami-app-ios/pull/183).
    - Ajout de la possibilité de télécharger des fichiers directement depuis la WebView [#176](https://github.com/numerique-gouv/ami-app-ios/pull/176).
- **Authentification** :
    - Amélioration de l'intégration avec l'application France Identité pour faciliter le processus d'authentification [#181](https://github.com/numerique-gouv/ami-app-ios/pull/181).

### Évolutions techniques
- **Architecture et performance** :
    - Introduction d'un `DependencyContainer` pour améliorer la gestion des dépendances et la composition de l'application.
    - Refonte de la gestion de la WebView dans la vue d'accueil pour permettre une réinitialisation dynamique lors du retour depuis un service.
    - Mise en place d'un nouveau système d'alertes plus généralisé pour la WebView.
- **Sécurité et Authentification** :
    - Activation du support des Passkeys sur l'environnement de staging [#172](https://github.com/numerique-gouv/ami-app-ios/pull/172).
    - Correction d'un problème empêchant la suppression du cookie de confiance (`fc-trusteddevice`) [#178](https://github.com/numerique-gouv/ami-app-ios/pull/178).
    - Ajout de l'en-tête HTTP `Referer` dans les requêtes de service pour améliorer la traçabilité.
- **Infrastructure et Versioning** :
    - Passage à la version 0.5.0 [#204](https://github.com/numerique-gouv/ami-app-ios/pull/204).
    - Ajout d'un flag Xcode dédié à la gestion de l'environnement de préproduction [#202](https://github.com/numerique-gouv/ami-app-ios/pull/202).

### Autres changements
- Mise à jour de la documentation (README) concernant la configuration des fichiers `.env`.
- Nettoyage du code (suppression d'imports inutiles et du composant `LogExporter`).
