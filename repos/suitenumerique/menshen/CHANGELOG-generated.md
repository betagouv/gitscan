## Changelog : menshen (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, le projet menshen a connu des avancées significatives en termes de déploiement et de structure interne. L'ajout d'un chart Helm permet une gestion simplifiée du déploiement sur Kubernetes, tandis que des refactorings importants améliorent la lisibilité et la maintenabilité du code. Une première version de l'API client a également été ajoutée.

### Évolutions fonctionnelles
- Ajout d'une API client de base. [#c74b37e](https://github.com/suitenumerique/menshen/commit/c74b37e)
- Amélioration des messages d'avertissement lorsque des scopes supplémentaires sont demandés lors de l'échange de jetons. [#782ad4e](https://github.com/suitenumerique/menshen/commit/782ad4e)
- Restriction du scope d'échange de jetons à `openid` dans le playground. [#039e9bb](https://github.com/suitenumerique/menshen/commit/039e9bb)

### Évolutions techniques
- Implémentation d'un chart Helm pour faciliter le déploiement sur Kubernetes, incluant des workflows pour le linting et la publication. [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc), [#5840f47](https://github.com/suitenumerique/menshen/commit/5840f47), [#573a09a](https://github.com/suitenumerique/menshen/commit/573a09a)
- Refactoring du service de requête pour améliorer la lisibilité. [#a12811c](https://github.com/suitenumerique/menshen/commit/a12811c)
- Déplacement de la révocation de jetons et de l'introspection vers des services dédiés. [#00e9cab](https://github.com/suitenumerique/menshen/commit/00e9cab), [#cae5fa1](https://github.com/suitenumerique/menshen/commit/cae5fa1)
- Factorisation des utilitaires de base du service dans un mixin. [#54634f2](https://github.com/suitenumerique/menshen/commit/54634f2)
- Simplification des messages d'erreur liés à la validation des jetons. [#0c48ab9](https://github.com/suitenumerique/menshen/commit/0c48ab9)
- Ajout de support pour un pool de connexions PostgreSQL. [#7b027c6](https://github.com/suitenumerique/menshen/commit/7b027c6)
- Suppression des suffixes "Enum" des énumérations. [#0ff6880](https://github.com/suitenumerique/menshen/commit/0ff6880)
- Suppression des paramètres OIDC inutilisés. [#05ca571](https://github.com/suitenumerique/menshen/commit/05ca571)

### Autres changements
- Correction d'une erreur d'importation de module. [#a570180](https://github.com/suitenumerique/menshen/commit/a570180)
- Correction d'une erreur de type de contenu JSON lors de la requête d'échange de jetons. [#ddcd221](https://github.com/suitenumerique/menshen/commit/ddcd221)
- Correction d'un problème d'état désynchronisé avec ArgoCD. [#573a09a](https://github.com/suitenumerique/menshen/commit/573a09a)
- Correction d'une erreur de copier/coller dans le playground. [#f76e461](https://github.com/suitenumerique/menshen/commit/f76e461)
- Ajout de la dépendance uvicorn. [#c8816ac](https://github.com/suitenumerique/menshen/commit/c8816ac)
- Ajout de la configuration Sentry pour Django. [#822aeed](https://github.com/suitenumerique/menshen/commit/822aeed)
- Bump de la version à 0.1.0 [#48c570d](https://github.com/suitenumerique/menshen/commit/48c570d)
