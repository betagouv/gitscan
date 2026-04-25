## Changelog : ami-app-ios (30 derniers jours, au 23 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la navigation et à l'expérience utilisateur, notamment la gestion des liens, des notifications et des pages externes. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Une page d'onboarding pour les notifications a été ajoutée.

### Évolutions fonctionnelles
- **Notifications :** L'application ouvre maintenant la page des notifications lorsqu'on clique sur une notification push [#54](https://github.com/numerique-gouv/ami-app-ios/pull/54).
- **Liens :** Gestion améliorée des liens `mailto` sur les pages partenaires [#65](https://github.com/numerique-gouv/ami-app-ios/pull/65).
- **Navigation :**
    - Ajout d'un bouton "Retour" lorsque l'on navigue vers une page externe dans la WebView [#78](https://github.com/numerique-gouv/ami-app-ios/pull/78).
    - Amélioration de la navigation vers la page d'accueil après le choix des préférences de réception de notifications [#76](https://github.com/numerique-gouv/ami-app-ios/pull/76).
    - Introduction d'une vue "Partenaire" simplifiée pour les pages externes, avec un bouton "Retour" visible [#74](https://github.com/numerique-gouv/ami-app-ios/pull/74).
- **Partage de logs :** Le bouton de partage de logs a été mis à jour avec le style DSFR [#72](https://github.com/numerique-gouv/ami-app-ios/pull/72) et [#73](https://github.com/numerique-gouv/ami-app-ios/pull/73).
- **Onboarding Notifications :** Ajout d'une page d'onboarding native pour la gestion des notifications [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71).
- **WebView :** Amélioration de la gestion de la navigation dans la WebView, avec la possibilité de réinitialiser la navigation à l'URL racine et la gestion des autorisations de navigation [#80](https://github.com/numerique-gouv/ami-app-ios/pull/80).

### Évolutions techniques
- **Architecture :** Introduction d'une classe `AppState` pour gérer l'état de l'application et d'un `NetworkMonitor` pour surveiller la connectivité réseau.
- **Refactoring :** Refactor de la WebView et des vues `HomeView` et `ReviewAppView` pour améliorer la structure du code et la maintenabilité.
- **Observabilité :** Utilisation de `@Observable` pour l'affichage d'informations dans l'application.
- **Gestion des certificats :** Acceptation uniquement des certificats auto-signés en mode DEBUG.
- **Configuration :** Suppression des fichiers de configuration obsolètes.
- **Compatibilité iOS :** L'application est maintenant compatible avec iOS 17.0.

### Autres changements
- Correction de fautes de frappe.
- Suppression de code inutile.
- Amélioration des messages de log.
- Mise à jour de la documentation.
- Amélioration de l'alignement vertical des sous-vues dans `HomeView`.
- Correction d'un problème d'initialisation des vues `HomeView` et `ReviewAppView` après le refactoring.
- Ajout de tests pour la gestion des notifications.
- Amélioration de la gestion de l'enregistrement des tokens Firebase.
- Exécution de `evaluateJavaScript` sur le thread principal.
- Log des réceptions de tokens FCM.
- Suppression de fichiers WebView obsolètes.
