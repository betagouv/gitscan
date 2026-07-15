## Changelog : menshen (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'infrastructure du projet, notamment l'ajout d'un support Helm pour le déploiement Kubernetes, l'amélioration de la gestion des connexions à la base de données et la refactorisation de plusieurs composants clés pour une meilleure lisibilité et maintenabilité. Des corrections de bugs et des ajustements ont également été apportés pour améliorer la robustesse et la conformité du serveur d'autorisation.

### Évolutions fonctionnelles
- Ajout de la prise en charge des "grants" dans la réponse de l'échange de jetons.
- Restriction de la portée (scope) de l'échange de jetons dans l'environnement de test (playground) à `openid` [#39e9bb](https://github.com/suitenumerique/menshen/issues/39e9bb).
- Ajout de messages d'avertissement lorsque des portées supplémentaires sont demandées lors de l'échange de jetons [#782ad4e](https://github.com/suitenumerique/menshen/issues/782ad4e).

### Évolutions techniques
- Refactorisation du service de gestion des requêtes pour améliorer la lisibilité [#a12811c](https://github.com/suitenumerique/menshen/issues/a12811c).
- Déplacement de la révocation de jetons et de l'introspection du jeton échangé vers des services dédiés [#00e9cab](https://github.com/suitenumerique/menshen/issues/00e9cab), [#cae5fa1](https://github.com/suitenumerique/menshen/issues/cae5fa1).
- Ajout d'un support pour le pool de connexions PostgreSQL [#5840f47](https://github.com/suitenumerique/menshen/issues/5840f47).
- Utilisation de Uvicorn pour l'exécution en production [#9414c22](https://github.com/suitenumerique/menshen/issues/9414c22).
- Ajout d'un chart Helm pour faciliter le déploiement sur Kubernetes [#573a09a](https://github.com/suitenumerique/menshen/issues/573a09a).
- Automatisation et documentation du développement basé sur Kubernetes [#7b027c6](https://github.com/suitenumerique/menshen/issues/7b027c6).
- Publication des images Docker automatisée [#e6246c2](https://github.com/suitenumerique/menshen/issues/e6246c2).
- Refactorisation des tests pour adopter le pattern LaSuite [#48dfce5](https://github.com/suitenumerique/menshen/issues/48dfce5).
- Utilisation de `msgspec.Struc` pour les structures de données [#60bf50a](https://github.com/suitenumerique/menshen/issues/60bf50a).
- Suppression des dépendances `drf-standardized-errors` et `annotated-types`.

### Autres changements
- Mise à jour de la version de Python à 3.14.6 [#ab12175](https://github.com/suitenumerique/menshen/issues/ab12175).
- Suppression des paramètres OIDC inutilisés [#05ca571](https://github.com/suitenumerique/menshen/issues/05ca571).
- Correction d'une erreur d'importation de module [#a570180](https://github.com/suitenumerique/menshen/issues/a570180).
- Correction du type de contenu (content-type) des requêtes d'échange de jetons pour s'assurer qu'il est JSON [#ddcd221](https://github.com/suitenumerique/menshen/issues/ddcd221).
- Correction de l'ignorance des champs supplémentaires dans la réponse d'introspection du jeton [#873376a](https://github.com/suitenumerique/menshen/issues/873376a).
- Simplification des messages d'erreur liés à la validation des jetons [#0c48ab9](https://github.com/suitenumerique/menshen/issues/0c48ab9).
- Ajout de la dépendance `uvicorn`.
- Bundle des fichiers statiques dans l'image Docker.
- Correction d'une erreur de copier/coller dans le playground.
- Bump de la release à 0.1.0 [#48c570d](https://github.com/suitenumerique/menshen/issues/48c570d).
