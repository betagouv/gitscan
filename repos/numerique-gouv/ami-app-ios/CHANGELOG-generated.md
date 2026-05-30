## Changelog : ami-app-ios (30 derniers jours, au 21 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations à l'affichage des bannières d'information sur l'écran d'accueil, corrige un problème lié à leur positionnement et met à jour l'URL d'accès aux réglages. Des ajustements techniques ont également été effectués pour une meilleure gestion des URLs spéciales.

### Évolutions fonctionnelles
- Réactivation de l'affichage des bannières d'information sur l'écran d'accueil. [#91](https://github.com/numerique-gouv/ami-app-ios/pull/91)
- Correction du positionnement des bannières d'information, qui étaient affichées incorrectement. [#93](https://github.com/numerique-gouv/ami-app-ios/pull/93)
- Mise à jour de l'URL d'accès aux réglages. [#86](https://github.com/numerique-gouv/ami-app-ios/pull/86)

### Évolutions techniques
- Introduction d'un `enum` pour la gestion des URLs spéciales (suffixe matching) afin de faciliter la détection des pages web spécifiques dans la vue d'accueil.
- Refactorisation du code pour déplacer le conteneur des bannières hors de la `NavigationStack`.

### Autres changements
- Suppression d'un conteneur de bannières inutile dans la vue principale. [#93](https://github.com/numerique-gouv/ami-app-ios/pull/93)
