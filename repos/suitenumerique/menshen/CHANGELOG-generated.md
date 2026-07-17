## Changelog : menshen (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu une avancée significative vers une version stable avec l'implémentation des endpoints de base pour l'échange de jetons OAuth 2.0 (RFC 8693).  Des améliorations ont été apportées à l'architecture interne pour une meilleure lisibilité et maintenabilité, ainsi qu'une automatisation accrue des processus de développement et de publication via Helm et Docker.

### Évolutions fonctionnelles
- Implémentation des endpoints de base pour l'échange de jetons OAuth 2.0, permettant l'échange de jetons selon la RFC 8693.
- Ajout des "grants" à la réponse de l'échange de jetons.
- Restriction de la portée (scope) de l'échange de jetons dans l'environnement de test (playground) à "openid".
- Ajout de messages d'avertissement lorsque des portées supplémentaires sont demandées lors de l'échange de jetons.
- Correction du type de contenu attendu pour les requêtes d'échange de jetons (doit être JSON).

### Évolutions techniques
- Refonte du service de requête pour une meilleure lisibilité.
- Déplacement de la logique de révocation de jetons et de l'introspection de jetons échangés vers des services dédiés.
- Factorisation des utilitaires principaux du service dans un mixin pour éviter la duplication de code.
- Simplification des messages d'erreur liés à la validation des jetons.
- Utilisation de `msgspec.Struc` pour les structures de données.
- Suppression des dépendances inutiles `drf-standardized-errors` et `annotated-types`.
- Ajout de la prise en charge du pool de connexions PostgreSQL.
- Utilisation de Uvicorn pour l'exécution en production.
- Migration des structures vers l'héritage de `msgspec.Struc`.
- Suppression des paramètres OIDC inutilisés.

### Autres changements
- Publication de la première version (0.1.0) avec les endpoints d'échange de jetons.
- Ajout d'un chart Helm pour faciliter le déploiement et la gestion de l'application sur Kubernetes.
- Automatisation du linting et de la publication du chart Helm.
- Automatisation et documentation du développement basé sur Kubernetes.
- Bundle des fichiers statiques dans l'image Docker.
- Mise à jour de la version de Python à 3.14.6.
- Ajout de tests pour le service de requête d'échange de jetons.
- Suppression du suffixe "Enum" des énumérations.
- Corrections mineures et améliorations de la documentation.
- Mises à jour des dépendances (actions GitHub, python, Docker).
