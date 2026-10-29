## Changelog : ami-app-ios (30 derniers jours, au 13 octobre 2026)

### Résumé
Cette période marque le passage de l'application à la version 0.5.0. Les utilisateurs bénéficieront d'une navigation plus fluide, notamment avec un bouton "Retour" qui ramène plus naturellement à l'accueil, et d'une meilleure gestion des liens (appels téléphoniques) et des téléchargements de fichiers. L'application introduit également la possibilité de mettre en avant certains contenus via de nouveaux liens promotionnels.

### Évolutions fonctionnelles
- **Mise à jour majeure** : Passage à la version 0.5.0.
- **Amélioration de la navigation** : Le bouton de retour permet désormais de revenir systématiquement à l'écran d'accueil [#185](https://github.com/numerique-gouv/ami-app-ios/pull/185).
- **Gestion des liens et fichiers** : 
    - Support étendu des types de fichiers téléchargeables.
    - Gestion des liens de type `tel:` pour permettre de passer des appels directement depuis l'application.
- **Contenus mis en avant** : Introduction de la fonctionnalité "Promoted URLs" pour afficher des contenus ou services spécifiques.
- **Interface** : Mise en place d'un nouveau système d'alertes pour les interactions au sein de la WebView.

### Évolutions techniques
- **Architecture** : 
    - Introduction d'un `DependencyContainer` pour améliorer la gestion des dépendances et la composition du code.
    - Refonte de la gestion des liens spéciaux via une nouvelle structure `SpecialLinks`.
- **Navigation et WebView** : Optimisation du cycle de vie de la WebView dans l'écran d'accueil pour garantir un réinitialisation propre lors du retour d'un service.
- **Sécurité et Réseau** : Ajout du header HTTP `Referer` dans les requêtes de service pour améliorer la conformité et la sécurité [#187](https://github.com/numerique-gouv/ami-app-ios/pull/187).
- **Robustesse** : 
    - Amélioration de la gestion des erreurs (distinction précise entre une page non prête et un payload invalide).
    - Résolution de conflits liés à la gestion de la concurrence avec Swift 6.
- **Tests** : Renforcement de la couverture de tests unitaires, notamment pour la nouvelle fonctionnalité de liens mis en avant.

### Autres changements
- **Configuration** : Ajout d'un flag Xcode dédié pour faciliter les tests en environnement de préproduction [#202](https://github.com/numerique-gouv/ami-app-ios/pull/202).
- **Nettoyage** : Suppression de code obsolète (observateurs inutilisés, URLs de pages spéciales supprimées) et des tests par défaut d'Xcode.
- **Documentation** : Ajout de la documentation technique pour la fonctionnalité de liens mis en avant.
