## Changelog : menshen (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, menshen a connu une refonte majeure de son API, passant de Django REST Framework à Django Ninja pour plus de performance et de simplicité. Des améliorations ont également été apportées à la gestion des jetons, à la journalisation et à la configuration, ainsi qu'une première version publique (0.2.0) a été publiée.

### Évolutions fonctionnelles
- Passage à Django Ninja pour l'API, offrant une nouvelle base pour les interactions avec le service [#809d4cd](https://github.com/suitenumerique/menshen/commit/809d4cd).
- Ajout d'un client API de base pour interagir avec le service [#c74b37e](https://github.com/suitenumerique/menshen/commit/c74b37e).
- Restriction de la portée (scope) de l'échange de jetons dans le playground à `openid` [#039e9bb](https://github.com/suitenumerique/menshen/commit/039e9bb).
- Ajout de messages d'avertissement lorsque des portées supplémentaires sont demandées lors de l'échange de jetons [#782ad4e](https://github.com/suitenumerique/menshen/commit/782ad4e).

### Évolutions techniques
- Refactorisation du service de révocation de jetons pour une meilleure organisation du code [#00e9cab](https://github.com/suitenumerique/menshen/commit/00e9cab).
- Factorisation des utilitaires principaux du service dans un mixin pour éviter la duplication de code [#54634f2](https://github.com/suitenumerique/menshen/commit/54634f2).
- Simplification des messages d'erreur liés à la validation des jetons [#0c48ab9](https://github.com/suitenumerique/menshen/commit/0c48ab9).
- Refonte du service d'introspection des jetons échangés [#cae5fa1](https://github.com/suitenumerique/menshen/commit/cae5fa1).
- Suppression des paramètres OIDC inutilisés [#05ca571](https://github.com/suitenumerique/menshen/commit/05ca571).
- Suppression du suffixe "Enum" des énumérations pour une meilleure lisibilité [#0ff6880](https://github.com/suitenumerique/menshen/commit/0ff6880).
- Amélioration de la lisibilité du service de requête [#a12811c](https://github.com/suitenumerique/menshen/commit/a12811c).
- Correction d'un problème d'importation de module [#a570180](https://github.com/suitenumerique/menshen/commit/a570180).
- Mise à jour de la commande de lancement en production dans le Dockerfile [#1e89c4f](https://github.com/suitenumerique/menshen/commit/1e89c4f).
- Correction de la version épinglée de l'action Docker login [#0b772b7](https://github.com/suitenumerique/menshen/commit/0b772b7).

### Autres changements
- Publication de la version 0.2.0 [#7cdfa16](https://github.com/suitenumerique/menshen/commit/7cdfa16).
- Publication de la version 0.1.0 [#48c570d](https://github.com/suitenumerique/menshen/commit/48c570d).
- Ajout de `django-extra` à `sentry-sdk` [#822aeed](https://github.com/suitenumerique/menshen/commit/822aeed).
- Correction du type de contenu attendu pour les requêtes d'échange de jetons (JSON) [#ddcd221](https://github.com/suitenumerique/menshen/commit/ddcd221).
- Ignorer les champs supplémentaires dans la réponse d'introspection du sujet du jeton [#873376a](https://github.com/suitenumerique/menshen/commit/873376a).
