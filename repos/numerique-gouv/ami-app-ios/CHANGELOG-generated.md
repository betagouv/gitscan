## Changelog : ami-app-ios (30 derniers jours, au 21 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une gestion améliorée des notifications, un accès facilité à la page d'accueil après la configuration des notifications, et l'ajout d'un bouton de partage de logs plus visible. Des corrections et refactorings techniques ont également été effectués pour améliorer la stabilité et la maintenabilité de l'application.

### Évolutions fonctionnelles
- **Notifications :** L'application ouvre maintenant la page des notifications lorsqu'un utilisateur clique sur une notification push. [#54](https://github.com/numerique-gouv/ami-app-ios/pull/54)
- **Onboarding Notifications :** La page de configuration des notifications est maintenant présentée en natif, améliorant l'expérience utilisateur. [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71)
- **Navigation :** Après avoir configuré les préférences de réception des notifications, l'application redirige automatiquement l'utilisateur vers la page d'accueil. [#76](https://github.com/numerique-gouv/ami-app-ios/pull/76)
- **Partage de logs :** Le bouton de partage de logs a été mis à jour avec le nouveau design DSFR et est maintenant plus facilement accessible en bas de page. [#72](https://github.com/numerique-gouv/ami-app-ios/pull/72) [#74](https://github.com/numerique-gouv/ami-app-ios/pull/74)
- **Contact par email :** La fonctionnalité de contact par email est maintenant disponible sur la page d'accueil. [#59](https://github.com/numerique-gouv/ami-app-ios/pull/59)
- **Liens Mailto :** La gestion des liens `mailto:` a été réactivée. [#65](https://github.com/numerique-gouv/ami-app-ios/pull/65)

### Évolutions techniques
- **WebView :** Refactorisation importante de la WebView, incluant la gestion de la navigation et la sécurité des certificats.
- **Gestion des URLs :** Ajout d'un mécanisme pour contrôler la navigation dans la WebView, permettant de bloquer certaines URLs si nécessaire.
- **Firebase :** Amélioration de la gestion de l'enregistrement du token Firebase, forçant la ré-inscription en cas d'échec initial.
- **Architecture :** Initialisation correcte des vues `HomeView` et `ReviewAppView` avec leurs modèles de données.
- **Configuration :** Suppression des fichiers de configuration inutilisés et simplification de la configuration de l'URL de base.
- **Compatibilité iOS :** L'application est maintenant compatible avec iOS 17.0.
- **Exécution JavaScript :** L'exécution de JavaScript dans la WebView est maintenant forcée sur le thread principal.

### Autres changements
- Mise à jour de la documentation et des messages de log pour plus de clarté.
- Correction de typos et suppression de code inutilisé.
- Amélioration de la gestion des previews en mode release.
