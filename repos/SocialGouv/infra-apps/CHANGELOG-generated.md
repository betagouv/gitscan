## Changelog : infra-apps (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois a été marqué par une phase importante de stabilisation de la plateforme Iterion. Les efforts se sont concentrés sur la fiabilité des moteurs d'exécution (runners), l'optimisation de la gestion des ressources et la transition vers une adresse web officielle (`iterion.cloud`). L'infrastructure est devenue plus robuste grâce à une meilleure gestion de la haute disponibilité des données et à un suivi d'erreurs amélioré.

### Évolutions fonctionnelles
- **Nouvelle identité web** : Transition vers `iterion.cloud` comme URL publique canonique et mise en place de redirections automatiques.
- **Refonte de l'accès au Studio** : Modification de la structure des URLs, le Studio étant désormais accessible via le chemin `/studio`.
- **Amélioration de l'expérience utilisateur** : Déblocage du catalogue de bots et correction de divers problèmes d'affichage (cartes de liens partagés, blocages de la "brand gate").
- **Alerting opérationnel** : Intégration des alertes de la plateforme directement dans Mattermost pour une meilleure réactivité des équipes.

### Évolutions techniques
- **Stabilisation des Runners (moteurs d'exécution)** :
    - Résolution de nombreux problèmes liés à la gestion des espaces de travail, à la disponibilité des outils et aux drivers [#61](https://github.com/SocialGouv/infra-apps/issues/61) [#59](https://github.com/SocialGouv/infra-apps/issues/59).
    - Optimisation de l'allocation des ressources (mémoire et CPU) pour éviter la saturation des nœuds [#732](https://github.com/SocialGouv/infra-apps/issues/732).
    - Amélioration de la gestion du cycle de vie des tâches pour éviter les interruptions lors des phases de mise à l'échelle (KEDA).
- **Fiabilité et Haute Disponibilité** :
    - Mise en œuvre de la réplication de flux JetStream pour garantir la haute disponibilité des données.
    - Sécurisation des déploiements par l'utilisation de digests d'images (pinning), évitant ainsi la rupture des tâches en cours lors des mises à jour.
- **Observabilité et Sécurité** :
    - Activation du tracing de production et intégration de Sentry pour un suivi précis des erreurs.
    - Renforcement de la sécurité des accès via l'ajout d'un proxy OAuth2 devant les instances de données.
    - Sécurisation des secrets de la CI via l'injection de tokens de forge dans les namespaces dédiés.
- **Maintenance de l'infrastructure** :
    - Mise en service d'un mécanisme de nettoyage automatique des ressources (board claim reaper - ADR-096).
    - Déclassement et suppression de composants obsolètes : `charon-carnets` et `metabase`.

### Autres changements
- **Documentation** : Mise à jour des notes techniques concernant le couplage entre le serveur et le runner, ainsi que la configuration des variables d'environnement.
- **Nettoyage** : Suppression de secrets obsolètes (clés API OpenAI).
