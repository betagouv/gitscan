## Changelog : docteur-proconnect (30 derniers jours, au 26 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion de l'authentification OIDC, corrigeant des problèmes de redirection et de configuration. L'interface utilisateur a également été améliorée avec l'ajout de pages d'erreur DSFR et un ajustement de la mise en page pour une meilleure expérience utilisateur. Enfin, le projet a été migré vers un runtime Bun pour de meilleures performances en production.

### Évolutions fonctionnelles
- **Authentification OIDC :** Correction d'un problème de redirection après authentification, renvoyant l'utilisateur vers la page d'accueil comme prévu [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Authentification OIDC :** Suppression du scope "siren" qui n'est pas autorisé pour ce client [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Authentification OIDC :** Envoi de l'URI de redirection publique lors de l'échange de jetons [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Authentification OIDC :** Suppression de la configuration `userinfo alg` par défaut dans le fichier `.env` [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Pages d'erreur :** Ajout de pages d'erreur DSFR pour les cas 404, 500 et les erreurs d'authentification [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Mise en page :** Ajustement de la mise en page pour maintenir le pied de page en bas de la fenêtre, même sur les pages courtes [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).
- **Logging :** Amélioration du logging pour les états d'authentification inhabituels, incluant la chaîne complète de `error.cause` pour faciliter le débogage [#67](https://github.com/proconnect-gouv/docteur-proconnect/issues/67).

### Évolutions techniques
- **Runtime :** Migration vers un runtime Bun natif pour améliorer les performances en production [#66](https://github.com/proconnect-gouv/docteur-proconnect/issues/66).
- **Dépendances :** Mise à jour de `morgan` vers la version 1.11.0 [#64](https://github.com/proconnect-gouv/docteur-proconnect/issues/64).
- **Dépendances :** Mise à jour de `ejs` vers la version 6.0.1 [#62](https://github.com/proconnect-gouv/docteur-proconnect/issues/62).
- **Dépendances :** Mise à jour de `actions/checkout` vers la version 7.0.0 [#68](https://github.com/proconnect-gouv/docteur-proconnect/issues/68).
