## Changelog : ami-fc-proxy (30 derniers jours, au 26 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au proxy FranceConnect au cours des 30 derniers jours. Les modifications se concentrent principalement sur l'amélioration de la compatibilité avec l'API FranceConnect, notamment pour les appels `userinfo` et `logout`, ainsi que sur la gestion des données et des exceptions lors de l'échange de tokens.

### Évolutions fonctionnelles
- Le point de terminaison de déconnexion (`logout`) est maintenant correctement proxifié, assurant une déconnexion complète via FranceConnect.  [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- L'appel à l'endpoint `userinfo` est maintenant correctement configuré avec les en-têtes nécessaires pour récupérer les informations utilisateur. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Amélioration de la gestion des données envoyées à l'endpoint d'échange de tokens, en utilisant l'encodage URL et la méthode POST. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Utilisation de `FileStore` pour la gestion des fichiers, améliorant potentiellement la performance et la fiabilité. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)

### Évolutions techniques
- Gestion améliorée des exceptions et ajout d'un gestionnaire d'exceptions pour une meilleure robustesse de l'application. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Refonte de la manière dont les données sont transmises lors de l'échange de tokens, passant à une approche basée sur `data` pour les requêtes POST. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
