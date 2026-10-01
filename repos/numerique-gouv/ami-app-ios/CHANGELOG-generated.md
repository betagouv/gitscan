## Changelog : ami-app-ios (30 derniers jours, au 30 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur au sein de la WebView, notamment pour faciliter le téléchargement de documents et la gestion des appels téléphoniques. L'application bénéficie également d'une meilleure intégration avec France Identité et d'une préparation accrue pour les environnements de préproduction, tout en consolidant sa structure technique pour plus de stabilité.

### Évolutions fonctionnelles
- **Amélioration de la gestion documentaire** : support de nouveaux types de fichiers et possibilité de télécharger et d'enregistrer des documents directement depuis la WebView ([#183](https://github.com/numerique-gouv/ami-app-ios/pull/183), [#176](https://github.com/numerique-gouv/ami-app-ios/pull/176)).
- **Gestion des liens spéciaux** : support des liens de type `tel:` permettant de lancer des appels téléphoniques directement depuis l'interface.
- **Optimisation de l'expérience France Identité** : l'application est désormais capable de détecter et d'ouvrir directement l'application France Identité pour faciliter l'authentification.
- **Navigation fluidifiée** : les services tiers ne s'ouvrent plus systématiquement dans une nouvelle fenêtre WebView, rendant la navigation plus naturelle ([#180](https://github.com/numerique-gouv/ami-app-ios/pull/180)).
- **Système d'alertes amélioré** : mise en place d'un nouveau système d'alertes plus généraliste au sein de la WebView pour une meilleure communication avec l'utilisateur.

### Évolutions techniques
- **Montée de version** : passage de l'application à la version 0.5.0 ([#204](https://github.com/numerique-gouv/ami-app-ios/pull/204)).
- **Refonte de l'architecture WebView** : introduction d'un `DependencyContainer` pour la couche de composition, d'un `SpecialLinkHandler` et passage à une version asynchrone du delegate `WKWebView`.
- **Gestion des environnements** : ajout d'un flag Xcode dédié à la préproduction ([#202](https://github.com/numerique-gouv/ami-app-ios/pull/202)) et activation des Passkeys sur l'environnement de staging ([#172](https://github.com/numerique-gouv/ami-app-ios/pull/172)).
- **Refactoring et nettoyage** : 
    - Renommage de composants pour plus de clarté sémantique (ex: `Partner` devient `Service` ou `DestinationLink`).
    - Suppression de fonctionnalités obsolètes comme le `LogExporter` et le bouton de téléchargement des logs ([#192](https://github.com/numerique-gouv/ami-app-ios/pull/192)).
- **Sécurité et réseau** : ajout du header HTTP `Referer` dans les requêtes de service et optimisation de la gestion des cookies via un nouveau `WebViewLocalStorageManager`.

### Autres changements
- **Documentation** : mise à jour du README concernant la configuration nécessaire des fichiers `.env`.
- **Maintenance** : nettoyage général du code, correction de typos et optimisation des messages de logs.
