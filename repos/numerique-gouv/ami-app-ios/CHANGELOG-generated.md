## Changelog : ami-app-ios (30 derniers jours, au 7 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations à la navigation et à l'initialisation des vues principales de l'application, ainsi qu'un correctif important pour l'ouverture des notifications push. Des optimisations ont également été apportées à la structure de certaines vues pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Correction : L'application ouvre désormais la page des notifications lorsqu'un utilisateur clique sur une notification push. [#54](https://github.com/numerique-gouv/ami-app-ios/issues/54)
- Amélioration : Optimisation de la structure de la vue d'accueil (HomeView) et de la vue du webView (AMIWebView) pour éviter l'apparition de plusieurs boutons "Retour" dans la barre d'outils.
- Compatibilité : L'application est désormais compatible avec iOS 17.0 et versions ultérieures.

### Évolutions techniques
- Refactorisation : Initialisation correcte des vues HomeView et ReviewAppView avec leurs modèles de données respectifs.
- Refactorisation : Suppression du code obsolète lié à l'ancien webView.
- Sécurité : Acceptation des certificats auto-signés uniquement en mode DEBUG pour une meilleure sécurité en production.
- Optimisation : Suppression de code inutilisé après refactorisation.

### Autres changements
- Configuration : Activation de la configuration par défaut pour les aperçus (Previews) en dehors du mode DEBUG.
