## Changelog : menshen (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, le projet menshen a connu une avancée significative avec la mise en place d'une infrastructure Kubernetes complète incluant un Helm chart pour faciliter le déploiement. Des améliorations ont également été apportées à la robustesse et à la lisibilité du code, notamment en refactorisant des services clés et en corrigeant des erreurs liées à la validation des jetons et à la gestion des scopes. La version 0.1.0 a été publiée, introduisant les endpoints de base pour l'échange de jetons OAuth 2.0.

### Évolutions fonctionnelles
- Publication de la version 0.1.0 implémentant les endpoints de base pour l'échange de jetons OAuth 2.0.
- Restriction du scope d'échange de jeton dans le playground à `openid` [#39e9bb](https://github.com/suitenumerique/menshen/commit/039e9bb).
- Ajout de messages d'avertissement lorsque des scopes supplémentaires sont demandés [#782ad4e](https://github.com/suitenumerique/menshen/commit/782ad4e).

### Évolutions techniques
- Implémentation d'un Helm chart pour simplifier le déploiement sur Kubernetes [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
- Automatisation et documentation du développement basé sur Kubernetes [#7b027c6](https://github.com/suitenumerique/menshen/commit/7b027c6).
- Ajout de support pour un pool de connexions PostgreSQL [#5840f47](https://github.com/suitenumerique/menshen/commit/5840f47).
- Refactorisation du service de requête pour améliorer la lisibilité [#a12811c](https://github.com/suitenumerique/menshen/commit/a12811c).
- Déplacement de la révocation de jeton et de l'introspection vers des services dédiés [#00e9cab](https://github.com/suitenumerique/menshen/commit/00e9cab) et [#cae5fa1](https://github.com/suitenumerique/menshen/commit/cae5fa1).
- Factorisation des utilitaires de service principaux dans un mixin [#54634f2](https://github.com/suitenumerique/menshen/commit/54634f2).
- Simplification des erreurs liées à la validation des jetons [#0c48ab9](https://github.com/suitenumerique/menshen/commit/0c48ab9).
- Suppression du suffixe "Enum" des énumérations [#0ff6880](https://github.com/suitenumerique/menshen/commit/0ff6880).
- Ajout de la dépendance `uvicorn` [#c8816ac](https://github.com/suitenumerique/menshen/commit/c8816ac).
- Bundle des fichiers statiques dans l'image Docker [#af7fd64](https://github.com/suitenumerique/menshen/commit/af7fd64).
- Ajout de `django extra` à `sentry-sdk` [#822aeed](https://github.com/suitenumerique/menshen/commit/822aeed).
- Ajout d'un client API de base [#c74b37e](https://github.com/suitenumerique/menshen/commit/c74b37e).

### Autres changements
- Correction d'une erreur d'importation de module [#a570180](https://github.com/suitenumerique/menshen/commit/a570180).
- Suppression des paramètres OIDC inutilisés [#05ca571](https://github.com/suitenumerique/menshen/commit/05ca571).
- Correction d'une erreur de copier/coller dans le playground [#f76e461](https://github.com/suitenumerique/menshen/commit/f76e461).
- Correction du type de contenu de la requête d'échange de jeton pour s'assurer qu'il s'agit de JSON [#ddcd221](https://github.com/suitenumerique/menshen/commit/ddcd221).
- Prévention de l'état "hors synchronisation" d'ArgoCD avec les jobs [#573a09a](https://github.com/suitenumerique/menshen/commit/573a09a).
- Ajout de workflows de linting et de publication du chart Helm [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
- Ignorer les champs supplémentaires de la réponse d'introspection du sujet du jeton [#873376a](https://github.com/suitenumerique/menshen/commit/873376a).
