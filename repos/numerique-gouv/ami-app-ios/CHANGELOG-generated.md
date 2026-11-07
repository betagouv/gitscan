## Changelog : ami-app-ios (30 derniers jours, au 3 novembre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte technique majeure visant à améliorer sa stabilité et sa structure interne. Pour l'utilisateur, ces évolutions se traduisent par une meilleure gestion du mode hors-ligne, l'ajout de fonctions de rafraîchissement et une nouvelle manière de mettre en avant certains contenus via des liens promus.

### Évolutions fonctionnelles
- Ajout d'un mode hors-ligne basique pour une meilleure résilience [#218](https://github.com/numerique-gouv/ami-app-ios/pull/218).
- Mise en place de la navigation par bordure [#209](https://github.com/numerique-gouv/ami-app-ios/pull/209).
- Introduction de la fonctionnalité "URLs promues" pour mettre en avant des contenus spécifiques dans l'interface.
- Ajout de la fonction "pull-to-refresh" (glisser pour rafraîchir) sur la vue de révision.
- Amélioration de la précision des messages d'erreur lors de l'accès aux données de la page.

### Évolutions techniques
- Refonte architecturale profonde du composant WebView (séparation stricte des couches de données, de modèle et de présentation).
- Modernisation du code pour la compatibilité Swift 6, notamment via l'isolation `MainActor` pour la gestion de la concurrence.
- Amélioration de la gestion des environnements en séparant distinctement la réception des notifications et la vue racine entre les versions de Staging et de Production.
- Optimisation de la logique de navigation grâce à l'introduction de nouveaux protocoles spécialisés (`WebViewNavigationHandler`, `WebViewNavigationPolicyDelegate`).
- Implémentation d'un système d'archivage web (`WebViewArchiver`) pour la gestion des fichiers.

### Autres changements
- Renforcement de la couverture de tests unitaires, notamment pour la nouvelle fonctionnalité d'URLs promues.
- Nettoyage de la configuration du projet Xcode et de la structure des dossiers de tests.
- Maintenance du code : suppression de code mort, corrections de la linter et mise à jour de la documentation technique.
