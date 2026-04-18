## Changelog : ami-app-ios (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'ajout d'un écran d'onboarding natif pour une meilleure première impression, la réactivation de la gestion des liens "mailto", et la possibilité d'ouvrir la page des notifications directement depuis une notification push. Des corrections et optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un écran d'onboarding natif pour les nouveaux utilisateurs [#71](https://github.com/numerique-gouv/ami-app-ios/pull/71).
- Réactivation de la gestion des liens "mailto" pour permettre l'envoi d'emails directement depuis l'application [#65](https://github.com/numerique-gouv/ami-app-ios/pull/65).
- Possibilité d'ouvrir la page des notifications en cliquant sur une notification push [#54](https://github.com/numerique-gouv/ami-app-ios/pull/54).
- Ajout d'un bouton de partage des logs en bas de page sur l'application de production [#72](https://github.com/numerique-gouv/ami-app-ios/pull/72).
- Gestion du lien "Contact par email" sur la page d'accueil.

### Évolutions techniques
- Refactor de la gestion des WebView pour améliorer la performance et la stabilité.
- Amélioration de la gestion de l'enregistrement des tokens Firebase pour garantir l'enregistrement même en cas d'échec initial.
- Optimisation de la structure de `HomeView` pour éviter les problèmes de boutons "retour" multiples.
- Mise à jour de la version minimale supportée d'iOS à 17.0.
- Amélioration de la gestion de la navigation dans la WebView avec la possibilité de bloquer certaines URL.
- Correction d'un bug empêchant l'initialisation correcte de `HomeView` et `ReviewAppView` après un refactoring.
- Exécution de `evaluateJavaScript` sur le thread principal pour éviter les problèmes de concurrence.

### Autres changements
- Suppression de fichiers de configuration inutilisés.
- Suppression de code commenté obsolète.
- Reformattage des messages de log pour une meilleure lisibilité.
- Correction de typos.
