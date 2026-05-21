## Changelog : ami-fc-proxy (30 derniers jours, au 20 mai 2026)

### Résumé
Ce proxy pour FranceConnect a connu des améliorations significatives concernant la gestion des appels à l'API FranceConnect, notamment pour les points de terminaison `userinfo` et `token`. Ces changements visent à simplifier et sécuriser l'intégration de FranceConnect sur Scalingo en automatisant la configuration et en réduisant les erreurs potentielles. Des corrections ont également été apportées pour assurer la compatibilité avec les déploiements sur Scalingo.

### Évolutions fonctionnelles
- Amélioration de la gestion des appels à l'endpoint `userinfo` en corrigeant les headers.  [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Implémentation de la proxyfication de l'endpoint `token` pour une gestion plus transparente des requêtes. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Prise en charge de l'envoi de données encodées en URL pour l'endpoint `token`. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Gestion des exceptions lors des appels à l'endpoint `token`. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Proxyfication de l'endpoint `authorize` pour une meilleure intégration avec FranceConnect. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Ajout de la gestion de l'origine de la requête lors de l'appel `authorize-callback`. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Stockage de l'origine de la requête dans `authorize-request`. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)

### Évolutions techniques
- Utilisation de `FileStore` pour la gestion des fichiers. [#708](https://github.com/numerique-gouv/ami-fc-proxy/issues/708)
- Correction des problèmes de déploiement sur Scalingo en ajustant la configuration et en supprimant le buildpack Heroku UV.

### Autres changements
- Aucune information supplémentaire ne ressort des commits analysés.
